# Daily Reports

最近三天日报（最新在前）：

# [20260730](./202607/20260730.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦于视觉-语言模型在检索任务中的优化，涵盖稀疏Token选择、细粒度上下文学习及医学影像检索等方向。多模态大语言模型与视觉检索的融合成为核心趋势，同时人脸超分辨率与重识别技术取得进展。

## ✨ 今日亮点

- ReToken提出单Token稀疏选择策略，有效压缩长上下文KV缓存
- FiRE引入细粒度上下文学习，提升MLLM复杂图像检索能力
- CXR-Retrieve针对胸部X光片构建组合式文本-图像检索框架

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260730] ReToken: One Token to Improve Vision-Language Models for Visual Retrieval | Xiao Yao, Tan Reuben, Zhu Zhen, Wu Yuqun, Gao Jianfeng, Hoiem Derek | University of Illinois at Urbana-Champaign；Microsoft Research；Google DeepMind | ReToken通过稀疏Token选择机制，以单Token优化视觉-语言模型的长上下文视觉检索效率。 | [#376](https://github.com/Larry2000error/Larry-PaperClaw/issues/376) |
| [20260730] Collaborative Feature Aggregation for Face Super-Resolution and Robust Re-Identification | Hwang Juheon, Kim Taewan, Kang Jiwoo | Yonsei University；Dongduk Women's University；Sookmyung Women's University | 该研究提出协作特征聚合方法，联合优化人脸超分辨率与鲁棒重识别任务性能。 | [#377](https://github.com/Larry2000error/Larry-PaperClaw/issues/377) |
| [20260730] FiRE: Enhancing MLLMs with Fine-Grained Context Learning for Complex Image Retrieval | Hou Bohan, Lin Haoqiang, Song Xuemeng, Wen Haokun, Liu Meng, Hu Yupeng, Zhao Xiangyu | Shandong University；City University of Hong Kong；Harbin Institute of Technology (Shenzhen)；Shandong Jianzhu University | FiRE为MLLM设计细粒度上下文学习模块，增强复杂组合图像检索的语义对齐能力。 | [#378](https://github.com/Larry2000error/Larry-PaperClaw/issues/378) |
| [20260730] CXR-Retrieve: Compositional Text-to-Image Retrieval in Chest Radiography | Erez Tomer, Kimhi Moshe, Baskin Chaim, Rivlin Ehud | Technion – Israel Institute of Technology；Ben-Gurion University of the Negev | CXR-Retrieve构建胸部X光片组合式检索基准，推动医学视觉-语言模型的临床适用性。 | [#379](https://github.com/Larry2000error/Larry-PaperClaw/issues/379) |

## 🔎 观察

- 视觉检索研究正从通用场景向医学等专业领域纵深发展，组合式推理成为关键能力。
- Token效率优化与细粒度学习形成技术张力，反映多模态模型规模化与精准化的双重诉求。

---

Powered by OpenClaw🦞

---

# [20260728](./202607/20260728.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦无人机视角地理定位技术，涵盖持续学习、跨模态检索与鲁棒性增强三大方向。西安交大团队提出几何感知适配器解决增量学习遗忘问题；中国海洋大学构建昼夜统一基准；哈工大联合团队针对退化场景设计可靠性引导的证据融合机制。行人重识别领域亦有邻域特征交互新进展。

## ✨ 今日亮点

- GeoMFD引入边缘场蒸馏，缓解无人机地理定位中的灾难性遗忘
- 首个昼夜跨模态无人机定位基准，统一处理可见光与红外影像
- ReLATE构建可靠性引导框架，提升退化场景下的跨视图匹配鲁棒性

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260728] GeoMFD: Continual Drone-View Geo-Localization with Geometry-Aware Adapter and Margin-Field Distillation | Chen Zhongwei, Rong Hai-jun, Zhang Tao, Nie Xianfeng, Zhang Xiangbao, Li Guoqi, Yang Zhao-Xu | School of Aerospace Engineering, Xi'an Jiaotong University；Institute of Automation, Chinese Academy of Sciences | GeoMFD通过几何感知适配器与边缘场蒸馏，实现无人机视角地理定位的持续学习，缓解域增量场景下的知识遗忘。 | [#370](https://github.com/Larry2000error/Larry-PaperClaw/issues/370) |
| [20260728] A Unified Benchmark and Modality-Adaptive Network for Day-and-Night Drone-View Geo-Localization | Xu Songtianhao, Chen Zhongwei, Yang Zhao-Xu, Wang Weifeng | Ocean University of China | 提出昼夜无人机定位统一基准与模态自适应网络，首次系统解决可见光-红外跨模态检索中的光照变化挑战。 | [#371](https://github.com/Larry2000error/Larry-PaperClaw/issues/371) |
| [20260728] ReLATE: Reliability-Guided Evidence Fusion for Robust UAV--Satellite cross-view Geo-Localization | Jiang Haochen, Pan Jialei, Sun Yuzhe, Dong Zhe, Ren Lecheng, Gu Yanfeng, Liu Tianzhu | School of Electronics and Information Engineering, Harbin Institute of Technology；National Key Laboratory of Radar Detection and Sensing, Nanjing Research Institute of Electronics Technology；School of Electrical and Electronic Engineering, University of Manchester | ReLATE设计可靠性引导的证据融合机制，针对模糊、噪声等退化场景提升UAV-卫星跨视图定位的鲁棒性。 | [#372](https://github.com/Larry2000error/Larry-PaperClaw/issues/372) |
| [20260728] ANFI: Rethinking Neighbor Feature Interaction in Person Re-ID | Li Xulin, Lu Yan, Liu Bin, Li Jiaze, Yang Qinhong, Gong Tao, Chu Qi, Yu Nenghai | University of Science and Technology of China；Anhui Province Key Laboratory of Digital Security；The Chinese University of Hong Kong | ANFI重新思考行人重识别中的邻域特征交互，通过自适应加权抑制噪声邻居干扰，优化亲和关系建模。 | [#373](https://github.com/Larry2000error/Larry-PaperClaw/issues/373) |

## 🔎 观察

- 无人机地理定位正从单一模态向持续学习、跨模态统一、退化鲁棒性多维度演进，技术栈日趋复杂
- 中国高校在该领域形成显著集群优势，西交大、哈工大、中国海洋大学等机构贡献核心方法论创新

---

Powered by OpenClaw🦞

---

# [20260727](./202607/20260727.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 0 篇；最终纳入日报 1 篇。

今日遥感AI领域研究聚焦于跨模态行人重识别技术，特别关注可见光-红外模态缺失场景下的可信AI方法。武汉大学等机构提出模态自适应匹配新思路，推动多模态融合向鲁棒性与可解释性方向发展。

## ✨ 今日亮点

- 提出同质模态相似性双刃剑理论，解决跨模态匹配中的模态不平衡难题
- 构建模态自适应匹配框架，提升可见光-红外行人重识别在模态缺失时的鲁棒性
- 融合可信AI理念，为跨模态检索系统的可靠性提供新保障机制

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260727] Dual-Edged Homogeneous-Modality Similarity: Towards Visible-Infrared Modality-Incomplete Person Re-Identification with Modality Adaptive Matching | Xu Xin, Zhan Shuhao, Liu Wei, Wang Zheng, Jiang Kui, Lin Chia-Wen | School of Computer Science and Technology, Wuhan University of Science and Technology；Hubei Province Key Laboratory of Intelligent Information Processing and Real-time Industrial System, Wuhan University of Science and Technology；School of Computer Science, Wuhan University；Faculty of Computing, Harbin Institute of Technology；Department of Electrical Engineering and the Institute of Communications Engineering, National Tsing Hua University | 本文针对可见光-红外模态不完整行人重识别问题，提出同质模态相似性双刃剑理论与模态自适应匹配方法。 | [#354](https://github.com/Larry2000error/Larry-PaperClaw/issues/354) |

## 🔎 观察

- 跨模态行人重识别正从'模态对齐'转向'模态缺失容忍'，反映实际部署场景的复杂需求
- 可信AI标签的出现表明该领域开始关注模型决策的可解释性与可靠性验证

---

Powered by OpenClaw🦞

---
