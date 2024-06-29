from pydantic import EmailStr

from app.models import User
from app.repositories import UserRepository
from app.schemas.extras import Token
from core.controller import BaseController
from core.database import Propagation, Transactional
from core.exceptions import BadRequestException, UnauthorizedException
