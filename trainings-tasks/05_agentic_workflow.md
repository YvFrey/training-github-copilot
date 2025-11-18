## 🎯 Module V: Agentic Workflow and Customization (The Future)

### 📚 Goal: Master the creation of a Custom Agent and delegate an iterative code-quality task using a GitHub Issue, utilizing both GitHub UI and local VS Code delegation methods.

### 🤖 Understanding the Coding Agent

The **Copilot Coding Agent** is the next evolution in AI-assisted coding. **Unlike the synchronous agent mode** in your chat panel (which proposes edits and waits for your approval), the **Coding Agent is autonomous and asynchronous**. It performs multi-step coding tasks at your command—analyzing your codebase, running terminal commands and tests in a loop until the task is completed. This powerful, iterative workflow runs in the **GitHub Actions cloud**.

| Step | Focus | Copilot Feature | Instructions |
| :--- | :--- | :--- | :--- |
| **5.1** | **Review Agent Profile** | **Custom Agent Creation** | **Action:** Review the contents of the **`.github/agents/MypyFixer.md`** file. Check if you currently have any Mypy issues. If not, deliberately introduce a Mypy error in the app. **Commit this buggy code.** |
| **5.2** | **Delegate Task via GitHub UI** | **GitHub Issue Assignment** | **Workflow:** 1. Go to your repository's **Issues** tab on GitHub. 2. Create a new Issue titled: **`@copilot Request: Fix All Outstanding Mypy Errors of the App`**. 3. **Assign** this new issue to the **`@copilot`** agent. 4. Use the custom agent profile dropdown to select **`MypyFixer`**. |
| **5.3** | **Delegate Task via VS Code Chat** | **Local Initiation** | **Action:** Use the main **Copilot Chat** panel. **Your Task:** Craft a prompt that successfully fixes any Mypy issues via the Coding Agent, resulting in a PR. This simple task **enables the autonomous workflow** directly from your IDE. |
| **5.4** | **Review the Iteration** | **Autonomous Feedback Loop** | **Observation:** Monitor the issue timeline and the resulting Pull Request (PR). The agent will iteratively **run Mypy, fix one error, commit, and repeat** until Mypy passes, showcasing the power of its iterative loop. This entire process is a simple task that enables the autonomous workflow. Feel free to explore how to integrate fixing code quality issues in any autonomous way into your workflow. |
| **5.5** | **Design Your Own Agent** | **Agent Profile Design Challenge** | **Action:** Think about a repetitive task or a simple feature you want to resolve. Design and create a new custom agent profile: **`.github/agents/YourAgentName.md`**. Let the Copilot Agent do the work, while you focus on something else. |

---

### 🧠 **Lesson Learned: Delegation for Quality**

* **The Difference:** ☁️ The **Coding Agent** is asynchronous and lives in the GitHub Actions cloud. This is the only tool that can autonomously fix errors, run tests, commit code, and open a PR. The local agent in VS Code is for real-time collaboration.
* **Delegation:** 🤖 Custom Agents transform technical debt into an automated, **delegated** workflow. By defining a strict **Agent Profile**, you ensure code quality is maintained autonomously.
* **Scalability:** 🚀 The system supports **concurrent task execution**, meaning multiple colleagues can assign fix-it tasks simultaneously, resulting in parallel Draft PRs.

### 💡 **References & Further Reading**

* **Copilot Coding Agent:** [Visual Studio Code Documentation: Delegate from Chat](https://code.visualstudio.com/docs/copilot/copilot-coding-agent#_method-2-delegate-from-chat)
* **About Custom Agents and How to design its Profile:** [GitHub Docs: About custom agents](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-custom-agents)