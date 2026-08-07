# Daily Reports

最近三天日报（最新在前）：

# [20260803](./202608/20260803.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦多模态表示学习与跨视角识别技术。四篇论文涵盖知识型视觉问答、空-地行人重识别、开放集动物重识别及通用多模态嵌入，核心趋势在于通过贝叶斯重加权、3D表征、图聚类校准等方法提升模型鲁棒性与泛化能力，尤其关注跨域、跨视角及开放场景下的识别难题。

## ✨ 今日亮点

- 贝叶斯数据重加权策略有效缓解多模态检索中的假阴性噪声问题
- VR3D框架通过视角鲁棒的3D表征学习突破空-地行人重识别瓶颈
- WildFusion方法结合相似度校准与图聚类实现开放集动物个体识别

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260803] Bayesian Data Reweighting Improves Multimodal Retrieval for Knowledge-Based Visual Question Answering | Sun Jingchen, Han Shaobo, Zhang Ruiyi, Naresh Kumar Devulapally, Liu Ming, Long Yitao, Vishnu Suresh Lokhande, Chen Changyou | University at Buffalo；NEC Laboratories America；Adobe Research；Iowa State University；New York University | 提出贝叶斯数据重加权框架，通过对比学习优化多模态检索，降低知识型视觉问答中的假阴性样本干扰。 | [#387](https://github.com/Larry2000error/Larry-PaperClaw/issues/387) |
| [20260803] VR3D: View-Robust 3D Representation Learning for Aerial-Ground Person Re-Identification | Ji Chao, Xuan Shiyu, Li Zechao | Nanjing University of Science and Technology | 构建视角鲁棒的3D表征学习网络VR3D，解决无人机与地面摄像头间行人重识别的跨视角匹配难题。 | [#388](https://github.com/Larry2000error/Larry-PaperClaw/issues/388) |
| [20260803] Calibrated Similarity and Graph Clustering for Open-Set Animal Re-Identification | ElBassat Mohamed, Elkerdany Seifeldin, ElBialy Mohamed, Abouelhamd Gamal, Ghoneim Jana, Elkady Assem, Elboraay Mohamed, Semenova Nelly | Made In Alexandria Artificial Intelligence Team；Faculty of Computer Science and Engineering, Alamein International University；Faculty of Computers and Data Science, Alexandria University；Faculty of Engineering, Alexandria University；Alexandria Higher Institute of Engineering and Technology；Moscow Pedagogical State University | 设计WildFusion系统，融合相似度校准与图聚类技术，提升开放集场景下野生动物个体重识别的可靠性。 | [#389](https://github.com/Larry2000error/Larry-PaperClaw/issues/389) |
| [20260803] Illuminating Visual Identity in Universal Multimodal Embeddings | Cao Jiawei, Feng Junyi, Hua Jiashen, Huang Ziheng, Deng Bing, Wu Kaijie, Gu Chaochen, Ye Jieping | Shanghai Jiao Tong University；Alibaba Group | 探索多模态大语言模型中的视觉身份保持机制，优化通用嵌入空间下的实例检索与跨模态对齐性能。 | [#390](https://github.com/Larry2000error/Larry-PaperClaw/issues/390) |

## 🔎 观察

- 重识别任务正从封闭集向开放集、从单一模态向跨视角/跨域扩展，3D表征与图结构方法成为关键突破口
- 多模态学习研究重心从规模扩张转向质量优化，数据重加权和嵌入空间校准技术受到更多关注

---

Powered by OpenClaw🦞

---

# [20260730](./202607/20260730.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦视觉检索与多模态学习，涵盖视觉语言模型优化、人脸超分辨率、多模态大语言模型图像检索及脑电信号视觉解码四大方向。学术界正通过稀疏令牌选择、细粒度上下文学习与跨模态特征聚合等技术，提升复杂场景下的检索精度与效率。

## ✨ 今日亮点

- ReToken提出单令牌稀疏选择机制，显著压缩视觉语言模型KV缓存
- FiRE引入细粒度上下文学习，增强多模态大语言模型复杂图像检索能力
- EEG-EditBench构建可控图像编辑基准，探针脑电视觉解码模型性能边界

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260730] ReToken: One Token to Improve Vision-Language Models for Visual Retrieval | Xiao Yao, Tan Reuben, Zhu Zhen, Wu Yuqun, Gao Jianfeng, Hoiem Derek | University of Illinois at Urbana-Champaign；Microsoft Research；Google DeepMind | ReToken通过稀疏令牌选择策略优化视觉语言模型长上下文处理能力，降低KV缓存开销。 | [#376](https://github.com/Larry2000error/Larry-PaperClaw/issues/376) |
| [20260730] Collaborative Feature Aggregation for Face Super-Resolution and Robust Re-Identification | Hwang Juheon, Kim Taewan, Kang Jiwoo | Yonsei University；Dongduk Women's University；Sookmyung Women's University | 该研究提出协同特征聚合框架，联合优化人脸超分辨率与跨视角行人重识别任务。 | [#377](https://github.com/Larry2000error/Larry-PaperClaw/issues/377) |
| [20260730] FiRE: Enhancing MLLMs with Fine-Grained Context Learning for Complex Image Retrieval | Hou Bohan, Lin Haoqiang, Song Xuemeng, Wen Haokun, Liu Meng, Hu Yupeng, Zhao Xiangyu | Shandong University；City University of Hong Kong；Harbin Institute of Technology (Shenzhen)；Shandong Jianzhu University | FiRE设计细粒度上下文学习机制，提升多模态大语言模型在组合图像检索中的复杂推理表现。 | [#378](https://github.com/Larry2000error/Larry-PaperClaw/issues/378) |
| [20260730] EEG-EditBench: Probing Visual Information in EEG-Image Retrieval Models with Controlled Image Edits | Zhang Kaifan, He Lihuo, Ji Yuqi, Ke Junjie, Wu Lukun, You Tianhao, Gao Xinbo | School of Electronic Engineering, Xidian University；School of Software, Tsinghua University；Chongqing University of Posts and Telecommunications | EEG-EditBench建立可控图像编辑评估体系，系统量化脑电-图像检索模型的视觉信息解码能力。 | [#383](https://github.com/Larry2000error/Larry-PaperClaw/issues/383) |

## 🔎 观察

- 视觉检索领域呈现'大模型轻量化'与'细粒度理解'并行的技术路线分化
- 脑电-视觉跨模态研究从概念验证迈向标准化基准建设，临床转化潜力值得关注

---

Powered by OpenClaw🦞

---

# [20260729](./202607/20260729.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日仅收录1篇研究，聚焦水产养殖场景下的多目标跟踪技术。该工作针对鱼类外观相似导致的身份混淆问题，提出双分支弹性匹配框架，兼顾实时性与边缘部署需求，体现农业智能化与轻量化AI的交叉趋势。

## ✨ 今日亮点

- 双分支架构解决鱼类外观相似导致的身份切换难题
- 弹性几何对应机制提升遮挡场景下的跟踪稳定性
- 面向边缘设备优化，满足水产养殖实时监测需求

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260729] When Fish Look Alike: Tracking Identities with Dual-branch Elasticity | Lee Vran, Liu Xin, Wei Yijie, Liu Yeqiang, Hwa Liang Leo, Li Zhenbo | China Agricultural University；Beijing Normal University；National University of Singapore | 中国农业大学等提出双分支弹性网络，通过几何对应学习解决养殖鱼群外观相似、密集遮挡下的身份保持问题，支持边缘端实时部署。 | [#375](https://github.com/Larry2000error/Larry-PaperClaw/issues/375) |

## 🔎 观察

- 农业垂直场景的跟踪任务正从通用模型向物种特异性设计演进，对领域知识嵌入提出更高要求
- 边缘部署与实时性约束成为水产养殖AI落地的关键瓶颈，轻量化架构创新空间显著

---

Powered by OpenClaw🦞

---
