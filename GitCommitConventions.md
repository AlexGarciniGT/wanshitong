# Normativa de Mensajes de Commit

Este documento define el formato y estilo obligatorio para los mensajes de commit en este repositorio.

---

## 🎯 Objetivos

- Mantener un historial claro y legible.
- Facilitar el uso de herramientas de generación de changelog.
- Mejorar la trazabilidad de cambios.

---

## 📝 Formato general

```bash
<tipo>(opcional: contexto): <mensaje breve en imperativo>
```

## Ejemplo

```bash
feat(login): permite recordar usuario al hacer login
```

## 📌 Tipos de commit permitidos

| Tipo       | Descripción                                         |
| ---------- | --------------------------------------------------- |
| `feat`     | Nueva funcionalidad                                 |
| `fix`      | Corrección de errores                               |
| `docs`     | Cambios en documentación                            |
| `style`    | Formato (espacios, comas, puntos y coma, etc.)      |
| `refactor` | Refactorización de código sin cambiar funcionalidad |
| `perf`     | Mejora de rendimiento                               |
| `test`     | Añadir o modificar tests                            |
| `chore`    | Tareas menores (build, config, dependencias…)       |
| `revert`   | Revertir un commit anterior                         |

## 💬 Reglas de redacción

- Usa el modo imperativo: “añade” en lugar de “añadido” o “añadiendo”.

- Usa minúsculas en el mensaje.

- No uses punto final (.).

- Sé claro y conciso (idealmente ≤ 72 caracteres).

- Puedes añadir una descripción más larga tras una línea en blanco.
