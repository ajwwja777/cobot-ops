# Cobot 使用、部署与运维

统一使用手册、部署维护、健康检查、服务启停、日志与 PID、备份恢复及故障分流，让命令行和网页使用同一套运行入口。

## 入口与位置

- 先读统一框架：`/data/LFT-W02_data/jiaan/jiaan/agent-guide/AGENTS.md`。
- A6000 主工作区：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-ops`。
- 笔记本对话入口：`D:\Code\jiaan_workspace\cobot-ops`。
- 自有独立仓库：`https://github.com/ajwwja777/cobot-ops`（目标分支 `main`）。
- Cobot 位置：`/home/agilex/jiaan/project/cobot-ops`，恢复证据和现场服务状态归入 `runtime/`，独立终端恢复入口见下文。
- 当前阶段：恢复证据已迁移；cobot-web 已在新目录服务 8015，日志和任务状态使用本项目 runtime。模型、数据、硬件历史环境仍有旧路径依赖，继续逐批验收。

## 现场故障入口

[网页故障与终端恢复手册](docs/WEB_RECOVERY.md)：刷新／重启的适用范围、HTTP 失败、保存结果不确定、任务 PID 与子进程、模型显存释放、磁盘故障。

在 Cobot 执行：

```bash
cd /home/agilex/jiaan/project/cobot-ops
python3 scripts/console_recovery.py status
python3 scripts/console_recovery.py snapshot
```

工具只需系统 Python 3 标准库，不依赖网页响应。停止命令默认预览；实际中断及限制请先读手册。测试放在 `tests/`，开发验证用 `python -m pytest -q tests`；现场不必安装 pytest。

## 负责什么

现场服务编排和真实健康验证、运行记录、路径及版本登记、故障证据和恢复方法。服务日志／PID／任务状态集中在本项目 runtime/<服务或任务>/；训练实验产物仍归所属算法项目。

先收集故障证据，再交给领域专家；不凭启动命令返回成功就声明硬件就绪。CAN／归位／相机交 cobot-control，数据交 cobot-dagger，模型交 vla-platform，RL 交 rl-platform，页面交 cobot-web。

## 机器与资产

A6000 负责主代码、Git、维护文档、主要开发验证环境、数据处理和离线评测；训练按资源需要在 A6000／已授权训练机进行。Cobot 只部署本项目现场实际需要的硬件、采集、推理、网页或维护组件，不复制仿真资产和完整训练环境。

Cobot 采集及评测数据统一规划在 `/home/agilex/jiaan/data/`。模型放所属项目的 `models/`（上游已有 `checkpoints/` 等目录时保留其源码布局，由配置明确实际权重位置）；同一资产跨项目引用，避免重复复制。现场服务日志、PID 和状态交由 `cobot-ops/runtime/` 管理；训练 checkpoint、配置和指标保留在所属项目 `outputs/<实验>/`。环境、模型、大数据与 runtime 不入 Git。

## 项目协作

每次交接至少带症状、机器／版本、命令与关键日志、复现条件、已检查项；专家修复后由运维验证部署并更新手册。跨对话通过项目记录交接，不能假设聊天自动共享记忆。

先读本次任务涉及的依赖项目入口和接口说明，再修改相关边界；接口变更要记录受影响调用方与验证方式。常用项目：`cobot-control`、`cobot-dagger`、`vla-platform`、`rl-platform`、`cobot-web`、`cobot-ops`，主工作区均在 `/data/LFT-W02_data/jiaan/jiaan/projects/`。需要专题对话时仍共享所属项目，不因此重复建立业务仓库。

## 下一步

继续补充故障实例和人工恢复经验，按明确范围迁移硬件与算法依赖；终端恢复入口与网页任务生命周期保持接口一致。不要把文档和只读验证当作真实机器人恢复演练。

旧位置、验收条件和切换／清理规则见迁移记录。

来源：2026-09-27 用户确认的项目划分、机器职责与逐批迁移方案。用户指定已有 cobot_rlt 对话继续统筹跨项目迁移；领域项目按需交接专业维护。当前已验收恢复证据批次，详见 `docs/MIGRATION.md`。

## 保留事项

2026-09-27 上一轮容量核对：内置盘可用约 171 GB，旧 projects 已约 193 GB，尚未计入数据。本轮目录/Git 初始化不受此限制；大文件迁移前必须重新确认容量与存储方案。
