from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import json
from datetime import datetime
import anthropic

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

# Initialize Claude client
client = anthropic.Anthropic(api_key=os.getenv('CLAUDE_API_KEY'))

# Campaign analysis system prompt
SYSTEM_PROMPT = """You are an expert campaign analysis AI assistant specialized in digital advertising performance optimization. You have deep expertise in:

- Campaign performance metrics and KPI analysis
- ROI and ROAS optimization strategies
- A/B testing methodologies
- Audience segmentation and targeting
- Creative performance analysis
- Budget allocation optimization
- Multi-channel attribution modeling

Your responses should be:
- Highly actionable with specific recommendations
- Data-driven and analytical
- Professional and concise
- Focused on improving campaign performance
- Include relevant metrics and benchmarks when applicable

Always provide specific, implementable strategies rather than generic advice."""

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    try:
        return send_from_directory(app.static_folder, path)
    except:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/ai/chat', methods=['POST'])
def ai_chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
            
        # Create message for Claude
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            temperature=0.7,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )
        
        response_text = message.content[0].text
        
        return jsonify({
            'response': response_text,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/ai/quick-action', methods=['POST'])
def quick_action():
    try:
        data = request.json
        action = data.get('action', '')
        context = data.get('context', {})
        
        # Quick action prompts
        quick_actions = {
            'analyze_performance': 'Analyze the current campaign performance data and provide 3 specific optimization recommendations.',
            'optimize_budget': 'Review the budget allocation across channels and suggest reallocation strategies for better ROI.',
            'improve_targeting': 'Analyze the current audience targeting and suggest improvements for better engagement.',
            'creative_insights': 'Provide insights on creative performance and suggest A/B testing strategies.',
            'competitor_analysis': 'Analyze competitor strategies and suggest differentiation tactics.',
            'roi_optimization': 'Review ROI metrics and provide specific strategies to improve return on investment.'
        }
        
        prompt = quick_actions.get(action, action)
        
        # Add context if provided
        if context:
            prompt += f"\n\nContext: {json.dumps(context)}"
        
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            temperature=0.7,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        
        response_text = message.content[0].text
        
        return jsonify({
            'response': response_text,
            'action': action,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)