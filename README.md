## Documentation
* Browseable API (Django REST framework): http://localhost:8000/
* OpenAPI
    - Swagger UI: http://localhost:8000/swagger/
    - ReDoc: http://localhost:8000/redoc/


TODO:
- [x] django project
- [x] django app
- [x] basic models
- [ ] upload + gltf viewer compatible download api
- [ ] django-debug-toolbar
- [x] ASGI-server
- [x] collectstatic / STATIC_ROOT (docker build issue)
- [x] real static files solution (-> DEBUG_UVICORN)
- [ ] split up settings (dev/prod/local)
  - proper secret key handling...
- [ ] logging config
- [ ] log rotation (docker compose)
- [ ] file upload limit - traefik?
- [ ] dev/prod build -> https://docs.docker.com/compose/compose-file/#target


unclear
- libs/apps distinction?

---
- https://docs.djangoproject.com/en/3.0/topics/security/#ssl-https
- https://docs.djangoproject.com/en/3.0/ref/request-response/#fileresponse-objects
