# Awesome Visual Spatial Reasoning

Contributors: 

Hao Ju, [Songsong Yu](https://song2yu.github.io/), Lianjie Jia, Rundi Cui, [Zaibin Zhang](https://scholar.google.com/citations?user=3SAk3GQAAAAJ&hl=en), [Zhipeng Zhang](https://zhipengzhang.cn/), [Yuxin Chen](https://github.com/Uason-Chen)<sup>🌟</sup>



<p align="center">
  <img src="https://www.tencent.net.cn/wp-content/uploads/2023/02/logo-vertical-white-1.png" width="105">
  <img src="https://upload.wikimedia.org/wikipedia/zh/d/d5/SJTU_emblem.svg" width="80">
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/69/University_of_Macau_logo.svg" width="80">
  <img src="https://upload.wikimedia.org/wikipedia/zh/7/76/Dalian_University_of_Technology_logo.svg" width="80">
</p>

🌟 Project Lead

# News and Updates



# Contributing

> We welcome contributions to this repository! If you'd like to contribute, please follow these steps:
>
> - Fork the repository.
> - Create a new branch with your changes.
> - Submit a pull request with a clear description of your changes.
>
> You can also open an issue if you have anything to add or comment.
>
> Please feel free to contact us (SongsongYu203@163.com).





# Overview

The research community is increasingly focused on the **visual spatial reasoning** (VSR) abilities of Vision-Language Models (VLMs). Yet, the field **lacks** a **clear overview of its evolution** and a **standardized benchmark for evaluation**. Current assessment methods are disparate and **lack a common toolkit**. This project aims to fill that void. We are developing a unified, comprehensive, and diverse evaluation toolkit, along with an accompanying survey paper. We are actively seeking collaboration and discussion with fellow experts to advance this initiative. 

## Task Expalnation

Visual spatial understanding is a key task at the intersection of computer vision and cognitive science. It aims to **enable intelligent agents** (such as robots and AI systems) to **parse spatial relationships** in the environment **through visual inputs** (images, videos, etc.), forming an abstract cognition of the physical world. In Embodied Intelligence, it serves as the foundation for agents to achieve the "perception-decision-action" loop—only by understanding attributes like object positions, distances, sizes, and orientations in space can intelligent agents navigate environments, manipulate objects, or interact with humans.



## 图





## Table of Contents

- [Papers](#Papers)
  - [Single Image](#Single-image)
  - [Monocular Video](#Monocular-video)
  - [Others](#Others)



# Papers



## Single Image
| Title | Venue | Date | Code | Impact | Benchmark | Illustration |
| --- | --- | --- | --- | --- | --- | --- |
| [3D-Aware Visual Question Answering about Parts, Poses and Occlusions](https://arxiv.org/pdf/2310.17914) | NIPS | 23-10 | [link](https://github.com/XingruiWang/3D-Aware-VQA) | ![Star](https://img.shields.io/github/stars/XingruiWang/3D-Aware-VQA.svg?style=social&label=Star) | Super-CLEVR-3D |  |
| [Improving Vision-and-Language Reasoning via Spatial Relations Modeling](https://arxiv.org/pdf/2311.05298) | WACV | 23-11 | -- | -- | -- |  |
| [Proximity QA: Unleashing the Power of Multi-Modal Large Language Models for Spatial Proximity Analysis](https://arxiv.org/abs/2401.17862) | ARXIV | 24-01 | [link](https://github.com/NorthSummer/ProximityQA) | ![Star](https://img.shields.io/github/stars/NorthSummer/ProximityQA.svg?style=social&label=Star) | Proximity-110K |  |
| [Visual CoT: Advancing Multi-Modal Language Models with a Comprehensive Dataset and Benchmark for Chain-of-Thought Reasoning](https://arxiv.org/pdf/2403.16999) | -- | 24-03 | [link](https://github.com/deepcs233/Visual-CoT) | ![Star](https://img.shields.io/github/stars/deepcs233/Visual-CoT.svg?style=social&label=Star) | 一个没说名字的CoT数据集，包含了空间理解数据 |  |
| [Can Transformers Capture Spatial Relations between Objects?](https://arxiv.org/abs/2403.00729) | ICLR | 24-03 | [link](https://github.com/AlvinWen428/spatial-relation-benchmark) | ![Star](https://img.shields.io/github/stars/AlvinWen428/spatial-relation-benchmark.svg?style=social&label=Star) | srp |  |
| [Mind's Eye of LLMs: Visualization-of-Thought Elicits Spatial Reasoning in Large Language Models](https://arxiv.org/abs/2404.03622) | NIPS | 24-04 | [link](https://github.com/microsoft/visualization-of-thought/) | ![Star](https://img.shields.io/github/stars/microsoft/visualization-of-thought.svg?style=social&label=Star) | 生成的谜题数据集 |  |
| [BLINK: Multimodal Large Language Models Can See but Not Perceive](https://arxiv.org/pdf/2404.12390) | ECCV | 24-04 | [link](https://github.com/zeyofu/BLINK_Benchmark) | ![Star](https://img.shields.io/github/stars/zeyofu/BLINK_Benchmark.svg?style=social&label=Star) | BLINK |  |
| [SpatialBot: Precise Spatial Understanding with Vision Language Models](https://arxiv.org/abs/2406.13642) | ICRA | 24-06 | [link](https://github.com/BAAI-DCAI/SpatialBot) | ![Star](https://img.shields.io/github/stars/BAAI-DCAI/SpatialBot.svg?style=social&label=Star) | SpatialBench |  |
| [SpatialRGPT: Grounded Spatial Reasoning in Vision-Language Models](https://arxiv.org/pdf/2406.01584) | ARXIV | 24-06 | [link](https://github.com/AnjieCheng/SpatialRGPT) | ![Star](https://img.shields.io/github/stars/AnjieCheng/SpatialRGPT.svg?style=social&label=Star) | SpatialRGBT-Bench |  |
| [TOPVIEWRS: Vision-Language Models as Top-View Spatial Reasoners](https://arxiv.org/pdf/2406.02537) | ARXIV | 24-06 | [link](https://topviewrs.github.io/) | -- | -- |  |
| [Is A Picture Worth A Thousand Words? Delving Into Spatial Reasoning for Vision Language Models](https://arxiv.org/pdf/2406.14852) | NIPS | 24-06 | [link](https://github.com/jiayuww/SpatialEval) | ![Star](https://img.shields.io/github/stars/jiayuww/SpatialEval.svg?style=social&label=Star) | SpatialEval |  |
| [Understanding Depth and Height Perception in Large Visual-Language Models](https://arxiv.org/pdf/2408.11748) | CVPRW | 24-08 | [link](https://github.com/sacrcv/GeoMeter) | ![Star](https://img.shields.io/github/stars/sacrcv/GeoMeter.svg?style=social&label=Star) | GeoMeter |  |
| [Coarse Correspondences Boost Spatial-Temporal Reasoning in Multimodal Language Model](https://arxiv.org/abs/2408.00754) | -- | 24-08 | -- | -- | ScanQA, OpenEQA’s episodic memory subset, EgoSchema, R2R, SQA3D |  |
| [Reasoning Paths with Reference Objects Elicit Quantitative Spatial Reasoning in Large Vision-Language Models](https://arxiv.org/pdf/2409.09788) | ARXIV | 24-09 | [link](https://github.com/andrewliao11/Q-Spatial-Bench-code) | ![Star](https://img.shields.io/github/stars/andrewliao11/Q-Spatial-Bench-code.svg?style=social&label=Star) | Q-Spatial Bench |  |
| [Can Vision Language Models Learn from Visual Demonstrations of Ambiguous Spatial Reasoning?](https://arxiv.org/pdf/2409.17080?) | ARXIV | 24-09 | [link](https://github.com/groundlight/vlm-visual-demonstrations) | ![Star](https://img.shields.io/github/stars/groundlight/vlm-visual-demonstrations.svg?style=social&label=Star) | SVAT |  |
| [Sparkle: Mastering Basic Spatial Capabilities in Vision Language Models Elicits Generalization to Spatial Reasoning](https://arxiv.org/abs/2410.16162) | NIPS | 24-10 | -- | -- | what's up, coco-spatial, GQA-spatial |  |
| [TopV-Nav: Unlocking the Top-View Spatial Reasoning Potential of MLLM for Zero-shot Object Navigation](https://arxiv.org/pdf/2411.16425?) | ARXIV | 24-11 | -- | -- | -- |  |
| [AnEmpirical Analysis on Spatial Reasoning Capabilities of Large Multimodal Models](https://arxiv.org/pdf/2411.06048) | EMNLP | 24-11 | [link](https://github.com/FatemehShiri/Spatial-MM) | ![Star](https://img.shields.io/github/stars/FatemehShiri/Spatial-MM.svg?style=social&label=Star) | Spatial-MM |  |
| [ROOT: VLM-based System for Indoor Scene Understanding and Beyond](https://arxiv.org/pdf/2411.15714) | ARXIV | 24-11 | [link](https://github.com/harrytea/ROOT) | ![Star](https://img.shields.io/github/stars/harrytea/ROOT.svg?style=social&label=Star) | SceneVLM |  |
| [LLaVA-SpaceSGG: Visual Instruct Tuning for Open-vocabulary Scene Graph Generation with Enhanced Spatial Relations](https://arxiv.org/pdf/2412.06322) | ARXIV | 24-12 | [link](https://github.com/Endlinc/LLaVA-SpaceSGG) | ![Star](https://img.shields.io/github/stars/Endlinc/LLaVA-SpaceSGG.svg?style=social&label=Star) | SpaceSGG |  |
| [3DSRBench: A Comprehensive 3D Spatial Reasoning Benchmark](https://arxiv.org/pdf/2412.07825) | ARXIV | 24-12 | [link](https://3dsrbench.github.io/) | -- | 3DSRBench |  |
| [SpatialCoT: Advancing Spatial Reasoning through Coordinate Alignment and Chain-of-Thought for Embodied Task Planning](https://arxiv.org/abs/2501.10074) | ARXIV | 25-01 | -- | -- | -- |  |
| [Imagine while Reasoning in Space: Multimodal Visualization-of-Thought](https://arxiv.org/abs/2501.07542) | ARXIV | 25-01 | -- | -- | LEC23, WMS+24, LZZ+24, RDT+24 |  |
| [Visual Agentic AI for Spatial Reasoning with a Dynamic API](https://arxiv.org/pdf/2502.06787) | ARXIV | 25-02 | [link](https://github.com/damianomarsili/VADAR) | ![Star](https://img.shields.io/github/stars/damianomarsili/VADAR.svg?style=social&label=Star) | -- |  |
| [iVISPAR —AnInteractive Visual-Spatial Reasoning Benchmark for VLMs](https://arxiv.org/pdf/2502.03214) | ARXIV | 25-02 | [link](https://github.com/SharkyBamboozle/iVISPAR) | ![Star](https://img.shields.io/github/stars/SharkyBamboozle/iVISPAR.svg?style=social&label=Star) | iVISPAR |  |
| [Visual Agentic AI for Spatial Reasoning with a Dynamic API](https://arxiv.org/abs/2502.06787) | ARXIV | 25-02 | [link](https://github.com/damianomarsili/VADAR) | ![Star](https://img.shields.io/github/stars/damianomarsili/VADAR.svg?style=social&label=Star) | Q-Spatial Bench, VSI-Bench |  |
| [Beyond Semantics Rediscovering Spatial Awareness in Vision-Language Models](https://arxiv.org/pdf/2503.17349) | -- | 25-03 | [link](https://user074.github.io/respatialaware/) | -- | -- |  |
|[MetaSpatial: Reinforcing 3D Spatial Reasoning in VLMs for the Metaverse](https://arxiv.org/pdf/2503.18470) | ARXIV | 25-03 | [link](https://github.com/PzySeere/MetaSpatial) | ![Star](https://img.shields.io/github/stars/PzySeere/MetaSpatial.svg?style=social&label=Star) | MetaSpatial |  |
| [Mind the Gap: Benchmarking Spatial Reasoning in Vision-Language Models](https://arxiv.org/pdf/2503.19707?) | ARXIV | 25-03 | [link](https://github.com/stogiannidis/srbench) | ![Star](https://img.shields.io/github/stars/stogiannidis/srbench.svg?style=social&label=Star) | SRBench |  |
| [Open3DVQA: ABenchmark for Comprehensive Spatial Reasoning with Multimodal Large Language Model in Open Space](https://arxiv.org/pdf/2503.11094) | ARXIV | 25-03 | [link](https://github.com/WeichenZh/Open3DVQA) | ![Star](https://img.shields.io/github/stars/WeichenZh/Open3DVQA.svg?style=social&label=Star) | Open3DVQA |  |
| [AutoSpatial: Visual-Language Reasoning for Social Robot Navigation through Efficient Spatial Reasoning Learning](https://arxiv.org/pdf/2503.07557) | ARXIV | 25-03 | [link](https://github.com/Yanko96/AutoSpatial) | ![Star](https://img.shields.io/github/stars/Yanko96/AutoSpatial.svg?style=social&label=Star) | AutoSpatial |  |
| [Why Is Spatial Reasoning Hard for VLMs? AnAttention Mechanism Perspective on Focus Areas](https://arxiv.org/pdf/2503.01773) | ARXIV | 25-03 | [link](https://github.com/shiqichen17/AdaptVis) | ![Star](https://img.shields.io/github/stars/shiqichen17/AdaptVis.svg?style=social&label=Star) | -- |  |
| [LEGO-Puzzles: How Good Are MLLMs at Multi-Step Spatial Reasoning](https://arxiv.org/pdf/2503.19990) | ARXIV | 25-03 | [link](https://github.com/Tangkexian/LEGO-Puzzles) | ![Star](https://img.shields.io/github/stars/Tangkexian/LEGO-Puzzles.svg?style=social&label=Star) | LEGO-Puzzles |  |
| [SpatialVLM Endowing Vision-Language Models with Spatial Reasoning Capabilities](https://arxiv.org/abs/2401.12168) | CVPR | 24-01 | [link](https://github.com/remyxai/VQASynth) | ![Star](https://img.shields.io/github/stars/remyxai/VQASynth.svg?style=social&label=Star) | -- |  |
| [Improved Visual-Spatial Reasoning via R1-Zero-Like Training](https://arxiv.org/pdf/2504.00883) | ARXIV | 25-04 | [link](https://github.com/zhijie-group/R1-Zero-VSI) | ![Star](https://img.shields.io/github/stars/zhijie-group/R1-Zero-VSI.svg?style=social&label=Star) | VSI-100K |  |
| [Perspective-Aware Reasoning in Vision-Language Models via Mental Imagery Simulation](https://arxiv.org/abs/2504.17207) | ARXIV | 25-04 | [link](https://github.com/KAIST-Visual-AI-Group/APC-VLM) | ![Star](https://img.shields.io/github/stars/KAIST-Visual-AI-Group/APC-VLM.svg?style=social&label=Star) | COMFORT++, 3DSRBench |  |
| [SpatialReasoner: Towards Explicit and Generalizable 3D Spatial Reasoning](https://arxiv.org/pdf/2504.20024?) | ARXIV | 25-04 | [link](https://spatial-reasoner.github.io/) | -- | -- |  |
| [Vision language models are unreliable at trivial spatial cognition](https://arxiv.org/pdf/2504.16061) | ARXIV | 25-04 | -- | -- | TableTest |  |
| [SpaRE: Enhancing Spatial Reasoning in Vision-Language Models with Synthetic Data](https://arxiv.org/abs/2504.20648) | ARXIV | 25-04 | -- | -- | vsr, what's up, 3DSR-Bench, RealWorldQA |  |
| [NUSCENES-SPATIALQA: A Spatial Understanding and Reasoning Benchmark for Vision-Language Models in Autonomous Driving](https://arxiv.org/pdf/2504.03164) | ARXIV | 25-04 | [link](https://github.com/taco-group/NuScenes-SpatialQA) | ![Star](https://img.shields.io/github/stars/taco-group/NuScenes-SpatialQA.svg?style=social&label=Star) | NuScenes-SpatialQA |  |
| [Can Multimodal Large Language Models Understand Spatial Relations](https://arxiv.org/pdf/2505.19015) | ARXIV | 25-05 | [link](https://github.com/ziyan-xiaoyu/SpatialMQA) | ![Star](https://img.shields.io/github/stars/ziyan-xiaoyu/SpatialMQA.svg?style=social&label=Star) | SpatialMQA |  |
| [SSR: Enhancing Depth Perception in Vision-Language Models via Rationale-Guided Spatial Reasoning](https://arxiv.org/abs/2505.12448) | -- | 25-05 | -- | -- | SSR-CoT |  |
| [Spatial-LLaVA: Enhancing Large Language Models with Spatial Referring Expressions for Visual Understanding](https://arxiv.org/pdf/2505.12194) | ARXIV | 25-05 | [link](https://arpg.github.io/sunspot/) | -- | SUNSPOT |  |
| [Are Multimodal Large Language Models Ready for Omnidirectional Spatial Reasoning?](https://arxiv.org/pdf/2505.11907) | ARXIV | 25-05 | [link](https://huggingface.co/datasets/UUUserna/OSR-Bench) | -- | OSR-Bench |  |
| [SITE: towards Spatial Intelligence Thorough Evaluation](https://arxiv.org/pdf/2505.05456) | ARXIV | 25-05 | [link](https://github.com/wenqi-wang20/SITE-Bench) | ![Star](https://img.shields.io/github/stars/wenqi-wang20/SITE-Bench.svg?style=social&label=Star) | SITE |  |
| [RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robtics](https://arxiv.org/pdf/2506.04308) | ARXIV | 25-06 | [link](https://zhoues.github.io/RoboRefer/) | -- | RefSpatial-Bench |  |
| [Visual Embodied Brain: Let Multimodal Large Language Models See, Think, and Control in Spaces](https://arxiv.org/abs/2506.00123) | ARXIV | 25-06 | [link](https://github.com/OpenGVLab/VeBrain) | ![Star](https://img.shields.io/github/stars/OpenGVLab/VeBrain.svg?style=social&label=Star) | VeBrain-600k |  |
| [SVQA-R1: Reinforcing Spatial Reasoning in MLLMs via View-Consistent Reward Optimization](https://arxiv.org/pdf/2506.01371?) | ARXIV | 25-06 | -- | -- | SVQA-R1 |  |
| [OmniSpatial: Towards Comprehensive Spatial Reasoning Benchmark for Vision Language Models](https://arxiv.org/abs/2506.03135) | -- | 25-06 | [link](https://github.com/qizekun/OmniSpatial) | ![Star](https://img.shields.io/github/stars/qizekun/OmniSpatial.svg?style=social&label=Star) | OmniSpatial |  |
| [Do Vision-Language Models Represent Space and How. Evaluating Spatial Frame of Reference under Ambiguities](https://openreview.net/pdf?id=84pDoCD4lH) | ICLR | -- | [link](https://spatial-comfort.github.io/) | -- | COMFORT |  |
| [ROBOSPATIAL: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics](https://openaccess.thecvf.com/content/CVPR2025/papers/Song_RoboSpatial_Teaching_Spatial_Understanding_to_2D_and_3D_Vision-Language_Models_CVPR_2025_paper.pdf) | CVPR | -- | -- | -- | -- |  |
| [Spatial457: A Diagnostic Benchmark for 6D Spatial Reasoning of Large Multimodal Models](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Spatial457_A_Diagnostic_Benchmark_for_6D_Spatial_Reasoning_of_Large_CVPR_2025_paper.pdf) | CVPR | -- | -- | -- | -- |  |
| [COARSE CORRESPONDENCES Boost Spatial-Temporal Reasoning in Multimodal Language Model](https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_Coarse_Correspondences_Boost_Spatial-Temporal_Reasoning_in_Multimodal_Language_Model_CVPR_2025_paper.pdf) | CVPR | -- | [link](https://coarse-correspondence.github.io/) | -- | -- |  |
| [SpatialLLM: A Compound 3D-Informed Design towards Spatially-Intelligent Large Multimodal Models](https://openaccess.thecvf.com/content/CVPR2025/papers/Ma_SpatialLLM_A_Compound_3D-Informed_Design_towards_Spatially-Intelligent_Large_Multimodal_Models_CVPR_2025_paper.pdf) | CVPR | -- | [link](https://3d-spatial-reasoning.github.io/spatial-llm/) | -- | -- |  |
| [LLaVA-VSD: Large Language-and-Vision Assistant for Visual Spatial Description](https://dl.acm.org/doi/pdf/10.1145/3664647.3688992) | ACM MM | -- | -- | -- | -- |  |
| [SpatialCLIP: Learning 3D-aware Image Representations from Spatially Discriminative Language](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_SpatialCLIP_Learning_3D-aware_Image_Representations_from_Spatially_Discriminative_Language_CVPR_2025_paper.pdf) | CVPR | -- | [link](https://github.com/SpatialVision/Spatial-CLIP) | ![Star](https://img.shields.io/github/stars/SpatialVision/Spatial-CLIP.svg?style=social&label=Star) | SpatialBench |  |
| [R2D3:ImpartingSpatial Reasoning by Reconstructing 3D Scenes from 2D Images](https://openreview.net/pdf?id=Ku4lylDpjq) | ARXIV | -- | -- | -- | R2D3 |  |
| [ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning](https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_ReasonGrounder_LVLM-Guided_Hierarchical_Feature_Splatting_for_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.pdf) | CVPR | -- | [link](https://zhenyangliu.github.io/ReasonGrounder/) | -- | ReasoningGD |  |



## Monocular Video
| Title | Venue | Date | Code | Impact | Benchmark | Illustration |
| --- | --- | --- | --- | --- | --- | --- |
| [Explore until Confident: Efficient Exploration for Embodied Question Answering](https://arxiv.org/pdf/2403.15941) | ARXIV | 24-03 | [link](https://github.com/Stanford-ILIAD/explore-eqa) | ![Star](https://img.shields.io/github/stars/Stanford-ILIAD/explore-eqa.svg?style=social&label=Star) | -- |  |
| [DOES SPATIAL COGNITION EMERGE IN FRONTIER MODELS?](https://arxiv.org/pdf/2410.06468?) | ICLR | 24-10 | [link](https://github.com/apple/ml-space-benchmark) | ![Star](https://img.shields.io/github/stars/apple/ml-space-benchmark.svg?style=social&label=Star) | SPACE |  |
| [EgoDTM:Towards 3D-Aware Egocentric Video-Language Pretraining](https://arxiv.org/pdf/2503.15470) | ARXIV | 25-03 | [link](https://github.com/xuboshen/EgoDTM) | ![Star](https://img.shields.io/github/stars/xuboshen/EgoDTM.svg?style=social&label=Star) | EgoMCQ... |  |
| [STI-Bench: Are MLLMsReadyfor Precise Spatial-Temporal World Understanding?](https://arxiv.org/pdf/2503.23765) | ARXIV | 25-03 | [link](https://github.com/MINT-SJTU/STI-Bench) | ![Star](https://img.shields.io/github/stars/MINT-SJTU/STI-Bench.svg?style=social&label=Star) | STI-Bench |  |
| [ST-Think: How Multimodal Large Language Models Reason About 4D Worlds from Ego-Centric Videos](https://arxiv.org/pdf/2503.12542?) | ARXIV | 25-03 | [link](https://github.com/WPR001/Ego-ST) | ![Star](https://img.shields.io/github/stars/WPR001/Ego-ST.svg?style=social&label=Star) | Ego-ST |  |
| [From Flatland to Space: Teaching Vision-Language Models to Perceive and Reason in 3D](https://arxiv.org/pdf/2503.22976?) | ARXIV | 25-03 | [link](https://github.com/fudan-zvg/spar) | ![Star](https://img.shields.io/github/stars/fudan-zvg/spar.svg?style=social&label=Star) | SPAR-Bench |  |
| [ST-VLM:KinematicInstruction Tuning for Spatio-Temporal Reasoning in Vision-Language Models](https://arxiv.org/pdf/2503.19355?) | ARXIV | 25-03 | [link](https://github.com/mlvlab/ST-VLM) | ![Star](https://img.shields.io/github/stars/mlvlab/ST-VLM.svg?style=social&label=Star) | STKit |  |
| [VideoChat-R1: Enhancing Spatio-Temporal Perception via Reinforcement Fine-Tuning](https://arxiv.org/pdf/2504.06958?) | ARXIV | 25-04 | [link](https://github.com/OpenGVLab/VideoChat-R1) | ![Star](https://img.shields.io/github/stars/OpenGVLab/VideoChat-R1.svg?style=social&label=Star) | -- |  |
| [Embodied-R: Collaborative Framework for Activating Embodied Spatial Reasoning in Foundation Models via Reinforcement Learning](https://arxiv.org/pdf/2504.12680) | ARXIV | 25-04 | [link](https://github.com/EmbodiedCity/Embodied-R.code) | ![Star](https://img.shields.io/github/stars/EmbodiedCity/Embodied-R.code.svg?style=social&label=Star) | Embodied-R |  |
| [SpaceR: Reinforcing MLLMs in Video Spatial Reasoning](https://arxiv.org/abs/2504.01805v2) | ARXIV | 25-04 | [link](https://github.com/OuyangKun10/SpaceR) | ![Star](https://img.shields.io/github/stars/OuyangKun10/SpaceR.svg?style=social&label=Star) | VSI-Bench, STI-Bench, and SPAR-Bench |  |
| [Towards Understanding Camera Motions in Any Video](https://arxiv.org/pdf/2504.15376) | ARXIV | 25-04 | [link](https://github.com/sy77777en/CameraBench) | ![Star](https://img.shields.io/github/stars/sy77777en/CameraBench.svg?style=social&label=Star) | CameraBench |  |
| [VLM-3R: Vision-Language Models Augmented with Instruction-Aligned 3D Reconstruction](https://arxiv.org/pdf/2505.20279) | ARXIV | 25-05 | [link](https://github.com/VITA-Group/VLM-3R) | ![Star](https://img.shields.io/github/stars/VITA-Group/VLM-3R.svg?style=social&label=Star) | VSTiBench |  |
| [3DLLM-Mem: Long-Term Spatial-Temporal Memory for Embodied 3D Large Language Model](https://arxiv.org/pdf/2505.22657?) | ARXIV | 25-05 | [link](https://github.com/3DLLM-Mem/3DLLM-Mem/) | ![Star](https://img.shields.io/github/stars/3DLLM-Mem/3DLLM-Mem.svg?style=social&label=Star) | 3DMEM-Bench |  |
| [Spatial-MLLM Boosting MLLM Capabilities in Visual-based Spatial Intelligence](https://arxiv.org/pdf/2505.23747) | ARXIV | 25-05 | [link](https://github.com/diankun-wu/Spatial-MLLM) | ![Star](https://img.shields.io/github/stars/diankun-wu/Spatial-MLLM.svg?style=social&label=Star) | Spatial-MLLM-120k |  |
| [Out of Sight, Not Out of Context? Egocentric Spatial Reasoning in VLMs Across Disjoint Frames](https://arxiv.org/pdf/2505.24257) | ARXIV | 25-05 | -- | -- | DISJOINT-3DQA |  |
| [Learning from Videos for 3D World: Enhancing MLLMs with 3D Vision Geometry Priors](https://arxiv.org/abs/2505.24625) | ARXIV | 25-05 | [link](https://github.com/LaVi-Lab/VG-LLM) | ![Star](https://img.shields.io/github/stars/LaVi-Lab/VG-LLM.svg?style=social&label=Star) | VSI-Bench |  |
| [SpatialPrompting: Keyframe-driven Zero-Shot Spatial Reasoning with Off-the-Shelf Multimodal Large Language Models](https://arxiv.org/pdf/2505.04911?) | ARXIV | 25-05 | -- | -- | -- |  |
| [Spatial Understanding from Videos: Structured Prompts Meet Simulation Data](https://arxiv.org/pdf/2506.03642) | ARXIV | 25-06 | [link](https://github.com/Hyu-Zhang/SpatialMind) | ![Star](https://img.shields.io/github/stars/Hyu-Zhang/SpatialMind.svg?style=social&label=Star) | -- |  |
| [Thinking in Space: How Multimodal Large Language Models See, Remember, and Recall Spaces](https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_Thinking_in_Space_How_Multimodal_Large_Language_Models_See_Remember_CVPR_2025_paper.pdf) | CVPR | -- | [link](https://github.com/vision-x-nyu/thinking-in-space) | ![Star](https://img.shields.io/github/stars/vision-x-nyu/thinking-in-space.svg?style=social&label=Star) | VSI-Bench |  |
| [M3: 3D-Spatial Multimodal Memory](https://openreview.net/pdf?id=XYdstv3ySl) | ICLR | -- | [link](https://github.com/MaureenZOU/m3-spatial) | ![Star](https://img.shields.io/github/stars/MaureenZOU/m3-spatial.svg?style=social&label=Star) | -- |  |
| [Video-3D LLM: Learning Position-Aware Video Representation for 3D Scene Understanding](https://openaccess.thecvf.com/content/CVPR2025/papers/Zheng_Video-3D_LLM_Learning_Position-Aware_Video_Representation_for_3D_Scene_Understanding_CVPR_2025_paper.pdf) | CVPR | -- | -- | -- | -- |  |
| [OpenEQA: Embodied Question Answering in the Era of Foundation Models](https://openaccess.thecvf.com/content/CVPR2024/papers/Majumdar_OpenEQA_Embodied_Question_Answering_in_the_Era_of_Foundation_Models_CVPR_2024_paper.pdf) | CVPR | -- | [link](https://github.com/facebookresearch/open-eqa) | ![Star](https://img.shields.io/github/stars/facebookresearch/open-eqa.svg?style=social&label=Star) | OpenEQA |  |
| [EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite Towards Embodied AI](https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.pdf) | CVPR | -- | -- | -- | -- |  |
| [Compositional 4D Dynamic Scenes Understanding with Physics Priors for Video Question Answering](https://xingruiwang.github.io/projects/DynSuperCLEVR/) | ICLR | -- | [link](https://github.com/XingruiWang/NS-4DPhysics) | ![Star](https://img.shields.io/github/stars/XingruiWang/NS-4DPhysics.svg?style=social&label=Star) | DynSuperCLEVR |  |


## Multi-View Images
| Title | Venue | Date | Code | Impact | Benchmark | Illustration |
| --- | --- | --- | --- | --- | --- | --- |
| [Explore until Confident: Efficient Exploration for Embodied Question Answering](https://arxiv.org/pdf/2403.15941) | ARXIV | 24-03 | [link](https://github.com/Stanford-ILIAD/explore-eqa) | ![Star](https://img.shields.io/github/stars/Stanford-ILIAD/explore-eqa.svg?style=social&label=Star) | -- |  |
| [DOES SPATIAL COGNITION EMERGE IN FRONTIER MODELS?](https://arxiv.org/pdf/2410.06468?) | ICLR | 24-10 | [link](https://github.com/apple/ml-space-benchmark) | ![Star](https://img.shields.io/github/stars/apple/ml-space-benchmark.svg?style=social&label=Star) | SPACE |  |
| [EgoDTM:Towards 3D-Aware Egocentric Video-Language Pretraining](https://arxiv.org/pdf/2503.15470) | ARXIV | 25-03 | [link](https://github.com/xuboshen/EgoDTM) | ![Star](https://img.shields.io/github/stars/xuboshen/EgoDTM.svg?style=social&label=Star) | EgoMCQ... |  |
| [STI-Bench: Are MLLMsReadyfor Precise Spatial-Temporal World Understanding?](https://arxiv.org/pdf/2503.23765) | ARXIV | 25-03 | [link](https://github.com/MINT-SJTU/STI-Bench) | ![Star](https://img.shields.io/github/stars/MINT-SJTU/STI-Bench.svg?style=social&label=Star) | STI-Bench |  |
| [ST-Think: How Multimodal Large Language Models Reason About 4D Worlds from Ego-Centric Videos](https://arxiv.org/pdf/2503.12542?) | ARXIV | 25-03 | [link](https://github.com/WPR001/Ego-ST) | ![Star](https://img.shields.io/github/stars/WPR001/Ego-ST.svg?style=social&label=Star) | Ego-ST |  |
| [From Flatland to Space: Teaching Vision-Language Models to Perceive and Reason in 3D](https://arxiv.org/pdf/2503.22976?) | ARXIV | 25-03 | [link](https://github.com/fudan-zvg/spar) | ![Star](https://img.shields.io/github/stars/fudan-zvg/spar.svg?style=social&label=Star) | SPAR-Bench |  |
| [ST-VLM:KinematicInstruction Tuning for Spatio-Temporal Reasoning in Vision-Language Models](https://arxiv.org/pdf/2503.19355?) | ARXIV | 25-03 | [link](https://github.com/mlvlab/ST-VLM) | ![Star](https://img.shields.io/github/stars/mlvlab/ST-VLM.svg?style=social&label=Star) | STKit |  |
| [VideoChat-R1: Enhancing Spatio-Temporal Perception via Reinforcement Fine-Tuning](https://arxiv.org/pdf/2504.06958?) | ARXIV | 25-04 | [link](https://github.com/OpenGVLab/VideoChat-R1) | ![Star](https://img.shields.io/github/stars/OpenGVLab/VideoChat-R1.svg?style=social&label=Star) | -- |  |
| [Embodied-R: Collaborative Framework for Activating Embodied Spatial Reasoning in Foundation Models via Reinforcement Learning](https://arxiv.org/pdf/2504.12680) | ARXIV | 25-04 | [link](https://github.com/EmbodiedCity/Embodied-R.code) | ![Star](https://img.shields.io/github/stars/EmbodiedCity/Embodied-R.code.svg?style=social&label=Star) | Embodied-R |  |
| [SpaceR: Reinforcing MLLMs in Video Spatial Reasoning](https://arxiv.org/abs/2504.01805v2) | ARXIV | 25-04 | [link](https://github.com/OuyangKun10/SpaceR) | ![Star](https://img.shields.io/github/stars/OuyangKun10/SpaceR.svg?style=social&label=Star) | VSI-Bench, STI-Bench, and SPAR-Bench |  |
| [Towards Understanding Camera Motions in Any Video](https://arxiv.org/pdf/2504.15376) | ARXIV | 25-04 | [link](https://github.com/sy77777en/CameraBench) | ![Star](https://img.shields.io/github/stars/sy77777en/CameraBench.svg?style=social&label=Star) | CameraBench |  |
| [VLM-3R: Vision-Language Models Augmented with Instruction-Aligned 3D Reconstruction](https://arxiv.org/pdf/2505.20279) | ARXIV | 25-05 | [link](https://github.com/VITA-Group/VLM-3R) | ![Star](https://img.shields.io/github/stars/VITA-Group/VLM-3R.svg?style=social&label=Star) | VSTiBench |  |
| [3DLLM-Mem: Long-Term Spatial-Temporal Memory for Embodied 3D Large Language Model](https://arxiv.org/pdf/2505.22657?) | ARXIV | 25-05 | [link](https://github.com/3DLLM-Mem/3DLLM-Mem/) | ![Star](https://img.shields.io/github/stars/3DLLM-Mem/3DLLM-Mem.svg?style=social&label=Star) | 3DMEM-Bench |  |
| [Spatial-MLLM Boosting MLLM Capabilities in Visual-based Spatial Intelligence](https://arxiv.org/pdf/2505.23747) | ARXIV | 25-05 | [link](https://github.com/diankun-wu/Spatial-MLLM) | ![Star](https://img.shields.io/github/stars/diankun-wu/Spatial-MLLM.svg?style=social&label=Star) | Spatial-MLLM-120k |  |
| [Out of Sight, Not Out of Context? Egocentric Spatial Reasoning in VLMs Across Disjoint Frames](https://arxiv.org/pdf/2505.24257) | ARXIV | 25-05 | -- | -- | DISJOINT-3DQA |  |
| [Learning from Videos for 3D World: Enhancing MLLMs with 3D Vision Geometry Priors](https://arxiv.org/abs/2505.24625) | ARXIV | 25-05 | [link](https://github.com/LaVi-Lab/VG-LLM) | ![Star](https://img.shields.io/github/stars/LaVi-Lab/VG-LLM.svg?style=social&label=Star) | VSI-Bench |  |
| [SpatialPrompting: Keyframe-driven Zero-Shot Spatial Reasoning with Off-the-Shelf Multimodal Large Language Models](https://arxiv.org/pdf/2505.04911?) | ARXIV | 25-05 | -- | -- | -- |  |
| [Spatial Understanding from Videos: Structured Prompts Meet Simulation Data](https://arxiv.org/pdf/2506.03642) | ARXIV | 25-06 | [link](https://github.com/Hyu-Zhang/SpatialMind) | ![Star](https://img.shields.io/github/stars/Hyu-Zhang/SpatialMind.svg?style=social&label=Star) | -- |  |
| [Thinking in Space: How Multimodal Large Language Models See, Remember, and Recall Spaces](https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_Thinking_in_Space_How_Multimodal_Large_Language_Models_See_Remember_CVPR_2025_paper.pdf) | CVPR | -- | [link](https://github.com/vision-x-nyu/thinking-in-space) | ![Star](https://img.shields.io/github/stars/vision-x-nyu/thinking-in-space.svg?style=social&label=Star) | VSI-Bench |  |
| [M3: 3D-Spatial Multimodal Memory](https://openreview.net/pdf?id=XYdstv3ySl) | ICLR | -- | [link](https://github.com/MaureenZOU/m3-spatial) | ![Star](https://img.shields.io/github/stars/MaureenZOU/m3-spatial.svg?style=social&label=Star) | -- |  |
| [Video-3D LLM: Learning Position-Aware Video Representation for 3D Scene Understanding](https://openaccess.thecvf.com/content/CVPR2025/papers/Zheng_Video-3D_LLM_Learning_Position-Aware_Video_Representation_for_3D_Scene_Understanding_CVPR_2025_paper.pdf) | CVPR | -- | -- | -- | -- |  |
| [OpenEQA: Embodied Question Answering in the Era of Foundation Models](https://openaccess.thecvf.com/content/CVPR2024/papers/Majumdar_OpenEQA_Embodied_Question_Answering_in_the_Era_of_Foundation_Models_CVPR_2024_paper.pdf) | CVPR | -- | [link](https://github.com/facebookresearch/open-eqa) | ![Star](https://img.shields.io/github/stars/facebookresearch/open-eqa.svg?style=social&label=Star) | OpenEQA |  |
| [EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite Towards Embodied AI](https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.pdf) | CVPR | -- | -- | -- | -- |  |
| [Compositional 4D Dynamic Scenes Understanding with Physics Priors for Video Question Answering](https://xingruiwang.github.io/projects/DynSuperCLEVR/) | ICLR | -- | [link](https://github.com/XingruiWang/NS-4DPhysics) | ![Star](https://img.shields.io/github/stars/XingruiWang/NS-4DPhysics.svg?style=social&label=Star) | DynSuperCLEVR |  |

## Others

| Title | Venue | Date | Code | Impact | Benchmark | Illustration |
| --- | --- | --- | --- | --- | --- | --- |
| [Advancing Spatial Reasoning in Large Language Models: An In-Depth Evaluation and Enhancement Using the StepGame Benchmark](https://arxiv.org/abs/2401.03991) | AAAI | 24-01 | -- | -- | StepGame |  |
| [Holistic Autonomous Driving Understanding by Bird's-Eye-View Injected Multi-Modal Large Models](https://arxiv.org/pdf/2401.00988) | CVPR | 24-01 | [link](https://github.com/xmed-lab/NuInstruct) | ![Star](https://img.shields.io/github/stars/xmed-lab/NuInstruct.svg?style=social&label=Star) | NuInstruct |  |
| [ShapeLLM: Universal 3D Object Understanding for Embodied Interaction](https://arxiv.org/pdf/2402.17766) | ECCV | 24-02 | [link](https://github.com/qizekun/ShapeLLM) | ![Star](https://img.shields.io/github/stars/qizekun/ShapeLLM.svg?style=social&label=Star) | -- |  |
| [BAT: Learning to Reason about Spatial Sounds with Large Language Models](https://arxiv.org/pdf/2402.01591) | ARXIV | 24-02 | [link](https://github.com/zszheng147/Spatial-AST) | ![Star](https://img.shields.io/github/stars/zszheng147/Spatial-AST.svg?style=social&label=Star) | -- |  |
| [Beyond Lines and Circles: Unveiling the Geometric Reasoning Gap in Large Language Models](https://arxiv.org/pdf/2402.03877) | ARXIV | 24-02 | -- | -- | euclidea |  |
| [Agent3D-Zero: An Agent for Zero-shot 3D Understanding](https://arxiv.org/pdf/2403.11835) | ECCV | 24-03 | -- | -- | -- |  |
| [Scene-LLM: Extending Language Model for 3D Visual Understanding and Reasoning](https://arxiv.org/abs/2403.11401) | WACV | 24-03 | -- | -- | ScanQA, SQA3D, ALFRED |  |
| [KnowYour Neighbors: Improving Single-View Reconstruction via Spatial Vision-Language Reasoning](https://arxiv.org/pdf/2404.03658) | CVPR | 24-04 | [link](https://github.com/ruili3/Know-Your-Neighbors) | ![Star](https://img.shields.io/github/stars/ruili3/Know-Your-Neighbors.svg?style=social&label=Star) | -- |  |
| [RoboPoint: AVision-Language Model for Spatial Affordance Prediction for Robotics](https://arxiv.org/pdf/2406.10721) | ARXIV | 24-06 | [link](https://github.com/wentaoyuan/RoboPoint) | ![Star](https://img.shields.io/github/stars/wentaoyuan/RoboPoint.svg?style=social&label=Star) | Robopoint |  |
| [SpaRC and SpaRP: Spatial Reasoning Characterization and Path Generation for Understanding Spatial Reasoning Capability of Large Language Models](https://arxiv.org/abs/2406.04566) | ACL | 24-06 | [link](https://github.com/UKPLab/acl2024-sparc-and-sparp) | ![Star](https://img.shields.io/github/stars/UKPLab/acl2024-sparc-and-sparp.svg?style=social&label=Star) | sparp |  |
| [I KnowAbout“Up”! Enhancing Spatial Reasoning in Visual Language Models Through 3D Reconstruction](https://arxiv.org/pdf/2407.14133) | ARXIV | 24-07 | -- | -- | -- |  |
| [GRASP: A Grid-Based Benchmark for Evaluating Commonsense Spatial Reasoning](https://arxiv.org/pdf/2407.01892?) | ARXIV | 24-07 | [link](https://github.com/jasontangzs0/GRASP) | ![Star](https://img.shields.io/github/stars/jasontangzs0/GRASP.svg?style=social&label=Star) | -- |  |
| [Do Vision-Language Models Represent Space and How? Evaluating Spatial Frame of Reference Under Ambiguities](https://arxiv.org/pdf/2410.17385) | ICLR-ORAL | 24-10 | [link](https://spatial-comfort.github.io/) | -- | COMFORT |  |
| [Synthetic Vision: Training Vision-Language Models to Understand Physics](https://arxiv.org/pdf/2412.08619) | -- | 24-12 | -- | -- | -- |  |
| [Emma-X: An Embodied Multimodal Action Model with Grounded Chain of Thought and Look-ahead Spatial Reasoning](https://arxiv.org/pdf/2412.11974) | -- | 24-12 | [link](https://github.com/declare-lab/Emma-X) | ![Star](https://img.shields.io/github/stars/declare-lab/Emma-X.svg?style=social&label=Star) | Emma-X |  |
| [Do Multimodal Language Models Really Understand Direction? A Benchmark for Compass Direction Reasoning](https://arxiv.org/pdf/2412.16599?) | ARXIV | 24-12 | -- | -- | -- |  |
| [PHYSBENCH: BENCHMARKING AND ENHANCING VISION-LANGUAGE MODELS FOR PHYSICAL WORLD UNDERSTANDING](https://arxiv.org/abs/2501.16411) | ARXIV | 25-01 | [link](https://github.com/USC-GVL/PhysBench) | ![Star](https://img.shields.io/github/stars/USC-GVL/PhysBench.svg?style=social&label=Star) | PhysBench |  |
| [EMBODIEDEVAL: Evaluate Multimodal LLMs as Embodied Agents](https://arxiv.org/pdf/2501.11858) | ARXIV | 25-01 | -- | -- | EMBODIEDEVAL |  |
| [Social-LLaVA: Enhancing Robot Navigation through Human-Language Reasoning in Social Spaces](https://arxiv.org/pdf/2501.09024) | ARXIV | 25-01 | [link](https://cs.gmu.edu/~xiao/Research/SNEI/) | -- | Social-LLaVA |  |
| [SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model](https://arxiv.org/abs/2501.15830) | ARXIV | 25-01 | [link](https://github.com/SpatialVLA/SpatialVLA) | ![Star](https://img.shields.io/github/stars/SpatialVLA/SpatialVLA.svg?style=social&label=Star) | SpatialVLA |  |
| [FoREST: Frame of Reference Evaluation in Spatial Reasoning Tasks](https://arxiv.org/pdf/2502.17775) | ARXIV | 25-02 | [link](https://github.com/HLR/FoREST) | ![Star](https://img.shields.io/github/stars/HLR/FoREST.svg?style=social&label=Star) | FoREST |  |
| [A Real-to-Sim-to-Real Approach to Robotic Manipulation with VLM-Generated Iterative Keypoint Rewards](https://arxiv.org/pdf/2502.08643) | ICRA | 25-02 | [link](https://github.com/shivanshpatel35/IKER) | ![Star](https://img.shields.io/github/stars/shivanshpatel35/IKER.svg?style=social&label=Star) | -- |  |
| [pace-Aware Instruction Tuning: Dataset and Benchmark for Guide Dog Robots Assisting the Visually Impaired](https://arxiv.org/pdf/2502.07183) | ARXIV | 25-02 | [link](https://github.com/byungokhan/Space-awareVLM) | ![Star](https://img.shields.io/github/stars/byungokhan/Space-awareVLM.svg?style=social&label=Star) | SA-Bench |  |
| [VL-Nav: Real-time Vision-Language Navigation with Spatial Reasoning](https://arxiv.org/pdf/2502.00931) | ARXIV | 25-02 | -- | -- | -- |  |
| [SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation](https://arxiv.org/pdf/2502.13143) | ARXIV | 25-02 | [link](https://github.com/qizekun/SoFar) | ![Star](https://img.shields.io/github/stars/qizekun/SoFar.svg?style=social&label=Star) | -- |  |
| [3DAxisPrompt: Promoting the 3D Grounding and Reasoning in GPT-4o](https://arxiv.org/pdf/2503.13185) | -- | 25-03 | -- | -- | -- |  |
| [EmbodiedVSR: Dynamic Scene Graph-Guided Chain-of-Thought Reasoning for Visual Spatial Tasks](https://arxiv.org/pdf/2503.11089) | ARXIV | 25-03 | -- | -- | -- |  |
| [Scaling and Beyond: Advancing Spatial Reasoning in MLLMs Requires New Recipes](https://arxiv.org/abs/2504.15037) | ARXIV | 25-04 | -- | -- | -- |  |
| [A Survey of Large Language Model-Powered Spatial Intelligence Across Scales: Advances in Embodied Agents, Smart Cities, and Earth Science](https://arxiv.org/pdf/2504.09848) | ARXIV | 25-04 | -- | -- | -- |  |
| [Ross3D: Reconstructive Visual Instruction Tuning with 3D-Awareness](https://arxiv.org/abs/2504.01901) | ARXIV | 25-04 | [link](https://github.com/haochen-wang409/ross3d) | ![Star](https://img.shields.io/github/stars/haochen-wang409/ross3d.svg?style=social&label=Star) | sqa3d, scanqa |  |
| [Locate 3D: Real-World Object Localization via Self-Supervised Learning in 3D](https://arxiv.org/pdf/2504.14151) | ARXIV | 25-04 | [link](https://github.com/facebookresearch/locate-3d) | ![Star](https://img.shields.io/github/stars/facebookresearch/locate-3d.svg?style=social&label=Star) | SR3D,NR3D,ScanRefer |  |
| [SpatialScore Towards Unified Evaluation for Multimodal Spatial Understanding](https://arxiv.org/pdf/2505.17012) | ARXIV | 25-05 | [link](https://github.com/haoningwu3639/SpatialScore/) | ![Star](https://img.shields.io/github/stars/haoningwu3639/SpatialScore.svg?style=social&label=Star) | SpatialScore |  |
| [A Light and Smart Wearable Platform with Multimodal Foundation Model for Enhanced Spatial Reasoning in People with Blindness and Low Vision](https://arxiv.org/pdf/2505.10875) | ECCV | 25-05 | -- | -- | LVSQA |  |
| [ManipBench: Benchmarking Vision-Language Models for Low-Level Robot Manipulation](https://arxiv.org/pdf/2505.09698) | ARXIV | 25-05 | [link](https://manipbench.github.io/) | -- | ManipBench |  |
| [InSpire: Vision-Language-Action Models with Intrinsic Spatial Reasoning](https://arxiv.org/pdf/2505.13888) | ARXIV | 25-05 | [link](https://github.com/Koorye/Inspire) | ![Star](https://img.shields.io/github/stars/Koorye/Inspire.svg?style=social&label=Star) | -- |  |
| [Universal Visuo-Tactile Video Understanding for Embodied Interaction](https://arxiv.org/pdf/2505.22566) | ARXIV | 25-05 | -- | -- | -- |  |
| [MineAnyBuild: Benchmarking Spatial Planning for Open-world AI Agents](https://arxiv.org/pdf/2505.20148) | ARXIV | 25-05 | [link](https://github.com/MineAnyBuild/MineAnyBuild) | ![Star](https://img.shields.io/github/stars/MineAnyBuild/MineAnyBuild.svg?style=social&label=Star) | -- |  |
| [LLaVA-4D: Embedding SpatioTemporal Prompt into LMMs for 4D Scene Understanding](https://arxiv.org/abs/2505.12253) | ARXIV | 25-05 | -- | -- | scan2cap, scanqa, scanref, multi3drefer, (自己提的)chat4d |  |
| [SpaCE-10: A Comprehensive Benchmark for Multimodal Large Language Models in Compositional Spatial Intelligence](https://arxiv.org/abs/2506.07966v1) | ARXIV | 25-06 | [link](https://github.com/VisionXLab/SpaCE-10) | ![Star](https://img.shields.io/github/stars/VisionXLab/SpaCE-10.svg?style=social&label=Star) | SpaCE-10 |  |
| [Robot-R1: Reinforcement Learning for Enhanced Embodied Reasoning in Robotics](https://arxiv.org/pdf/2506.00070) | ARXIV | 25-06 | -- | -- | Robot-R1 Bench |  |
| [Struct2D: A Perception-Guided Framework for Spatial Reasoning in Large Multimodal Models](https://arxiv.org/pdf/2506.04220) | ARXIV | 25-06 | [link](https://github.com/neu-vi/struct2d) | ![Star](https://img.shields.io/github/stars/neu-vi/struct2d.svg?style=social&label=Star) | -- |  |
| [Evaluating and enhancing spatial cognition abilities of large language models](https://www.tandfonline.com/doi/pdf/10.1080/13658816.2025.2490701) | IJGIS | 25-24 | [link](https://github.com/tbressers/WizardLM-2-8x22B) | ![Star](https://img.shields.io/github/stars/tbressers/WizardLM-2-8x22B.svg?style=social&label=Star) | -- |  |
| [LL3DA: Visual Interactive Instruction Tuning for Omni-3D Understanding, Reasoning, and Planning](https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_LL3DA_Visual_Interactive_Instruction_Tuning_for_Omni-3D_Understanding_Reasoning_and_CVPR_2024_paper.pdf) | CVPR | -- | [link](https://github.com/Open3DA/LL3DA) | ![Star](https://img.shields.io/github/stars/Open3DA/LL3DA.svg?style=social&label=Star) | -- |  |
| [GPT-4V(ision) for Robotics: Multimodal Task Planning From Human Demonstration](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10711245) | OBOTICS AND AUTOMATION LETTERS | -- | -- | -- | -- |  |
| [3D-Mem: 3DScene Memory for Embodied Exploration and Reasoning](https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_3D-Mem_3D_Scene_Memory_for_Embodied_Exploration_and_Reasoning_CVPR_2025_paper.pdf) | CVPR | -- | [link](https://github.com/UMass-Embodied-AGI/3D-Mem) | ![Star](https://img.shields.io/github/stars/UMass-Embodied-AGI/3D-Mem.svg?style=social&label=Star) | -- |  |
| [PhysVLM: Enabling Visual Language Models to Understand Robotic Physical Reachability](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhou_PhysVLM_Enabling_Visual_Language_Models_to_Understand_Robotic_Physical_Reachability_CVPR_2025_paper.pdf) | CVPR | -- | -- | -- | -- |  |


# Acknowledge

- [Awesome-Spatial-Reasoning](https://github.com/yyyybq/Awesome-Spatial-Reasoning)



# 🌍 Visitor Statistics

[![Visitor Map](https://clustrmaps.com/map_v2.png?d=qwnP2zUR1Jr_dpMlFJj47-CNhM7vXZ1nnbcTbZy1Bw4)](https://clustrmaps.com/site/1btRk)



# ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=prism-visual-spatial-intelligence/Awesome-Visual-Spatial-Reasoning&type=Date)](https://www.star-history.com/#prism-visual-spatial-intelligence/Awesome-Visual-Spatial-Reasoning&Date)