# AI Agent Training Home｜Workspace 使用約定

## Folder 用途

| Folder | 用途 |
|--------|------|
| 00_Inbox/ | 未整理、未確認、暫時先收住的材料 |
| 01_Action_Center/ | 要推進、要等待、要停車、要 review 的工作 |
| 01_Action_Center/outputs/drafts/ | Agent 產出的草稿，未確認前不算正式內容 |
| 01_Action_Center/outputs/test_logs/ | 測試紀錄和 improvement log |
| 02_Knowledge_Base/ | 已批准、可安全給 agent 使用的知識材料 |
| 03_Agents/ | AI 員工本體和各自的 session records |
| 04_Memory_Logs/ | 交接、長期記憶、每日 summary |

## Routing 偏好

- **不確定放哪裏：** → 00_Inbox/
- **草稿 review 方式：** → 01_Action_Center/outputs/drafts/，等人類確認後才算正式內容
- **Session 結束要更新：** → 04_Memory_Logs/Latest_State.md
- **長期記憶只記：** → 04_Memory_Logs/MEMORY.md

## Agent 要遵守的規則

1. 改動任何 files / folders 前先 **propose**，等我確認。
2. 不可以 delete / overwrite；要移除東西，先用 **archive** 或 **rename**。
3. 不知道放哪裏，先放 **00_Inbox/** 或問我，不要自己猜。
4. 未批准材料**不可**放入 `approved_references`。
5. Credential、真實員工 / 客戶 / 薪酬 / 合約 / legal / medical / investigation 資料**不可**放入 training folder。
