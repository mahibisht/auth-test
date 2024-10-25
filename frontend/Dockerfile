# Use the official Nginx image as the base image
FROM nginx:alpine

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy the custom Nginx configuration file into the container
COPY default.conf /etc/nginx/conf.d/

# Remove the default Nginx HTML file
RUN rm /usr/share/nginx/html/index.html

COPY ./ /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

# Start Nginx when the container has provisioned.
CMD ["nginx", "-g", "daemon off;"]

# docker build:  docker build -t ui-app:latest .
# docker run -d -p 8080:80 ui-app