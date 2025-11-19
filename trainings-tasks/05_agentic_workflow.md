## 🎯 Module V: Agentic Workflow and Customization (The Future)

### 📚 Goal: Master the creation of a Custom Agent
Delegate an iterative code-quality task using a GitHub Issue, utilizing both GitHub UI and local VS Code delegation methods.

### 🤖 Understanding the Coding Agent

The **Copilot Coding Agent** `@copilot` is the next evolution in AI-assisted coding. Unlike the synchronous agent mode in your chat panel (which proposes edits and waits for your approval), the **Coding Agent is autonomous and asynchronous**. It performs multi-step coding tasks at your command—analyzing your codebase, running terminal commands and tests in a loop until the task is completed. This powerful, iterative workflow runs in the **GitHub Actions cloud**. 

| Step | Feature | Instructions |
| :--- | :--- | :--- |
| **5.1** | **Prepare the Error and Profile** | **Action:** 1. Review the contents of the custom agent file: **`.github/agents/MypyFixer.md`**. 2. Check for any mypy errors but do not fix. |
| **5.2** | **Delegate Task via GitHub UI** | **Workflow:** 1. Go to your repository's **Issues** tab on GitHub. 2. Create a new Issue titled: **`@copilot Request: Fix All Outstanding Mypy Errors of the App`**. 3. **Assign** this new issue to the **`@copilot`** agent. 4. Use the custom agent profile dropdown to select **`MypyFixer`**. |
| **5.3** | **Delegate Task via VS Code Chat** | **Action:** Use the main **Copilot Chat** panel. **Your Task:** Craft a simple prompt (e.g., `Fix the Mypy issues now`) that successfully initiates the **autonomous workflow** directly from your IDE, resulting in a new Draft Pull Request. |
| **5.4** | **Review the Iteration** | **Observation:** Monitor the issue timeline and the resulting Pull Request (PR). Observe how the agent iteratively **runs Mypy, fixes one error, commits, and repeats** until Mypy passes, showcasing the power of its autonomous loop. |
| **5.5** | **Design Your Own Agent** | **Challenge:** Think about a repetitive maintenance task or a simple feature you want to resolve. Design and create a new custom agent profile: **`.github/agents/YourAgentName.md`**. Delegate the work to this new Agent while you focus on something else. |

---

### 🧠 Lesson Learned: Delegation for Quality

Delegating tasks to the autonomous Coding Agent transforms technical debt into an automated, scalable workflow, allowing developers to focus their time on complex feature development.

---

#### ☁️ Agent Autonomy vs. Local Collaboration

* **Coding Agent (Autonomous):** ☁️ Runs **asynchronously** in the GitHub Actions cloud. This is the **only** tool that can autonomously fix code, run tests, commit changes, and open a Draft PR in an iterative loop.
* **Local Agent (Collaborative):** The local agent in VS Code is **synchronous** and used for real-time suggestions and collaboration, always requiring developer approval for code edits.

#### 🚀 Scalability and Delegation

* **Delegation:** 🤖 Custom Agents (triggered via **`@copilot`**) transform technical debt into an automated, **delegated** workflow. By defining a strict **Agent Profile**, you ensure code quality is maintained autonomously according to project standards.
* **Concurrency:** 🚀 The system supports **concurrent task execution**, meaning multiple colleagues can assign fix-it tasks simultaneously, resulting in parallel Draft PRs for review.

### 💡 References & Further Reading

* **Copilot Coding Agent:** [Visual Studio Code Documentation: Delegate from Chat](https://code.visualstudio.com/docs/copilot/copilot-coding-agent#_method-2-delegate-from-chat)
* **About Custom Agents and How to design its Profile:** [GitHub Docs: About custom agents](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-custom-agents)