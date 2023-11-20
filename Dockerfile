FROM node:20.9.0-alpine3.18 AS builder
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
RUN npm prune --production

# Build production image
# NodeJS 20.9.0 
FROM node:20.9.0-alpine3.18 
WORKDIR /app
COPY --from=builder /app/build build/
COPY --from=builder /app/node_modules node_modules/
COPY package.json .

# Run the app
EXPOSE 3000
ENV NODE_ENV=production
CMD [ "node", "build" ]