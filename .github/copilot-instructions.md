# Copilot Instructions

## Application structure

- The Flask site lives in `teste/`: `main.py` creates the app and imports `rotas.py`, which registers page and calculation routes on that app. Start it from the repository root with `python teste\main.py`.
- `rotas.py` renders Jinja templates from `teste/templates/`; shared CSS is in `teste/static/style.css`. Use Flask's `url_for('static', filename='style.css')` pattern for stylesheet references.
- The root-level Python files are separate interactive command-line formula calculators; they use `input()`/`print()` and are not imported by the Flask site.

## Calculator conventions

- Keep each calculator's form action and HTTP method, HTML input `name` values, matching `request.form.get(...)` keys, and result variable passed to `render_template(...)` in sync. For example, the density form posts to `/calculo_densidade`, whose handler reads its named fields and renders `densidade.html` with `vdensidade`.
- The web calculation handlers use `Decimal` for submitted numeric values. Existing forms use `step="any"` and use zero to mark the value the user wants calculated.
- User-facing text and many route, template, and field names are in Portuguese; preserve existing spellings and accents when connecting these surfaces.

## Install, run, and test

- Run `python install.py` to install Flask with the Python interpreter running the installer.
- Run the site with `python teste\main.py` from the repository root.
- No automated tests or test/lint runner are currently configured, so there is no existing single-test command.
