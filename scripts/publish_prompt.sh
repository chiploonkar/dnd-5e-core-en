#!/bin/bash
# Prompt for PyPI token (hidden) and call publish_final.sh
set -e

if [ ! -f "publish_final.sh" ]; then
  echo "publish_final.sh introuvable dans le répertoire courant. Exécutez depuis la racine du projet."
  exit 1
fi

read -p "Nom d'utilisateur TWINE (laisser vide pour __token__): " input_user
if [ -z "$input_user" ]; then
  export TWINE_USERNAME="__token__"
else
  export TWINE_USERNAME="$input_user"
fi

read -s -p "Entrez votre PyPI API token: " input_token
echo
if [ -z "$input_token" ]; then
  echo "Aucun token fourni. Abandon."
  exit 1
fi

export TWINE_PASSWORD="$input_token"

# Call the final publish script (it will ask for confirmation)
chmod +x publish_final.sh
./publish_final.sh

# Unset token from env
unset TWINE_PASSWORD
unset TWINE_USERNAME

echo "Token unset from environment."
