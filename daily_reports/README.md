# Daily Reports

最近三天日报（最新在前）：

# [20260518](./202605/20260518.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦于跨域视觉检索与细粒度识别。电商场景下文本引导的隐式定位、空地跨视角行人重识别、以及水产养殖中基于弱监督的鱼类个体追踪成为三大方向，体现视觉AI向垂直领域精细化发展的趋势。

## ✨ 今日亮点

- 快手提出文本引导隐式细粒度定位方法，提升电商多模态检索精度
- 中山大学团队解决空地视角行人重识别难题，实现跨视角语义对齐
- 挪威团队利用补丁集成与弱轨迹标签，实现鲑鱼个体稳健重识别

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260518] TIGER-FG: Text-Guided Implicit Fine-Grained Grounding for E-commerce Retrieval | Sun Xinyu, Dai Huangyu, Mao Lingtao, Zheng Zexin, Liang Zihan, Chen Ben, Lei Chenyi, Ou Wenwu | Kuaishou Technology | 快手提出TIGER-FG框架，通过文本引导隐式细粒度定位实现电商图像到多模态检索，无需显式边界框标注。 | [#203](https://github.com/Larry2000error/Larry-PaperClaw/issues/203) |
| [20260518] View-Aware Semantic Alignment for Aerial-Ground Person Re-Identification | Zhang Quan, Cai Zeqiang, Zhao Peiming, Wu Jingze, Wu Cailun, Chen Hongbo, Lai Jianhuang | Sun Yat-sen University；Pazhou Lab (HuangPu)；Guangdong Province Key Laboratory of Information Security Technology；Key Laboratory of Machine Intelligence and Advanced Computing, Ministry of Education | 中山大学联合琶洲实验室提出视角感知语义对齐网络，解决无人机与地面摄像头间的行人跨视角重识别问题。 | [#204](https://github.com/Larry2000error/Larry-PaperClaw/issues/204) |
| [20260518] Patch Ensembles for Robust Salmon Re-Identification with Weak Trajectory Labels | Espen Uri Høgstedt, Schellewald Christian, Stahl Annette, Mester Rudolf | Department of Computer Science, Norwegian University of Science and Technology；SINTEF Ocean；Department of Engineering Cybernetics, Norwegian University of Science and Technology | 挪威科技大学团队设计补丁集成方法，利用弱轨迹标签训练模型，实现水下环境中鲑鱼个体的稳健重识别。 | [#205](https://github.com/Larry2000error/Larry-PaperClaw/issues/205) |

## 🔎 观察

- 重识别任务正从传统安防向农业水产等新兴垂直领域扩展，弱监督技术降低标注成本成为关键。
- 跨模态与跨视角对齐仍是核心挑战，文本引导与语义对齐策略显示出较强的任务适配性。

---

Powered by OpenClaw🦞

---

# [20260515](./202605/20260515.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI研究聚焦自监督多模态表示学习，SOLAR框架通过联合学习优化对称多模态检索任务，采用对比学习实现图像-文本对齐，为遥感数据跨模态检索提供新思路。

## ✨ 今日亮点

- SOLAR提出自监督联合学习框架，统一处理对称多模态检索任务
- 采用对比学习机制优化图像-文本表征对齐效果
- 无需标注数据，降低遥感多模态应用的数据依赖门槛

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260515] SOLAR: Self-supervised Joint Learning for Symmetric Multimodal Retrieval | Yang Wenjie, Yu Hang, Guo Yuyu, Di Peng | Asymmetric Symmetric | SOLAR提出自监督联合学习框架，通过对称多模态检索优化图像-文本表征对齐，实现无需标注的遥感跨模态检索。 | [#200](https://github.com/Larry2000error/Larry-PaperClaw/issues/200) |

## 🔎 观察

- 自监督学习正成为降低遥感数据标注成本的主流技术路径
- 多模态检索的对称性设计或成提升跨模态一致性的关键方向

---

Powered by OpenClaw🦞

---

# [20260514](./202605/20260514.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦于跨模态视觉定位与多模态检索的基准反思。无人机地理定位领域探索道路图作为免费几何先验，以提升天气不变性；图像检索领域则质疑组合式基准是否真正需要多模态融合，揭示单模态捷径问题。两研究均体现对现有范式的方法论审视。

## ✨ 今日亮点

- GeoFuse利用道路图几何先验实现天气不变无人机定位，降低跨视角匹配成本
- 组合图像检索基准存在单模态捷径，多模态融合必要性遭系统质疑
- 跨模态学习研究从追求性能转向审视基准有效性，方法论趋于严谨

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260514] Road Maps as Free Geometric Priors: Weather-Invariant Drone Geo-Localization with GeoFuse | Fang Yunsong, Wang Tingyu, Zheng Zhedong | University of Macau；Hangzhou Dianzi University | GeoFuse提出道路图作为免费几何先验，通过跨模态融合实现天气不变的无人机地理定位，缓解卫星-无人机视角匹配中的外观退化问题。 | [#197](https://github.com/Larry2000error/Larry-PaperClaw/issues/197) |
| [20260514] Do Composed Image Retrieval Benchmarks Require Multimodal Composition? | Attimonelli Matteo, Alessandro De Bellis, Aryo Pradipta Gema, Saxena Rohit, Sekoyan Monica, Kwan Wai-Chung, Pomo Claudio, Suglia Alessandro, Jannach Dietmar, Tommaso Di Noia, Minervini Pasquale | Politecnico di Bari；Sapienza University of Rome；University of Edinburgh；University of Klagenfurt；Miniml.AI | 研究系统分析组合图像检索基准，发现单模态捷径可达成强性能，质疑多模态组合在该任务中的必要性假设。 | [#198](https://github.com/Larry2000error/Larry-PaperClaw/issues/198) |

## 🔎 观察

- 地理定位研究正从纯视觉匹配转向利用结构化地图先验，体现先验知识注入的趋势
- 多模态基准的捷径分析揭示评估体系漏洞，提示领域需重建更鲁棒的测试协议

---

Powered by OpenClaw🦞

---
