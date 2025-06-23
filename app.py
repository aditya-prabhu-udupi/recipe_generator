# import openai
import os
from flask import Flask, render_template_string, request

# openai.api_key = os.environ['OPENAI_API_KEY']

def generate_tutorial(components):
    # Simulated response
    return f"Recipe generated for: {components}\n\n(This is a demo. API is disabled.)"


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    output = ""
    if request.method == 'POST':
        components = request.form['components']
        output = generate_tutorial(components)
    
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <title>Recipe Generator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        .container {
            max-width: 900px;
        }
        
        .main-card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            padding: 40px;
            margin: 20px 0;
            animation: slideUp 0.8s ease-out;
        }
        
        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .title {
            background: linear-gradient(45deg, #ff6b6b, #ffa500, #ff6b6b);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 800;
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 30px;
            animation: gradientShift 3s ease-in-out infinite;
        }
        
        @keyframes gradientShift {
            0%, 100% { filter: hue-rotate(0deg); }
            50% { filter: hue-rotate(20deg); }
        }
        
        .input-group {
            position: relative;
            margin-bottom: 25px;
        }
        
        .form-control {
            border: 2px solid #e9ecef;
            border-radius: 15px;
            padding: 15px 20px;
            font-size: 16px;
            transition: all 0.3s ease;
            background: rgba(255, 255, 255, 0.9);
        }
        
        .form-control:focus {
            border-color: #667eea;
            box-shadow: 0 0 20px rgba(102, 126, 234, 0.3);
            background: white;
            transform: translateY(-2px);
        }
        
        .form-label {
            font-weight: 600;
            color: #495057;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .btn-primary {
            background: linear-gradient(45deg, #667eea, #764ba2);
            border: none;
            border-radius: 15px;
            padding: 15px 40px;
            font-weight: 600;
            font-size: 16px;
            transition: all 0.3s ease;
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
        }
        
        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
            background: linear-gradient(45deg, #764ba2, #667eea);
        }
        
        .output-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
            margin-top: 30px;
            animation: fadeIn 0.6s ease-out;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        .card-header {
            background: linear-gradient(45deg, #ff6b6b, #ffa500);
            color: white;
            padding: 20px;
            font-weight: 600;
            font-size: 18px;
        }
        
        .btn-copy {
            background: rgba(255, 255, 255, 0.2);
            border: 2px solid rgba(255, 255, 255, 0.3);
            color: white;
            border-radius: 10px;
            padding: 8px 16px;
            transition: all 0.3s ease;
        }
        
        .btn-copy:hover {
            background: rgba(255, 255, 255, 0.3);
            border-color: rgba(255, 255, 255, 0.5);
            color: white;
        }
        
        .output-content {
            padding: 30px;
            font-size: 16px;
            line-height: 1.8;
            color: #333;
            white-space: pre-wrap;
            background: rgba(248, 249, 250, 0.5);
        }
        
        .loading-animation {
            background: linear-gradient(45deg, #ff9a9e, #fecfef, #fecfef, #ff9a9e);
            background-size: 400% 400%;
            animation: gradientAnimation 2s ease infinite;
            border-radius: 15px;
            padding: 20px;
            color: #333;
            margin-top: 20px;
        }
        
        @keyframes gradientAnimation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .icon {
            color: #667eea;
        }
        
        .ingredients-info {
            background: rgba(255, 255, 255, 0.7);
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            border-left: 4px solid #ffa500;
        }
    </style>
    <script>
        async function generateTutorial() {
            const components = document.querySelector('#components').value;
            const output = document.querySelector('#output');
            
            output.innerHTML = `
                <div class="loading-animation">
                    <div class="d-flex align-items-center">
                        <i class="fas fa-utensils fa-2x me-3"></i>
                        <div>
                            <strong>🍳 Cooking a delicious recipe for you...</strong><br>
                            <div class="ingredients-info mt-2">
                                <small><strong>Your ingredients:</strong> ${components}</small><br>
                                <small><strong>Always available:</strong> Haldi, Chilly Powder, Tomato Ketchup, Water, Garam Masala, Oil</small>
                            </div>
                        </div>
                    </div>
                </div>
            `;
            
            try {
                const response = await fetch('/generate', {
                    method: 'POST',
                    body: new FormData(document.querySelector('#tutorial-form'))
                });
                const newOutput = await response.text();
                output.textContent = newOutput;
            } catch (error) {
                output.innerHTML = '<div class="alert alert-danger">Sorry, something went wrong. Please try again!</div>';
            }
        }
        
        function copyToClipboard() {
            const output = document.querySelector('#output');
            const textarea = document.createElement('textarea');
            textarea.value = output.textContent;
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand('copy');
            document.body.removeChild(textarea);
            
            // Show success message
            const button = event.target;
            const originalText = button.innerHTML;
            button.innerHTML = '<i class="fas fa-check"></i> Copied!';
            setTimeout(() => {
                button.innerHTML = originalText;
            }, 2000);
        }
    </script>
</head>

<body>    
    <div class="container py-5">   
        <div class="main-card">
            <h1 class="title">
                <i class="fas fa-chef-hat"></i> Recipe Generator
            </h1>
            
            <form id="tutorial-form" onsubmit="event.preventDefault(); generateTutorial();" class="mb-4">   
                <div class="input-group">   
                    <label for="components" class="form-label">
                        <i class="fas fa-carrot icon"></i> What ingredients do you have?
                    </label>    
                    <input type="text" class="form-control" id="components" name="components" 
                           placeholder="Enter your ingredients: chicken, rice, onions, etc." required>   
                </div>   
                
                <div class="text-center">
                    <button type="submit" class="btn btn-primary" disabled>
                        <i class="fas fa-magic me-2"></i> Share a recipe with me
                    </button>
                    <p style="color: #dc3545; margin-top: 10px; font-weight: 500;">
                        🔒 Recipe generation is disabled to prevent misuse of API credits.<br> For more details contact 
                                  <a href="mailto:aditya.prabhu0910@gmail.com">Aditya Prabhu</a>
                            <br><br> You can still watch the demo of the app over here -- 
                                  <a href="https://drive.google.com/file/d/1toxF7uTQUhgIiDAKIBLKcxOs1yG1OM5q/view?usp=sharing">Demo Video</a> 
                    </p>
                </div>

            </form>
            
            <div class="output-card">
                <div class="card-header d-flex justify-content-between align-items-center">    
                    <span><i class="fas fa-scroll me-2"></i> Your Recipe</span>    
                    <button class="btn btn-copy btn-sm" onclick="copyToClipboard()">
                        <i class="fas fa-copy me-1"></i> Copy
                    </button>   
                </div>    
                <div class="output-content">   
                    <div id="output" class="mb-0">
                        {{ output if output else "Enter your ingredients above and click the button to get a personalized recipe!" }}
                    </div>    
                </div>    
            </div>
        </div>    
    </div>
    
    <!-- Footer -->
    <footer class="text-center py-4">
        <div class="container">
            <div style="background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); border-radius: 15px; padding: 20px; color: white;">
                <p class="mb-0" style="font-weight: 600;">
                    Made with
                    <i class="fas fa-heart" style="color: #ff6b6b;"></i> 
                     by <span style="color: #ffa500;">Aditya Prabhu</span>
                </p>
                <small style="opacity: 0.8;">Recipe Generator App</small>
            </div>
        </div>
    </footer>
</body>    
</html>
''', output=output)

@app.route('/generate', methods=['POST'])
def generate():
    components = request.form['components']
    return f"This is a demo. You entered: {components}\n\n(Real recipe generation is disabled for public use.)"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
