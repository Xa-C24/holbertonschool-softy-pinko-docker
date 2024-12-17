# Utilise la dernière version d'Ubuntu comme base
FROM ubuntu:latest

# Mise à jour et installation des dépendances
RUN apt-get update && \
    apt-get upgrade -y
RUN apt-get install -y python3 python3-pip

# Résoudre l'erreur EXTERNALLY-MANAGED
RUN rm /usr/lib/python*/EXTERNALLY-MANAGED

# Installation de Flask
RUN pip3 install flask
RUN pip3 install flask-cors

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier Python dans le conteneur
COPY ./api.py /app/api.py

# Définit la commande exécutée par défaut
CMD ["python3", "api.py"]
