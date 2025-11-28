## 🎯 Module II: Dynamic Interaction via Chat Panel, Inline Chat, and Code Completions

### 📚 Goal: Learn to switch between Copilot’s interaction modes and channels to maximize developer productivity.

Copilot provides three primary interaction channels:

* **Code Completions** → Quick scaffolding and filling in code as you type.
* **Inline Chat (`Ctrl/Cmd + I`)** → Focused, in-place edits and actions on selected code.
* **Chat Panel** → Global reasoning, architectural questions, and multi-file context.
* **Copilot CLI** → Shell/Terminal Interaction for generating and executing commands.

Switching modes and channels intentionally improves speed, accuracy, and clarity.

## Exercises

| Step | Feature | Instructions |
| :--- | :--- | :--- |
| **2.1** | **Code Completions** | Open `app/main.py`. Above the `/status` route, type: `# Add a new POST route /item/create that accepts the existing 'Item' Pydantic model. The route handler should immediately return the received item as JSON.` Use the Command Palette to search "Copilot: Open Completions Panel" and iterate through suggestions. **Accept the suggested block and delete the comment afterward.** ctrl + Shift + P or Cmd + Shift + P if someone does not know how to access the palette search |
| **2.2** | **Inline Chat (`/fix`)** | Select the `post_calculate_order` function. Open **Inline Chat** and type: `/fix this route to validate and return the calculated total using the 'OrderResponse' Pydantic model.` |
| **2.3** | **Chat Panel (`/fix`)** | Select the entire **`calculate_total`** function. Use the main **Copilot Chat** panel and prompt: `/fix the bug of the function.` |
| **2.4** | **Chat Panel (`/explain`)** | Select the `calculate_total` function. Use **Copilot Chat** and type: `/explain this function to a junior developer. Focus on the math and correct return type, referencing its usage in the '/calculate' endpoint.` |
| **2.5** | **Inline Chat (Selection)** | Select the `create_item` function. Use Inline Chat and prompt: `Explain this code in a single sentence.` Observe how it provides an in-place, focused explanation. |
| **2.6** | **Mode Comparison** | Select the **entire `calculate_total` function** after switching the return type to **int ?? is this a change we need to make before?**. In the main **Copilot Chat** panel, submit the exact same prompt three times, using a different mode prefix each time. Use the simple request: **`Change the return type of this function.`** Switch between **ASK Mode, EDIT Mode** and **AGENT Mode** and observe the different behavior.  <-- ins this exercise Ask mode with GPT5.0 failed with Claude 4.5 was fine (just saying) |
| **2.7** | **Inline Chat (`/docs`)** | Select the body of `get_status`. Use Inline Chat and type: `/docs add a Google-style docstring explaining the function’s purpose and return value.` |
| **2.8** | **Inline Terminal Chat (`@terminal`)** | **Open your terminal** and press **`Command/Ctrl + I`** to launch the inline chat. Type: `@terminal I need to run my FastAPI application using uvicorn with hot-reloading` The inline agent generates the executable command in the shell. |
| **2.9** | **Custom Prompt File Creation (/security-audit)** | Review `security-audit.prompt.md`. Select `create_item` and run the prompt: `/security-audit`. Create your own prompt (`my-use-case.prompt.md`) for a repetitive task and validate by running it in the chat.  <- should we mention that create_item is in main.py, maybe add a break line between Review... and Select create_item..|

---

### 📚 Inspiration: Designing Custom Prompt Files

Prompt Files are how you turn repetitive workflow tasks into standard, reusable commands. This prevents lengthy, complex instructions from being typed repeatedly and ensures standardization for tasks like documentation or custom code audits across the entire codebase. [GitHub Docs: Your First Prompt File](https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file)

---

### 🧠 Lesson Learned: Dynamic Interaction and Agent Capabilities

The most effective way to use Copilot is by **choosing the right mode** and understanding how its agents provide context. **Change the mode → change the context → change the result.**

#### 💡 1. Core Thinking Modes

All interactions fall into one of three conceptual modes, dictating the AI's response style:

* **ASK Mode** → Reasoning, explanations, conceptual questions (e.g., asking `/explain`).
* **EDIT Mode** → Rewriting, fixing, or refactoring existing, selected code (e.g., using `/fix`).
* **AGENT Mode** → Multi-step, autonomous workflows that coordinate actions or external tools (e.g., using `@workspace`).

#### ⚡ 2. Interaction Channels and Focus

| Channel | Focus | Key Use Case |
| :--- | :--- | :--- |
| **Code Completions** | Instant, code-as-you-type | Quick scaffolding and small function generation. |
| **Inline Chat** | **Local Precision** | Small refactors, documentation (`/docs`), or quick fixes (`/fix`) on selected code. |
| **Chat Panel** | **Global Reasoning** | Architectural questions, multi-file context, and complex explanations. |

#### 🌍 3. Environment Agents and Slash Commands

This layer defines the scope of the action, whether it’s code or a command.

* **Slash Commands** (`/fix`, `/docs`, `/explain`): **Power Tools** for fast, deterministic edits or actions on **selected code**.
* **Environment Agents:** **External Sensors** that connect the AI to your development environment.
    * `@workspace`: Queries project structure, files, and dependencies.
    * `@terminal`: Generates commands for tools like Git, Docker, and shell utilities.
    * `@vscode`: Accesses debugging context and editor state (e.g., problems panel).

---

### ⭐ Key Insight: Context = Results
When Copilot gives unexpected output: **Change the mode → change the context → change the result.**
