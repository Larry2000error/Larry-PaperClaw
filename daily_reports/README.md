# Daily Reports

最近三天日报（最新在前）：

# [20260618](./202606/20260618.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦多模态检索与对齐技术，涵盖通用多模态检索、跨模态目标重识别及时尚图像检索三大方向。核心趋势表现为：强化学习与排序优化驱动检索性能提升，频域分析与特征解耦成为跨模态对齐新范式，两阶段微调策略推动MLLM在垂直领域落地。

## ✨ 今日亮点

- ELVA提出排序驱动的通用多模态检索框架，融合强化学习与对比学习优化检索质量
- FUSE创新频域统一与谱能量对齐机制，解决跨模态目标重识别中的特征失配难题
- 时尚图像检索探索MLLM两阶段微调，验证领域适配对组合式检索的关键作用

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260618] ELVA: Exploring Ranking-Driven Universal Multimodal Retrieval | Liu Yuhan, Fu Pei, Li Hang, Qi Yukun, Jiang Chao, Fu Jingwen, Liu Zhen, Qin Bin, Luo Zhenbo, Luan Jian, Xin Jingmin | National Key Laboratory of Human-Machine Hybrid Augmented Intelligence, Institute of Artificial Intelligence and Robotics, Xi'an Jiaotong University；MiLM Plus, Xiaomi Inc；Zhongguancun Academy | ELVA构建基于排序优化的通用多模态检索系统，通过强化学习显式建模排序目标，突破传统对比学习在检索任务中的性能瓶颈。 | [#276](https://github.com/Larry2000error/Larry-PaperClaw/issues/276) |
| [20260618] FUSE: Frequency-domain Unification and Spectral Energy Alignment for Multi-modal Object Re-Identification | Qi Xuanhao, Tom H. Luan, Zhang Yukang, Zheng Jinkai, Su Zhou, Li Shuwei, Tan Lei | Tsinghua University；Chinese Academy of Sciences | FUSE提出频域统一与谱能量对齐框架，利用频域分解实现跨模态特征解耦与对齐，提升多模态目标重识别的鲁棒性。 | [#277](https://github.com/Larry2000error/Larry-PaperClaw/issues/277) |
| [20260618] Exploring Multi-Modal Large Language Models and Two-Stage Fine-Tuning for Fashion Image Retrieval | Nguyen Cao Hoang, Hoang Bui Le, Nam Vo Hoang, Le Trung-Nghia | University of Science, VNU-HCM；Vietnam National University | 该研究探索多模态大语言模型在时尚图像检索中的应用，设计两阶段微调策略优化组合式图像检索的语义理解能力。 | [#278](https://github.com/Larry2000error/Larry-PaperClaw/issues/278) |

## 🔎 观察

- 排序优化正成为多模态检索的新焦点，从传统对比学习向强化学习驱动的显式排序建模演进
- 频域分析工具向跨模态任务渗透，谱分解技术为特征解耦与对齐提供了可解释的几何视角

---

Powered by OpenClaw🦞

---

# [20260617](./202606/20260617.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦跨模态检索的精细化与实用化。视觉-语言模型持续演进，学者从注意力机制优化、生成式消歧、冷启动应对等多维度突破，电商视频、复杂场景等应用导向明显，交互式检索与不确定性量化成为新关注点。

## ✨ 今日亮点

- DREAM提出双目标编码扩展视觉-语言模型，强化视频时序建模与跨模态检索能力
- 生成式视觉消歧结合共形预测，实现交互式组合图像检索的覆盖验证
- LARE针对低注意力区域编码，缓解显著性偏置以提升密集场景图文检索精度

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260617] DREAM: Extending Vision-Language Models with Dual-Objective Encoding for Cross-Modal Retrieval | Ullah Kaleem, Hussain Altaf, Munsif Muhammad, Sung Wook Baik | Institution unavailable | DREAM通过双目标编码扩展视觉-语言模型，优化视频时序建模以提升跨模态检索性能。 | [#271](https://github.com/Larry2000error/Larry-PaperClaw/issues/271) |
| [20260617] Show, Don't Ask: Generative Visual Disambiguation for Composed Image Retrieval with Turn-Valid Coverage | Tran Amsisan, Le Baogh, Tuan Kiet Pham, Sui Yang Guang | Institution unavailable | 该研究以生成式视觉消歧替代显式询问，结合共形预测实现组合图像检索的交互优化。 | [#272](https://github.com/Larry2000error/Larry-PaperClaw/issues/272) |
| [20260617] LARE: Low-Attention Region Encoding for Text-Image Retrieval | Alquwayfili Abdulmalik, Almeshal Faisal, Almajnouni Jumanah, Alotaibi Leena, Alhajari Faisal, Alkhrashi Mohammed, Almuhrij Alreem, Aldwyish Abdullah, Aljadaany Raied, Alamri Huda, Muhammad Kamran J. Khan | Institution unavailable | LARE聚焦低注意力区域编码，旨在解决显著性偏置问题以改善密集场景下的图文检索。 | [#273](https://github.com/Larry2000error/Larry-PaperClaw/issues/273) |
| [20260617] VCG: A Multimodal Retrieval Framework for E-Commerce Video Feeds under Extreme Cold-Start Conditions | Mirylenka Katya, Malykh Egor, Ravanbakhsh Mahdyar, Gygli Michael, Buchmann Marco-Andrea, Dzhoha Andrew, Borzenko Svitlana, Catino Francesca, Gaafar Mohamed, Versteegh Maarten, Kober Thomas, d'Andrea Dario, Langhans Ellie | TU Wien；Zalando SE；Zalando Switzerland AG | VCG构建多模态检索框架，针对电商视频推荐的极端冷启动场景进行优化设计。 | [#275](https://github.com/Larry2000error/Larry-PaperClaw/issues/275) |

## 🔎 观察

- 检索任务正从粗粒度匹配转向细粒度理解，注意力机制与区域编码成为关键切入点
- 电商场景驱动明显，冷启动与交互式检索反映学术界对工业落地痛点的回应

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
