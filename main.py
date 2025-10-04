from langchain.agents import AgentExecutor
from orquestador import AgenteOrquestador

def main():
    agente = AgenteOrquestador()
    orquestador = AgentExecutor(
        agent=agente.agent,
        tools=agente.tools,
        verbose=True
    )

    pergunta = 'Faça uma análise da imagem image.png'
    resposta = orquestador.invoke({'input': pergunta })
    print(resposta)

if __name__ == '__main__':
    main()