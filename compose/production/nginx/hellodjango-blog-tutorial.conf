upstream hellodjango_blog_tutorial  {
    server hellodjango_blog_tutorial:8000;
}

server {
    server_name  hellodjango-blog-tutorial-demo.zmrenwu.com;

    location /static {
        alias /apps/hellodjango_blog_tutorial/static;
    }

    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_pass http://hellodjango_blog_tutorial;
    }

    listen 80;
}