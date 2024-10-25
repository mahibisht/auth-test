# # Stage 1: Build the Angular application
# FROM node:20.17.0-slim as build-stage

# WORKDIR /app

# COPY package*.json /app/

# RUN npm install

# COPY . /app

# RUN npm run build -- --outputPath=./dist/out

# Stage 2: Serve the app with NGINX
FROM nginx:alpine

# Remove the default nginx static assets
RUN rm -rf /usr/share/nginx/html/*

# Copy the built app from the previous stage and place it in the appropriate directory
# COPY --from=build-stage /app/dist/out/ /var/www/myfrontend

COPY . /var/www/myfrontend

# Copy your custom nginx config
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

# docker build:  docker build -t ui-app:latest .