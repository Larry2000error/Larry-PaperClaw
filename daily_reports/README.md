# Daily Reports

最近三天日报（最新在前）：

# [20260617](./202606/20260617.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦跨模态检索的精细化与交互式创新。三篇论文分别从双目标编码、生成式视觉消歧、低注意力区域编码三个维度，探索如何突破传统视觉-语言模型的检索瓶颈，提升复杂场景下的检索精度与用户体验。

## ✨ 今日亮点

- DREAM提出双目标编码框架，强化视频-文本跨模态时序建模能力
- 生成式视觉消歧方法通过交互式生成替代文本查询，优化组合图像检索
- LARE针对显著性偏差问题，显式编码低注意力区域以改善密集场景检索

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260617] DREAM: Extending Vision-Language Models with Dual-Objective Encoding for Cross-Modal Retrieval | Ullah Kaleem, Hussain Altaf, Munsif Muhammad, Sung Wook Baik | Institution unavailable | DREAM通过双目标编码扩展视觉-语言模型，实现视频-文本跨模态检索中的时序对齐与语义匹配联合优化。 | [#271](https://github.com/Larry2000error/Larry-PaperClaw/issues/271) |
| [20260617] Show, Don't Ask: Generative Visual Disambiguation for Composed Image Retrieval with Turn-Valid Coverage | Tran Amsisan, Le Baogh, Tuan Kiet Pham, Sui Yang Guang | Institution unavailable | 提出生成式视觉消歧框架，利用共形预测保证交互式组合图像检索的覆盖有效性，以视觉生成替代文本歧义。 | [#272](https://github.com/Larry2000error/Larry-PaperClaw/issues/272) |
| [20260617] LARE: Low-Attention Region Encoding for Text-Image Retrieval | Alquwayfili Abdulmalik, Almeshal Faisal, Almajnouni Jumanah, Alotaibi Leena, Alhajari Faisal, Alkhrashi Mohammed, Almuhrij Alreem, Aldwyish Abdullah, Aljadaany Raied, Alamri Huda, Muhammad Kamran J. Khan | Institution unavailable | LARE显式编码图像低注意力区域，缓解显著性偏差，提升密集场景下细粒度文本-图像检索性能。 | [#273](https://github.com/Larry2000error/Larry-PaperClaw/issues/273) |

## 🔎 观察

- 跨模态检索正从单一模态对齐转向多粒度、交互式的精细化建模，时序与空间注意力成为关键突破口
- 生成式方法开始渗透检索任务，视觉生成与判别式检索的融合可能重塑查询交互范式

---

Powered by OpenClaw🦞

---

# [20260613](./202606/20260613.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日研究聚焦多模态大语言模型（MLLM）的视觉表征学习。伊利诺伊大学团队提出从冻结MLLM中提取语义属性梯度的新方法，突破传统标量距离对比学习的局限，结合群体相对策略优化（GRPO）优化视觉嵌入，为遥感图像的细粒度语义理解提供新思路。

## ✨ 今日亮点

- 突破标量距离限制，引入语义属性梯度丰富视觉嵌入
- 利用冻结MLLM的隐式知识，无需昂贵微调即可提取高层语义
- GRPO优化策略使视觉编码器对齐人类偏好的语义结构

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260613] Beyond Scalar Distances: Semantic Attribute Gradients from Frozen MLLMs for Visual Embeddings | Bhatnagar Shubhang, Baiju Dheeraj, Ahuja Narendra | University of Illinois Urbana-Champaign | 该研究提出从冻结MLLM提取语义属性梯度，以GRPO优化视觉嵌入，超越传统对比学习的标量距离限制。 | [#268](https://github.com/Larry2000error/Larry-PaperClaw/issues/268) |

## 🔎 观察

- 冻结MLLM知识蒸馏或成视觉表征学习新范式，降低算力门槛
- 语义属性梯度方法对遥感地物细粒度区分具有潜在应用价值

---

Powered by OpenClaw🦞

---

# [20260610](./202606/20260610.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦跨模态检索与重识别技术，涵盖法医图像、昼夜场景、可见光-红外及换装场景等复杂应用。低秩结构学习与提示学习成为主流技术路线，多专家网络与正交子空间方法受到关注，显示领域对鲁棒特征表示的持续探索。

## ✨ 今日亮点

- 跨域重识别研究活跃，昼夜场景与换装问题各有一篇工作
- 低秩结构学习成为热点，两篇论文分别应用于组合检索与换装重识别
- 多专家网络架构首次引入可见光-红外行人重识别任务

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260610] Bridging the Modality Gap in Forensic Image Retrieval | González-Gazapo Ricardo, Morales-González Annette, Martínez-Díaz Yoanna, Méndez-Vázquez Heydi, García-Borroto Milton | Advanced Technologies Application Center (CENATAV)；Centro de Sistemas Complejos, Facultad de Física, Universidad de La Habana | 提出跨模态法医图像检索框架，整合纹身与素描检索任务，探索大语言模型在取证场景的应用潜力。 | [#261](https://github.com/Larry2000error/Larry-PaperClaw/issues/261) |
| [20260610] Bridging Day and Night: Unsupervised Cross-Domain Re-Identification with Synergistic Prompt and Prototype Learning | Xu Jiyang, Liu Rui, Dai Hang | School of Computer Science, Wuhan University | 设计协同提示与原型学习机制，实现无监督昼夜跨域行人重识别，缓解域间分布差异。 | [#262](https://github.com/Larry2000error/Larry-PaperClaw/issues/262) |
| [20260610] MFEN:Multi-Frequency Expert Network for Visible-Infrared Person Re-ID | Li Xulin, Lu Yan, Liu Bin, Yang Qinhong, Chu Qi, Gong Tao, Yu Nenghai | University of Science and Technology of China；Anhui Province Key Laboratory of Digital Security；The Chinese University of Hong Kong | 构建多频率专家网络，通过频域学习与混合专家架构，有效缩小可见光-红外模态差异。 | [#263](https://github.com/Larry2000error/Larry-PaperClaw/issues/263) |
| [20260610] RankVR: Low-Rank Structure Perception and Value Recalibration for Robust Composed Image Retrieval | Huang Jiale, Li Zixu, Fu Zhiheng, Chen Zhiwei, Huang Qinlei, Hu Yupeng | Shandong University | 提出低秩结构感知与价值重校准方法，增强组合图像检索的全局结构一致性与噪声鲁棒性。 | [#264](https://github.com/Larry2000error/Larry-PaperClaw/issues/264) |
| [20260610] Learning Instance-Adaptive Low-Rank Orthogonal Subspaces for Clothes-Changing Person Re-Identification | Kim Dong-Woo, Kim Tae-Kyun | Imperial College London | 学习实例自适应低秩正交子空间，利用视觉-语言模型解决换装场景下行人重识别的表观变化难题。 | [#265](https://github.com/Larry2000error/Larry-PaperClaw/issues/265) |

## 🔎 观察

- 低秩表示学习成为本日最突出技术趋势，在检索与重识别两类任务中均获应用，反映领域对高效降维表征的共识
- 视觉-语言模型向 specialized 下游任务渗透加速，提示学习与原型学习结合成为跨域迁移的标准范式

---

Powered by OpenClaw🦞

---
