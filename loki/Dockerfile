FROM  node:21-alpine
COPY ./node-js-getting-started /app
WORKDIR /app
RUN npm install
RUN date
EXPOSE 5001
ENTRYPOINT ["/usr/local/bin/npm", "start"]

