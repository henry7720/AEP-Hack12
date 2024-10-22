# AEP Challenge: HackOHI/O 12
The Hackathon was a 2-day event, although we made this in probably one day for the purpose of experiential learning. For the AEP challenge, then, our objective was to take in a 20,000-line CSV data source, parse it, then categorize the events listed based on their safety risk by presence of "high energy" situations using power of LLMs. These events had lengthy descriptions and titles, with many being red-herrings. We used Ollama with `llama3.2:3b` running locally to maintain data privacy. Unfortunately, I can't share the source data CSV at American Electric Power's request for privacy. However, I am happy to share more about the process.

# Language and Dependencies
This was run on Python 3.12 (although the version shouldn't matter a great deal), with `ollama`, `csv`, `pandas`, and `plotly.express` libraries installed and imported.

# Code Below
Please see [`chat.py`](chat.py) to see the main processing and `llama3.2` prompting script and [`graph.py`](graph.py) to see my graphing methodology.

# License
[`MIT`](LICENSE)
