from langchain.agents import AgentExecutor
from orquestador import AgenteOrquestador

def main():
    agente = AgenteOrquestador()
    orquestador = AgentExecutor(
        agent=agente.agent,
        tools=agente.tools,
        verbose=True
    )

    pergunta = 'Gostaria que você me explicasse como funcionan os desvios condicionais'
    resposta = orquestador.invoke({'input': pergunta })
    print(resposta)

if __name__ == '__main__':
    main()