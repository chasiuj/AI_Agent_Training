# AI Agent Training System

> Personal AI Assistant CHA 的培訓與管理系統

---

## 📁 Folder Structure

| Folder | 名稱 | 用途 |
|--------|------|------|
| `00_Inbox/` | 暫存入口 | 未整理想法、未確認材料、臨時 notes |
| `01_Action_Center/` | 行動中心 | Now / Next / Waiting / Someday，以及草稿、測試紀錄、封存產出 |
| `02_Knowledge_Base/` | 知識庫 | 已批准可餵 agent 的 SOP、FAQ、examples、templates |
| `03_Agents/` | AI 員工區 | Personal AI Assistant 和之後其他 agents |
| `04_Memory_Logs/` | 交接記憶 | 最新狀態、長期記憶、每日 / 每次 session 摘要 |

---

## 🚨 安全鐵則

見到以下關鍵字**立刻停**：
- `delete` / `del` / `rm` / `rm -rf`
- `force` / `--force` / `-f`

**真要移除，先用：** Bin → Archive → Rename → Backup

---

## 🛡️ 三層保護

| 層 | 保護 | 設定 |
|----|------|------|
| 第一層 | 垃圾桶保護 | 見 rm/delete/force 就停 |
| 第二層 | 危險指令黑名單 | `tirith_enabled: true` |
| 第三層 | 權限模式 | `approvals.mode: smart` |

詳見 `03_Agents/Personal_AI_Assistant/.hermes.md`
