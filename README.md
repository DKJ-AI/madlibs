# 📝 MadLibs

A browser-based Mad Libs game with random story templates — fill in random words without context, then watch the story reveal itself in glorious absurdity.

🔗 **Live Demo:** [madlibs-random.streamlit.app](https://madlibs-random.streamlit.app/)

## What is MadLibs?

Mad Libs is a word substitution game. You're asked to provide random words (nouns, verbs, adjectives, etc.) with zero context — then those words get plugged into a hidden story template. The result is almost always chaotic, funny, and completely unexpected.

## Demo

```
Enter a noun: elephant
Enter a verb (past tense): exploded
Enter an adjective: sparkly
Enter a place: the moon

👇 Your Story:

Once upon a time, a sparkly elephant exploded its way to the moon
and was never seen again.
```

## Features

- 🎲 Random story templates on every round
- 📝 Prompts for specific word types (noun, verb, adjective, etc.)
- 🌐 Fully browser-based — no installation needed for players
- ⚡ Built with Streamlit for instant deployment
- 🔄 Play again with a new template each time

## Tech Stack

| Layer | Tool |
|---|---|
| Language | Python 3 |
| Framework | Streamlit |
| Deployment | Streamlit Community Cloud |

## Project Structure

```
madlibs/
├── .devcontainer/         # Dev container config
├── madlib.py              # Core game logic
├── madlibs-random.py      # Streamlit app entry point
├── templates.py           # Story templates library
└── README.md
```

## Run Locally

### Prerequisites

- Python 3.x
- Streamlit

### Setup

```bash
git clone https://github.com/DKJ-AI/madlibs.git
cd madlibs
pip install streamlit
streamlit run madlibs-random.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

## Adding New Templates

Story templates live in `templates.py`. To add your own:

```python
{
    "title": "The Heist",
    "blanks": ["noun", "adjective", "verb", "place"],
    "story": "The {adjective} {noun} decided to {verb} the entire {place}."
}
```

Add as many templates as you like — the app picks one at random each round.

## Deployment

This project is deployed on **Streamlit Community Cloud** for free.

To deploy your own fork:
1. Push to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo and set `madlibs-random.py` as the entry point
4. Deploy — done

## Contributing

Pull requests are welcome. Ideas for contribution:
- New story templates
- Difficulty levels (more blanks = harder)
- Score tracking across rounds
- Multiplayer mode

## Author

**Dipak Jena** — [DKJ-AI](https://github.com/DKJ-AI)


