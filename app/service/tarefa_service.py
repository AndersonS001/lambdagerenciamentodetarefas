from http import HTTPStatus
import json
from repository.db import cria_tarefa, deleta_tarefa_por_id, obtem_todas_tarefas
from aws_lambda_powertools.event_handler import (
    Response,
    content_types,
)


class tarefa_service:
    def obtem_todas_tarefas():
        retorno = []

        result = obtem_todas_tarefas()

        for r in result:
            retorno.append({"id": r[0], "tarefa": r[1], "data": r[3], "status": r[5]})

        return Response(
            status_code=HTTPStatus.OK.value,
            content_type=content_types.APPLICATION_JSON,
            body=retorno,
        )

    def cria_tarefa(tarefa):
        tarefa = json.loads(tarefa)

        result = cria_tarefa(tarefa=tarefa)
        retorno = {
            "id": result[0],
            "tarefa": result[1],
            "data": result[3],
            "status": result[5],
        }

        return Response(
            status_code=HTTPStatus.CREATED.value,
            content_type=content_types.APPLICATION_JSON,
            body=retorno,
        )

    def deleta_tarefa(id):
        
        deleta_tarefa_por_id(id=id)

        return Response(
                status_code=HTTPStatus.NO_CONTENT.value,
                content_type=content_types.APPLICATION_JSON
            )