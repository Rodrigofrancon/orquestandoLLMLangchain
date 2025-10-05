from langchain_google_genai import ChatGoogleGenerativeAI
from my_models import GEMINI_FLASH
from my_keys import GEMINI_API_KEY
from langchain.globals import set_debug
set_debug(False)

from langchain import hub
from langchain.agents import create_react_agent
from langchain.agents import Tool
from ferramenta_analisadora_imagem import FerramentaAnalisadoraImagem 
from ferramenta_explicadora import FerramentaExplicadora

class AgenteOrquestador:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            api_key=GEMINI_API_KEY,
            model=GEMINI_FLASH
        )

        ferramente_analisador_imagem = FerramentaAnalisadoraImagem()
        ferramenta_explicadora = FerramentaExplicadora()

        self.tools = [
            Tool(
                name = ferramente_analisador_imagem.name,
                func = ferramente_analisador_imagem.run,
                description = ferramente_analisador_imagem.description,
                return_direct = ferramente_analisador_imagem.return_direct
            ),
             Tool(
                name = ferramenta_explicadora.name,
                func = ferramenta_explicadora.run,
                description = ferramenta_explicadora.description,
                return_direct = ferramenta_explicadora.return_direct
            )
        ]

        prompt = hub.pull("hwchase17/react")
        self.agent = create_react_agent(self.llm, self.tools, prompt)
