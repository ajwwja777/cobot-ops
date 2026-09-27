# 项目入口

先读 `/data/LFT-W02_data/jiaan/jiaan/agent-guide/AGENTS.md`，再读本项目 [README.md](README.md) 与 [迁移记录](docs/MIGRATION.md)。按用户当前任务执行，保留已有成果和其他对话的改动。

项目：cobot-ops。目标：统一使用手册、部署维护、健康检查、服务启停、日志与 PID、备份恢复及故障分流，让命令行和网页使用同一套运行入口。

进度见迁移记录：已完成入口、Cobot 目录与恢复证据迁移，cobot-web 已切换新目录并使用本项目 runtime；算法／数据和历史硬件依赖仍待逐批验收。现场 HTTP／任务故障先读 [恢复手册](docs/WEB_RECOVERY.md)，终端工具默认只读或预览，停止须按现场真实状态执行。用户指定跨项目迁移由已有 cobot_rlt 对话统筹；不得把旧资产登记视为已迁移或把源码 clone 视为运行验证。跨项目问题按项目说明交给对应领域，证据与进展写回所属项目。
