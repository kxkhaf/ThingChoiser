# 👗 Fashion Assistant Bot

AI-powered Telegram bot that helps you create perfect outfits using your wardrobe items and current weather conditions.

## 🌟 Key Features

- **AI Clothing Recognition**: Identifies garment types from your photos
- **Smart Outfit Suggestions**: Recommends combinations based on:
  - Your personal wardrobe
  - Current weather conditions
  - Preferred style (casual/formal)
  - Color preferences
- **Wardrobe Management**: Digital closet of your clothing items

## 🤖 How It Works

1. **Add Items**:
   - Send photos of your clothes
   - Bot identifies each item using neural network
   - Stores them in your digital wardrobe

2. **Get Recommendations**:
   - Share your location or city
   - Specify preferred style/color
   - Receive perfect outfit suggestions

## 🧠 AI Technology

- Custom-trained neural network (`model.h5`)
- Classifies 10 clothing categories:
  ```python
  ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']