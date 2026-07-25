#!/bin/bash
# Turn the markdown templates into printable PDFs (needs pandoc + Google Chrome).
cd "$(dirname "$0")" || exit 1
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for f in templates/*.md; do
  name="${f%.md}"
  pandoc "$f" -f markdown -t html5 -s -o "$name.html" --css="style/master.css" 2>/dev/null
  "$CHROME" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="$name.pdf" "file://$PWD/$name.html" 2>/dev/null
  echo "built $name.pdf"
done
