# Cobot 运维旧入口（已并入对应项目）

2026-09-27 用户决定不再单独维护 ops 项目。网页使用、启停、任务／PID 管理、故障恢复和终端操作归 [cobot-web](https://github.com/ajwwja777/cobot-web)；硬件、数采和算法直接在相应项目沟通。

## 现在使用哪里

- A6000：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web`。
- Cobot：`/home/agilex/jiaan/project/cobot-web`。
- [完整命令行流程](https://github.com/ajwwja777/cobot-web/blob/main/docs/COMMAND_LINE.md)。
- [故障恢复手册](https://github.com/ajwwja777/cobot-web/blob/main/docs/WEB_RECOVERY.md)。
- 常用入口：在 cobot-web 中运行 `python3 scripts/console.py --help`。
- 原 `scripts/console_recovery.py` 仅转发到同级 cobot-web，不再维护第二份实现。

## 为什么旧目录还在

现场 `runtime/` 中有运行中的网页日志、PID、任务状态、恢复证据，`tools/uv` 仍被部署流程使用。本批保留这些路径，不能在服务写入时直接删除。它们由对应项目接管，后续在明确停机／验证批次搬迁；保留目录不表示仍有独立运维服务。

本仓库只保留迁移历史和兼容指引，Git 历史不删除。具体证据见 [迁移记录](docs/MIGRATION.md)。
