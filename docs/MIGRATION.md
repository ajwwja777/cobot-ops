# Cobot 使用、部署与运维：迁移记录

日期：2026-09-27。已完成入口初始化与**恢复证据归档迁移**，业务代码、模型和服务尚未迁移。跨项目迁移由当前已有 cobot_rlt 对话统筹执行。

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
