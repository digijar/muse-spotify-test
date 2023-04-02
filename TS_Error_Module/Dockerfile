# Use Node.js LTS (Long Term Support) version
FROM node:lts

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the source files
COPY ./ .

# Expose the application port
EXPOSE 4997

# Start the application using ts-node
CMD [ "npx", "ts-node", "./error.ts" ]