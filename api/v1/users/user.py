from typing import Callable

from fastapi import APIRouter, Depends

from app.controllers import AuthController, UserController
from app.models import User
from app.schemas.extras import Token
from core.factory import Factory