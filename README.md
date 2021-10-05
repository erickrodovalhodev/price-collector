# price-collector

Collects public competitor prices into a CSV for a comparison table.

## run

    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    python -m coletor.main

## notes

Identifiers are in Portuguese (`coletor/`, `preco`), which is how the client
codebase was written. Later repos in this profile are in English.

Rotating user agent, 3 attempts with exponential backoff, SKU dedupe before
writing. No headless browser — the two targets serve price in the HTML.
