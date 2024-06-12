from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(descripion="Nome do centro de treinamento", example="CT King", max_length=20)]
    endereco: Annotated[str, Field(descripion="Endereço do centro de treinamento", example="CT King", max_length=60)]
    proprietario: Annotated[str, Field(descripion="Proprietário do centro de treinamento", example="CT King", max_length=30)]
