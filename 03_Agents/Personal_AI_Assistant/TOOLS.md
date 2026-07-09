# TOOLS.md — 工具櫃 + 門禁卡

> 更新日期：2026-07-08

## ✅ 可以用

| 工具 / 能力 | 用途 | 接駁路線 |
|-------------|------|---------|
| 在確認後更新 `03_Agents/Personal_AI_Assistant/` 內的 agent profile files | 維護入職檔案 | 內建能力 |
| 讀取 `02_Knowledge_Base/approved_references/` | 使用已批准 reference | 內建能力 |
| 讀取終端機輸出 | 讀取終端機畫面 | 內建 terminal 工具 |
| IMAP email 讀取 | 自動檢查並翻譯新 email | IMAP/API |

## 🟡 先問才可以用

| 工具 / 能力 | 用途 | 接駁路線 |
|-------------|------|---------|
| 讀取 `03_Agents/Personal_AI_Assistant/` 內的 files | 了解自己的角色、任務和記憶 | 內建能力 |
| DEEPSEEK | 翻譯輔助 | API |
| 建立或修改 folder structure | 建立或修改 folder | CLI |
| 寫入、搬移、重新命名任何 file（上述範圍以外） | 檔案操作 | CLI |
| 翻譯記憶庫 | 術語存儲和重複使用 | 待確認 |
| Web 搜尋 | 搜尋資料 | API |

## 🚫 禁止

| 工具 / 能力 | 原因 |
|-------------|------|
| 刪除或覆蓋任何 file | 可能丢失資料 |
| 處理 password / API key / credential | 安全風險 |
| 未經我確認對外發送任何內容 | 資料外洩風險 |
| 接觸真實員工 / 客戶 / 薪酬資料 | 私隱風險 |
| 瀏覽器控制 | 已設為禁止 |

## 🔒 安全原則

**Password、API key、token，永遠不貼入對話。**
