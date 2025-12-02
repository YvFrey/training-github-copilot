## 🎯 Module II: Dynamic Interaction Modes

### 📚 Goal: Learn to switch between Copilot’s interaction modes and channels to maximize developer productivity

Copilot provides four primary interaction channels:

* **Code Completions** → Quick scaffolding and filling in code as you type.
* **Inline Chat (`Ctrl/Cmd + I`)** → Focused, in-place edits and actions on selected code.
* **Chat Panel** → Global reasoning, architectural questions, and multi-file context.
* **Copilot CLI** → Shell/Terminal Interaction for generating and executing commands.

Switching modes and channels intentionally improves speed, accuracy, and clarity.

## Exercises

| Step | Feature | Instructions |
| :--- | :--- | :--- |
| **2.1** | **Code Completions** | 1. In `app/main.py` above the `/status` route **type:** `# Add a new POST route /item/create that accepts the existing 'Item' Pydantic model. The route handler should immediately return the received item as JSON`. <br>2. Open `Copilot: Open Completions Panel` and iterate through suggestions. Once accepted ensure the comment is deleted. <br> **Hint:** If you don't know how to open the right tool use `@vscode` agent.|
| **2.2** | **Inline Chat (`/fix`)** | 1. **Select**  the `post_calculate_order` function. <br>2. **Inline Chat**: `/fix this route to validate and return the calculated total using the 'OrderResponse' Pydantic model`. |
| **2.3** | **Chat Panel (`/fix`)** | 1. **Select** the entire **`calculate_total`** function.  <br>2.**Chat Panel:** `/fix the bug of the function` |
| **2.4** | **Chat Panel (`/explain`)** | 1. **Select**  the `calculate_total` function. <br>2.**Chat Panel: Ask:** `/explain this function to a junior developer. Focus on the math and correct return type, referencing its usage in the '/calculate' endpoint`. |
| **2.5** | **Inline Chat (Selection)** | 1. **Select** the `create_item` function. <br>2. **Inline Chat**: `Explain this code in a single sentence.` Observe how it provides an in-place, focused explanation. |
| **2.6** | **Mode Comparison** | 1. **Select** the **entire `calculate_total` function** after changing the return type to int. <br>2. **Chat Panel:** Submit three times the exact same prompt: `Change the return type of this function`. Switch between **ASK Mode, EDIT Mode** and **AGENT Mode** and observe the different behavior. |
| **2.7** | **Inline Chat (`/docs`)** | 1. **Select** the body of `get_status`. <br>2. **Inline Chat**: `/docs add a Google-style docstring explaining the function’s purpose and return value`. |
| **2.8** | **Inline Terminal (`@terminal`)** | 1. **Open your terminal** and press **`Command/Ctrl + I`** to launch the inline chat. <br>2. **Inline Chat:** `I need to run my FastAPI application using uvicorn with hot-reloading`. Observe how it picks up the terminal agent natively. |
| **2.9** | **Custom Prompt** | 1. **Review** `security-audit.prompt.md`. **Select** `create_item` in `app/main.py` and run the prompt: `/security-audit`. <br>2. **Create** your own prompt (`my-use-case.prompt.md`). |
| **2.9** | **Challenge: Custom Prompt** | Think about a repetitive task/prompt during your daily coding. Leverage a prompting framework of your choice. Validate the output and potentially refine the prompt. |

---

### 📚 Inspiration: Designing Custom Prompt Files
 
Prompt Files are how you turn repetitive workflow tasks into standard, reusable commands. This prevents lengthy, complex instructions from being typed repeatedly and ensures standardization for tasks like documentation or custom code audits across the entire codebase. <br> [GitHub Docs: Your First Prompt File](https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file)

---

### 🧠 Lesson Learned: Dynamic Interaction and Agent Capabilities

The most effective way to use Copilot is by **choosing the right mode** and understanding how to provide and switch context.
**Change the mode → change the context → change the result.**

#### 💡 Core Thinking Modes

All interactions fall into one of following modes, dictating the AI's response style:

* **ASK Mode** → Reasoning, explanations, conceptual questions (e.g., asking `/explain`).
* **EDIT Mode** → Rewriting, fixing, or refactoring existing, selected code (e.g., using `/fix`).
* **AGENT Mode** → Multi-step workflows that coordinate actions or external tools.
* **Plan Mode** → Helps you generate a step‑by‑step plan before coding. [Plan Mode](https://github.blog/changelog/2025-11-18-plan-mode-in-github-copilot-now-in-public-preview-in-jetbrains-eclipse-and-xcode/?utm_source=chatgpt.com) is one of the latest features.

#### ⚡ Interaction Channels and Focus

| Channel | Focus | Key Use Case |
| :--- | :--- | :--- |
| **Code Completions** | **Instant** | Quick scaffolding and small function generation. |
| **Inline Chat** | **Local Precision** | Small refactors, documentation (`/docs`), or quick fixes (`/fix`) on selected code. |
| **Chat Panel** | **Global Reasoning** | Architectural questions, multi-file context, and complex explanations. |
| **Terminal/CLI** | **Command Execution** | Generating and executing commands for Git, Docker, and shell utilities. |

### ⭐ Key Insight: Context = Results
**Change the mode → change the context → change the result.**

The ultimate insight is that **the input channel acts as the primary router** for your query, dictating which specialized agent or tool handles the request. Copilot is engineered to be a powerful problem-solver, adept at handling complex tasks and quickly grasping the right context, but the human must guide the interaction.

1.  **Channel is the Router:** The channel you use (Inline Chat, Terminal, or Chat Panel) is the first factor that determines the AI's scope and focus.
2.  **Implicit Routing:** The system automatically invokes the required agent based on context (e.g., **Inline Chat inside the terminal automatically routes the request to the `@terminal` Agent**). This means you don't always need to explicitly type the agent tag.
3.  **Efficiency:** The most effective workflow combines these factors efficiently. The ultimate goal is to find the fastest way to get a reliable result. If you prefer typing commands over clicking UI elements, sticking to **Slash Commands** and **Context Variables** is a great strategy.
4.  **Personal Preference:** Remember that finding the 'best' interaction channel is ultimately a matter of **personal workflow preference**; it's perfectly fine and even recommended to stick with the methods and settings that you find most efficient.

