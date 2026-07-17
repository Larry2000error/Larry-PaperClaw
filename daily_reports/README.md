# Daily Reports

最近三天日报（最新在前）：

# [20260714](./202607/20260714.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日仅收录一篇论文，聚焦组合图像检索（CIR）领域的前沿探索。该研究提出无需视觉输入的CIR新范式，通过属性增强评分与大语言模型重排序实现零样本检索，标志着CIR技术向轻量化、语义驱动方向演进，对降低计算成本与拓展应用场景具有潜在价值。

## ✨ 今日亮点

- 提出Vision-Free CIR新框架，摆脱对视觉特征的依赖
- 融合属性增强评分与LLM重排序，实现零样本检索能力
- 东京大学与铠侠公司合作，产学研结合推动技术落地

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260714] Towards Vision-Free CIR: Attribute-Augmented Scoring and LLM-Based Reranking for Zero-Shot Composed Image Retrieval | Shimada Ryotaro, Lin Yu-Chieh, Nozawa Yuji, Ng Youyang, Torii Osamu, Matsui Yusuke | The University of Tokyo；Kioxia Corporation | 该研究提出无需视觉输入的组合图像检索方法，通过属性增强评分与LLM重排序实现零样本检索，为CIR轻量化部署提供新思路。 | [#334](https://github.com/Larry2000error/Larry-PaperClaw/issues/334) |

## 🔎 观察

- Vision-Free范式或成CIR新趋势，但属性描述的完备性与准确性将直接影响检索效果
- LLM重排序引入推理开销，需在精度提升与实时性之间权衡取舍

---

Powered by OpenClaw🦞

---

# [20260712](./202607/20260712.md)
## 📌 今日概况

今日共检索候选论文 2 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日仅收录一篇论文，聚焦无人机视角下的车辆重识别技术。该研究针对模拟天气条件下的模型鲁棒性进行基准测试，体现了遥感AI领域对复杂环境适应性与合成数据应用的关注趋势，为低空遥感智能监控的可靠性评估提供参考。

## ✨ 今日亮点

- 构建无人机车辆重识别天气鲁棒性基准测试框架
- 利用合成数据模拟多样化气象干扰场景
- 填补航拍视角下恶劣天气识别性能评估空白

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260712] Benchmarking UAV-based Vehicle Re-Identification under Simulated Weather Conditions | Vu Minh Tran, Nguyen Khang | University of Information Technology；Vietnam National University Ho Chi Minh City | 该论文提出无人机车辆重识别在模拟天气条件下的基准测试方法，评估模型对合成气象干扰的鲁棒性。 | [#333](https://github.com/Larry2000error/Larry-PaperClaw/issues/333) |

## 🔎 观察

- 单一论文收录反映当日遥感AI领域发文活跃度较低，或存在期刊会议截稿周期影响
- 合成数据驱动天气鲁棒性研究成为低成本验证极端场景的有效路径，但模拟与真实域差距仍需关注

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
