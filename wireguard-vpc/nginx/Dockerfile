FROM nginx:latest

# Copy SSL certificates (adjusted path)
COPY nginx/etc/atharvavyas.com.pem /etc/ssl/atharvavyas.com.pem
COPY nginx/etc/atharvavyas.com.key /etc/ssl/atharvavyas.com.key

# Copy Nginx main configuration
COPY nginx/nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf

# optional backup, not required
# COPY nginx/nginx/conf.d/default.conf.old /etc/nginx/conf.d/default.conf.old

EXPOSE 80
EXPOSE 443

# Verify config and start Nginx in foreground
CMD ["sh", "-c", "nginx -t && nginx -g 'daemon off;'"]
