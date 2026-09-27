# Cobot 使用、部署与运维：迁移记录

当前归属：2026-09-27 用户取消独立 ops 维护层，工具／手册转入 cobot-web；本文件保留历史。

更新：2026-09-27。入口初始化、恢复证据归档、网页新目录切换和本页末尾的终端恢复入口批次已完成；模型／数据和部分硬件环境仍有旧路径依赖。跨项目迁移由当前已有 cobot_rlt 对话统筹执行。以下早期批次保留当时状态。

## 已有位置与成果

以下是已读项目记录与前序目录核验的入口清单，不表示本轮重新完整验证每项资产。执行某批迁移前须核对实际目录、符号链接、Git 状态和使用者。

| 机器 | 旧位置／已有依赖 | 保留事项 |
|---|---|---|
| Cobot | `/media/agilex/Getea1/jiaan/projects/cobot-platform/scripts` | 现有启停、状态和维护入口，与控制、网页项目共同厘清最终归属。 |
| Cobot（原址） | `/home/agilex/jiaan-recovery/20260927-getea-offline` | 已验收迁移，原目录已清理，不再作为可用入口。 |
| Cobot（现址） | `/home/agilex/jiaan/project/cobot-ops/runtime/recovery/20260927-getea-offline` | 17 个恢复证据文件保留原内容、权限及时间，不自动清理。 |
| A6000 | `/data/LFT-W02_data/jiaan/projects/proj-20260904-cobot-realworld-rl/methods/openpi_rlt/audits/2026-09-27-getea-usb-offline-ui-recovery.md` | 已保存的恢复审计；不能据此宣称整盘完整性已经验证。 |

## 首个候选验收范围

先整理现用命令、路径、健康检查和故障分流，迁移一项只读状态查询；核验日志来源和 PID 对应关系，不重启现有服务。

验收要求：状态来自实际进程／服务，命令可追溯且不触发意外运动；能把错误交给正确项目，并保留可复现证据。

## 逐批迁移约定

一次只处理一个明确范围，记录来源、目标、依赖、版本／校验值和回退入口；先复制与验证，再切换，最后清理对应旧文件。未验收不切换，仍被依赖或缺少可靠备份的原件不清理。共有目录按文件实际归属处理，保留其他对话的未提交修改及共享资产。

迁移批次记录至少包括：范围、来源与目标、验证结果、切换状态、可清理清单及实际清理结果。初始化完成仅表示入口与 Git 可接管，不代表运行环境或业务功能已验收。

入口初始化批次没有迁移／删除旧文件。后续恢复证据批次结果如下；未安装运行环境、启动训练、加载模型或控制机器人，也没有变更当前网页服务。

## 初始化发布记录

- 2026-09-27：项目目录与维护入口已建立，基础提交已 push 并核对远端 main 一致。
- 仓库：https://github.com/ajwwja777/cobot-ops（独立仓库，非 GitHub fork）。
- 首次发布提交：`22651c7ee958ae22ae81b0c1f18a226c5620ac5b`。
- 本记录在首次发布验证后追加并单独提交；最新版本以 main 为准。
- 运行状态：源码／文档基础已发布，业务迁移、环境安装及新位置运行验收尚未开展。

## 2026-09-27：Cobot 目录与恢复证据（已验收）

- 执行：用户指定当前跨项目迁移对话（笔记本 `cobot_rlt`）持续统筹，领域问题按需交接专家，结果写回所属项目和 guide。
- 六个目录已建立：`/home/agilex/jiaan/project/` 下的 `cobot-control`、`cobot-dagger`、`vla-platform`、`rl-platform`、`cobot-web`、`cobot-ops`。
- 数据目录已建立：`/home/agilex/jiaan/data/raw`、`datasets`、`evaluations`。仅建立目录，不等于部署代码或安装环境。
- 来源：`/home/agilex/jiaan-recovery`；现址：`/home/agilex/jiaan/project/cobot-ops/runtime/recovery`。事故子目录 `20260927-getea-offline` 不变。
- 范围：17 个文件，共 761220 字节；不含业务程序和当前服务数据。
- 验收：复制前后清单、SHA-256、权限和修改时间一致；7 个 JSON 可解析，PNG 文件头有效，保存脚本通过 `bash -n`；没有执行脚本。
- A6000 备份：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-ops/outputs/migrations/20260927-recovery`，归档内 17 个文件再次逐项校验。原始日志和备份在 Git 忽略的 outputs 中，不公开提交。
- 归档 SHA-256：`2cd7bff9cefc0a7e78a7ff14e016453b9ba393c4cac234188ebee7aa6957d6f8`。
- 原始清单 SHA-256：`78dc015d02bf6444d7f92d7592ed928192edf4c1b69347d62bca8ac8907efc4c`。
- Cobot 回执：`/home/agilex/jiaan/project/cobot-ops/runtime/migrations/20260927-recovery/receipt.json`。
- 清理：新位置与异机备份验证后，按清单清理旧文件和空目录；`/home/agilex/jiaan-recovery` 已不存在，没有保留旧位置软链接。
- 当前入口使用现址；原始证据正文保留历史路径，不改写事故记录。网页、ROS、相机、机械臂及模型服务未重启或切换。
- 新建 Cobot 项目文件，包括临时排障和恢复证据，均归到 `/home/agilex/jiaan/project/<项目>/`；采集和评测数据归到 `/home/agilex/jiaan/data/`。其他历史散落资产按后续明确批次处理。

下一批候选仍是只读状态查询及现用命令梳理；本次未扩展迁移业务代码、模型或完整运行环境。


## 2026-09-27：网页故障手册与独立终端恢复入口（已验证部署）

- 用户需求：演示时可不依赖网页／助手自行诊断 HTTP 失败、重启网页、核验并中断任务及其残留进程。
- 本批新增：`docs/WEB_RECOVERY.md`、`scripts/console_recovery.py`、`tests/test_console_recovery.py`；更新项目入口。没有迁移模型／数据或清理任何旧业务文件。
- 主工作区：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-ops`；Cobot 现场副本：`/home/agilex/jiaan/project/cobot-ops`。运维脚本仅需 Python 3 标准库；Git 和测试留在 A6000。
- 代码发布：`2bebb3f6f183f53e5a8fe34c3312082f5a21ff3e` 为初始恢复工具；`da1f9a9cbbb61fae72569e51b8df0a45778ca2ea` 补齐 ROS 子节点独立 session 的追踪，均已 push 并核对 origin/main。当前记录在验证后追加，后续文档版本以 main 为准。
- A6000 验证：13 个 pytest 用例通过；Python 3.8 编译与 git diff --check 通过。模拟独立进程测试覆盖普通子进程、不同进程组、ROS 式新 session、父进程先退出、残留身份登记、PID 复用拒绝、网页仅发单 PID 信号、Stage 1 使用中拒绝、暂停响应确认。
- Cobot 验证：状态、帮助、web／arms／cameras 停止预览成功；实际识别 web 1、arms 7、cameras 4、ROS Core 3 个进程。4 项网页 API 返回 200；模型 offline、普通采集 active_mode 为空，8026 未启动符合当前无模型状态。
- 所有现场检查均只读或生成诊断文件；没有调用 pause、带 execute 的 interrupt、归位、重启或任何运动命令。网页及已有硬件进程保持原 PID。测试不是实机停止／恢复演练。
- 文档／脚本首批 4 个文件 A6000 与 Cobot SHA-256 一致；记录追加后同步迁移说明，最终现场校验登记在 Cobot `.release.json`。
- 证据：A6000 `outputs/verification/20260927-web-recovery/`。现场 snapshot：`/home/agilex/jiaan/project/cobot-ops/runtime/incidents/20260927T212036-936826`。输出和日志不入 Git。
- 当前网页源版本：`3b54cf7f58f1a35f70756194cb218484ee39c0e9`，运行目录 `/home/agilex/jiaan/project/cobot-web/app/backend`，端口 8015；相关切换证据和接口修复归 cobot-web。运维 runtime 已被使用，不再处于“只有空目录”的状态。
- 已查明 ROS launch 为每个节点创建独立 session：单纯杀父 PID 或只观察父 session 不足。工具按真实父子关系记录已见子进程，在自身中断后继续核验残留；在观察之前已脱离父进程且缺少可靠身份的任务仍需要人工核查，绝不泛匹配杀进程。
- 下一步：按现场真实故障继续补充手册；算法／模型迁移仍按所属项目逐批进行。本批不改变采集、模型或硬件启动策略。


## 2026-09-27：归并到 Cobot Web

- 用户要求直接在对应项目维护，不再单开 ops 项目对话。网页使用／任务与 HTTP 故障归 cobot-web，其他领域直接交对应项目。
- 新主代码：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/scripts/console.py`、`scripts/console_recovery.py`；手册在其 `docs/COMMAND_LINE.md`、`docs/WEB_RECOVERY.md`。
- Cobot 同步副本：`/home/agilex/jiaan/project/cobot-web`。web 代码 `94840c1175227e7e339acbf3b8d15494065be8b6` 已 push、285 文件校验；现场只读 CLI、接口索引和文档可用后，旧工具改成转发。
- 原 tests/test_console_recovery.py 迁入 web 的 app/backend/tests，不再保留两份；原完整手册在本仓库 Git 历史保留，当前文件只指向新入口。
- 已有 runtime／恢复证据／tools/uv 均保持原位置，当前工作由对应项目接管；没有删除旧仓库或现场状态。兼容路径的实体迁移留待核对使用者后另批验收。
- 验证与现场网页重启记录统一见 cobot-web/docs/MIGRATION.md，不再为同一业务在两个项目分别维护。
