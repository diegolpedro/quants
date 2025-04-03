FROM python:3.10

# Configura el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia y actualiza dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código del proyecto
COPY . .

# Expone el puerto 8080
EXPOSE 8080

# Ejecuta Gunicorn
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:8080", "quants.wsgi:application"]
