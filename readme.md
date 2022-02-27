# Projeto e-diaristas

### Instalando o projeto

#### Clonar o projeto
`git clone https://github.com/lgustavoss/ediaristas.git`

#### Instalar dependencias
`pip install -r requirements.txt`

#### Alterar configurações do DB no arquivo `setting.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_bd',
        'HOST': 'host_bd',
        'PORT': porta_bd,
        'USER': 'usuario_db',
        'PASSWORD': 'senha_db'
    }
}
```

#### Migrar banco de dados
`python manage.py migrate`

#### Iniciar o servidor
`python manage.py runserver`