import re
from bs4 import BeautifulSoup

PATTERN = re.compile(r"R\$\s*([\d\.]+),?(\d{2})?")


def normalize(txt):
    m = PATTERN.search(txt or "")
    if not m:
        return None
    whole = m.group(1).replace(".", "")
    cents = m.group(2) or "00"
    return float("%s.%s" % (whole, cents))


def extract(html):
    soup = BeautifulSoup(html, "lxml")
    results = []
    for item in soup.select("[data-product]"):
        price = normalize(item.select_one(".price").get_text())
        if price:
            results.append({"sku": item["data-product"], "price": price})
    return results
# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback
