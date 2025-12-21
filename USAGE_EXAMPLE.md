# Canadia Start - Usage Example

## Quick Start

```bash
# Option 1: Using the shell wrapper
./canadia.sh start

# Option 2: Using Python directly
python3 canadia_cli.py start
```

## What Happens When You Run It

1. **Port Cleanup**: The command first checks if anything is running on port 9800 and cleans it up
2. **Server Start**: Launches a lightweight HTTP server on http://127.0.0.1:9800
3. **Browser Opens**: Your default browser automatically opens to the test interface
4. **Ready to Test**: You can now ask questions and see answers in real-time!

## Example Session

```bash
$ ./canadia.sh start
�� Cleaning port 9800...
🚀 Starting Canadia on http://127.0.0.1:9800...
📱 Using Canadia demo server...
⏳ Waiting for server to start...

============================================================
🇨🇦 Canadia Demo Server Started!
============================================================
URL: http://127.0.0.1:9800

Server is running on port 9800
Press Ctrl+C to stop the server
============================================================

🌐 Opening browser at http://127.0.0.1:9800...

# Your browser opens automatically...
# You can now ask questions in the web interface!

# Press Ctrl+C when done:
^C

🛑 Stopping Canadia Demo Server...
✅ Server stopped.
```

## Testing the Interface

Once the browser opens, you can:

1. **Type a question** in the input field
2. **Click example questions** to auto-fill and submit
3. **View responses** with context and detailed answers

### Example Questions

Try these in the interface:
- "Qu'est-ce que Canadia ?" - Learn about the system
- "Comment fonctionne ce système ?" - Understand how it works  
- "Quelles sont les fonctionnalités disponibles ?" - Explore features

## API Testing

You can also test the API directly with curl:

```bash
# Start the server first
./canadia.sh start

# In another terminal, test the API
curl -X POST http://127.0.0.1:9800/api/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"What is Canadia?"}'
```

Response:
```json
{
  "answer": "Canadia est un assistant citoyen intelligent...",
  "question": "What is Canadia?",
  "context": "Demo mode - This is a test interface"
}
```

## Requirements

- Python 3.6 or higher
- Modern web browser
- No additional packages needed!

## Troubleshooting

### Port Already in Use
If you get an error that port 9800 is in use, the cleanup should handle it automatically. If not, manually kill the process:

```bash
lsof -ti tcp:9800 | xargs kill -9
```

### Browser Doesn't Open
If the browser doesn't open automatically, manually navigate to:
```
http://127.0.0.1:9800
```

### Server Won't Start
Make sure Python 3 is installed:
```bash
python3 --version
```

## Next Steps

- Explore the web interface
- Try different questions
- Check the API responses
- Read the full documentation in CANADIA_CLI_README.md
