FROM dockercloud/haproxy

WORKDIR /etc/haproxy/

COPY haproxy.cfg ./

RUN systemctl restart haproxy