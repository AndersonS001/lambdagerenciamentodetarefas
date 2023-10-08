from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import LambdaFunctionUrlResolver
from service.status_service import status_service
from service.tarefa_service import tarefa_service
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

app = LambdaFunctionUrlResolver()
logger = Logger()


@app.get("/status")
def lista_todos_status():
    return status_service.lista_todos_status()

@app.get("/status/<id>")
def lista_status_por_id(id: str):
    return status_service.lista_status_por_id(id=id)

@app.post("/status")
def create_status():
    return status_service.create_status(app.current_event.body)

@app.delete("/status/<id>")
def deleta_status_por_id(id: str):
    return status_service.deleta_status_por_id(id=id)

@app.get("/tarefas")
def obtem_todas_tarefas():
    return tarefa_service.obtem_todas_tarefas()

@app.post("/tarefas")
def cria_tarefa():
    return tarefa_service.cria_tarefa(app.current_event.body)

@app.put(".+")
def put():
    return {"path_received": app.current_event.raw_event}

@app.delete("/tarefas/<id>")
def delete(id: str):
    return tarefa_service.deleta_tarefa(id=id)

# @logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)