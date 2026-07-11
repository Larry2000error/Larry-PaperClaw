# Daily Reports

最近三天日报（最新在前）：

# [20260709](./202607/20260709.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日仅收录1篇论文，聚焦车辆重识别（Vehicle ReID）领域。研究提出多查询场景下的增强视图专家混合模型，结合对比学习与跨视图融合技术，并发布大规模基准数据集，推动智能交通监控系统的实用化发展。

## ✨ 今日亮点

- 提出增强视图专家混合架构，解决多查询车辆重识别难题
- 构建大规模基准数据集，填补该场景下公开数据空白
- 融合对比学习与跨视图特征融合，提升复杂场景识别鲁棒性

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260709] Mixture of Enhanced-View Experts for Multi-Query Vehicle ReID and A Large-Scale Benchmark | Zheng Aihua, Zhen Jie, Li Chenglong, Wang Jiaxiang, Tang Jin | Institution unavailable | 该文提出增强视图专家混合模型，实现多查询车辆重识别，并发布大规模基准数据集。 | [#326](https://github.com/Larry2000error/Larry-PaperClaw/issues/326) |

## 🔎 观察

- 多查询学习正成为ReID领域新方向，反映实际监控场景中连续帧利用需求增长
- Mixture of Experts架构在遥感与视觉任务中持续渗透，或成高效模型设计新范式

---

Powered by OpenClaw🦞

---

# [20260707](./202607/20260707.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 3 篇。

今日研究聚焦跨模态检索与不确定性量化。遥感领域出现证据学习驱动的图文检索新方法；细粒度图像检索引入关系建模与频域感知；多模态推荐系统探索视频到音乐的语义对齐。整体趋势显示检索任务正向不确定性量化与细粒度语义理解深化。

## ✨ 今日亮点

- 证据学习首次系统应用于遥感跨模态检索，实现不确定性显式建模
- RFHNet融合关系推理与频域特征，突破细粒度食品图像哈希检索瓶颈
- 时序重排序机制创新性地桥接视频语义与音乐推荐的时间动态性

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260707] RFHNet: Relational and Frequency-Aware Hashing Network for Large-Scale Fine-Grained Food Image Retrieval | Wang Junsong, Min Weiqing, Sheng Guorui, Yao Tao, Wang Lili, Jiang Shuqiang | College of Computer Science and Artificial Intelligence, Ludong University；Institute of Computing Technology, Chinese Academy of Sciences；University of Chinese Academy of Sciences | RFHNet提出关系与频域感知哈希网络，通过图关系建模与离散余弦变换增强，解决大规模细粒度食品图像检索中的语义鸿沟与效率问题。 | [#322](https://github.com/Larry2000error/Larry-PaperClaw/issues/322) |
| [20260707] Uncertainty-Aware Cross-Modal Remote Sensing Image-Text Retrieval via Evidential Learning | Wang Zhuoyue, Wang Xueqian, Li Gang, Li Chengxi, Liu Yongpan, Ban Yifang | Institution unavailable | 该研究将证据学习引入遥感图文检索，构建不确定性感知跨模态框架，有效量化预测置信度以提升检索可靠性。 | [#323](https://github.com/Larry2000error/Larry-PaperClaw/issues/323) |
| [20260707] Multimodal Video-to-Music Recommendation via Semantic Retrieval and Temporal Reranking | Doh Seungheon, Lee Minhee, Lee Sangmoon, Ben Sangbae Chon, Nam Juhan | Korea Advanced Institute of Science and Technology；Kakao Entertainment Corp. | 研究提出语义检索与时序重排序两阶段框架，利用多模态Transformer编码视频-音乐语义关联，并通过时序对齐优化推荐时序连贯性。 | [#324](https://github.com/Larry2000error/Larry-PaperClaw/issues/324) |

## 🔎 观察

- 证据学习在遥感多模态任务中的应用尚处早期，其不确定性量化能力对高 stakes 地理决策具有潜在价值，但计算开销需权衡
- 细粒度食品检索与视频-音乐推荐均显示：领域特定语义（食材纹理、节拍情绪）需超越通用视觉表征的专用架构设计

---

Powered by OpenClaw🦞

---

# [20260706](./202607/20260706.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦视觉-语言多模态检索的效率优化。两篇论文分别探索零样本组合图像检索的直接学习方法，以及视觉令牌压缩中的对象感知策略，均致力于在保持精度的同时降低计算开销，体现多模态模型轻量化与实用化的发展趋势。

## ✨ 今日亮点

- DiCE-CIR提出直接组合学习框架，实现高效零样本组合图像检索
- Object-Evidence Preserving Token Merging通过对象感知合并优化视觉-语言检索
- 两篇工作均关注多模态检索中的效率-精度平衡问题

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260706] DiCE-CIR: Direct Composition Learning for Efficient Zero-Shot Composed Image Retrieval | Na Gwang-Ho, Kim Ho-Joong, Lee Seong-Whan | Korea University | DiCE-CIR通过直接组合学习替代传统多阶段训练，提升零样本组合图像检索效率。 | [#318](https://github.com/Larry2000error/Larry-PaperClaw/issues/318) |
| [20260706] Do All Visual Tokens Matter Equally? Object-Evidence Preserving Token Merging for Vision-Language Retrieval | Park Suhyeong, Jung Junha, Park Jungwoo, Kang Jaewoo | The Catholic University of Korea；Korea University；AIGEN Sciences Inc. | 该研究提出对象证据保留的令牌合并方法，解决视觉-语言检索中视觉令牌冗余问题。 | [#320](https://github.com/Larry2000error/Larry-PaperClaw/issues/320) |

## 🔎 观察

- 韩国高校在视觉-语言多模态检索领域形成研究集群，两所机构合作紧密。
- 令牌压缩与直接学习范式正成为多模态检索效率优化的主流技术路线。

---

Powered by OpenClaw🦞

---
