from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ENTRY = ROOT / "index.html"

class AssetParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.assets = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("src", "href", "poster"):
            if attrs.get(key):
                self.assets.append(attrs[key])

if not ENTRY.is_file():
    raise SystemExit("index.html is missing")
parser = AssetParser()
parser.feed(ENTRY.read_text(encoding="utf-8"))
for value in parser.assets:
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc or value.startswith(("#", "data:", "mailto:", "tel:", "javascript:")):
        continue
    path = unquote(parsed.path)
    if path and not (ROOT / path.lstrip("/")).resolve().is_file():
        raise SystemExit(f"Missing local asset: {value}")
print(f"Checked {len(parser.assets)} HTML asset references.")
