# Cookie Clicker Bot Setup Instructions

## Problem
Your CookieClickerBot is getting a `net::ERR_ADDRESS_INVALID` error because it's trying to navigate to an invalid URL.

## Solution Options

### Option 1: Use Local HTTP Server (Recommended)

1. **Start the local server:**
   ```powershell
   # In PowerShell
   .\start-server.ps1
   
   # Or in Command Prompt
   start-server.bat
   
   # Or directly with Python
   python serve.py
   ```

2. **Update your bot's URL to:**
   ```
   http://localhost:8000
   ```

3. **In your C# bot code, change the URL:**
   ```csharp
   driver.Navigate().GoToUrl("http://localhost:8000");
   ```

### Option 2: Use File Protocol (Alternative)

Update your bot to use the local file path:
```csharp
string cookieClickerPath = @"file:///C:/Users/Willi/Documents/Repos/cookie-clicker/index.html";
driver.Navigate().GoToUrl(cookieClickerPath);
```

### Option 3: Use Original Online Version

If you want to use the original game:
```csharp
driver.Navigate().GoToUrl("https://orteil.dashnet.org/cookieclicker/");
```

## Testing the Setup

1. Start the local server using one of the methods above
2. Open your browser and go to `http://localhost:8000`
3. Verify Cookie Clicker loads correctly
4. Update your bot's URL and test again

## Troubleshooting

- **Port 8000 in use?** Try: `python serve.py 8001`
- **Python not found?** Install Python from https://www.python.org/downloads/
- **Still having issues?** Check that your bot has the correct URL format

## Common Bot URLs by Method
- Local server: `http://localhost:8000`
- File protocol: `file:///C:/Users/Willi/Documents/Repos/cookie-clicker/index.html`
- Online version: `https://orteil.dashnet.org/cookieclicker/`
