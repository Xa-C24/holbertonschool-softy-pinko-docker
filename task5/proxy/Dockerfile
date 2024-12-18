# Contains instructions for creating the Docker image.

# Utilise l'image officielle Nginx la plus récente
FROM nginx:latest

# Copie le fichier proxy.conf dans le bon emplacement dans le conteneur Nginx
COPY proxy.conf /etc/nginx/conf.d/default.conf

# Expose le port 80 pour permettre au serveur d'écouter les connexions
EXPOSE 80

# Commande pour démarrer Nginx
CMD ["nginx", "-g", "daemon off;"]
