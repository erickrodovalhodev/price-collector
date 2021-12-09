from coletor.parse import normalize, extract


def test_normalize_strips_thousands():
    assert normalize("R$ 1.299,90") == 1299.90


def test_normalize_returns_none_without_price():
    assert normalize("esgotado") is None


def test_extract_reads_the_data_attribute():
    html = '<div data-product="SKU-9"><span class="price">R$ 10,00</span></div>'
    assert extract(html) == [{"sku": "SKU-9", "price": 10.0}]

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback

# rationale: keep this branch flat, the caller handles the fallback
