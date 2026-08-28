# Daily Reports

最近三天日报（最新在前）：

# [20260817](./202608/20260817.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦视觉定位与跨模态识别两大方向。视觉定位领域呈现从静态图像向视频序列、从粗粒度匹配向渐进式细粒度对齐的发展趋势；跨模态学习则关注可见光-红外场景下的行人重识别，强调多尺度特征分解与注意力机制的结合。数据集构建与真实环境适应性仍是关键挑战。

## ✨ 今日亮点

- YILDIZ-VPR发布密集覆盖、多环境条件的行人视角视觉定位数据集
- X²Localizer提出跨粒度渐进式跨视角视频地理定位框架
- 多尺度分解卷积网络优化可见光-红外跨模态行人重识别性能

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260817] YILDIZ-VPR: A Novel Dataset with Dense Coverage Under Diverse Environmental Conditions for Visual Place Recognition | Yildiz Serdar, Memiş Abbas, Varli Songül | Yildiz Technical University；Istanbul University；BILGEM, TUBITAK | YILDIZ-VPR构建了涵盖多样环境条件的密集覆盖行人视角视觉定位数据集，为VPR研究提供更贴近实际应用的基准。 | [#427](https://github.com/Larry2000error/Larry-PaperClaw/issues/427) |
| [20260817] X$^2$Localizer: Cross-grained Alignment for Progressive Cross-view Video Geo-localization | Zeng Zichao, Fan Weijia, Chen Yufan, June Moh Goo, Zheng Junwei, Liu Ruiping, Peng Kunyu, Zhang Jiaming, Stiefelhagen Rainer, Boehm Jan | University College London；Karlsruhe Institute of Technology；Hunan University；University of Alberta；Shenzhen University | X²Localizer通过跨粒度对齐机制实现渐进式跨视角视频地理定位，在有限时间预算下平衡检索效率与定位精度。 | [#428](https://github.com/Larry2000error/Larry-PaperClaw/issues/428) |
| [20260817] Multi-scale Decomposed Convolution Refinement Network for Visible-Infrared Person Re-Identification | Zheng Mingsheng, Jiang Zirui, Liu Bo, Chen Yupeng, Zhang Jun, Zhao Kai | School of Computer Science and Technology, Xinjiang University；Joint International Research Laboratory of Silk Road Multilingual Cognitive Computing, Xinjiang University | 多尺度分解卷积细化网络针对可见光-红外行人重识别任务，利用注意力机制与度量学习缓解模态差异问题。 | [#429](https://github.com/Larry2000error/Larry-PaperClaw/issues/429) |

## 🔎 观察

- 视觉定位研究正从单帧图像检索向时序视频理解演进，时间信息与渐进式推理成为提升定位精度的关键路径
- 跨模态行人重识别持续依赖多尺度特征学习与注意力机制，但现有方法在极端光照变化下的鲁棒性仍需验证

---

Powered by OpenClaw🦞

---

# [20260816](./202608/20260816.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究呈现两大方向：一是视觉语言基础模型的对齐优化，AlignJEPA提出预测式对齐新范式；二是面向体育视频的无训练多目标跟踪，强调相机运动补偿与重识别技术。整体趋势显示基础模型架构创新与特定场景高效推理并重。

## ✨ 今日亮点

- AlignJEPA融合JEPA预测架构与对比学习，实现遥感视觉语言基础模型的高效对齐
- 无训练长期多目标跟踪方案，通过相机运动补偿降低体育场景标注依赖
- ISRO与IIT Bombay等机构联合推进遥感大模型，强化印度空间技术自主能力

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260816] Training-Free Long-Term Multi-Object Tracking for Sports Video Analytics | Stanczyk Tomasz, Yoon Seongro, Bremond Francois | Inria；Université Côte d'Azur | 提出无需训练的长期多目标跟踪框架，结合相机运动补偿与重识别技术，专为体育视频分析设计。 | [#424](https://github.com/Larry2000error/Larry-PaperClaw/issues/424) |
| [20260816] AlignJEPA: Predictive Vision-Language Alignment for Remote Sensing Foundation Models | Md Aminur Hossain, Vaghasiya Omkumar, Rajeev Ranjan Dwivedi, Kurmi Vinod, Banerjee Biplab | Space Applications Centre, ISRO；CSRE, Indian Institute of Technology Bombay；Indian Institute of Science Education and Research (IISER) Bhopal | AlignJEPA将JEPA预测机制引入遥感视觉语言对齐，通过掩码预测与对比学习联合优化基础模型表征。 | [#425](https://github.com/Larry2000error/Larry-PaperClaw/issues/425) |

## 🔎 观察

- JEPA架构正从自然图像向遥感领域迁移，预测式学习或成为多模态遥感模型的新基线范式
- 无训练跟踪方案虽降低标注成本，但体育场景的剧烈相机运动对补偿算法鲁棒性提出更高要求

---

Powered by OpenClaw🦞

---

# [20260815](./202608/20260815.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI领域研究聚焦于跨模态学习技术，国防科技大学等机构提出MODAL框架，通过模型驱动的稀疏解耦与文本-图像差分滤波实现多模态目标重识别，推动特征解耦与稀疏编码在遥感场景中的应用。

## ✨ 今日亮点

- MODAL框架实现多模态目标重识别，融合稀疏编码与模型驱动深度学习
- 提出文本-图像差分滤波机制，优化跨模态特征对齐与判别
- 国防科大、湖南大学、合工大联合攻关特征解耦技术

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260815] MODAL: Multi-Modal Object Re-ID via Model-Driven Sparse Decoupling and Text-Image Differential Filtering | Huang Chengbo, Huang Jun-Jie, Lan Long, Liu Tianrui, Li Xueqiong, Peng Yuanxi, Liu Xinwang, Wang Meng | National University of Defense Technology；Hunan University；Hefei University of Technology | MODAL通过模型驱动稀疏解耦与文本-图像差分滤波，实现多模态目标重识别中的特征分离与噪声抑制。 | [#422](https://github.com/Larry2000error/Larry-PaperClaw/issues/422) |

## 🔎 观察

- 稀疏编码与深度学习的模型驱动结合成为跨模态Re-ID的新范式
- 多机构联合研究反映该方向在国防与民用遥感应用中的战略价值

---

Powered by OpenClaw🦞

---
