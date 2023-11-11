for i in {1..10}; do
  for j in {1..32}; do
    echo -n $((RANDOM % 2))
  done
  echo
done

