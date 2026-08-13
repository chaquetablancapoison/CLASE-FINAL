# Tkinter con POO

Implementando arquitectura de separación por capas (un prototipo de la misma).

## Arrancar la aplicación

```
python | python3 -B main.py
```

## Estructra del proyecto

```
proyecto/
│
├── repositories/
│   └── task_repository.py
│
├── services/
│   └── task_service.py
│
├── models/
│   └── task.py
│
├── ui/
│   └── app_window.py
│
└── main.py
```


## Actividad .grid()
La interfaz de `ui/app_window.py` fue reorganizada utilizando exclusivamente el manejador de geometría `.grid()`, con `row`, `column`, `sticky`, `padx`, `pady` y `columnspan`.
