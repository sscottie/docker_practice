FROM dockercloud/haproxy

WORKDIR /etc/haproxy/

COPY haproxy.cfg ./