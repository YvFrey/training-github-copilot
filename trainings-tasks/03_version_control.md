## 🎯 Module III: Version Control and Quality

### 📚 Goal: Integrate Copilot's contextual features into Git workflows
Improve commit messages, code review, and branch documentation, while reinforcing the developer's ultimate responsibility for code integrity.

| Step | Feature | Instructions |
| :--- | :--- | :--- |
| **3.1** | **Code Review** | **Action:** 1. **Stage** the file(s) containing the changes from the previous module. 2. Open the **Source Control** panel. 3. Click the **"Review changes with Copilot"** button. Review the feedback provided by Copilot on the staged code. |
| **3.2** | **Commit Message** | **Action:** 1. Ensure changes are **staged**. 2. In the **Source Control** panel, click the **Copilot icon (sparkle)** next to the commit message box. **Challenge:** Try typing a *partial* message (e.g., `feat: Added item create...`) before clicking the icon to see how Copilot completes your thought. |
| **3.3** | **Pull Reuqest Summary** | **Goal:** Create a concise summary for a Pull Request, avoiding the issue of getting an overly broad history summary.<br>**Action:** Use the main **Copilot Chat** panel. **Your Task:** Craft a precise prompt using the **`@workspace` agent** that forces Copilot to summarize *only* the specific changes for this PR (which likely involves the last few commits). **HINT:** You may need to use **Git references** (like commit hashes via `git log`) or restrict the summary by file path to get the exact result you want. |

---

### 🧠 Lesson Learned: Git Workflow and Developer Responsibility

You can **embed GitHub Copilot directly into your Git workflow** to ensure cleaner branch history and detect issues ahead of your colleagues review. Remember that **developers are responsible for the code quality and integrity**.

---

#### 🛡️ Responsibility Boundaries

* **You are the Guardian:** 🧑‍💻 You are still fully responsible for the quality, correctness, and security of the code you commit. Copilot is an acceleration tool, not a replacement for human judgment.
* **Verification is Mandatory:** 🔬 Always review the output from Copilot's SCM review and manually test any changes it suggests before committing.
* **Senseful Code:** ✅ Ensure you commit **correct and senseful** code. Copilot accelerates the writing process, but **human validation and testing** is the non-negotiable final step.