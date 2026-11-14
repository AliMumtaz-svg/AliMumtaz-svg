"""Inline id.png and right_pointing.png into the SVGs in this folder as base64 data URIs.

Run from the assets/ folder after adding the PNGs:
    python3 inline_images.py

Each SVG contains a marker such as
    <!--INLINE_IMAGE id=hero-portrait x=600 y=36 w=190 h=228 file=id.png mode=slice-->
The script replaces it with an <image> element whose href is a data: URI, so the
SVG makes no network requests. PNG bytes are embedded unchanged, so alpha is preserved.
Re-running is safe: an existing inlined image is replaced, not duplicated.
If a PNG is missing, its marker is left alone and the placeholder stays.
"""
import base64, glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MARKER = re.compile(r"<!--INLINE_IMAGE ([^>]*?)-->(?:<image data-inline=\"[^\"]*\"[^>]*/>)?")

def parse(attrs):
    out = {}
    for token in attrs.split():
        key, _, value = token.partition("=")
        out[key] = value
    return out

def build_image(a, data_uri):
    mode = "slice" if a.get("mode") == "slice" else "meet"
    return (f'<image data-inline="{a["id"]}" href="{data_uri}" x="{a["x"]}" y="{a["y"]}" '
            f'width="{a["w"]}" height="{a["h"]}" preserveAspectRatio="xMidYMid {mode}"/>')

def process(svg_path):
    text = open(svg_path, encoding="utf-8").read()
    cache, changed = {}, False
    def repl(m):
        nonlocal changed
        marker = m.group(0).split("-->")[0] + "-->"
        a = parse(m.group(1))
        path = os.path.join(HERE, a["file"])
        if not os.path.exists(path):
            return marker  # keep placeholder; no image yet
        raw = open(path, "rb").read()
        if raw[:8] != b"\x89PNG\r\n\x1a\n":
            raise SystemExit(f"{a['file']} is not a PNG; export it as PNG and rerun")
        data_uri = "data:image/png;base64," + base64.b64encode(raw).decode("ascii")
        changed = True
        return marker + build_image(a, data_uri)
    new = MARKER.sub(repl, text)
    if changed and new != text:
        open(svg_path, "w", encoding="utf-8").write(new)
        return True
    return False

if __name__ == "__main__":
    for svg in sorted(glob.glob(os.path.join(HERE, "*.svg"))):
        if process(svg):
            print("inlined images into", os.path.basename(svg))
    print("done")
