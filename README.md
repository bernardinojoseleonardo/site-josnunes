# Josnunes - Site Web Profissional

Site web para a empresa **Josnunes**, especializada em Gráfica e Têxtil, localizada em Huambo, Angola.

## Stack
- **Backend/Frontend**: Python + Django
- **UI**: Django Templates + Tailwind CSS (CDN)
- **Imagens**: Pillow + Fancybox (CDN)
- **Forms**: Django Crispy Forms + Crispy Tailwind
- **Deploy**: Gunicorn + Whitenoise

## Estrutura do Projeto
- `josnunes/`: Configurações principais.
- `core/`: App principal com models, views e admin.
- `templates/`: Arquivos HTML.
- `static/`: Arquivos CSS e JS.
- `media/`: Uploads de imagens da galeria.

## Como rodar localmente
1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Configure o arquivo `.env` baseado no `.env.example`.
4. Execute as migrações: `python manage.py migrate`.
5. Carregue os dados iniciais: `python manage.py loaddata initial_data.json`.
6. Crie um superusuário: `python manage.py createsuperuser`.
7. Rode o servidor: `python manage.py runserver`.

## Deploy no Railway.app
1. Instale a [Railway CLI](https://docs.railway.app/guides/cli).
2. Faça login: `railway login`.
3. Inicialize o projeto: `railway init`.
4. Adicione as variáveis de ambiente no painel da Railway:
   - `SECRET_KEY`
   - `DEBUG=False`
   - `DATABASE_URL` (A Railway fornece uma automaticamente ao adicionar um DB)
   - `WHATSAPP_NUMBER`
   - `INSTAGRAM_URL`
   - `FACEBOOK_URL`
5. O `Procfile` já está configurado para o Gunicorn.
6. O Whitenoise cuidará dos arquivos estáticos automaticamente.

## Contato
Localização: Huambo, Angola
WhatsApp: +244 [NUMERO]
