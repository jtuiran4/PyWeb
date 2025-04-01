# USAMOS LA IMAGEN BASE DE PYTHON
FROM python:3.13

# SE ESTABLECE EL DIRECTORIO DE TRABAJO
WORKDIR /app

# COPIAMOS LOS ARCHIVOS AL CONTENEDOR
COPY app/ app/
COPY requirements.txt .

# INSTALAMOS DEPENDENCIAS 
RUN pip install --no-cache-dir -r requirements.txt

# EXPONEMOS EL PUERTO 5000
EXPOSE 5000

CMD ["python", "app/main.py"]