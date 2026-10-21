# GulfGate 海湾之门 · 国别研判助手

[简体中文](README.md) · [English](README.en.md) · [العربية](README.ar.md)

<div align="center">
  <img src="docs/images/hero-analysis.png" alt="GulfGate Country Analysis Skill hero" width="100%">
</div>

> 把海湾六国的零散信息，压缩成一条能开会、能分工、能停损的决策简报。

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-compatible-1f6f50)](SKILL.md)
[![Markets](https://img.shields.io/badge/GCC%20markets-6-c18b49)](#覆盖范围)
[![Python](https://img.shields.io/badge/Python-3%20standard%20library-3776ab)](#安装)
[![Validation](https://img.shields.io/badge/tests-passing-2f7d55)](tests/validate_package.py)

这不是又一个“生成中东市场报告”的提示词。它会把国家、细分法域、产品用途、交易角色、证据状态和行动阶段拆开，最后回答四个管理者真正关心的问题：

1. 做不做？
2. 先做什么？
3. 什么条件满足后再加码？
4. 什么信号出现时暂停、改道或退出？

## 为什么需要它

出海项目最常见的误判，不是信息太少，而是把不同层级的信息混成了一个结论：

- “市场很大”被当成企业能成交；
- “伙伴有关系”被当成伙伴能履约；
- “产品有证书”被当成项目和用途都已放行；
- “网页还能打开”被当成规则仍然有效；
- “见过两次面”被当成可以报价、签约或压库存。

国别研判助手把这些跳跃拆开，要求每条建议回到证据、计算或明确的规划假设。

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

完整匿名示例见 [examples/analysis-demo.md](examples/analysis-demo.md)。示例只演示判断结构，不把历史知识包装成已经核验的现行规则。

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

必须复制整个目录，不能只拿走 `SKILL.md`。`references/`、`assets/` 和 `scripts/` 是运行资源的一部分。

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

测试只证明“包可读、结构可用、脚本能运行”，不证明所有政策、税率或认证结论在当前时点仍然有效。

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

## 事实边界

本 Skill 提供研究方法和历史检索线索，不替代律师、税务师、医生、工程师或主管机关的个案判断。政策、费率、资质、项目状态和法律责任等高影响事实，必须按当次来源核验并保留发布日期、适用范围与核验日期。

Skill 不附带搜索权限、API Key 或后台服务。宿主没有联网能力时，应当明确输出“待核验”，继续完成不依赖实时事实的分析与补证清单。

## 同系列项目

出海新人培训使用独立的 [GulfGate 出海判断力训练助手](https://github.com/origami3521905038-hash/gulfgate-country-training)。两个仓库可以单独安装；训练主线临时调用研判能力时，支持带着阶段简报返回原情境。

## 共创者

本项目由 [@origami3521905038-hash](https://github.com/origami3521905038-hash) 与 [@18719203981lkr-spec](https://github.com/18719203981lkr-spec) 共同完成。

欢迎通过 Issue 和 Pull Request 提交来源核验、行业补充、方法改进与跨宿主测试。协作规范见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可

本仓库暂未附加开放许可证。版权归共创者所有；公开复用、商业使用或再分发前，请先取得作者书面许可。

