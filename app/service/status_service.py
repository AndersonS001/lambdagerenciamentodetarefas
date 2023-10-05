from http import HTTPStatus
import json
from repository.db import insere_status, obtem_status_by_name, obtem_todos_status
from aws_lambda_powertools.event_handler import (
    Response,
    content_types,
)


class status_service:
    def lista_todos_status():
        result = obtem_todos_status()

        retorno = []

        for res in result:
            retorno.append({"id": res[0], "status": res[1]})


        return Response(
            status_code=HTTPStatus.OK.value,
            content_type=content_types.APPLICATION_JSON,
            body=retorno,
        )


    def create_status(status):
        # valida se o status existe
        status = json.loads(status)
        status = status.get("status")

        # insere_status(status=status)
        result = obtem_status_by_name(status=status)

        if len(result) == 0:
            # se não existe, cria
            status = insere_status(status=status)

        return Response(
            status_code=HTTPStatus.CREATED.value,  # 201
            content_type=content_types.APPLICATION_JSON,
            body={"id": status[0], "status": status[1]},
        )
        # else:
        #     # se existir, retorna erro
