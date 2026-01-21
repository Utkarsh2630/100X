# AI Interview Voice Bot 🎙️

A voice-based AI chatbot built with Streamlit and OpenAI's API that responds to interview questions as Utkarsh Kumar from IIT ISM Dhanbad.
## LINK
https://fnomzxxtuqfeypmrqqydxt.streamlit.app/
## Features

✅ **Voice Input** - Ask questions using your microphone
✅ **AI-Powered Responses** - Generates contextual answers using GPT-4 mini
✅ **Text-to-Speech** - Listens to AI responses with realistic voice output
✅ **User-Friendly Web App** - No coding knowledge required
✅ **Simple Deployment** - One-click deployment on Streamlit Cloud

## Setup Instructions

### Option 1: Local Testing (Developer Setup)

**Easiest Way - Automated Setup:**

1. **Open terminal/PowerShell in this folder**

2. **Run the setup script** (no manual configuration needed!)
   ```bash
   python setup.py
   ```
   - Script will check dependencies
   - Prompts you for OpenAI API key
   - Creates `.env` file automatically
   - Installs missing packages

3. **Run the app**
   ```bash
   streamlit run main.py
   ```

4. **Access the app**
   - Opens automatically at `http://localhost:8501`
   - Click "🎤 Start Recording" and ask a question

---

**Manual Setup (Alternative):**

If you prefer to set up manually:

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create `.env` file** in the project folder with:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
   - Get your API key from [OpenAI API Platform](https://platform.openai.com/api-keys)

3. **Run the app**
   ```bash
   streamlit run main.py
   ```

### Option 2: Web Deployment (For Submission)

#### Deploy on Streamlit Cloud (FREE & RECOMMENDED)

1. **Push code to GitHub**
   - Create a GitHub repository
   - Push this project to GitHub

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your GitHub repository
   - Choose `main.py` as the main file
   - Click "Deploy"

3. **Add API Key Securely**
   - In Streamlit Cloud dashboard, go to "Settings"
   - Add a secret: `OPENAI_API_KEY = your_api_key`
   - The app will automatically use this secret

4. **Share the URL**
   - Your app will be live at: `https://share.streamlit.io/[username]/[repo]/main.py`
   - Share this URL with 100x

#### Deploy on Heroku/Railway (Alternative)

- Both platforms support Streamlit apps
- Similar secret management for API keys
- Deploy via GitHub integration

## API Requirements

- **OpenAI API Key** (Free trial: $5 credit)
  - Get at: [platform.openai.com](https://platform.openai.com)
  - Uses `gpt-4o-mini` (cheapest GPT-4 model)
  - Text-to-speech: `tts-1` (low latency)

## How It Works

1. User clicks "🎤 Start Recording"
2. Records a question via microphone
3. Google Speech-to-Text converts audio to text
4. OpenAI GPT-4 mini generates response based on system prompt
5. Text-to-Speech converts response back to audio
6. User hears the AI answer

## Customization

Edit the `SYSTEM_PROMPT` in `main.py` to change how the AI responds:

```python
SYSTEM_PROMPT = """You are Ebad Sayed...
[Your custom personality/background]
"""
```

## Troubleshooting

**Microphone not working?**
- Allow browser microphone permissions
- Use HTTPS (required for microphone access in browsers)

**API errors?**
- Check OpenAI API key is valid
- Ensure you have API credits remaining
- Check API usage limits

**Audio playback issues?**
- Ensure your device has speakers
- Check browser audio permissions

## Support

For issues, check:
- OpenAI API documentation
- Streamlit documentation: [docs.streamlit.io](https://docs.streamlit.io)
- GitHub Issues (if deployed from GitHub)

---

**Submission Requirements Met:**
✅ Web app deployment (no manual API key entry)
✅ User-friendly interface (non-technical users can use)
✅ No coding knowledge required
✅ One-click deployment option

