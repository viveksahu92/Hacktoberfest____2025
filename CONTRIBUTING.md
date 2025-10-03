# 🤝 Contributing to Open Source Learning Stories

First off, thank you for taking the time to contribute! 🎉 This project is all about **sharing your journey in open source** so others can learn and get inspired.

We welcome all kinds of contributors—beginners, students, professionals, writers, and creators. You don’t need to be a developer to add value here. 🚀

---

## 🛠 How to Contribute

We've broken down the contribution process into simple steps:

### The Git Workflow

1.  **Fork the repository**
    Click the **Fork** button at the top right of this repo's page on GitHub.

2.  **Clone your fork**
    Open your terminal and clone your copy of the repository:
    ```bash
    git clone [https://github.com/](https://github.com/)<your-username>/open-source-learning-stories.git
    cd open-source-learning-stories
    ```

3.  **Create a new branch**
    Always create a new branch for your contribution. **Replace `add-my-story` with a unique name.**
    ```bash
    git checkout -b add-my-story
    ```

4.  **Add your story**
    * Navigate to the **`stories/`** folder.
    * Create a new file named: **`<your-github-username>.md`** (e.g., `stories/superman.md`).
    * Follow the format below for your story content:

    ```markdown
    # My Open Source Journey ✨

    **👤 Name:** Your Name
    **📅 First Contribution:** Month Year
    **🔧 Tools/Tech Used:** e.g. Python, FastAPI, GitHub
    **🌟 My Experience:** (Write 5–10 lines about your journey)
    **📌 Advice for Beginners:** (Share one tip)
    ```

5.  **Commit your changes**
    Stage your new file and commit it with a clear message:
    ```bash
    git add stories/<your-github-username>.md
    git commit -m "feat: Added story from <Your Name>"
    ```

6.  **Push to your fork**
    Push the new branch to your remote fork:
    ```bash
    git push origin add-my-story
    ```

7.  **Create a Pull Request (PR)**
    * Go to the original repository on GitHub.
    * GitHub should show a prompt to create a **New Pull Request**.
    * Submit your PR for review!

---

## ✅ Contribution Rules

* **Respect Branches:** Do not push directly to the `main` or `develop` branch.
* **Be Welcoming:** Keep stories respectful and beginner-friendly.
* **Format:** Use Markdown format only for all story files.
* **Integrity:** Only add your own story and do not edit/delete others' files.
* **Language:** English is preferred, but translations are welcome.
* **No Spam:** All submissions must be genuine personal stories.