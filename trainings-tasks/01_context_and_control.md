## 🎯 Module I: The AI's Focus. Context and Control

**Goal:** Understand how explicit context (instructions and chat variables) dictates the quality and scope of Copilot's suggestions.

| Step | Focus | Copilot Feature | Instructions |
| :--- | :--- | :--- | :--- |
| **1.1** | **Setup & Instructions** | **`uv` & `@workspace`** | 1. **Terminal:** Run `uv sync` to install dependencies.<br>2. **Review:** Open and read the `.github/copilot-instructions.md` file.<br>3. **Chat Panel:** Ask: `@workspace Which file must I create next to satisfy Mandatory Coding Guideline #4, and please provide the command to create it.` **Execute the suggested command.** |
| **1.2** | **Workspace Awareness** | **`@workspace` Agent** | Open the main **Copilot Chat** panel. Ask: `@workspace what are the two main dependencies listed in pyproject.toml and what is the required Python version?` |
| **1.3** | **Terminal Help** | **`@terminal` Agent** | Open a terminal in VS Code. Use the chat panel and ask: `@terminal I need to create a new branch named 'feature/calc-fix'. Provide the exact git command for this.` Execute the suggested command. |
| **1.4** | **Editor Awareness** | **`@vscode` Agent** | 1. **Action:** Introduce a small syntax error in `app/main.py` (for example, remove a closing parenthesis).<br>2. In the **Copilot Chat** panel, ask: `@vscode what problems are currently reported in this file?`<br>Observe that Copilot describes the diagnostics and how to view them, but does not automatically fix them.<br>3. Next, ask: `@vscode open the Problems panel.`<br>Depending on permissions, it may either describe or execute this action.<br>4. Ask `@vscode can you automatically fix this issue?`<br>Notice that it explains its current limitations rather than performing autonomous edits. |
| **1.5** | **Context-Aware Chat** | **Chat Panel** | In the main **Copilot Chat** window, ask: `Based on the repository's files, what is the required location for new Pydantic models and what is the rule for function signatures?` |
| **1.6** | **Global Model Generation** | **Code Completions** | Open the newly created **`app/models.py`** file. Type: `class OrderResponse(BaseModel):`. Let Copilot complete the class with appropriate fields (e.g., `total_price: float`). Observe how Copilot infers fields using repository-level context (e.g., models or schemas used in other files). Accept or refine its suggestion. |
| **1.7** | **Context: The Selection** | **Chat Variable (`#selection`)** | Open `app/main.py`. **Select** only the `calculate_total` function. Use the main **Copilot Chat** panel and ask: `What are the parameters and return type for #selection and is there a type hint error?` |
| **1.8** | **Context: The File** | **Chat Variable (`#file`)** | Use the main **Copilot Chat** panel. Ask: `In the function defined in #file:app/main.py, what is the current logic error in the 'calculate_total' function?` |
| **1.9** | **Context: The Workspace** | **Chat Participant (`@workspace`)** | Use the main **Copilot Chat** panel. Ask: `@workspace Which file contains the Pydantic models, and which file contains the main FastAPI application?` Observe that @workspace answers by scanning file contents — it’s aware of code structure, not just filenames. |

---

### 🧠 **Lesson Learned: Context, Control & Autonomy**

The most effective way to use Copilot is by **explicitly defining its scope** and understanding each agent’s level of autonomy.

* **Global Constraints:** 🛡️ Use the **`.github/copilot-instructions.md`** file for project-wide rules and architectural standards.
* **External Tool Agents:** 🤖 Use **`@workspace`** to query project structure, **`@terminal`** to get command-line assistance, and **`@vscode`** to troubleshoot IDE-specific issues. These three built-in agents connect the AI to your development environment.
* **Context Control:** 🎯 For local, precise questions, use **Chat Variables** (`#selection` and `#file:`) to enforce focus on precise code blocks or files.
* **Autonomy Boundaries:** 🚦 The agents in the IDE remain **contextual collaborators** who **execute code modifications by proposing changes** (e.g., via Inline Chat or the Chat Panel). The change is **staged** but requires the human developer's **explicit final approval** to be written to the active file. The **autonomous, iterative workflow** is reserved for tasks delegated via GitHub Issues (as seen in Module IV).

---
### 💡 **Generating Instructions for Existing Repositories**

When integrating Copilot into existing codebases, you can **ensure specific rules and standards are enforced** immediately by auto-generating the `.github/copilot-instructions.md` file. This prevents the AI from inferring old or bad practices and ensures it adheres to your defined standards.

* **Option 1: Command Palette (Recommended)**: `Copilot: Generate Project Instructions`
* **Option 2: Chat Input (Codespaces/GitHub.dev)**: `@workspace generate project instructions file`

In both cases, Copilot analyzes the existing code and configuration files, creating a draft `.github/copilot-instructions.md` that you can then review and refine with your **Mandatory Coding Guidelines**. You can confirm the file is generated and active: `@workspace summarize the active workspace instructions.` Copilot will quote the main rules from that file if it’s being used correctly.

---