# Daily Reports

最近三天日报（最新在前）：

# [20260714](./202607/20260714.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日研究聚焦多模态图像检索新范式，东京大学与铠侠公司联合提出无视觉特征的组合图像检索框架。该工作突破传统依赖视觉编码器的局限，通过属性增强评分与大语言模型重排序实现零样本检索，为资源受限场景下的跨模态检索提供新思路。

## ✨ 今日亮点

- 首创Vision-Free CIR框架，摆脱视觉编码器依赖
- 属性增强评分机制实现细粒度语义对齐
- LLM重排序优化零样本场景下的检索精度

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260714] Towards Vision-Free CIR: Attribute-Augmented Scoring and LLM-Based Reranking for Zero-Shot Composed Image Retrieval | Shimada Ryotaro, Lin Yu-Chieh, Nozawa Yuji, Ng Youyang, Torii Osamu, Matsui Yusuke | The University of Tokyo；Kioxia Corporation | 该研究提出无需视觉特征的组合图像检索方法，通过属性文本增强与大语言模型重排序实现零样本跨模态检索。 | [#334](https://github.com/Larry2000error/Larry-PaperClaw/issues/334) |

## 🔎 观察

- 视觉-语言模型轻量化趋势明显，纯文本驱动的图像检索或成边缘计算新方向
- LLM重排序在检索任务中的增益机制值得进一步量化分析

---

Powered by OpenClaw🦞

---

# [20260712](./202607/20260712.md)
## 📌 今日概况

今日共检索候选论文 2 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日研究聚焦无人机视角下的车辆重识别技术，特别关注恶劣天气条件下的模型鲁棒性。越南研究团队通过合成数据模拟多种气象场景，为低空遥感智能交通应用提供了基准测试框架，反映出无人机交通监控向复杂环境适应的发展趋势。

## ✨ 今日亮点

- 无人机航拍车辆重识别任务面临天气干扰挑战
- 合成数据模拟为恶劣天气鲁棒性测试提供新路径
- 低空遥感与智能交通交叉应用持续深化

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260712] Benchmarking UAV-based Vehicle Re-Identification under Simulated Weather Conditions | Vu Minh Tran, Nguyen Khang | University of Information Technology；Vietnam National University Ho Chi Minh City | 越南学者构建无人机车辆重识别基准，系统评估模型在模拟雨雾等恶劣天气下的识别性能。 | [#333](https://github.com/Larry2000error/Larry-PaperClaw/issues/333) |

## 🔎 观察

- 合成天气数据成为解决真实场景标注稀缺的有效替代方案
- 无人机交通监控正从理想环境向复杂气象条件拓展

---

Powered by OpenClaw🦞

---

# [20260710](./202607/20260710.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦于跨视角重识别与自监督学习。四项工作涵盖动物重识别、室内导航、空地行人匹配及无监督地理定位，核心趋势为：利用视觉语言模型、超几何空间表征与弹性自训练机制，解决跨域、跨视角场景下的身份关联难题，参数高效适配与伪标签净化成为关键技术路径。

## ✨ 今日亮点

- 超几何学习引入空地行人重识别，缓解欧氏空间嵌入失真
- 视觉语言模型结合连续元数据条件，实现动物重识别参数高效适配
- 弹性匹配与自适应净化机制，支撑无监督跨视角地理定位稳定训练

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260710] Parameter-Efficient Vision-Language Adaptation with Continuous Metadata Conditioning for Animal Re-Identification | Anil Osman Tur, Tonje Knutsen Sordalen, Kim Tallaksen Halvorsen, Beyan Cigdem | Department of Computer Science, University of Verona；Institute of Marine Research；University of Agder, Centre for Coastal Research | 提出连续元数据条件化的参数高效视觉语言适配方法，用于动物重识别任务。 | [#328](https://github.com/Larry2000error/Larry-PaperClaw/issues/328) |
| [20260710] REMIND: RE-Identification with Memory for INDoor Navigation | Diaz-Pereda Pablo, Rodriguez-Ramos Alejandro, Perez-Saura David, Campoy Pascual | Institution unavailable | REMIND框架融合DINOv3特征与视觉记忆机制，服务室内导航场景的多目标重识别。 | [#329](https://github.com/Larry2000error/Larry-PaperClaw/issues/329) |
| [20260710] HiHR: Hierarchical Hyperbolic Representation for Aerial-Ground Person Re-Identification | Yang Qiwei, Zhang Pingping | Dalian University of Technology | HiHR构建层次化双曲表征空间，解决无人机与地面监控跨视角行人匹配的几何失真问题。 | [#330](https://github.com/Larry2000error/Larry-PaperClaw/issues/330) |
| [20260710] STEAM: Stable Self-Training with Elastic Matching and Adaptive Purification | Wang Shaoxiang, Zhang Kejia, Pan Haiwei, Zhang Lan | Harbin Engineering University, School of Computer Science and Technology；Northeast Forestry University, School of Computer and Artificial Intelligence | STEAM通过弹性匹配与自适应净化实现稳定自训练，用于无监督跨视角地理定位。 | [#331](https://github.com/Larry2000error/Larry-PaperClaw/issues/331) |

## 🔎 观察

- 重识别任务正从单一模态向视觉语言融合演进，元数据条件化成为提升泛化性的新范式
- 超几何空间与自训练净化技术的引入，反映领域对表征几何结构与噪声鲁棒性的双重关注

---

Powered by OpenClaw🦞

---
