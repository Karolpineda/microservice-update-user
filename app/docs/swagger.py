# docs/swagger.py
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/custom-docs", include_in_schema=False)
async def custom_swagger_ui_html(request: Request):
    openapi_url = request.url_for("openapi")
    return HTMLResponse(f"""
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8">
        <title>Documentación API - Custom Swagger UI</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.15.5/swagger-ui.css" />
      </head>
      <body>
        <div id="swagger-ui"></div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.15.5/swagger-ui-bundle.js"></script>
        <script>
          window.onload = function() {{
            const ui = SwaggerUIBundle({{
              url: '{openapi_url}',
              dom_id: '#swagger-ui',
              presets: [
                SwaggerUIBundle.presets.apis,
                SwaggerUIBundle.SwaggerUIStandalonePreset
              ],
              layout: "BaseLayout"
            }});
          }};
        </script>
      </body>
    </html>
    """)
