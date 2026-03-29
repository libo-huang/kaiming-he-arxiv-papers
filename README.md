# Kaiming He newest airxiv papers

> Page last update: 2026-03-29 04:28:27 
> 
> The project automatically fetches the latest papers from the arXiv of [Kaiming He](https://people.csail.mit.edu/kaiming/).
>
> You can click the 'Watch' button to receive daily email notifications.

## Papers Summary
- **Total Papers**: 30
- **Paper Last Update**: 2026-02-23

## Papers List


### 1. GeoPT: Scaling Physics Simulation via Lifted Geometric Pre-Training

**Authors**: Haixu Wu, Minghao Guo, Zongyi Li, Zhiyang Dou, Mingsheng Long, Kaiming He, Wojciech Matusik  
**Affiliation**: MIT CSAIL  
**Published Date**: 2026-02-23  
**Primary Category**: cs.LG  

<details>
<summary>📄 Abstract (click to expand)</summary>

Neural simulators promise efficient surrogates for physics simulation, but scaling them is bottlenecked by the prohibitive cost of generating high-fidelity training data. Pre-training on abundant off-the-shelf geometries offers a natural alternative, yet faces a fundamental gap: supervision on static geometry alone ignores dynamics and can lead to negative transfer on physics tasks. We present GeoPT, a unified pre-trained model for general physics simulation based on lifted geometric pre-training. The core idea is to augment geometry with synthetic dynamics, enabling dynamics-aware self-supervision without physics labels. Pre-trained on over one million samples, GeoPT consistently improves industrial-fidelity benchmarks spanning fluid mechanics for cars, aircraft, and ships, and solid mechanics in crash simulation, reducing labeled data requirements by 20-60% and accelerating convergence by 2$\times$. These results show that lifting with synthetic dynamics bridges the geometry-physics gap, unlocking a scalable path for neural simulation and potentially beyond. Code is available at https://github.com/Physics-Scaling/GeoPT.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2602.20399v1) 
- [🔗 arXiv url](https://arxiv.org/abs/2602.20399v1)

---

### 2. Generative Modeling via Drifting

**Authors**: Mingyang Deng, He Li, Tianhong Li, Yilun Du, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2026-02-04  
**Primary Category**: cs.LG  

<details>
<summary>📄 Abstract (click to expand)</summary>

Generative modeling can be formulated as learning a mapping f such that its pushforward distribution matches the data distribution. The pushforward behavior can be carried out iteratively at inference time, for example in diffusion and flow-based models. In this paper, we propose a new paradigm called Drifting Models, which evolve the pushforward distribution during training and naturally admit one-step inference. We introduce a drifting field that governs the sample movement and achieves equilibrium when the distributions match. This leads to a training objective that allows the neural network optimizer to evolve the distribution. In experiments, our one-step generator achieves state-of-the-art results on ImageNet at 256 x 256 resolution, with an FID of 1.54 in latent space and 1.61 in pixel space. We hope that our work opens up new opportunities for high-quality one-step generation.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2602.04770v2) 
- [🔗 arXiv url](https://arxiv.org/abs/2602.04770v2)

---

### 3. One-step Latent-free Image Generation with Pixel Mean Flows

**Authors**: Yiyang Lu, Susie Lu, Qiao Sun, Hanhong Zhao, Zhicheng Jiang, Xianbang Wang, Tianhong Li, Zhengyang Geng, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2026-01-29  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

Modern diffusion/flow-based models for image generation typically exhibit two core characteristics: (i) using multi-step sampling, and (ii) operating in a latent space. Recent advances have made encouraging progress on each aspect individually, paving the way toward one-step diffusion/flow without latents. In this work, we take a further step towards this goal and propose "pixel MeanFlow" (pMF). Our core guideline is to formulate the network output space and the loss space separately. The network target is designed to be on a presumed low-dimensional image manifold (i.e., x-prediction), while the loss is defined via MeanFlow in the velocity space. We introduce a simple transformation between the image manifold and the average velocity field. In experiments, pMF achieves strong results for one-step latent-free generation on ImageNet at 256x256 resolution (2.22 FID) and 512x512 resolution (2.48 FID), filling a key missing piece in this regime. We hope that our study will further advance the boundaries of diffusion/flow-based generative models.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2601.22158v2) 
- [🔗 arXiv url](https://arxiv.org/abs/2601.22158v2)

---

### 4. Bidirectional Normalizing Flow: From Data to Noise and Back

**Authors**: Yiyang Lu, Qiao Sun, Xianbang Wang, Zhicheng Jiang, Hanhong Zhao, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2025-12-11  
**Primary Category**: cs.LG  

<details>
<summary>📄 Abstract (click to expand)</summary>

Normalizing Flows (NFs) have been established as a principled framework for generative modeling. Standard NFs consist of a forward process and a reverse process: the forward process maps data to noise, while the reverse process generates samples by inverting it. Typical NF forward transformations are constrained by explicit invertibility, ensuring that the reverse process can serve as their exact analytic inverse. Recent developments in TARFlow and its variants have revitalized NF methods by combining Transformers and autoregressive flows, but have also exposed causal decoding as a major bottleneck. In this work, we introduce Bidirectional Normalizing Flow ($\textbf{BiFlow}$), a framework that removes the need for an exact analytic inverse. BiFlow learns a reverse model that approximates the underlying noise-to-data inverse mapping, enabling more flexible loss functions and architectures. Experiments on ImageNet demonstrate that BiFlow, compared to its causal decoding counterpart, improves generation quality while accelerating sampling by up to two orders of magnitude. BiFlow yields state-of-the-art results among NF-based methods and competitive performance among single-evaluation ("1-NFE") methods. Following recent encouraging progress on NFs, we hope our work will draw further attention to this classical paradigm.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2512.10953v1) 
- [🔗 arXiv url](https://arxiv.org/abs/2512.10953v1)

---

### 5. Improved Mean Flows: On the Challenges of Fastforward Generative Models

**Authors**: Zhengyang Geng, Yiyang Lu, Zongze Wu, Eli Shechtman, J. Zico Kolter, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2025-12-01  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

MeanFlow (MF) has recently been established as a framework for one-step generative modeling. However, its ``fastforward'' nature introduces key challenges in both the training objective and the guidance mechanism. First, the original MF's training target depends not only on the underlying ground-truth fields but also on the network itself. To address this issue, we recast the objective as a loss on the instantaneous velocity $v$, re-parameterized by a network that predicts the average velocity $u$. Our reformulation yields a more standard regression problem and improves the training stability. Second, the original MF fixes the classifier-free guidance scale during training, which sacrifices flexibility. We tackle this issue by formulating guidance as explicit conditioning variables, thereby retaining flexibility at test time. The diverse conditions are processed through in-context conditioning, which reduces model size and benefits performance. Overall, our $\textbf{improved MeanFlow}$ ($\textbf{iMF}$) method, trained entirely from scratch, achieves $\textbf{1.72}$ FID with a single function evaluation (1-NFE) on ImageNet 256$\times$256. iMF substantially outperforms prior methods of this kind and closes the gap with multi-step methods while using no distillation. We hope our work will further advance fastforward generative modeling as a stand-alone paradigm.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2512.02012v1) 
- [🔗 arXiv url](https://arxiv.org/abs/2512.02012v1)

---

### 6. ARC Is a Vision Problem!

**Authors**: Keya Hu, Ali Cy, Linlu Qiu, Xiaoman Delores Ding, Runqian Wang, Yeyin Eva Zhu, Jacob Andreas, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2025-11-18  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

The Abstraction and Reasoning Corpus (ARC) is designed to promote research on abstract reasoning, a fundamental aspect of human intelligence. Common approaches to ARC treat it as a language-oriented problem, addressed by large language models (LLMs) or recurrent reasoning models. However, although the puzzle-like tasks in ARC are inherently visual, existing research has rarely approached the problem from a vision-centric perspective. In this work, we formulate ARC within a vision paradigm, framing it as an image-to-image translation problem. To incorporate visual priors, we represent the inputs on a "canvas" that can be processed like natural images. It is then natural for us to apply standard vision architectures, such as a vanilla Vision Transformer (ViT), to perform image-to-image mapping. Our model is trained from scratch solely on ARC data and generalizes to unseen tasks through test-time training. Our framework, termed Vision ARC (VARC), achieves 60.4% accuracy on the ARC-1 benchmark, substantially outperforming existing methods that are also trained from scratch. Our results are competitive with those of leading LLMs and close the gap to average human performance.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2511.14761v1) 
- [🔗 arXiv url](https://arxiv.org/abs/2511.14761v1)

---

### 7. Back to Basics: Let Denoising Generative Models Denoise

**Authors**: Tianhong Li, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2025-11-17  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

Today's denoising diffusion models do not "denoise" in the classical sense, i.e., they do not directly predict clean images. Rather, the neural networks predict noise or a noised quantity. In this paper, we suggest that predicting clean data and predicting noised quantities are fundamentally different. According to the manifold assumption, natural data should lie on a low-dimensional manifold, whereas noised quantities do not. With this assumption, we advocate for models that directly predict clean data, which allows apparently under-capacity networks to operate effectively in very high-dimensional spaces. We show that simple, large-patch Transformers on pixels can be strong generative models: using no tokenizer, no pre-training, and no extra loss. Our approach is conceptually nothing more than "Just image Transformers", or JiT, as we call it. We report competitive results using JiT with large patch sizes of 16 and 32 on ImageNet at resolutions of 256 and 512, where predicting high-dimensional noised quantities can fail catastrophically. With our networks mapping back to the basics of the manifold, our research goes back to basics and pursues a self-contained paradigm for Transformer-based diffusion on raw natural data.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2511.13720v2) 
- [🔗 arXiv url](https://arxiv.org/abs/2511.13720v2)

---

### 8. Diffuse and Disperse: Image Generation with Representation Regularization

**Authors**: Runqian Wang, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2025-06-10  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

The development of diffusion-based generative models over the past decade has largely proceeded independently of progress in representation learning. These diffusion models typically rely on regression-based objectives and generally lack explicit regularization. In this work, we propose \textit{Dispersive Loss}, a simple plug-and-play regularizer that effectively improves diffusion-based generative models. Our loss function encourages internal representations to disperse in the hidden space, analogous to contrastive self-supervised learning, with the key distinction that it requires no positive sample pairs and therefore does not interfere with the sampling process used for regression. Compared to the recent method of representation alignment (REPA), our approach is self-contained and minimalist, requiring no pre-training, no additional parameters, and no external data. We evaluate Dispersive Loss on the ImageNet dataset across a range of models and report consistent improvements over widely used and strong baselines. We hope our work will help bridge the gap between generative modeling and representation learning.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2506.09027v2) 
- [🔗 arXiv url](https://arxiv.org/abs/2506.09027v2)

---

### 9. Mean Flows for One-step Generative Modeling

**Authors**: Zhengyang Geng, Mingyang Deng, Xingjian Bai, J. Zico Kolter, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2025-05-19  
**Primary Category**: cs.LG  

<details>
<summary>📄 Abstract (click to expand)</summary>

We propose a principled and effective framework for one-step generative modeling. We introduce the notion of average velocity to characterize flow fields, in contrast to instantaneous velocity modeled by Flow Matching methods. A well-defined identity between average and instantaneous velocities is derived and used to guide neural network training. Our method, termed the MeanFlow model, is self-contained and requires no pre-training, distillation, or curriculum learning. MeanFlow demonstrates strong empirical performance: it achieves an FID of 3.43 with a single function evaluation (1-NFE) on ImageNet 256x256 trained from scratch, significantly outperforming previous state-of-the-art one-step diffusion/flow models. Our study substantially narrows the gap between one-step diffusion/flow models and their multi-step predecessors, and we hope it will motivate future research to revisit the foundations of these powerful models.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2505.13447v1) 
- [🔗 arXiv url](https://arxiv.org/abs/2505.13447v1)

---

### 10. Transformers without Normalization

**Authors**: Jiachen Zhu, Xinlei Chen, Kaiming He, Yann LeCun, Zhuang Liu  
**Affiliation**: MIT CSAIL  
**Published Date**: 2025-03-13  
**Primary Category**: cs.LG  

<details>
<summary>📄 Abstract (click to expand)</summary>

Normalization layers are ubiquitous in modern neural networks and have long been considered essential. This work demonstrates that Transformers without normalization can achieve the same or better performance using a remarkably simple technique. We introduce Dynamic Tanh (DyT), an element-wise operation $DyT($x$) = \tanh(α$x$)$, as a drop-in replacement for normalization layers in Transformers. DyT is inspired by the observation that layer normalization in Transformers often produces tanh-like, $S$-shaped input-output mappings. By incorporating DyT, Transformers without normalization can match or exceed the performance of their normalized counterparts, mostly without hyperparameter tuning. We validate the effectiveness of Transformers with DyT across diverse settings, ranging from recognition to generation, supervised to self-supervised learning, and computer vision to language models. These findings challenge the conventional understanding that normalization layers are indispensable in modern neural networks, and offer new insights into their role in deep networks.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2503.10622v2) 
- [🔗 arXiv url](https://arxiv.org/abs/2503.10622v2)

---

### 11. Denoising Hamiltonian Network for Physical Reasoning

**Authors**: Congyue Deng, Brandon Y. Feng, Cecilia Garraffo, Alan Garbarz, Robin Walters, William T. Freeman, Leonidas Guibas, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2025-03-10  
**Primary Category**: cs.LG  

<details>
<summary>📄 Abstract (click to expand)</summary>

Machine learning frameworks for physical problems must capture and enforce physical constraints that preserve the structure of dynamical systems. Many existing approaches achieve this by integrating physical operators into neural networks. While these methods offer theoretical guarantees, they face two key limitations: (i) they primarily model local relations between adjacent time steps, overlooking longer-range or higher-level physical interactions, and (ii) they focus on forward simulation while neglecting broader physical reasoning tasks. We propose the Denoising Hamiltonian Network (DHN), a novel framework that generalizes Hamiltonian mechanics operators into more flexible neural operators. DHN captures non-local temporal relationships and mitigates numerical integration errors through a denoising mechanism. DHN also supports multi-system modeling with a global conditioning mechanism. We demonstrate its effectiveness and flexibility across three diverse physical reasoning tasks with distinct inputs and outputs.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2503.07596v1) 
- [🔗 arXiv url](https://arxiv.org/abs/2503.07596v1)

---

### 12. Fractal Generative Models

**Authors**: Tianhong Li, Qinyi Sun, Lijie Fan, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2025-02-24  
**Primary Category**: cs.LG  

<details>
<summary>📄 Abstract (click to expand)</summary>

Modularization is a cornerstone of computer science, abstracting complex functions into atomic building blocks. In this paper, we introduce a new level of modularization by abstracting generative models into atomic generative modules. Analogous to fractals in mathematics, our method constructs a new type of generative model by recursively invoking atomic generative modules, resulting in self-similar fractal architectures that we call fractal generative models. As a running example, we instantiate our fractal framework using autoregressive models as the atomic generative modules and examine it on the challenging task of pixel-by-pixel image generation, demonstrating strong performance in both likelihood estimation and generation quality. We hope this work could open a new paradigm in generative modeling and provide a fertile ground for future research. Code is available at https://github.com/LTH14/fractalgen.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2502.17437v2) 
- [🔗 arXiv url](https://arxiv.org/abs/2502.17437v2)

---

### 13. Is Noise Conditioning Necessary for Denoising Generative Models?

**Authors**: Qiao Sun, Zhicheng Jiang, Hanhong Zhao, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2025-02-18  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

It is widely believed that noise conditioning is indispensable for denoising diffusion models to work successfully. This work challenges this belief. Motivated by research on blind image denoising, we investigate a variety of denoising-based generative models in the absence of noise conditioning. To our surprise, most models exhibit graceful degradation, and in some cases, they even perform better without noise conditioning. We provide a theoretical analysis of the error caused by removing noise conditioning and demonstrate that our analysis aligns with empirical observations. We further introduce a noise-unconditional model that achieves a competitive FID of 2.23 on CIFAR-10, significantly narrowing the gap to leading noise-conditional models. We hope our findings will inspire the community to revisit the foundations and formulations of denoising generative models.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2502.13129v2) 
- [🔗 arXiv url](https://arxiv.org/abs/2502.13129v2)

---

### 14. Fluid: Scaling Autoregressive Text-to-image Generative Models with Continuous Tokens

**Authors**: Lijie Fan, Tianhong Li, Siyang Qin, Yuanzhen Li, Chen Sun, Michael Rubinstein, Deqing Sun, Kaiming He, Yonglong Tian  
**Affiliation**: MIT CSAIL  
**Published Date**: 2024-10-17  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

Scaling up autoregressive models in vision has not proven as beneficial as in large language models. In this work, we investigate this scaling problem in the context of text-to-image generation, focusing on two critical factors: whether models use discrete or continuous tokens, and whether tokens are generated in a random or fixed raster order using BERT- or GPT-like transformer architectures. Our empirical results show that, while all models scale effectively in terms of validation loss, their evaluation performance -- measured by FID, GenEval score, and visual quality -- follows different trends. Models based on continuous tokens achieve significantly better visual quality than those using discrete tokens. Furthermore, the generation order and attention mechanisms significantly affect the GenEval score: random-order models achieve notably better GenEval scores compared to raster-order models. Inspired by these findings, we train Fluid, a random-order autoregressive model on continuous tokens. Fluid 10.5B model achieves a new state-of-the-art zero-shot FID of 6.16 on MS-COCO 30K, and 0.69 overall score on the GenEval benchmark. We hope our findings and results will encourage future efforts to further bridge the scaling gap between vision and language models.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2410.13863v1) 
- [🔗 arXiv url](https://arxiv.org/abs/2410.13863v1)

---

### 15. Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers

**Authors**: Lirui Wang, Xinlei Chen, Jialiang Zhao, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2024-09-30  
**Primary Category**: cs.RO  

<details>
<summary>📄 Abstract (click to expand)</summary>

One of the roadblocks for training generalist robotic models today is heterogeneity. Previous robot learning methods often collect data to train with one specific embodiment for one task, which is expensive and prone to overfitting. This work studies the problem of learning policy representations through heterogeneous pre-training on robot data across different embodiments and tasks at scale. We propose Heterogeneous Pre-trained Transformers (HPT), which pre-train a large, shareable trunk of a policy neural network to learn a task and embodiment agnostic shared representation. This general architecture aligns the specific proprioception and vision inputs from distinct embodiments to a short sequence of tokens and then processes such tokens to map to control robots for different tasks. Leveraging the recent large-scale multi-embodiment real-world robotic datasets as well as simulation, deployed robots, and human video datasets, we investigate pre-training policies across heterogeneity. We conduct experiments to investigate the scaling behaviors of training objectives, to the extent of 52 datasets. HPTs outperform several baselines and enhance the fine-tuned policy performance by over 20% on unseen tasks in multiple simulator benchmarks and real-world settings. See the project website (https://liruiw.github.io/hpt/) for code and videos.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2409.20537v1) 
- [🔗 arXiv url](https://arxiv.org/abs/2409.20537v1)

---

### 16. Autoregressive Image Generation without Vector Quantization

**Authors**: Tianhong Li, Yonglong Tian, He Li, Mingyang Deng, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2024-06-17  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

Conventional wisdom holds that autoregressive models for image generation are typically accompanied by vector-quantized tokens. We observe that while a discrete-valued space can facilitate representing a categorical distribution, it is not a necessity for autoregressive modeling. In this work, we propose to model the per-token probability distribution using a diffusion procedure, which allows us to apply autoregressive models in a continuous-valued space. Rather than using categorical cross-entropy loss, we define a Diffusion Loss function to model the per-token probability. This approach eliminates the need for discrete-valued tokenizers. We evaluate its effectiveness across a wide range of cases, including standard autoregressive models and generalized masked autoregressive (MAR) variants. By removing vector quantization, our image generator achieves strong results while enjoying the speed advantage of sequence modeling. We hope this work will motivate the use of autoregressive generation in other continuous-valued domains and applications. Code is available at: https://github.com/LTH14/mar.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2406.11838v3) 
- [🔗 arXiv url](https://arxiv.org/abs/2406.11838v3)

---

### 17. Physically Compatible 3D Object Modeling from a Single Image

**Authors**: Minghao Guo, Bohan Wang, Pingchuan Ma, Tianyuan Zhang, Crystal Elaine Owens, Chuang Gan, Joshua B. Tenenbaum, Kaiming He, Wojciech Matusik  
**Affiliation**: MIT CSAIL  
**Published Date**: 2024-05-30  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

We present a computational framework that transforms single images into 3D physical objects. The visual geometry of a physical object in an image is determined by three orthogonal attributes: mechanical properties, external forces, and rest-shape geometry. Existing single-view 3D reconstruction methods often overlook this underlying composition, presuming rigidity or neglecting external forces. Consequently, the reconstructed objects fail to withstand real-world physical forces, resulting in instability or undesirable deformation -- diverging from their intended designs as depicted in the image. Our optimization framework addresses this by embedding physical compatibility into the reconstruction process. We explicitly decompose the three physical attributes and link them through static equilibrium, which serves as a hard constraint, ensuring that the optimized physical shapes exhibit desired physical behaviors. Evaluations on a dataset collected from Objaverse demonstrate that our framework consistently enhances the physical realism of 3D models over existing methods. The utility of our framework extends to practical applications in dynamic simulations and 3D printing, where adherence to physical compatibility is paramount.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2405.20510v3) 
- [🔗 arXiv url](https://arxiv.org/abs/2405.20510v3)

---

### 18. TetSphere Splatting: Representing High-Quality Geometry with Lagrangian Volumetric Meshes

**Authors**: Minghao Guo, Bohan Wang, Kaiming He, Wojciech Matusik  
**Affiliation**: MIT CSAIL  
**Published Date**: 2024-05-30  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

We introduce TetSphere Splatting, a Lagrangian geometry representation designed for high-quality 3D shape modeling. TetSphere splatting leverages an underused yet powerful geometric primitive -- volumetric tetrahedral meshes. It represents 3D shapes by deforming a collection of tetrahedral spheres, with geometric regularizations and constraints that effectively resolve common mesh issues such as irregular triangles, non-manifoldness, and floating artifacts. Experimental results on multi-view and single-view reconstruction highlight TetSphere splatting's superior mesh quality while maintaining competitive reconstruction accuracy compared to state-of-the-art methods. Additionally, TetSphere splatting demonstrates versatility by seamlessly integrating into generative modeling tasks, such as image-to-3D and text-to-3D generation.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2405.20283v4) 
- [🔗 arXiv url](https://arxiv.org/abs/2405.20283v4)

---

### 19. Dynamic Inhomogeneous Quantum Resource Scheduling with Reinforcement Learning

**Authors**: Linsen Li, Pratyush Anand, Kaiming He, Dirk Englund  
**Affiliation**: MIT CSAIL  
**Published Date**: 2024-05-25  
**Primary Category**: cs.LG  

<details>
<summary>📄 Abstract (click to expand)</summary>

A central challenge in quantum information science and technology is achieving real-time estimation and feedforward control of quantum systems. This challenge is compounded by the inherent inhomogeneity of quantum resources, such as qubit properties and controls, and their intrinsically probabilistic nature. This leads to stochastic challenges in error detection and probabilistic outcomes in processes such as heralded remote entanglement. Given these complexities, optimizing the construction of quantum resource states is an NP-hard problem. In this paper, we address the quantum resource scheduling issue by formulating the problem and simulating it within a digitized environment, allowing the exploration and development of agent-based optimization strategies. We employ reinforcement learning agents within this probabilistic setting and introduce a new framework utilizing a Transformer model that emphasizes self-attention mechanisms for pairs of qubits. This approach facilitates dynamic scheduling by providing real-time, next-step guidance. Our method significantly improves the performance of quantum systems, achieving more than a 3$\times$ improvement over rule-based agents, and establishes an innovative framework that improves the joint design of physical and control systems for quantum applications in communication, networking, and computing.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2405.16380v1) 
- [🔗 arXiv url](https://arxiv.org/abs/2405.16380v1)

---

### 20. A Decade's Battle on Dataset Bias: Are We There Yet?

**Authors**: Zhuang Liu, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2024-03-13  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

We revisit the "dataset classification" experiment suggested by Torralba & Efros (2011) a decade ago, in the new era with large-scale, diverse, and hopefully less biased datasets as well as more capable neural network architectures. Surprisingly, we observe that modern neural networks can achieve excellent accuracy in classifying which dataset an image is from: e.g., we report 84.7% accuracy on held-out validation data for the three-way classification problem consisting of the YFCC, CC, and DataComp datasets. Our further experiments show that such a dataset classifier could learn semantic features that are generalizable and transferable, which cannot be explained by memorization. We hope our discovery will inspire the community to rethink issues involving dataset bias.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2403.08632v2) 
- [🔗 arXiv url](https://arxiv.org/abs/2403.08632v2)

---

### 21. Deconstructing Denoising Diffusion Models for Self-Supervised Learning

**Authors**: Xinlei Chen, Zhuang Liu, Saining Xie, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2024-01-25  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

In this study, we examine the representation learning abilities of Denoising Diffusion Models (DDM) that were originally purposed for image generation. Our philosophy is to deconstruct a DDM, gradually transforming it into a classical Denoising Autoencoder (DAE). This deconstructive procedure allows us to explore how various components of modern DDMs influence self-supervised representation learning. We observe that only a very few modern components are critical for learning good representations, while many others are nonessential. Our study ultimately arrives at an approach that is highly simplified and to a large extent resembles a classical DAE. We hope our study will rekindle interest in a family of classical methods within the realm of modern self-supervised learning.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2401.14404v1) 
- [🔗 arXiv url](https://arxiv.org/abs/2401.14404v1)

---

### 22. Return of Unconditional Generation: A Self-supervised Representation Generation Method

**Authors**: Tianhong Li, Dina Katabi, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2023-12-06  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

Unconditional generation -- the problem of modeling data distribution without relying on human-annotated labels -- is a long-standing and fundamental challenge in generative models, creating a potential of learning from large-scale unlabeled data. In the literature, the generation quality of an unconditional method has been much worse than that of its conditional counterpart. This gap can be attributed to the lack of semantic information provided by labels. In this work, we show that one can close this gap by generating semantic representations in the representation space produced by a self-supervised encoder. These representations can be used to condition the image generator. This framework, called Representation-Conditioned Generation (RCG), provides an effective solution to the unconditional generation problem without using labels. Through comprehensive experiments, we observe that RCG significantly improves unconditional generation quality: e.g., it achieves a new state-of-the-art FID of 2.15 on ImageNet 256x256, largely reducing the previous best of 5.91 by a relative 64%. Our unconditional results are situated in the same tier as the leading class-conditional ones. We hope these encouraging observations will attract the community's attention to the fundamental problem of unconditional generation. Code is available at https://github.com/LTH14/rcg.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2312.03701v4) 
- [🔗 arXiv url](https://arxiv.org/abs/2312.03701v4)

---

### 23. Scaling Language-Image Pre-training via Masking

**Authors**: Yanghao Li, Haoqi Fan, Ronghang Hu, Christoph Feichtenhofer, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2022-12-01  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

We present Fast Language-Image Pre-training (FLIP), a simple and more efficient method for training CLIP. Our method randomly masks out and removes a large portion of image patches during training. Masking allows us to learn from more image-text pairs given the same wall-clock time and contrast more samples per iteration with similar memory footprint. It leads to a favorable trade-off between accuracy and training time. In our experiments on 400 million image-text pairs, FLIP improves both accuracy and speed over the no-masking baseline. On a large diversity of downstream tasks, FLIP dominantly outperforms the CLIP counterparts trained on the same data. Facilitated by the speedup, we explore the scaling behavior of increasing the model size, data size, or training length, and report encouraging results and comparisons. We hope that our work will foster future research on scaling vision-language learning.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2212.00794v2) 
- [🔗 arXiv url](https://arxiv.org/abs/2212.00794v2)

---

### 24. Masked Autoencoders As Spatiotemporal Learners

**Authors**: Christoph Feichtenhofer, Haoqi Fan, Yanghao Li, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2022-05-18  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

This paper studies a conceptually simple extension of Masked Autoencoders (MAE) to spatiotemporal representation learning from videos. We randomly mask out spacetime patches in videos and learn an autoencoder to reconstruct them in pixels. Interestingly, we show that our MAE method can learn strong representations with almost no inductive bias on spacetime (only except for patch and positional embeddings), and spacetime-agnostic random masking performs the best. We observe that the optimal masking ratio is as high as 90% (vs. 75% on images), supporting the hypothesis that this ratio is related to information redundancy of the data. A high masking ratio leads to a large speedup, e.g., > 4x in wall-clock time or even more. We report competitive results on several challenging video datasets using vanilla Vision Transformers. We observe that MAE can outperform supervised pre-training by large margins. We further report encouraging results of training on real-world, uncurated Instagram data. Our study suggests that the general framework of masked autoencoding (BERT, MAE, etc.) can be a unified methodology for representation learning with minimal domain knowledge.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2205.09113v2) 
- [🔗 arXiv url](https://arxiv.org/abs/2205.09113v2)

---

### 25. Exploring Plain Vision Transformer Backbones for Object Detection

**Authors**: Yanghao Li, Hanzi Mao, Ross Girshick, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2022-03-30  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

We explore the plain, non-hierarchical Vision Transformer (ViT) as a backbone network for object detection. This design enables the original ViT architecture to be fine-tuned for object detection without needing to redesign a hierarchical backbone for pre-training. With minimal adaptations for fine-tuning, our plain-backbone detector can achieve competitive results. Surprisingly, we observe: (i) it is sufficient to build a simple feature pyramid from a single-scale feature map (without the common FPN design) and (ii) it is sufficient to use window attention (without shifting) aided with very few cross-window propagation blocks. With plain ViT backbones pre-trained as Masked Autoencoders (MAE), our detector, named ViTDet, can compete with the previous leading methods that were all based on hierarchical backbones, reaching up to 61.3 AP_box on the COCO dataset using only ImageNet-1K pre-training. We hope our study will draw attention to research on plain-backbone detectors. Code for ViTDet is available in Detectron2.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2203.16527v2) 
- [🔗 arXiv url](https://arxiv.org/abs/2203.16527v2)

---

### 26. Benchmarking Detection Transfer Learning with Vision Transformers

**Authors**: Yanghao Li, Saining Xie, Xinlei Chen, Piotr Dollar, Kaiming He, Ross Girshick  
**Affiliation**: MIT CSAIL  
**Published Date**: 2021-11-22  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

Object detection is a central downstream task used to test if pre-trained network parameters confer benefits, such as improved accuracy or training speed. The complexity of object detection methods can make this benchmarking non-trivial when new architectures, such as Vision Transformer (ViT) models, arrive. These difficulties (e.g., architectural incompatibility, slow training, high memory consumption, unknown training formulae, etc.) have prevented recent studies from benchmarking detection transfer learning with standard ViT models. In this paper, we present training techniques that overcome these challenges, enabling the use of standard ViT models as the backbone of Mask R-CNN. These tools facilitate the primary goal of our study: we compare five ViT initializations, including recent state-of-the-art self-supervised learning methods, supervised initialization, and a strong random initialization baseline. Our results show that recent masking-based unsupervised learning methods may, for the first time, provide convincing transfer learning improvements on COCO, increasing box AP up to 4% (absolute) over supervised and prior self-supervised pre-training methods. Moreover, these masking-based initializations scale better, with the improvement growing as model size increases.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2111.11429v1) 
- [🔗 arXiv url](https://arxiv.org/abs/2111.11429v1)

---

### 27. Masked Autoencoders Are Scalable Vision Learners

**Authors**: Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, Ross Girshick  
**Affiliation**: MIT CSAIL  
**Published Date**: 2021-11-11  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

This paper shows that masked autoencoders (MAE) are scalable self-supervised learners for computer vision. Our MAE approach is simple: we mask random patches of the input image and reconstruct the missing pixels. It is based on two core designs. First, we develop an asymmetric encoder-decoder architecture, with an encoder that operates only on the visible subset of patches (without mask tokens), along with a lightweight decoder that reconstructs the original image from the latent representation and mask tokens. Second, we find that masking a high proportion of the input image, e.g., 75%, yields a nontrivial and meaningful self-supervisory task. Coupling these two designs enables us to train large models efficiently and effectively: we accelerate training (by 3x or more) and improve accuracy. Our scalable approach allows for learning high-capacity models that generalize well: e.g., a vanilla ViT-Huge model achieves the best accuracy (87.8%) among methods that use only ImageNet-1K data. Transfer performance in downstream tasks outperforms supervised pre-training and shows promising scaling behavior.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2111.06377v3) 
- [🔗 arXiv url](https://arxiv.org/abs/2111.06377v3)

---

### 28. A Large-Scale Study on Unsupervised Spatiotemporal Representation Learning

**Authors**: Christoph Feichtenhofer, Haoqi Fan, Bo Xiong, Ross Girshick, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2021-04-29  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

We present a large-scale study on unsupervised spatiotemporal representation learning from videos. With a unified perspective on four recent image-based frameworks, we study a simple objective that can easily generalize all these methods to space-time. Our objective encourages temporally-persistent features in the same video, and in spite of its simplicity, it works surprisingly well across: (i) different unsupervised frameworks, (ii) pre-training datasets, (iii) downstream datasets, and (iv) backbone architectures. We draw a series of intriguing observations from this study, e.g., we discover that encouraging long-spanned persistency can be effective even if the timespan is 60 seconds. In addition to state-of-the-art results in multiple benchmarks, we report a few promising cases in which unsupervised pre-training can outperform its supervised counterpart. Code is made available at https://github.com/facebookresearch/SlowFast

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2104.14558v1) 
- [🔗 arXiv url](https://arxiv.org/abs/2104.14558v1)

---

### 29. An Empirical Study of Training Self-Supervised Vision Transformers

**Authors**: Xinlei Chen, Saining Xie, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2021-04-05  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

This paper does not describe a novel method. Instead, it studies a straightforward, incremental, yet must-know baseline given the recent progress in computer vision: self-supervised learning for Vision Transformers (ViT). While the training recipes for standard convolutional networks have been highly mature and robust, the recipes for ViT are yet to be built, especially in the self-supervised scenarios where training becomes more challenging. In this work, we go back to basics and investigate the effects of several fundamental components for training self-supervised ViT. We observe that instability is a major issue that degrades accuracy, and it can be hidden by apparently good results. We reveal that these results are indeed partial failure, and they can be improved when training is made more stable. We benchmark ViT results in MoCo v3 and several other self-supervised frameworks, with ablations in various aspects. We discuss the currently positive evidence as well as challenges and open questions. We hope that this work will provide useful data points and experience for future research.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2104.02057v4) 
- [🔗 arXiv url](https://arxiv.org/abs/2104.02057v4)

---

### 30. Exploring Simple Siamese Representation Learning

**Authors**: Xinlei Chen, Kaiming He  
**Affiliation**: MIT CSAIL  
**Published Date**: 2020-11-20  
**Primary Category**: cs.CV  

<details>
<summary>📄 Abstract (click to expand)</summary>

Siamese networks have become a common structure in various recent models for unsupervised visual representation learning. These models maximize the similarity between two augmentations of one image, subject to certain conditions for avoiding collapsing solutions. In this paper, we report surprising empirical results that simple Siamese networks can learn meaningful representations even using none of the following: (i) negative sample pairs, (ii) large batches, (iii) momentum encoders. Our experiments show that collapsing solutions do exist for the loss and structure, but a stop-gradient operation plays an essential role in preventing collapsing. We provide a hypothesis on the implication of stop-gradient, and further show proof-of-concept experiments verifying it. Our "SimSiam" method achieves competitive results on ImageNet and downstream tasks. We hope this simple baseline will motivate people to rethink the roles of Siamese architectures for unsupervised representation learning. Code will be made available.

</details>

**Resource**: 
- [📄 PDF url](https://arxiv.org/pdf/2011.10566v1) 
- [🔗 arXiv url](https://arxiv.org/abs/2011.10566v1)

---

## 📄 Licence
The paper is copyrighted by the original authors, and this project is for academic research purposes only.
