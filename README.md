# Chatwise 💬
### Turning Conversations into Meaningful Insights

Voxora is an interactive WhatsApp Chat Analyzer built using Python and Streamlit. It transforms exported WhatsApp conversations into meaningful insights through data analysis and visualization.

## 🚀 Features

- **Overall Statistics:** Total messages, words, media shared, and links.
- **User Activity Analysis:** Identify the most active participants in a group.
- **Word Cloud:** Visualize frequently used words in conversations.
- **Most Common Words:** Discover the most frequently used words by participants.
- **Individual Analysis:** Analyze conversations of specific users or the entire group.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- WordCloud
- URLExtract

## 📂 Project Structure

```text
Chatwise/
│
├── app.py
├── helper.py
├── preprocessor.py
├── stop_hinglish.txt
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd Voxora
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
streamlit run app.py
```

## 📊 How to Use

1. Export your WhatsApp chat as a `.txt` file.
2. Open the Voxora application.
3. Upload your exported chat file.
4. Select a user or choose Overall.
5. Click on Show Analysis to explore the insights.

## 🔮 Future Improvements

- Emoji analysis
- Monthly and daily timeline analysis
- Activity heatmaps
- Advanced conversation insights

## ⚠️ Privacy Notice

Chatwise analyzes uploaded WhatsApp chat exports. Use your own chat data or obtain appropriate consent before analyzing conversations containing other people's messages. Avoid uploading private chat data to public repositories.

## 👩‍💻 Author

Developed as a Python and Data Analytics project.

---

**Voxora — Every conversation has a story.**
