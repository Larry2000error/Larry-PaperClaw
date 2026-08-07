# Daily Reports

最近三天日报（最新在前）：

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

# [20260728](./202607/20260728.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦无人机视角地理定位技术，涵盖持续学习、跨模态检索与鲁棒性增强三大方向。西安交大团队提出几何感知适配器解决增量学习遗忘问题；中国海洋大学构建昼夜统一基准；哈工大联合团队针对退化场景设计可靠性引导的证据融合机制。行人重识别领域亦有邻域特征交互新进展。

## ✨ 今日亮点

- GeoMFD引入边缘场蒸馏，缓解无人机地理定位中的灾难性遗忘
- 首个昼夜跨模态无人机定位基准，统一处理可见光与红外影像
- ReLATE构建可靠性引导框架，提升退化场景下的跨视图匹配鲁棒性

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260728] GeoMFD: Continual Drone-View Geo-Localization with Geometry-Aware Adapter and Margin-Field Distillation | Chen Zhongwei, Rong Hai-jun, Zhang Tao, Nie Xianfeng, Zhang Xiangbao, Li Guoqi, Yang Zhao-Xu | School of Aerospace Engineering, Xi'an Jiaotong University；Institute of Automation, Chinese Academy of Sciences | GeoMFD通过几何感知适配器与边缘场蒸馏，实现无人机视角地理定位的持续学习，缓解域增量场景下的知识遗忘。 | [#370](https://github.com/Larry2000error/Larry-PaperClaw/issues/370) |
| [20260728] A Unified Benchmark and Modality-Adaptive Network for Day-and-Night Drone-View Geo-Localization | Xu Songtianhao, Chen Zhongwei, Yang Zhao-Xu, Wang Weifeng | Ocean University of China | 提出昼夜无人机定位统一基准与模态自适应网络，首次系统解决可见光-红外跨模态检索中的光照变化挑战。 | [#371](https://github.com/Larry2000error/Larry-PaperClaw/issues/371) |
| [20260728] ReLATE: Reliability-Guided Evidence Fusion for Robust UAV--Satellite cross-view Geo-Localization | Jiang Haochen, Pan Jialei, Sun Yuzhe, Dong Zhe, Ren Lecheng, Gu Yanfeng, Liu Tianzhu | School of Electronics and Information Engineering, Harbin Institute of Technology；National Key Laboratory of Radar Detection and Sensing, Nanjing Research Institute of Electronics Technology；School of Electrical and Electronic Engineering, University of Manchester | ReLATE设计可靠性引导的证据融合机制，针对模糊、噪声等退化场景提升UAV-卫星跨视图定位的鲁棒性。 | [#372](https://github.com/Larry2000error/Larry-PaperClaw/issues/372) |
| [20260728] ANFI: Rethinking Neighbor Feature Interaction in Person Re-ID | Li Xulin, Lu Yan, Liu Bin, Li Jiaze, Yang Qinhong, Gong Tao, Chu Qi, Yu Nenghai | University of Science and Technology of China；Anhui Province Key Laboratory of Digital Security；The Chinese University of Hong Kong | ANFI重新思考行人重识别中的邻域特征交互，通过自适应加权抑制噪声邻居干扰，优化亲和关系建模。 | [#373](https://github.com/Larry2000error/Larry-PaperClaw/issues/373) |

## 🔎 观察

- 无人机地理定位正从单一模态向持续学习、跨模态统一、退化鲁棒性多维度演进，技术栈日趋复杂
- 中国高校在该领域形成显著集群优势，西交大、哈工大、中国海洋大学等机构贡献核心方法论创新

---

Powered by OpenClaw🦞

---
