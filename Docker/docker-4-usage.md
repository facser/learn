


```bash

docker swarm init --advertise-addr <manager node IP>

--publish mode=host,target=80,published=8080 

--constraint node.labels.region==east 

```