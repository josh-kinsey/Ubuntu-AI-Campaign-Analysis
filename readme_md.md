# AI Campaign Analysis Platform

An AI-powered campaign analysis engine designed to extract highly actionable insights from campaign performance data using Claude AI.

## Features

- **AI-Powered Analysis**: Integration with Claude AI for intelligent campaign insights
- **Performance Optimization**: Real-time campaign performance analysis and recommendations
- **Quick Actions**: Pre-built analysis templates for common optimization tasks
- **RESTful API**: Clean API endpoints for integration with frontend applications
- **Scalable Architecture**: Built with Flask and designed for production deployment

## API Endpoints

### AI Chat
- `POST /api/ai/chat` - Send messages to AI assistant
- `POST /api/ai/quick-action` - Execute predefined analysis actions

### User Management
- `GET /api/users` - Get all users
- `POST /api/users` - Create new user
- `GET /api/users/<id>` - Get specific user
- `PUT /api/users/<id>` - Update user
- `DELETE /api/users/<id>` - Delete user

### System
- `GET /api/health` - Health check endpoint
- `GET /` - Serve frontend application

## Quick Actions

The platform supports several predefined analysis actions:

- **analyze_performance**: Analyze current campaign performance
- **optimize_budget**: Review and optimize budget allocation
- **improve_targeting**: Analyze and improve audience targeting
- **creative_insights**: Provide creative performance insights
- **competitor_analysis**: Analyze competitor strategies
- **roi_optimization**: Optimize return on investment

## Environment Variables

Required environment variables for deployment:

- `CLAUDE_API_KEY` - Your Claude AI API key
- `FLASK_ENV` - Set to 'production' for production deployment
- `SECRET_KEY` - Flask secret key for session management
- `PORT` - Port number (default: 5000)

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variables:
```bash
export CLAUDE_API_KEY=your_api_key_here
export FLASK_ENV=development
```

3. Run the application:
```bash
python src/main.py
```

## Deployment

### Vercel (Recommended)
1. Deploy using Vercel CLI:
```bash
vercel --prod
```

2. Set environment variables in Vercel dashboard

### Other Platforms
- **Heroku**: Use the included `Procfile`
- **Railway**: Connect GitHub repository
- **DigitalOcean**: Use App Platform

## Project Structure

```
├── src/
│   ├── main.py              # Flask application entry point
│   ├── routes/
│   │   ├── ai_chat.py       # AI chat endpoints
│   │   └── user.py          # User management
│   ├── models/
│   │   └── user.py          # Database models
│   └── static/              # Frontend build files
├── requirements.txt         # Python dependencies
├── vercel.json             # Vercel configuration
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details