# TOOLS.md — 工具櫃 + 門禁卡

> 更新日期：2026-07-08

## ✅ 可以使用

| 工具 / 動作 | 用途 | 接駁路線 |
|-------------|------|---------|
| 讀取 `03_Agents/Personal_AI_Assistant/` 內的 files | 了解自己的角色、任務和記憶 | 內建能力 |
| 在確認後更新 `03_Agents/Personal_AI_Assistant/` 內的 agent profile files | 維護入職檔案 | 內建能力 |
| 讀取 `02_Knowledge_Base/approved_references/` | 使用已批准 reference | 內建能力 |
| DEEPSEEK | 翻譯輔助 | API |
| 讀取終端機輸出 | 讀取終端機畫面 | 內建 terminal 工具 |

## 📁 讀寫權限

| 動作 | 範圍 |
|------|------|
| 讀取 | 整個 `AI_Agent_Training/` folder |
| 寫入 | `01_Action_Center/outputs/drafts/`、`01_Action_Center/outputs/test_logs/`、`01_Action_Center/outputs/archive/` |

## ⚠️ 先問才可以用

- 建立或修改 folder structure
- 寫入、搬移、重新命名任何 file（上述範圍以外）
- 翻譯記憶庫（需要先建立）
- 瀏覽器控制（讀取頁面、點擊、填表）
- Web 搜尋（搜尋資料）

## 🚫 禁止

- ❌ 刪除或覆蓋任何 file（要移除先 propose archive / rename）
- ❌ 處理 password / API key / token / credential
- ❌ 對外發送任何內容（email、訊息）
- ❌ 接觸原始機密文件

## 🔒 安全原則

**Password、API key、token，永遠不貼入對話。**
