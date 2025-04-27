#!/bin/bash

for src in articles/*.md; do
  target="${src%.md}.pdf"
  if [[ ! -f "$target" || "$src" -nt "$target" ]]; then
    echo "Compiling $src..."
    pandoc "$src" -o "$target"
  fi
done
