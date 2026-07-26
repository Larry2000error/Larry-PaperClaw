# Daily Reports

最近三天日报（最新在前）：

# [20260716](./202607/20260716.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦跨模态定位与行人重识别两大方向。地理定位领域关注证据推理与轨迹序列建模，以缓解地标偏差并提升连续观测下的定位精度。行人重识别研究呈现多模态融合趋势，可见光-红外跨模态学习与无监督方法成为热点，同时出现系统性综述梳理单模态到多模态的技术演进。

## ✨ 今日亮点

- HoloGeo提出证据驱动推理框架，缓解视觉地理定位中的地标偏差问题
- AlphaWiSE设计自适应权重插值策略，实现持续多模态表征学习
- 轨迹感知跨视角地理定位利用序列观测，提升视频-文本-卫星匹配精度

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260716] HoloGeo: Mitigating Landmark Bias in Geo-localization via Evidence-Driven Reasoning | Zhou Pengcheng, Liu Xuanyu, Yin Yanchen, Li Bobo, Wu Shengqiong, Lee Mong-Li, Hsu Wynne | National University of Singapore；Shandong University of Science and Technology；University of Oxford | HoloGeo通过证据驱动推理机制识别并抑制地标偏差，提升视觉地理定位的泛化能力。 | [#337](https://github.com/Larry2000error/Larry-PaperClaw/issues/337) |
| [20260716] Structural-Semantic Reciprocal Learning for Unsupervised Visible-Infrared Person Re-Identification | Tian Moyao, Liu Shijia, Yang Yan, Yuan Xin, Chen Minshi, Wang Wei, Wang Xiao | School of Computer Science and Technology, Wuhan University of Science and Technology；Hubei Province Key Laboratory of Intelligent Information Processing and Real-Time Industrial System, Wuhan University of Science and Technology；State Key Laboratory of Robotics and Intelligent Systems, Shenyang Institute of Automation, Chinese Academy of Sciences；China University of Chinese Academy of Sciences | 提出结构-语义互惠学习框架，在无监督设定下实现可见光-红外行人重识别。 | [#338](https://github.com/Larry2000error/Larry-PaperClaw/issues/338) |
| [20260716] AlphaWiSE: Adaptive Weight Interpolation for Continual Multimodal Representation Learning | Jain Sarthak, Hu Qiran, Zhu Zhen, Liu Yaoyao | University of Illinois Urbana-Champaign；Google DeepMind | AlphaWiSE采用自适应权重插值实现持续多模态学习，缓解跨模态检索中的灾难性遗忘。 | [#339](https://github.com/Larry2000error/Larry-PaperClaw/issues/339) |
| [20260716] Blurring Modal Boundaries: A Unified Survey from Single- to Multi-Modal Person Re-ldentification | Wang Xiao, Wang Bing, Yang Bin, Chen Cuiqun, Xu Xin, Ye Mang | School of Computer Science and Technology, Wuhan University of Science and Technology；Hubei Province Key Laboratory of Intelligent Information Processing and Real-time Industrial System, Wuhan University of Science and Technology；School of Computer, Wuhan University；School of Computer, Anhui University | 系统综述单模态到多模态行人重识别技术，涵盖文本-图像检索与可见光-红外匹配方法。 | [#340](https://github.com/Larry2000error/Larry-PaperClaw/issues/340) |
| [20260716] Trajectory-aware Cross-view Geo-localization with Sequential Observations | Gao Tianyi, Lin Jiayu, Beaulieu Danielle, Jacobs Nathan | Washington University in St. Louis | 利用轨迹序列建模实现跨视角地理定位，整合视频、文本描述与卫星图像进行路径匹配。 | [#342](https://github.com/Larry2000error/Larry-PaperClaw/issues/342) |

## 🔎 观察

- 地理定位研究正从静态图像匹配向动态序列推理演进，轨迹感知与证据推理成为提升鲁棒性的关键路径。
- 行人重识别领域多模态融合趋势显著，武汉科技大学团队在同日贡献两篇相关成果，显示该机构在此方向的集中布局。

---

Powered by OpenClaw🦞

---

# [20260714](./202607/20260714.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI领域研究聚焦于视觉-语言融合技术，东京大学与Kioxia联合团队提出零样本组合图像检索新范式，通过属性增强评分与LLM重排序摆脱视觉特征依赖，推动跨模态检索向轻量化、可解释方向发展。

## ✨ 今日亮点

- 零样本组合图像检索实现无需视觉编码器
- LLM重排序机制提升检索语义对齐精度
- 属性增强评分桥接文本与图像语义鸿沟

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260714] Towards Vision-Free CIR: Attribute-Augmented Scoring and LLM-Based Reranking for Zero-Shot Composed Image Retrieval | Shimada Ryotaro, Lin Yu-Chieh, Nozawa Yuji, Ng Youyang, Torii Osamu, Matsui Yusuke | The University of Tokyo；Kioxia Corporation | 该研究提出Vision-Free CIR框架，以属性增强评分结合LLM重排序实现零样本组合图像检索，摆脱传统视觉编码器依赖。 | [#334](https://github.com/Larry2000error/Larry-PaperClaw/issues/334) |

## 🔎 观察

- 视觉-语言模型'去视觉化'趋势显现，文本模态或成跨模态检索新主导
- LLM重排序介入检索流程可能增加推理延迟，需权衡精度与效率

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
