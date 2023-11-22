# How to run this ?

1. Clone the repo
2. `cd loki`
3. Run `docker-compose up -d`
```
lenovo@lenovo-ThinkPad-E570:~/projects/arival-test/loki$ docker-compose up -d
[+] Building 1.4s (10/10) FINISHED                                                                                            docker:default
 => [arival-nodejs internal] load build definition from Dockerfile                                                                      0.0s
 => => transferring dockerfile: 190B                                                                                                    0.0s
 => [arival-nodejs internal] load .dockerignore                                                                                         0.0s
 => => transferring context: 2B                                                                                                         0.0s
 => [arival-nodejs internal] load metadata for docker.io/library/node:21-alpine                                                         0.8s
 => [arival-nodejs internal] load build context                                                                                         0.1s
 => => transferring context: 419.73kB                                                                                                   0.1s
 => [arival-nodejs 1/5] FROM docker.io/library/node:21-alpine@sha256:4a512d1538b1a8281b58cab0b366a5c62436566bb63e7dcd4a6769c98edb3b5f   0.0s
 => CACHED [arival-nodejs 2/5] COPY ./node-js-getting-started /app                                                                      0.0s
 => CACHED [arival-nodejs 3/5] WORKDIR /app                                                                                             0.0s
 => CACHED [arival-nodejs 4/5] RUN npm install                                                                                          0.0s
 => [arival-nodejs 5/5] RUN date                                                                                                        0.4s
 => [arival-nodejs] exporting to image                                                                                                  0.0s
 => => exporting layers                                                                                                                 0.0s
 => => writing image sha256:4fc98f0ef6f17a687bf20afdd8c616cf2d4a9dda64616a97f8a5fef3da098783                                            0.0s
 => => naming to docker.io/library/loki-arival-nodejs                                                                                   0.0s
[+] Running 7/7
 ✔ Container loki-arival-nodejs-1  Started                                                                                             10.3s 
 ✔ Container loki-minio-1          Running                                                                                              0.0s 
 ✔ Container loki-write-1          Running                                                                                              0.0s 
 ✔ Container loki-read-1           Running                                                                                              0.0s 
 ✔ Container loki-gateway-1        Running                                                                                              0.0s 
 ✔ Container loki-promtail-1       Running                                                                                              0.0s 
 ✔ Container loki-grafana-1        Running  ----
```
4. The app will be accessible at http://localhost:5001/
5. The app logs can be found in grafana at http://localhost:3000/explore?panes=%7B%2255F%22:%7B%22datasource%22:%22P8E80F9AEF21F6940%22,%22queries%22:%5B%7B%22refId%22:%22A%22,%22expr%22:%22%7Bcontainer%3D%5C%22loki-arival-nodejs-1%5C%22%7D%20%7C%3D%20%60%60%22,%22queryType%22:%22range%22,%22datasource%22:%7B%22type%22:%22loki%22,%22uid%22:%22P8E80F9AEF21F6940%22%7D,%22editorMode%22:%22builder%22%7D%5D,%22range%22:%7B%22from%22:%22now-6h%22,%22to%22:%22now%22%7D%7D%7D&schemaVersion=1&orgId=1