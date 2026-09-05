# Daily Reports

最近三天日报（最新在前）：

# [20260830](./202608/20260830.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦视觉语言模型在地理定位任务中的智能化升级。三篇论文分别从代理推理、困难样本挖掘和具身导航评估三个维度推进开放世界地理定位技术，体现出从静态感知向动态交互、从单一检索向多步验证的发展趋势。

## ✨ 今日亮点

- 港科广团队提出感知-假设-验证的代理推理框架，实现多跳地理定位
- RePair方法通过反事实生成将检索失败转化为困难训练样本
- GeoAgent构建具身导航环境，系统评估VLM地理定位能力

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260830] Perceive to Hypothesize, Verify to Ground: An Agentic Reasoning Framework for Open-World Geo-Localization | Jiang Yutian, Li Ruijie, Lyu Sisuo, Hao Xixuan, Liu Qingxiang, Yu Yongzi, Liang Yuxuan | The Hong Kong University of Science and Technology (Guangzhou)；The Hong Kong University of Science and Technology | 提出代理推理框架，通过感知假设与验证 grounding 实现开放世界地理定位的多跳推理。 | [#459](https://github.com/Larry2000error/Larry-PaperClaw/issues/459) |
| [20260830] RePair: Turning Retrieval Failures into Counterfactual Hard Pairs | Liu Siyi, Zhu Xiaorong, Du Enjun, Zuo Xinyu, Duan Lisheng, Liang Haijin, Ma Jin, Pu Junfu, Zhang Yongqi | The Hong Kong University of Science and Technology (Guangzhou)；Tencent Yuanbao；The University of Hong Kong；ARC Lab, Tencent | 设计反事实样本生成机制，将跨模态检索失败案例转化为有效困难训练对。 | [#460](https://github.com/Larry2000error/Larry-PaperClaw/issues/460) |
| [20260830] GeoAgent: Evaluating VLM Geolocalization Through Embodied Navigation | Mukherjee Arka, Roy Soham, Trivedi Kartikeya, Ghosh Shreya | KIIT Bhubaneswar；IIT Bhubaneswar | 构建基于具身导航的评估基准，检验视觉语言模型在动态街景中的地理定位性能。 | [#461](https://github.com/Larry2000error/Larry-PaperClaw/issues/461) |

## 🔎 观察

- 地理定位研究正从静态图像匹配转向具备环境交互能力的代理系统，技术路线与具身智能深度融合
- 困难样本挖掘与反事实学习成为跨模态检索的新方向，数据工程与模型训练形成闭环优化

---

Powered by OpenClaw🦞

---

# [20260827](./202608/20260827.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦视觉-语言模型的可解释性与检索能力。四项工作分别探索视觉检索头的因果机制、跨视角地理定位的多模态融合、生成式图像检索的隐式推理，以及基于智能体的图像叙事组合，体现出从单模态匹配向复杂视觉推理演进的趋势。

## ✨ 今日亮点

- KAIST团队揭示VLM中视觉检索头的因果可解释机制
- UniGeo实现文本引导的无人机跨视角地理定位
- 阿里提出隐式图像思维机制用于生成式商品检索

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260827] Retrieval Heads Meet Vision: Uncovering How VLMs Locate and Extract Visual Information | Park Chanho, Choi Daehyeon, Lee Jihyun, Sung Minhyuk | KAIST；Independent Researcher | 首次在视觉-语言模型中识别并验证视觉检索头，揭示其定位与提取视觉信息的因果机制。 | [#447](https://github.com/Larry2000error/Larry-PaperClaw/issues/447) |
| [20260827] UniGeo: A Multi-modal Large Language Model for Text-Guided Cross-View Geo-Localization | Wen Jiahao, Yu Hang, Zheng Zhedong | Institution unavailable | 提出多模态大语言模型UniGeo，通过文本引导实现无人机与地面视角的跨模态地理定位。 | [#448](https://github.com/Larry2000error/Larry-PaperClaw/issues/448) |
| [20260827] PailitaoGR: Latent Think-with-Images for Generative Image Retrieval | Fan Xiaomeng, Liu Yueran, Zhou Shengyu, Fu Chenghan, Guan Wanxian, Li Feng, Yu Chuan, Xu Jian, Zheng Bo | Alibaba Group | 设计隐式图像思维框架，使模型在生成式图像检索中模拟人类视觉推理过程。 | [#449](https://github.com/Larry2000error/Larry-PaperClaw/issues/449) |
| [20260827] Weaving Visual Narratives: Agentic Image Bundle Composition Beyond Atomic Visual Matching | Shan Rong, Xu Tianyi, Zheng Congmin, Chen Wenteng, Zhu Jiachen, Wu Junjie, Wang Teng, Liu Weiwen, Zhang Changwang, Zhang Weinan, Wang Jun, Lin Jianghao | Shanghai Jiao Tong University；Shanghai Innovation Institute；OPPO | 构建智能体驱动的图像组合系统，超越原子级视觉匹配实现叙事性图像集生成。 | [#457](https://github.com/Larry2000error/Larry-PaperClaw/issues/457) |

## 🔎 观察

- 视觉检索头的因果分析为VLM黑箱机制研究开辟新路径，或可迁移至遥感图像理解任务。
- 生成式检索与智能体组合成为视觉搜索新范式，传统相似度匹配方法面临范式转换压力。

---

Powered by OpenClaw🦞

---

# [20260826](./202608/20260826.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日研究聚焦于多模态检索与视觉理解技术，涵盖文档级视觉检索、组合图像检索、医疗多模态检索及基础设施合规检查等方向。研究趋势显示，领域特定应用（医疗、土木）与高效检索方法（稀疏化、训练无关）成为热点，跨模态对齐与RAG架构持续演进。

## ✨ 今日亮点

- DocPC提出文档级视觉检索新范式，通过代表性页面选择解决多页文档检索难题
- MulVec实现无需训练的零样本组合图像检索，采用细粒度角色感知匹配机制
- PlanSightRAG面向土木标准图纸，构建视觉优先的多模态RAG系统实现自动合规检查

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260826] DocPC: Document-Level Visual Retrieval via Representative Page Composition | You Chengsong, Zhou Junwei, Cao Xiaoyu, Wang Weiyao, Xu Yiwei, Zhao Ziyan, Sun Zhen, Zhu Qicheng, Fu Xuanyi, Chen Yufan, Li Yilun, Xiong Rongkang, Hu Yunhai, Du Nan | East China Normal University；Matter Innovation Inc.；Shandong University of Science and Technology；Thin Red Line；UC Berkeley；New York University | DocPC通过代表性页面组合策略，实现多页文档的高效视觉检索，无需处理全部页面。 | [#444](https://github.com/Larry2000error/Larry-PaperClaw/issues/444) |
| [20260826] MulVec: Fine-Grained Role-Aware Matching for Training-Free Zero-Shot Composed Image Retrieval | Zhang Zihao, Wu Dayan, Liu Xinze, Zhu Hengjie, Zhu Yiliang, Wang Ding, Fu Peng, Lin Zheng, Wang Weiping | Chinese Academy of Sciences | MulVec提出训练无关的零样本组合图像检索方法，利用细粒度角色感知匹配提升检索精度。 | [#445](https://github.com/Larry2000error/Larry-PaperClaw/issues/445) |
| [20260826] Case2Flow: Bridging Patient Cases and Guideline Flowcharts through Multimodal Retrieval | Wei Jiale, Chen Yufan, Jaus Alexander, Marinov Zdravko, Friedrich Julian, Reiß Simon, Kleesiek Jens, Stiefelhagen Rainer | Karlsruhe Institute of Technology；Helmholtz Information and Data Science School for Health (HIDSS4Health)；University Hospital Essen | Case2Flow构建多模态检索桥梁，连接患者病例与医疗指南流程图以支持临床决策。 | [#454](https://github.com/Larry2000error/Larry-PaperClaw/issues/454) |
| [20260826] PlanSightRAG: A Visual-First Multimodal RAG for Automating Question Answering and Compliance Checking for Civil Standard Plans | Subedi Nabaraj, Shuvo Dip Datta, Abdelaty Ahmed, Shivanand Venkanna Sheshappanavar | Institution unavailable | PlanSightRAG采用视觉优先架构，针对土木标准图纸实现自动化问答与合规性检查。 | [#455](https://github.com/Larry2000error/Larry-PaperClaw/issues/455) |
| [20260826] PUMA: Post-Hoc Sparsification of Universal Multimodal Embeddings for Efficient Retrieval | Attimonelli Matteo, Alessandro De Bellis, Franco Maria Nardini, Pomo Claudio, Rulli Cosimo, Venturini Rossano, Tommaso Di Noia | Politecnico di Bari；Sapienza University of Rome；ISTI–CNR；University of Pisa | PUMA通过后验稀疏化技术压缩通用多模态嵌入，在保持检索性能的同时提升效率。 | [#456](https://github.com/Larry2000error/Larry-PaperClaw/issues/456) |

## 🔎 观察

- 多模态检索正深度垂直化，医疗与基础设施等专业领域成为技术落地的重要场景
- 训练无关与后验优化方法涌现，反映学界对检索系统部署效率与成本的关注提升

---

Powered by OpenClaw🦞

---
