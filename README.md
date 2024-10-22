# AEP Challenge: HackOHI/O 12
For the AEP challenge our objective was to take in a CSV data source, parse it, then categorize the events listed based on their safety risk by presence of "high energy" situations. These events had lengthy descriptions and titles, with many being useless to the purpose. We used Ollama with llama3.2:3b running locally to maintain data privacy. Unfortunately, I can't share the source data at American Electric Power's request for privacy.. However, I am happy to share more about the process.

This was run on Python 3.12 (although the version shouldn't matter), with ollama, csv, pandas, and plotly (express) libraries imported.

Please see [`chat.py`](chat.py) to see the main script and [`graph.py`](graph.py) to see my graphing library usage.
