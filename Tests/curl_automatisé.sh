if curl -s -o /dev/null -w "%{http_code}" http://localhost:5001/login | grep -q 200; then
  echo "Vous êtes bien loggé "
else
  echo "Login raté"
fi

