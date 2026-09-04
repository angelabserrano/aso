"""Hook «Próximamente».

Cada unidad cuyo fichero .md lleve al principio esta cabecera:

    ---
    draft: true
    ---

se publica en el sitio, pero SIN su contenido: en su lugar se muestra un
aviso de «Próximamente». Además, en la portada (index.md) el enlace de esa
unidad aparece atenuado y con la etiqueta «Próximamente».

Para publicar una unidad, borra esas tres líneas de su fichero .md (o pon
`draft: false`) y vuelve a desplegar.
"""

import re
from pathlib import Path

AVISO = (
    '!!! info "Próximamente"\n'
    "    Esta unidad todavía no está publicada. Su contenido se irá subiendo\n"
    "    a medida que se trabaje en clase.\n"
)

_FRONT_MATTER = re.compile(r"^-{3}\s*\n(.*?)\n-{3}\s*\n", re.DOTALL)
_DRAFT_LINE = re.compile(r"^\s*draft:\s*(true|yes|on|1)\s*$", re.IGNORECASE | re.MULTILINE)
_H1 = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
_MD_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+\.md)\)")


def _es_borrador(meta) -> bool:
    valor = meta.get("draft", False)
    if isinstance(valor, str):
        return valor.strip().lower() in ("true", "yes", "on", "1")
    return bool(valor)


def _fichero_es_borrador(ruta: Path) -> bool:
    try:
        texto = ruta.read_text(encoding="utf-8")
    except OSError:
        return False
    m = _FRONT_MATTER.match(texto)
    return bool(m and _DRAFT_LINE.search(m.group(1)))


def on_page_markdown(markdown, page, config, files):
    # 1) La propia unidad está en borrador: sustituir el cuerpo por el aviso.
    if _es_borrador(page.meta):
        titulo = page.meta.get("title")
        if not titulo:
            m = _H1.search(markdown)
            titulo = m.group(1) if m else "Unidad"
        return f"# {titulo}\n\n{AVISO}"

    # 2) En la portada: marcar los enlaces de las unidades aún sin publicar.
    if page.file.src_uri == "index.md":
        base = (Path(config["docs_dir"]) / page.file.src_uri).parent

        def _marca(match):
            etiqueta, destino = match.group(1), match.group(2)
            if _fichero_es_borrador(base / destino):
                return (
                    f"[{etiqueta}]({destino}){{ .proximamente }} "
                    f'<span class="proximamente-tag">Próximamente</span>'
                )
            return match.group(0)

        markdown = _MD_LINK.sub(_marca, markdown)

    return markdown
