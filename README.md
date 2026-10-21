# GulfGate 海湾之门 · 国别研判助手

<p><a href="README.md"><u>简体中文</u></a> · <a href="README.en.md"><u>English</u></a> · <a href="README.ar.md"><u>العربية</u></a></p>

<div align="center">
  <img src="docs/images/hero-analysis.png" alt="GulfGate Country Analysis Skill hero" width="100%">
</div>

> 把海湾六国的零散信息，转化为能开会、能分工、能立即行动的业务决策。

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-compatible-1f6f50)](SKILL.md)
[![Markets](https://img.shields.io/badge/GCC%20markets-6-c18b49)](#覆盖范围)
[![Python](https://img.shields.io/badge/Python-3%20standard%20library-3776ab)](#安装)
[![Validation](https://img.shields.io/badge/tests-passing-2f7d55)](tests/validate_package.py)

GulfGate 把国家、细分法域、产品用途、交易角色、证据状态和行动阶段放进同一套分析框架，让团队快速形成共识，并直接回答四个管理者关心的问题：

1. 做不做？
2. 先做什么？
3. 什么条件满足后再加码？
4. 什么信号出现时暂停、改道或退出？

## 一套输入，直接得到可执行结果

- **进入顺序**：先做哪个国家、哪个客户、哪条交易路径；
- **决策证据**：市场、买方、伙伴、准入、交付与回款分别需要什么；
- **行动路线**：30/60/90 天动作、责任角色、里程碑与升级条件；
- **管理层简报**：一页看清机会、成本、关键变量、下一步与资源投入。

## 适合这些团队

| 角色 | 你能得到什么 |
| --- | --- |
| 创始人 / 海外负责人 | 国家与进入路径比较、资源优先级、阶段闸门 |
| 销售 / 商务 | 客户与伙伴判断、采购链拆解、成交与回款路径 |
| 项目 / 交付 | 准入、进口、安装、验收与本地运营准备清单 |
| 法务 / 合规 | 法域、产品用途、证据层级和升级事项的结构化梳理 |

## 三个高频案例

<div align="center">
  <img src="docs/images/cases-analysis.png" alt="Three Gulf market analysis use cases" width="100%">
</div>

1. **阿联酋 · 商用储能经销进入**：从“找经销商”推进到买方、进口责任、技术服务和 90 天小单验证。
2. **沙特 · 医疗器械伙伴筛选**：把企业注册、产品准入、授权代表、项目资格和售后能力拆成独立证据。
3. **卡塔尔 · 建材项目投标预检**：在报价前核对项目买方、采购资格、技术文件、交付和付款条件。

## 真实使用示例

<div align="center">
  <img src="docs/images/demo-analysis.png" alt="Country analysis demo output" width="100%">
</div>

示例输入：

```text
使用 $gulfgate-country-analysis。
我们是一家中型商用储能企业，计划通过当地经销商进入阿联酋，暂无当地实体。
首批目标客户为工业园区和商业楼宇。请判断是否值得推进，并给出 90 天验证计划。
```

完整匿名示例与案例清单见 [examples/analysis-demo.md](examples/analysis-demo.md)。

## 三种工作模式

| 模式 | 适合什么时候使用 | 典型产出 |
| --- | --- | --- |
| 研究 `research` | 了解机会、选择市场、形成进入规划 | 市场假设、客户与采购链、路径比较、验证计划 |
| 诊断 `diagnosis` | 已有方案，需要检查逻辑与证据缺口 | 误判点、缺失证据、修复顺序、重判条件 |
| 预检 `precheck` | 投标、签约、设实体或重大投入前 | 可推进/暂缓条件、关键闸门、停止条件 |

复杂任务会交付一个自包含的 Markdown 文件，图、表、比例条和关键来源都在同一份文件中，不要求读者再拼装其他附件。

## 安装

### Codex 或其他支持 `SKILL.md` 的宿主

```bash
git clone https://github.com/origami3521905038-hash/gulfgate-country-analysis.git
mkdir -p ~/.codex/skills
cp -R gulfgate-country-analysis ~/.codex/skills/
```

完整安装整个目录即可使用；`references/`、`assets/` 和 `scripts/` 会随 Skill 一起提供。

### 快速验证

```bash
cd gulfgate-country-analysis
python tests/validate_package.py
```

本地检索不依赖第三方 Python 包：

```bash
python scripts/lookup.py record C-AE-M2-01
python scripts/lookup.py search 清关 --country AE --limit 3
python scripts/lookup.py term 清关 --limit 3
```

## 覆盖范围

- 国家：沙特阿拉伯、阿联酋、卡塔尔、科威特、巴林、阿曼
- 行业入口：新能源、建材与工程承包、跨境电商与消费电子、医疗器械、轻工业产品
- 业务链：市场机会、商业生态、伙伴筛选、跨文化接触、准入投标、合同回款、交付运营、合规危机
- 资源：565 条结构化记录、1,549 条业务术语、6 国与 5 行业知识文件、8 套方法文件

## 测试证据

<div align="center">
  <img src="docs/images/test-analysis.png" alt="Country analysis validation results" width="100%">
</div>

`tests/validate_package.py` 检查：

- YAML frontmatter 与 Skill 名称；
- README 和 Skill 内部本地链接；
- 核心知识路径、记录文件和术语文件；
- `records.jsonl` 能否解析；
- 本地检索脚本能否返回可引用的结构化记录；
- GitHub Actions 每次 push 和 pull request 自动执行同一套校验。

同一套校验会随每次更新自动运行，持续保障知识结构、检索脚本、文档链接和发布文件的一致性。

## 工作流

```text
业务问题
  → 界定国家 / 法域 / 产品用途 / 交易角色
  → 按知识路由读取必要资料
  → 对高影响可变事实进行当次官方核验
  → 建立决策地图与情景
  → 比较路径、成本、证据与可逆性
  → 交付单一 Markdown 报告
  → 写明阶段闸门、下一动作和停止条件
```

## 仓库结构

```text
.
├── SKILL.md
├── references/
│   ├── knowledge/
│   └── modes/
├── assets/
│   └── terms.csv
├── scripts/
│   └── lookup.py
├── examples/
├── tests/
└── docs/
```

## 官方来源核验链

遇到政策、费率、资质、项目状态和法律要求时，Skill 会优先定位主管机关和官方正文，核对发布日期、适用范围、版本线索和本次核验日期。

复杂报告会把关键来源直接放在对应结论附近，让读者能沿着“来源 → 判断 → 影响 → 行动”完整复核。联网工具可用时执行实时核验；本地知识库则持续支持框架分析、案例比较和补证清单。

## 同系列项目

出海新人培训使用独立的 [GulfGate 出海判断力训练助手](https://github.com/origami3521905038-hash/gulfgate-country-training)。两个仓库可以单独安装；训练主线临时调用研判能力时，支持带着阶段简报返回原情境。

## 共创者

本项目由 [@origami3521905038-hash](https://github.com/origami3521905038-hash) 与 [@18719203981lkr-spec](https://github.com/18719203981lkr-spec) 共同完成。

欢迎通过 Issue 和 Pull Request 提交来源核验、行业补充、方法改进与跨宿主测试。协作规范见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可

版权归两位共创者共同所有。欢迎就公开复用、商业合作、行业扩展和定制版本联系作者获取授权。

