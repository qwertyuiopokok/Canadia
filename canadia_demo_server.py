#!/usr/bin/env python3
"""
Simple demo server for Canadia - standalone version that doesn't require venv
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import urllib.parse
import webbrowser
import threading
import time


HTML_TEMPLATE = r"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Canadia - Test Interface</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 2rem;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        .header {
            background: #b30000;
            color: white;
            padding: 2rem;
            text-align: center;
        }
        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        .header p {
            opacity: 0.9;
            font-size: 1.1rem;
        }
        .content {
            padding: 2rem;
        }
        .question-form {
            margin-bottom: 2rem;
        }
        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: #333;
        }
        input[type="text"], textarea {
            width: 100%;
            padding: 1rem;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 1rem;
            font-family: inherit;
            transition: border-color 0.3s;
        }
        input[type="text"]:focus, textarea:focus {
            outline: none;
            border-color: #667eea;
        }
        button {
            background: #667eea;
            color: white;
            border: none;
            padding: 1rem 2rem;
            font-size: 1rem;
            font-weight: 600;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s;
            margin-top: 1rem;
            width: 100%;
        }
        button:hover {
            background: #5568d3;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        button:active {
            transform: translateY(0);
        }
        .response-section {
            margin-top: 2rem;
            padding: 1.5rem;
            background: #f8f9fa;
            border-radius: 10px;
            display: none;
        }
        .response-section.show {
            display: block;
        }
        .response-title {
            font-weight: 600;
            color: #333;
            margin-bottom: 1rem;
            font-size: 1.2rem;
        }
        .response-content {
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid #667eea;
            line-height: 1.6;
        }
        .loading {
            text-align: center;
            padding: 2rem;
            color: #666;
        }
        .examples {
            margin-top: 2rem;
            padding: 1rem;
            background: #fff8e1;
            border-radius: 10px;
        }
        .examples h3 {
            margin-bottom: 0.5rem;
            color: #f57c00;
        }
        .examples ul {
            list-style: none;
            padding-left: 0;
        }
        .examples li {
            padding: 0.5rem 0;
            color: #666;
            cursor: pointer;
            transition: color 0.3s;
        }
        .examples li:hover {
            color: #667eea;
        }
        .footer {
            text-align: center;
            padding: 1.5rem;
            color: #999;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🇨🇦 Canadia</h1>
            <p>Test Interface - Questions & Answers</p>
        </div>
        
        <div class="content">
            <form class="question-form" id="questionForm">
                <label for="question">Posez votre question :</label>
                <input 
                    type="text" 
                    id="question" 
                    name="question" 
                    placeholder="Ex: Qu'est-ce que Canadia ?"
                    required
                    autocomplete="off"
                />
                <button type="submit">Envoyer la question</button>
            </form>
            
            <div class="examples">
                <h3>💡 Exemples de questions :</h3>
                <ul>
                    <li class="example-question" data-question="Qu'est-ce que Canadia ?">• Qu'est-ce que Canadia ?</li>
                    <li class="example-question" data-question="Comment fonctionne ce système ?">• Comment fonctionne ce système ?</li>
                    <li class="example-question" data-question="Quelles sont les fonctionnalités disponibles ?">• Quelles sont les fonctionnalités disponibles ?</li>
                </ul>
            </div>
            
            <div class="response-section" id="responseSection">
                <div class="response-title">📝 Réponse :</div>
                <div class="response-content" id="responseContent"></div>
            </div>
        </div>
        
        <div class="footer">
            &copy; 2025 Canadia - Your Canadian civic assistant
        </div>
    </div>
    
    <script>
        const form = document.getElementById('questionForm');
        const questionInput = document.getElementById('question');
        const responseSection = document.getElementById('responseSection');
        const responseContent = document.getElementById('responseContent');
        
        // Handle example question clicks
        document.querySelectorAll('.example-question').forEach(item => {
            item.addEventListener('click', function() {
                const question = this.getAttribute('data-question');
                questionInput.value = question;
                form.dispatchEvent(new Event('submit'));
            });
        });
        
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const question = questionInput.value.trim();
            
            if (!question) return;
            
            // Show loading
            responseSection.classList.add('show');
            responseContent.innerHTML = '<div class="loading">⏳ Traitement de votre question...</div>';
            
            try {
                const response = await fetch('/api/ask', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ question })
                });
                
                const data = await response.json();
                
                // Display response
                responseContent.innerHTML = `
                    <p><strong>Question:</strong> ${question}</p>
                    <hr style="margin: 1rem 0; border: none; border-top: 1px solid #eee;">
                    <p><strong>Réponse:</strong> ${data.answer}</p>
                    ${data.context ? `<p style="margin-top: 1rem; font-size: 0.9rem; color: #666;"><strong>Contexte:</strong> ${data.context}</p>` : ''}
                `;
            } catch (error) {
                responseContent.innerHTML = `
                    <p style="color: #d32f2f;">❌ Erreur lors du traitement de la question.</p>
                    <p style="font-size: 0.9rem; color: #666; margin-top: 0.5rem;">${error.message}</p>
                `;
            }
        });
    </script>
</body>
</html>
"""


class CanadiaHandler(BaseHTTPRequestHandler):
    """Simple HTTP request handler for the demo server"""
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(HTML_TEMPLATE.encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        """Handle POST requests"""
        if self.path == '/api/ask':
            try:
                # Validate Content-Length header
                content_length_str = self.headers.get('Content-Length')
                if not content_length_str:
                    self.send_response(400)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    error_response = {'error': 'Missing Content-Length header'}
                    self.wfile.write(json.dumps(error_response).encode())
                    return
                
                content_length = int(content_length_str)
                post_data = self.rfile.read(content_length)
                
                data = json.loads(post_data.decode())
                question = data.get('question', '')
                
                # Simple demo response
                answer = self.generate_answer(question)
                
                response = {
                    'answer': answer,
                    'question': question,
                    'context': 'Demo mode - This is a test interface'
                }
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
                
            except (ValueError, json.JSONDecodeError) as e:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                error_response = {'error': f'Invalid request: {str(e)}'}
                self.wfile.write(json.dumps(error_response).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                error_response = {'error': str(e)}
                self.wfile.write(json.dumps(error_response).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def generate_answer(self, question):
        """Generate a simple answer based on the question"""
        question_lower = question.lower()
        
        if 'canadia' in question_lower or 'qu\'est-ce' in question_lower:
            return ("Canadia est un assistant citoyen intelligent conçu pour aider les Canadiens "
                   "à accéder à l'information gouvernementale et civique de manière simple et efficace. "
                   "Il fournit des réponses basées sur des données officielles et des sources vérifiées.")
        elif 'fonction' in question_lower or 'comment' in question_lower:
            return ("Canadia fonctionne en analysant votre question, en recherchant dans sa base de "
                   "connaissances d'informations gouvernementales et citoyennes, puis en générant une "
                   "réponse claire et structurée. Le système utilise le traitement du langage naturel "
                   "pour comprendre vos besoins.")
        elif 'fonctionnalité' in question_lower or 'feature' in question_lower:
            return ("Canadia offre plusieurs fonctionnalités : recherche d'informations gouvernementales, "
                   "réponses aux questions citoyennes, accès aux programmes et services publics, "
                   "et navigation dans les ressources officielles canadiennes.")
        else:
            return (f"Je comprends que vous me demandez : '{question}'. "
                   "Dans cette version de démonstration, je peux répondre aux questions générales "
                   "sur Canadia et ses fonctionnalités. Pour accéder à toutes les capacités du système, "
                   "veuillez vous assurer que le serveur principal est configuré avec tous ses services.")
    
    def log_message(self, format, *args):
        """Custom log message to make output cleaner"""
        pass  # Suppress default logging


def run_server(port=9800, open_browser=True):
    """Run the demo server"""
    # Bind to 0.0.0.0 to allow connections from any network interface
    # This is required for remote environments like GitHub Codespaces
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, CanadiaHandler)
    
    url = f"http://127.0.0.1:{port}"
    print(f"\n{'='*60}")
    print(f"🇨🇦 Canadia Demo Server Started!")
    print(f"{'='*60}")
    print(f"URL: {url}")
    print(f"Additional: Server is accessible on all network interfaces (0.0.0.0:{port})")
    print(f"\nServer is running on port {port}")
    print(f"Press Ctrl+C to stop the server")
    print(f"{'='*60}\n")
    
    if open_browser:
        # Open browser after a short delay
        def open_browser_delayed():
            time.sleep(1)
            print(f"🌐 Opening browser at {url}...")
            webbrowser.open(url)
        
        thread = threading.Thread(target=open_browser_delayed, daemon=True)
        thread.start()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(f"\n\n🛑 Stopping Canadia Demo Server...")
        httpd.shutdown()
        print("✅ Server stopped.")


if __name__ == '__main__':
    run_server()
