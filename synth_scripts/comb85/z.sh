for file in ./*.v; do sed -i 's/[A-Z][A-Z0-9_]*[[:space:]]*(/(/' "$file"; done
