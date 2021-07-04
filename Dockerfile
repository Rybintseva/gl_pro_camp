FROM python:3

# Install requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy repo into Docker image
WORKDIR /gl_pro_camp
COPY . .