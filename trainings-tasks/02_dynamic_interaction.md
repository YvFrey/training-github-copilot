# 🎯 Module II: Dynamic Interaction (Chat, Inline, and Completions)

**Goal:**  
Learn to **switch between Copilot’s interaction modes** to match the task at hand and maximize developer productivity. Copilot provides three main “thinking modes”:

- **ASK Mode** → Reasoning, explanations, conceptual questions  
- **EDIT Mode** → Rewrite or refactor selected code  
- **AGENT Mode** → Multi-step, autonomous workflows  

Also available:

- **Slash Commands** (`/fix`, `/docs`, `/explain`) → Fast, deterministic local edits  
- **Environment Agents** (`@workspace`, `@terminal`, `@vscode`) → Bring context from project and editor  
- **Code Completions** → Quick scaffolding inside the editor  

Switching modes intentionally improves speed, accuracy, and clarity.

---

## Exercises

| Step | Focus | Copilot Feature | Instructions |
| :--- | :--- | :--- | :--- |
| **2.1** | **Multi-Step Generation** | **Code Completions & Inline Comment** | Open `app/main.py`. Above the `/status` route, type: `# Add a new POST route at /item/create that accepts the existing 'Item' Pydantic model. The route handler must be 'async def' and should immediately return a 201 Created status code and the received item JSON.` Use the Command Palette to search "Copilot: Open Completions Panel" and iterate through suggestions. **Accept the suggested block and delete the comment afterward.** |
| **2.2** | **Focused Refactoring** | **Inline Chat (`/fix`)** | Select the `post_calculate_order` function. Open **Inline Chat** (`Ctrl/Cmd + I`) and type: `/fix this route to validate and return the calculated total using the 'OrderResponse' Pydantic model.` |
| **2.3** | **Fixing Code Logic** | **Chat (`/fix`)** | Select the entire **`calculate_total`** function. Use the main **Copilot Chat** panel or **Inline Chat** to: `/fix the bug of the function.` |
| **2.4** | **Explaining Code** | **Chat Panel (`/explain`)** | Select the `calculate_total` function. Use **Copilot Chat** and type: `/explain this function to a junior developer. Focus on the math and correct return type, referencing its usage in the '/calculate' endpoint.` |
| **2.5** | **Inline Explanation (Speed)** | **Inline Chat (Selection)** | Select the `create_item` function. Use Inline Chat (`Ctrl/Cmd + I`) and prompt: `Explain this code in a single sentence.` Observe how it provides an in-place, focused explanation. |
| **2.6** | **One-Click Documentation** | **Inline Chat (`/docs`)** | Select the body of `get_status`. Use Inline Chat and type: `/docs add a Google-style docstring explaining the function’s purpose and return value.` |
| **2.7** | **Custom Prompt File Creation** | **Prompt Files (`.github/prompts`)** | Review `security-audit.prompt.md`. Select `create_item` and run the prompt: `/security-audit`. Create your own prompt (`my-use-case.prompt.md`) for a repetitive task and validate by running it in the chat. |

---

### 📚 Inspiration: Designing Custom Prompt Files

To maximize Prompt Files, turn repetitive tasks into structured commands.  
[GitHub Docs: Your First Prompt File](https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file)

---

# 🧠 Lesson Learned: Dynamic Interaction

Dynamic interaction is about **choosing the right mode** and using the proper context:

### ⚡ 1. Completions – “Instant Code Generation”
- Quick scaffolding, small functions  
- Triggered by natural-language comments above or in code  

### 🎯 2. Slash Commands – “Power Tools”
- `/fix`, `/docs`, `/explain`  
- Fast, deterministic edits on **selected code**  

### 🌍 3. Environment Agents – “External Sensors”
- `@workspace` → project structure, files, dependencies  
- `@terminal` → commands (git, docker, curl, uv)  
- `@vscode` → debugging context and editor state  
- Do **not** modify code; provide context  

### ✏️ 4. Inline Chat – “Local Precision”
- Acts directly on selected lines  
- Best for small refactors, documentation, or quick fixes  

### 🧩 5. Chat Panel – “Global Reasoning”
- Has access to **multi-file context** and workspace insights  
- Use for explanations, architectural reasoning, or multi-step instructions  

---

### ⭐ Key Insight: Context = Results
When Copilot gives unexpected output:  
**Change the mode → change the context → change the result.**
