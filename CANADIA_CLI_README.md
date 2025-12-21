# Canadia CLI Usage

## Starting Canadia

To start the Canadia server and open a browser for testing:

```bash
./canadia.sh start
```

Or use the Python CLI directly:

```bash
python3 canadia_cli.py start
```

This will:
1. Clean any processes using port 9800
2. Start the Canadia demo server
3. Automatically open your default browser to http://127.0.0.1:9800
4. Present a test interface for asking questions and receiving answers

## Testing Questions and Answers

Once the browser opens, you can:

1. **Type your question** in the input field
2. **Click "Envoyer la question"** to submit
3. **View the response** in the response section below

### Example Questions

Try these example questions:
- "Qu'est-ce que Canadia ?"
- "Comment fonctionne ce système ?"
- "Quelles sont les fonctionnalités disponibles ?"

You can also click on the example questions in the interface to automatically populate and submit them.

## Stopping the Server

Press `Ctrl+C` in the terminal where the server is running to stop it.

## Features

- 🇨🇦 Clean, modern web interface
- 📝 Real-time question and answer testing
- 💡 Example questions for quick testing
- 🎨 Responsive design that works on all devices
- ⚡ Fast, lightweight demo server

## Technical Details

- **Port**: 9800 (default)
- **Host**: 127.0.0.1 (localhost)
- **Server**: Python HTTP server (standalone, no dependencies required)
- **Frontend**: Pure HTML/CSS/JavaScript (no frameworks)

## Requirements

- Python 3.6 or higher (standard library only)
- Modern web browser (Chrome, Firefox, Safari, Edge)

No additional packages or dependencies needed for the demo server!
