# Typer Bot

A simple automation tool for [typer.io](https://typer.io/) typing competitions using Playwright.

## Features

- Automatically detects and types the current word
- Configurable typing delay for human-like behavior
- Colored console logging for better visibility
- Error handling to keep the bot running

## Installation

1. Clone the repository:

```bash
git clone https://github.com/hikmatazimzade/typer-bot
cd typer-bot
```

2. Install dependencies:

```bash
uv sync
```

3. Install Playwright browsers:

```bash
uv run playwright install chromium
```

## Usage

Run the bot:

```bash
uv run python -m src.typer
```

The bot will:

1. Open a Chromium browser window
2. Navigate to typer.io
3. Start automatically typing the displayed words
4. Continue until you stop the program (Ctrl+C)

## Configuration

- **Typing delay**: Adjust the `sleep(uniform(0.1, 0.2))` in `typer.py` to change typing speed
- **Browser mode**: Set `headless=True` in `typer.py` to run without GUI

## License

Apache 2.0
