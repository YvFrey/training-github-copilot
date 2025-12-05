## 🎯 Module I: Context and Control

### 📚 Goal: Understand how explicit context (instructions and chat variables) dictate the quality and scope of Copilot's suggestions.


## Exercises: Explicit Context-Awareness
| Step | Feature | Instructions |
| :--- | :--- | :--- |
| **1.1** | **Repository Instructions** | 1. **Review:** Open and read the `.github/copilot-instructions.md` file.<br>2. **Chat: Ask:** `Which file must I create next to satisfy Mandatory Coding Guideline #4, and please provide the command to create it` Execute the suggested command. |
| **1.2** | **Workspace Awareness (`@workspace` Agent)** | **Chat: Ask:** `@workspace what are the two main dependencies listed in pyproject.toml and what is the required Python version?` |
| **1.3** | **Terminal Help (`@terminal` Agent)** | **Chat: Ask:** `@terminal I need to create a new branch named 'feature/calc-fix'. Provide the exact git command for this` Execute the suggested command. |
| **1.4** | **Editor Diagnostics (`@vscode` Agent)** | 1. Introduce a small syntax error in `app/main.py`. <br>2. **Chat: Ask:** `@vscode what problems are currently reported in this file?`<br>3. Ask: `@vscode open the Problems panel.`<br>4. Ask: `@vscode can you automatically fix this issue?` Notice its limitations. |
| **1.5** | **Chat Variable (`#selection`)** | 1. Open `app/main.py`. **Select** only the `calculate_total` function. <br>2.**Chat: Ask:** `What are the parameters and return type for #selection and is there a type hint error?` |
| **1.6** | **Chat Variable (`#file`)** | **Chat: Ask:**: `In the function defined in #file:app/main.py, what is the current logic error in the 'calculate_total' function?` |

## Exercises: Implicit Context-Awareness
| Step | Feature | Instructions |
| :--- | :--- | :--- |
| **1.7** | **Context-Aware Chat** | **Chat: Ask:** `Based on the repository's files, what is the required location for new Pydantic models and what is the rule for function signatures?` |
| **1.8** | **Context-Aware Code Completions** | 1. Open the newly created **`app/models.py`** file. <br>2. **Type**: `class OrderResponse(BaseModel):`. <br>2. Let Copilot complete the class with appropriate fields. Observe how Copilot infers fields using repository-level context. Accept or refine its suggestion. |

---

### 🧠 **Lesson Learned: Context, Control & Autonomy**
* **Global Constraints:** 🛡️ Use the **`.github/copilot-instructions.md`** file for project-wide rules and architectural standards.
* **External Tool Agents:** 🤖
    * `@workspace` — query project structure, inspect files, and read configuration.
    * `@terminal` — provide exact CLI commands and command-line assistance.
    * `@vscode` — report editor/IDE diagnostics and help troubleshoot workspace-specific issues.
* **Context Control:** 🎯 For local, precise questions, use **Chat Variables** (`#selection` and `#file`) to enforce focus on precise code blocks or files.
* **Dynamic Model Selection:** The model you choose affects the quality, speed, and relevance of Copilot's responses. Use the right tool for the job.
    * **Velocity:** ⚡ Prioritize Speed (Low-Latency) for quick tasks like generating comments or snippets, e.g. GPT-4.1, GPT-4o, Claude Haiku 4.5.
    * **Reasoning:** 🧠 Prioritize Accuracy (Deep Reasoning) for complex tasks like multi-file refactoring or critical debugging, e.g. GPT-5, Claude Opus 4.5.
* **Autonomy Boundaries:** 🚦 The agents in the IDE remain **contextual collaborators** who **execute code modifications by proposing changes**. The change is **staged** but requires the human developer's **explicit final approval** to be written to the active file. The **autonomous, iterative workflow** is reserved for tasks delegated via GitHub Issues (as seen in Module V).
* **Inference is Strong:** 🧠 Often AI is intelligent enough to ground its response in the project's configuration files even when you don't use a specific agent. This high degree of inference works particularly well with simple, small repositories like our training app.

---
### 💡 **Generating Instructions for Existing Repositories**

When integrating Copilot into existing codebases, you can **ensure specific rules and standards are enforced** immediately by auto-generating the `.github/copilot-instructions.md` file. This prevents the AI from inferring old or bad practices and ensures it adheres to your defined standards.

* **Option 1: Command Palette (Recommended)**: `Copilot: Generate Project Instructions`
* **Option 2: Chat Input (Codespaces/GitHub.dev)**: `@workspace generate project instructions file`

In both cases, Copilot analyzes the existing code and configuration files, creating a draft `.github/copilot-instructions.md` that you can then review and refine with your **Mandatory Coding Guidelines**. You can confirm the file is generated and active: `@workspace summarize the active workspace instructions.` Copilot will quote the main rules from that file if it’s being used correctly.

---

### 💡 References & Further Reading

* [GitHub Copilot: Repository Instructions](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/configure-custom-instructions/add-repository-instructions?tool=webui)