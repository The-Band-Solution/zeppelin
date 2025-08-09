Perfeito 👍
Segue o **README revisado e completo**, agora contendo a explicação do **Makefile** e do **.env** de forma organizada e profissional:

---

# ZEPPELIN: A DIAGNOSTIC INSTRUMENT FOR Continuous Software Engineering

It helps identify the degree of adoption of Continuous Software Engineering (CSE) practices in each StH stage. This way, organizations can have a panoramic view of the CSE practices they perform, identify where they are in the CSE evolutionary path, and which areas should be improved. Thus, it is possible to develop a plan to improve and advance software development towards CSE. Zeppelin uses StH \[3] as a reference model and also considers Continuous\* activities proposed in \[2], CSE practices and aspects provided in the Eye of CSE \[4], and CSE processes constituting the CSE framework (hereafter, called FCSE) proposed in \[1].

> The name Zeppelin was chosen because the diagnosis instrument allows viewing an organization in a panoramic way, as if we were in a zeppelin seeing a city. Besides, Led Zeppelin band created the Stairway to Heaven song.

---

## References

1. Monalessa Perini Barcellos. 2020. Towards a Framework for Continuous Software Engineering. In Proceedings of the 34th Brazilian Symposium on Software Engineering (Natal, Brazil) (SBES ’20). ACM, 626–631.
2. Brian Fitzgerald and Klaas-Jan Stol. 2017. Continuous software engineering: A roadmap and agenda. Journal of Systems and Software 123 (2017), 176–189.
3. Helena Holmström Olsson, Hiva Alahyari, and Jan Bosch. 2012. Climbing the "Stairway to Heaven": A Multiple-Case Study Exploring Barriers in the Transition from Agile Development towards Continuous Deployment of Software. In 2012 38th Euromicro Conference on Software Engineering and Advanced Applications. 392–399.
4. Jan Ole Johanssen, Anja Kleebaum, Barbara Paech, and Bernd Bruegge. 2019. Continuous software engineering and its support by usage and decision knowledge: An interview study with practitioners. Journal of Software: Evolution and Process 31, 5 (2019), 21–69.

---

## ⚙️ Makefile Commands

O projeto inclui um `Makefile` para facilitar a execução de tarefas no ambiente Docker.

| Comando          | Descrição                                                                      |
| ---------------- | ------------------------------------------------------------------------------ |
| `make up`        | Sobe os containers definidos no `docker-compose.yml`.                          |
| `make build`     | Reconstrói as imagens e sobe os containers. Use após alterações no Dockerfile. |
| `make down`      | Para e remove os containers, preservando volumes.                              |
| `make destroy`   | Para e remove containers **e** volumes (apaga dados persistidos).              |
| `make superuser` | Executa o script `create_superuser.sh` para criar um superusuário Django.      |

**Exemplos:**

```bash
# Iniciar o ambiente
make up

# Rebuild e iniciar containers
make build

# Parar containers
make down

# Remover tudo (inclusive volumes)
make destroy

# Criar superusuário Django
make superuser
```

---

## 📄 Environment Variables (`.env`)

O arquivo `.env` contém todas as variáveis de ambiente necessárias para configuração e execução do Zeppelin.

### 🔹 Configurações Gerais

| Variável                 | Descrição                                                  | Exemplo                   |
| ------------------------ | ---------------------------------------------------------- | ------------------------- |
| `ALLOWED_HOSTS`          | Lista de hosts permitidos pelo Django (`*` permite todos). | `*`                       |
| `DEBUG`                  | Modo de depuração (`True` ou `False`).                     | `True`                    |
| `SECRET_KEY`             | Chave secreta usada pelo Django (mantenha privada).        | `3izb^ryg...`             |
| `DJANGO_SETTINGS_MODULE` | Módulo de configurações do Django.                         | `zeppelin.settings.local` |

---

### 🔹 Banco de Dados

| Variável            | Descrição                                                       | Exemplo                         |
| ------------------- | --------------------------------------------------------------- | ------------------------------- |
| `USE_SQLITE`        | Define se o SQLite será usado (`True`) ou PostgreSQL (`False`). | `False`                         |
| `DB_ENGINE_LOCAL`   | Backend do banco.                                               | `django.db.backends.postgresql` |
| `DB_HOST_LOCAL`     | Host do banco.                                                  | `zeppelin-db`                   |
| `DB_NAME_LOCAL`     | Nome do banco.                                                  | `zeppelin`                      |
| `DB_USER_LOCAL`     | Usuário do banco.                                               | `zeppelin`                      |
| `DB_PASSWORD_LOCAL` | Senha do banco.                                                 | `zeppelin`                      |
| `DB_PORT_LOCAL`     | Porta do banco.                                                 | `5432`                          |

---

### 🔹 Configuração de E-mail

| Variável              | Descrição                    | Exemplo                |
| --------------------- | ---------------------------- | ---------------------- |
| `DEFAULT_FROM_EMAIL`  | E-mail padrão de envio.      | `no-reply@exemplo.com` |
| `EMAIL_HOST`          | Servidor SMTP.               | `smtp.exemplo.com`     |
| `EMAIL_HOST_USER`     | Usuário SMTP.                | `no-reply@exemplo.com` |
| `EMAIL_HOST_PASSWORD` | Senha SMTP.                  | `minhasenha`           |
| `EMAIL_PORT`          | Porta SMTP.                  | `587`                  |
| `EMAIL_USE_TLS`       | Uso de TLS (`True`/`False`). | `True`                 |

---

### 🔹 Segurança e Hash

| Variável       | Descrição                             | Exemplo        |
| -------------- | ------------------------------------- | -------------- |
| `HASHIDS_SALT` | Salt para geração de IDs codificados. | `hA8(scA@!...` |

---

### 🔹 URLs e Integrações

| Variável         | Descrição                      | Exemplo                 |
| ---------------- | ------------------------------ | ----------------------- |
| `URL_VALIDATION` | URL para validação (opcional). | *(vazio)*               |
| `URL`            | URL base do sistema.           | `http://localhost:8000` |

---

### 🔹 PostgreSQL (Docker)

Usadas pelo container PostgreSQL no `docker-compose.yml`:

| Variável            | Descrição         | Exemplo    |
| ------------------- | ----------------- | ---------- |
| `POSTGRES_DB`       | Nome do banco.    | `zeppelin` |
| `POSTGRES_USER`     | Usuário do banco. | `zeppelin` |
| `POSTGRES_PASSWORD` | Senha do banco.   | `zeppelin` |

---

### 🔹 Superusuário Django (Criação Automática)

| Variável                    | Descrição        | Exemplo           |
| --------------------------- | ---------------- | ----------------- |
| `DJANGO_SUPERUSER_USERNAME` | Nome do admin.   | `admin`           |
| `DJANGO_SUPERUSER_EMAIL`    | E-mail do admin. | `admin@admin.org` |
| `DJANGO_SUPERUSER_PASSWORD` | Senha do admin.  | `xxxxxx!` |

---

Se quiser, posso já **incluir um passo-a-passo de inicialização rápida** no final do README para que novos usuários consigam rodar o projeto em menos de 5 minutos.
Quer que eu adicione essa seção também?
