# Daily Reports

最近三天日报（最新在前）：

# [20260716](./202607/20260716.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日研究聚焦跨模态感知与地理定位两大方向。视觉-语言模型在地理定位中的推理能力持续深化，轨迹序列与证据驱动成为新范式；行人重识别领域呈现多模态融合趋势，可见光-红外跨模态学习与无监督方法受到关注；持续学习与权重插值技术为多模态表征提供新思路。

## ✨ 今日亮点

- HoloGeo提出证据驱动推理框架，缓解地标偏差对视觉地理定位的影响
- 两篇行人重识别论文分别探索结构-语义互惠学习与统一多模态综述
- AlphaWiSE通过自适应权重插值实现持续多模态表征学习

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260716] HoloGeo: Mitigating Landmark Bias in Geo-localization via Evidence-Driven Reasoning | Zhou Pengcheng, Liu Xuanyu, Yin Yanchen, Li Bobo, Wu Shengqiong, Lee Mong-Li, Hsu Wynne | National University of Singapore；Shandong University of Science and Technology；University of Oxford | HoloGeo构建证据驱动推理框架，通过显式视觉证据聚合缓解地标偏差，提升视觉地理定位的泛化能力。 | [#337](https://github.com/Larry2000error/Larry-PaperClaw/issues/337) |
| [20260716] Structural-Semantic Reciprocal Learning for Unsupervised Visible-Infrared Person Re-Identification | Tian Moyao, Liu Shijia, Yang Yan, Yuan Xin, Chen Minshi, Wang Wei, Wang Xiao | School of Computer Science and Technology, Wuhan University of Science and Technology；Hubei Province Key Laboratory of Intelligent Information Processing and Real-Time Industrial System, Wuhan University of Science and Technology；State Key Laboratory of Robotics and Intelligent Systems, Shenyang Institute of Automation, Chinese Academy of Sciences；China University of Chinese Academy of Sciences | 提出结构-语义互惠学习框架，以无监督方式联合挖掘可见光与红外模态的结构与语义一致性。 | [#338](https://github.com/Larry2000error/Larry-PaperClaw/issues/338) |
| [20260716] AlphaWiSE: Adaptive Weight Interpolation for Continual Multimodal Representation Learning | Jain Sarthak, Hu Qiran, Zhu Zhen, Liu Yaoyao | University of Illinois Urbana-Champaign；Google DeepMind | AlphaWiSE设计自适应权重插值策略，在持续学习场景下保持多模态表征的稳定性与可塑性平衡。 | [#339](https://github.com/Larry2000error/Larry-PaperClaw/issues/339) |
| [20260716] Blurring Modal Boundaries: A Unified Survey from Single- to Multi-Modal Person Re-ldentification | Wang Xiao, Wang Bing, Yang Bin, Chen Cuiqun, Xu Xin, Ye Mang | School of Computer Science and Technology, Wuhan University of Science and Technology；Hubei Province Key Laboratory of Intelligent Information Processing and Real-time Industrial System, Wuhan University of Science and Technology；School of Computer, Wuhan University；School of Computer, Anhui University | 系统综述单模态到多模态行人重识别演进，涵盖文本-图像检索与可见光-红外匹配等跨模态任务。 | [#340](https://github.com/Larry2000error/Larry-PaperClaw/issues/340) |
| [20260716] Trajectory-aware Cross-view Geo-localization with Sequential Observations | Gao Tianyi, Lin Jiayu, Beaulieu Danielle, Jacobs Nathan | Washington University in St. Louis | 引入轨迹感知机制，利用序列观测与路线描述实现跨视角视频-文本-卫星地理定位。 | [#342](https://github.com/Larry2000error/Larry-PaperClaw/issues/342) |

## 🔎 观察

- 地理定位任务正从静态图像匹配向动态序列推理演进，轨迹信息与语言描述成为关键输入模态。
- 行人重识别领域呈现明显的多模态融合趋势，武汉科技大学团队在同日贡献两篇相关研究，显示该方向的活跃程度。

---

Powered by OpenClaw🦞

---

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
