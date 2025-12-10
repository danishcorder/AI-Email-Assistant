# AI Email Assistant

A modern web application that transforms rough text into professional emails with different tones (formal, friendly, urgent, marketing) using AI-powered text processing.

## 🚀 Features

- **Multi-tone Email Rewriting**: Transform rough text into formal, friendly, urgent, or marketing emails
- **Modern UI**: Clean, responsive design with smooth animations
- **Real-time Processing**: Instant text transformation with loading states
- **Copy to Clipboard**: Easy copying of rewritten emails
- **Character Counter**: Real-time character counting with warnings
- **Keyboard Shortcuts**: Efficient workflow with shortcuts
- **Mobile Responsive**: Works perfectly on all devices
- **Error Handling**: Robust error handling and user feedback

## 🛠️ Technology Stack

### Frontend
- **HTML5**: Semantic markup with modern features
- **CSS3**: Modern styling with animations and responsive design
- **JavaScript (ES6+)**: Modern JavaScript with async/await
- **Font Awesome**: Beautiful icons
- **Google Fonts**: Professional typography

### Backend
- **Python Flask**: Lightweight web framework
- **Flask-CORS**: Cross-origin resource sharing
- **Custom AI Text Processor**: Rule-based tone transformation
- **RESTful API**: Clean API design

## 📁 Project Structure

```
Email Assistant/
├── app.py                 # Main Flask application
├── text_processor.py      # AI text processing logic
├── requirements.txt       # Python dependencies
├── static/               # Frontend assets
│   ├── index.html       # Main HTML page
│   ├── styles.css       # CSS styling
│   └── script.js        # JavaScript functionality
└── README.md            # This file
```

## 🏃‍♂️ Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
   ```bash
   # If you have the files in a directory
   cd Email-Assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your web browser
   - Navigate to `http://localhost:5000`
   - Start writing professional emails!

## 💡 Usage Guide

### Writing Your First Email

1. **Enter your rough text** in the input area
   - Type naturally as if talking to a friend
   - Don't worry about grammar or tone
   - Example: "Hey, I wanted to ask if you could help me with the project deadline. It's really important and I need it by Friday. Thanks!"

2. **Select the desired tone**
   - **Formal**: Professional business language
   - **Friendly**: Warm and conversational
   - **Urgent**: Concise and action-oriented
   - **Marketing**: Persuasive and benefit-focused

3. **Click "Rewrite Email"**
   - Wait for processing (usually 1-2 seconds)
   - Review the rewritten email
   - Copy to clipboard if satisfied

### Keyboard Shortcuts

- **Ctrl/Cmd + Enter**: Rewrite email
- **Ctrl/Cmd + C**: Copy output (when output is focused)
- **Escape**: Clear output

## 🎨 Customization

### Adding New Tones

To add a new tone, modify the `text_processor.py` file:

1. Add tone configuration in `tone_transformations`:
```python
'new_tone': {
    'greetings': ['Hello', 'Hi'],
    'closings': ['Best', 'Regards'],
    'transitions': ['Additionally', 'Furthermore'],
    'fillers_to_remove': ['um', 'uh'],
    'style_adjustments': {
        'contractions': True,
        'casual_language': True,
        'exclamation_marks': False
    }
}
```

2. Update the tone selection in `static/index.html`:
```html
<div class="tone-option" data-tone="new_tone">
    <!-- Your tone option HTML -->
</div>
```

### Styling Customization

The CSS is organized into sections:
- **Reset and base styles**: Universal styling
- **Component styles**: Individual component styling
- **Responsive design**: Mobile-first responsive rules
- **Animations**: Smooth transitions and effects

### Backend API

The application exposes these endpoints:

- `GET /`: Serves the main HTML page
- `POST /api/rewrite`: Rewrite text with specified tone
- `GET /api/tones`: Get available tones

Example API call:
```javascript
fetch('/api/rewrite', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        text: 'Your rough text here',
        tone: 'formal'
    })
})
```

## 🔧 Configuration

### Environment Variables

You can configure the application using environment variables:

- `FLASK_ENV`: Set to `development` for debug mode
- `FLASK_HOST`: Host to bind to (default: `0.0.0.0`)
- `FLASK_PORT`: Port to bind to (default: `5000`)

### Performance Tuning

For production deployment:

1. **Use a production WSGI server**:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

2. **Enable caching**:
   - Add caching headers to static files
   - Use a CDN for better performance

3. **Security headers**:
   - Add security headers for production
   - Enable HTTPS

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment

#### Using Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

#### Using Docker
Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

#### Using Heroku
1. Create `Procfile`:
   ```
   web: python app.py
   ```
2. Deploy to Heroku:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

## 🧪 Testing

### Manual Testing

1. **Input Validation**:
   - Test with empty input
   - Test with very short text (< 10 characters)
   - Test with very long text (> 2000 characters)

2. **Tone Processing**:
   - Test each tone option
   - Verify different outputs for same input
   - Check greeting and closing additions

3. **UI Functionality**:
   - Test responsive design on mobile
   - Verify all buttons work correctly
   - Check animations and transitions

### Automated Testing

You can add automated tests using pytest:

```bash
pip install pytest
```

Create test files:
- `test_text_processor.py`: Test text processing logic
- `test_api.py`: Test API endpoints
- `test_ui.py`: Test frontend functionality

## 🐛 Troubleshooting

### Common Issues

1. **Flask not found**:
   ```bash
   pip install Flask
   ```

2. **CORS errors**: Ensure Flask-CORS is installed and configured

3. **Static files not loading**: Check that the `static` folder exists and contains the files

4. **Port already in use**: Change the port in `app.py` or kill the process using the port

### Debug Mode

For debugging, set environment variable:
```bash
export FLASK_ENV=development
python app.py
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section
2. Review the code comments
3. Create an issue with detailed information

## 🎯 Future Enhancements

Potential features to add:

- [ ] Multiple language support
- [ ] Email templates library
- [ ] Draft saving functionality
- [ ] Export to different formats (PDF, DOC)
- [ ] User authentication
- [ ] Usage analytics
- [ ] Advanced tone customization
- [ ] Integration with email clients
- [ ] Bulk email processing
- [ ] AI-powered suggestions

---

**Made with ❤️ using Flask and modern web technologies**
