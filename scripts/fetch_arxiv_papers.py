import arxiv
import json
import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import time
import urllib.parse

def get_kaiminghe_affiliation():
    """从Kaiming He个人主页获取最新 affiliation 信息"""
    try:
        url = "https://people.csail.mit.edu/kaiming/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 尝试多种方式获取机构信息
        title = soup.find('title')
        if title:
            title_text = title.get_text()
            if "mit" in title_text.lower() or "kaiming" in title_text.lower():
                return "MIT CSAIL"
        
        # 查找包含机构信息的元素
        for elem in soup.find_all(['div', 'p', 'span']):
            text = elem.get_text().lower()
            if 'mit' in text or 'csa' in text:
                return "MIT CSAIL"
                
        return "MIT"
    except Exception as e:
        print(f"获取机构信息失败: {e}")
        return "MIT"

def fetch_kaiminghe_papers_direct():
    """直接使用arXiv API获取论文数据"""
    base_url = "https://export.arxiv.org/api/query"
    
    # 搜索查询 - 根据姓名和可能的机构变体
    search_query = 'au:"Kaiming He" OR au:"Kaiming H." OR au:"He, Kaiming"'
    
    params = {
        'search_query': search_query,
        'start': 0,
        'max_results': 50,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending'
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=30)
        response.raise_for_status()
        
        # 解析Atom feed
        from xml.etree import ElementTree as ET
        root = ET.fromstring(response.content)
        
        # 定义命名空间
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        
        papers = []
        current_affiliation = get_kaiminghe_affiliation()
        
        for entry in root.findall('atom:entry', ns):
            # 提取论文信息
            title_elem = entry.find('atom:title', ns)
            summary_elem = entry.find('atom:summary', ns)
            published_elem = entry.find('atom:published', ns)
            updated_elem = entry.find('atom:updated', ns)
            id_elem = entry.find('atom:id', ns)
            
            # 提取作者信息
            authors = []
            for author_elem in entry.findall('atom:author/atom:name', ns):
                authors.append(author_elem.text)
            
            # 验证是否包含Kaiming He
            kaiminghe_variants = ["Kaiming He", "Kaiming H.", "He, Kaiming"]
            if not any(variant in authors for variant in kaiminghe_variants):
                continue
            
            # 提取分类信息
            categories = []
            primary_category = ""
            for category_elem in entry.findall('atom:category', ns):
                category = category_elem.get('term', '')
                categories.append(category)
                if not primary_category:
                    primary_category = category
            
            # 提取PDF链接
            pdf_url = ""
            for link_elem in entry.findall('atom:link', ns):
                if link_elem.get('title') == 'pdf' or link_elem.get('type') == 'application/pdf':
                    pdf_url = link_elem.get('href')
                    break
            
            # 生成短ID
            paper_id = id_elem.text.split('/')[-1] if id_elem is not None else ""
            
            paper_data = {
                "id": paper_id,
                "title": title_elem.text.strip() if title_elem is not None else "No title",
                "authors": authors,
                "summary": summary_elem.text.strip() if summary_elem is not None else "No summary available",
                "published": published_elem.text[:10] if published_elem is not None else "Unknown",
                "updated": updated_elem.text[:10] if updated_elem is not None else None,
                "pdf_url": pdf_url,
                "primary_category": primary_category,
                "affiliation": current_affiliation,
                "arxiv_url": f"https://arxiv.org/abs/{paper_id}" if paper_id else ""
            }
            papers.append(paper_data)
        
        return papers
        
    except Exception as e:
        print(f"arXiv API请求失败: {e}")
        return []

def fetch_kaiminghe_papers_arxiv_lib():
    """使用arxiv库的备用方法"""
    try:
        client = arxiv.Client()
        
        search = arxiv.Search(
            query='au:"Kaiming He"',
            max_results=30,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending
        )
        
        papers = []
        current_affiliation = get_kaiminghe_affiliation()
        
        for result in client.results(search):
            authors = [str(author) for author in result.authors]
            kaiminghe_variants = ["Kaiming He", "Kaiming H.", "He, Kaiming"]
            
            if not any(variant in authors for variant in kaiminghe_variants):
                continue
                
            paper_data = {
                "id": result.get_short_id(),
                "title": result.title,
                "authors": authors,
                "summary": result.summary,
                "published": result.published.strftime("%Y-%m-%d"),
                "updated": result.updated.strftime("%Y-%m-%d") if result.updated else None,
                "pdf_url": result.pdf_url,
                "primary_category": result.primary_category if result.primary_category else "",
                "affiliation": current_affiliation,
                "arxiv_url": f"https://arxiv.org/abs/{result.get_short_id()}"
            }
            papers.append(paper_data)
        
        return papers
    except Exception as e:
        print(f"arxiv库方法失败: {e}")
        return []

def save_papers_to_json(papers, filename="data/papers.json"):
    """保存论文数据到JSON文件"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    data = {
        "last_updated": datetime.now().isoformat(),
        "papers": papers
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def generate_markdown(papers_data, output_file="README.md"):
    """生成Markdown文档到根目录"""
    
    markdown_content = f"""# Kaiming He newest airxiv papers

> Page last update: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} 
> 
> The project automatically fetches the latest papers from the arXiv of [Kaiming He](https://people.csail.mit.edu/kaiming/).
>
> You can click the 'Watch' button to receive daily email notifications.

## Papers Summary
- **Total Papers**: {len(papers_data)}
- **Paper Last Update**: {papers_data[0]['published'] if papers_data else 'N/A'}

## Papers List

"""
    
    for i, paper in enumerate(papers_data, 1):
        markdown_content += f"""
### {i}. {paper['title']}

**Authors**: {', '.join(paper['authors'])}  
**Affiliation**: {paper['affiliation']}  
**Published Date**: {paper['published']}  
**Primary Category**: {paper['primary_category']}  

<details>
<summary>📄 Abstract (click to expand)</summary>

{paper['summary']}

</details>

**Resource**: 
- [📄 PDF url]({paper['pdf_url']}) 
- [🔗 arXiv url]({paper['arxiv_url']})

---
"""
    
    markdown_content += """
## 📄 Licence
The paper is copyrighted by the original authors, and this project is for academic research purposes only.
"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

if __name__ == "__main__":
    print("开始抓取 Kaiming He 的 arXiv 论文...")
    
    papers = fetch_kaiminghe_papers_direct()
    
    if not papers:
        print("直接API方法失败，尝试使用arxiv库...")
        papers = fetch_kaiminghe_papers_arxiv_lib()
    
    print(f"找到 {len(papers)} 篇论文")
    
    if papers:
        save_papers_to_json(papers)
        generate_markdown(papers)  # 现在会生成到根目录
        print("Markdown文档生成完成！")
    else:
        print("未找到论文，请检查网络连接或arXiv服务状态")
        save_papers_to_json([])
        generate_markdown([])
