"""Vercel serverless entry point.

Vercel's Python runtime imports this file and uses the module-level ASGI
callable named `app`. We simply re-export the FastAPI app from our package so
that all relative imports inside `app/` keep working normally.
"""
from app.main import app  # noqa: F401  (re-exported as the ASGI handler)
