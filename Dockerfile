# Etapa 1: Construção da imagem
FROM python:3.10-slim AS build

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de requirements para o container e instala as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# Etapa 2: Executar a aplicação
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia as dependências instaladas na etapa anterior
COPY --from=build /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=build /app /app

# Expor a porta que será utilizada pela aplicação
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]