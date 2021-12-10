import csv, sys
from .spider import fetch

COMPETITORS = ["https://exemplo-a.com.br/lista", "https://exemplo-b.com.br/ofertas"]


def main():
    vistos = set()
    with open("prices.csv", "w", newline="") as f:
        w = csv.DictWriter(f, ["sku", "price", "source"])
        w.writeheader()
        for url in COMPETITORS:
            for p in fetch(url):
                if p["sku"] in vistos:
                    continue
                vistos.add(p["sku"])
                w.writerow({**p, "source": url})
                print(p, file=sys.stderr)


if __name__ == "__main__":
    main()
# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback
