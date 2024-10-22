# AEP Challenge: HackOHI/O 12
For the AEP challenge our objective was to take in a CSV data source, parse it, then categorize the events listed based on their safety risk by presence of "high energy" situations. These events had lengthy descriptions and titles, with many being useless to the purpose. We used Ollama with `llama3.2:3b` running locally to maintain data privacy. Unfortunately, I can't share the source data CSV at American Electric Power's request for privacy. However, I am happy to share more about the process.

# Language and Dependencies
This was run on Python 3.12 (although the version shouldn't matter a great deal), with `ollama`, `csv`, `pandas`, and `plotly.express` libraries installed and imported.

# Code Below
Please see [`chat.py`](chat.py) to see the main processing and `llama3.2` prompting script and [`graph.py`](graph.py) to see my graphing methodology.
