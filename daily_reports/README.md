# Daily Reports

最近三天日报（最新在前）：

# [20260601](./202606/20260601.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦重识别任务的核心挑战：跨模态优化冲突与泛化瓶颈。两篇论文分别从行人Re-ID的图像-文本多任务优化矛盾，以及车辆Re-ID的域泛化极限评估切入，体现该领域对模型鲁棒性与实际部署可靠性的深度关注。

## ✨ 今日亮点

- 行人Re-ID中图像与文本模态的优化目标冲突首次被系统分析
- 车辆重识别泛化性能存在显著瓶颈，现有评估方法暴露局限性
- 跨模态学习与域泛化成为Re-ID领域两大关键研究方向

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260601] Towards Resolving Optimization Conflicts Between Image- and Text-Based Person Re-Identification | Kvanchiani Karina, Mamedov Timur | Tevian；Lomonosov Moscow State University | 提出解决行人Re-ID中基于图像与文本模态的优化冲突方法，提升跨模态表征学习一致性。 | [#236](https://github.com/Larry2000error/Larry-PaperClaw/issues/236) |
| [20260601] Generalization Limits in Vehicle Re-Identification | Anis Yassine Ben Mabrouk, Tadros Antoine, Rafael Grompone von Gioi, Facciolo Gabriele, Davy Axel, Verschae Rodrigo | Université Paris-Saclay, ENS Paris-Saclay, CNRS, Centre Borelli；HGH Infrared Systems；Institut Universitaire de France；Universidad Técnica Federico Santa María | 系统评估车辆Re-ID方法的泛化极限，揭示现有模型在跨场景部署时的性能衰减问题。 | [#237](https://github.com/Larry2000error/Larry-PaperClaw/issues/237) |

## 🔎 观察

- Re-ID研究正从追求单一指标提升转向关注多任务协同与真实场景鲁棒性，反映领域成熟度提升。
- 跨模态与泛化问题的并置出现，暗示智能监控系统的实际部署需求正在驱动基础研究范式转变。

---

Powered by OpenClaw🦞

---

# [20260530](./202605/20260530.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦跨模态理解与定位技术。三篇论文分别探索跨视角地理定位、遥感图像检索及热成像视觉语言模型，体现多模态融合与自监督学习成为核心趋势，Mamba架构与JEPA框架等新兴方法开始渗透遥感领域。

## ✨ 今日亮点

- DINO-GFSA将Mamba序列聚合引入无人机自定位，结合语义门控融合提升跨视角匹配精度
- CR-JEPA首次将联合嵌入预测架构应用于遥感跨模态检索，推动自监督表征学习
- T-CLIP突破可见光限制，实现热成像与语言的对齐预训练，拓展低光环境感知能力

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260530] DINO-GFSA: Geo-Localization via Semantic Gated Fusion and Mamba-based Sequential Aggregation | Hu Beier, Guo Yuanshen, Cai Jialu, Li Chengwei, Wang Yong, Wu Shunan, Wu Zhigang | Sun Yat-sen University | DINO-GFSA提出基于DINOv3特征与Mamba序列聚合的跨视角地理定位方法，通过语义门控融合模块优化无人机自定位性能。 | [#231](https://github.com/Larry2000error/Larry-PaperClaw/issues/231) |
| [20260530] CR-JEPA: Cross-Modal Joint-Embedding Predictive Learning for Remote Sensing Image Retrieval | Md Aminur Hossain, Ayush V. Patel, Dube Nitant, Banerjee Biplab | Space Applications Centre, Indian Space Research Organisation；Centre of Studies in Resources Engineering, Indian Institute of Technology Bombay | CR-JEPA构建跨模态联合嵌入预测架构，以自监督方式学习遥感图像与文本的共享表征，提升检索任务效率。 | [#232](https://github.com/Larry2000error/Larry-PaperClaw/issues/232) |
| [20260530] T-CLIP: Enabling Thermal Perception for Contrastive Language-Image Pretraining | Qazi Tayeba, Maheshwari Ayush, Mukherjee Prerana, Lall Brejesh | Indian Institute of Technology Delhi；NVIDIA AI Technology Center；Jawaharlal Nehru University | T-CLIP扩展CLIP框架至热成像域，建立热图像-文本对比预训练范式，增强模型在低光照条件下的视觉理解能力。 | [#233](https://github.com/Larry2000error/Larry-PaperClaw/issues/233) |

## 🔎 观察

- Mamba架构正从NLP向遥感视觉任务迁移，其线性复杂度特性对高分辨率卫星影像处理具有潜在优势
- 跨模态检索技术路线分化：JEPA类生成式表征与CLIP类对比学习并存，遥感领域尚未形成统一范式

---

Powered by OpenClaw🦞

---

# [20260529](./202605/20260529.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦多模态大模型的空间推理与地理定位能力，涵盖具身智能基准测试、持续学习检索及密集城市场景视觉定位。学界正推动MLLM从分类任务向动态推理与真实环境适应演进，同时关注GPS拒止条件下的鲁棒定位方案。

## ✨ 今日亮点

- ERGeoBench构建具身推理与地理定位综合评测体系，填补MLLM空间认知能力评估空白
- 动态适配器路由机制解决多模态检索中的持续学习难题，实现任务自适应模型融合
- 中国城中村案例验证视觉定位在密集城市环境的可行性，为GPS拒止导航提供新思路

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260529] ERGeoBench:A Comprehensive Benchmark for Embodied Reasoning and Geo-localization in Multimodal Large Language Models | Xue Kaiwen, Wei Tao, Zhang Guoxin, Ou Zhonghong, Lu Kaoyan, Feng Yu, Zhu Yifan, Luo Haoran | Institution unavailable | ERGeoBench建立多模态大模型具身推理与地理定位基准，系统评估视觉感知与空间推理能力。 | [#226](https://github.com/Larry2000error/Larry-PaperClaw/issues/226) |
| [20260602] Beyond Classification: Dynamic Adapter Routing for Continual Multimodal Retrieval | Dobrzeniecka Alicja, Szatkowski Filip, Cygert Sebastian, Łukasik Szymon, Twardowski Bartłomiej | NASK National Research Institute；IDEAS Research Institute；Warsaw University of Technology；Universitat Autonoma de Barcelona | 提出动态适配器路由方法，通过任务特定适配器选择与模型合并实现持续多模态检索。 | [#227](https://github.com/Larry2000error/Larry-PaperClaw/issues/227) |
| [20260602] Vision-Based Localization in Dense Urban Environments: A Case Study of an Urban Village in China | Wu Menglin, Cao Rui | The Hong Kong University of Science and Technology (Guangzhou) | 以中国城中村为案例，验证全景视觉定位在密集城市GPS拒止环境中的有效性。 | [#229](https://github.com/Larry2000error/Larry-PaperClaw/issues/229) |

## 🔎 观察

- 具身智能与地理定位交叉成为新热点，但现有MLLM空间推理能力缺乏标准化评测，ERGeoBench或推动该领域规范化发展
- 持续学习与模型合并技术向多模态检索渗透，动态路由机制可能缓解视觉-语言模型任务增量时的灾难性遗忘问题

---

Powered by OpenClaw🦞

---
