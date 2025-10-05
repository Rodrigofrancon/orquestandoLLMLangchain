from langchain.tools import BaseTool
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from my_models import GEMINI_FLASH
from my_keys import GEMINI_API_KEY
import ast

class FerramentaExplicadora(BaseTool):
    name: str = 'ferramenta_explicadora'
    description: str = '''
    Utilize esta ferramenta sempre que for solictado que você explique um conteúde para pessoas.

    # Entradas Requiridas
    - 'tema' (str): O tema principal informado na pergunta do usuário.
    '''
    return_direct: bool = True

    def _run(self, acao):
        acao = ast.literal_eval(acao)
        tema_parametro = acao.get('tema','')

        llm = ChatGoogleGenerativeAI(
            api_key=GEMINI_API_KEY,
            model=GEMINI_FLASH
        )

        template_resposta = PromptTemplate(
            template='''
            Assuma o papel de um professor preocupado com aspectos de didática do usuário.

            1. Elabore uma explicação sobre o tema {tema} que seja compreensível por estudantes na fase de 
            conclusão do ensino médio.
            2. Utilize exemplos do cotidiano para tornar a explicação mais facil.
            3. Caso sugira algum recurso para apoiar na explicação, lembre-se do cenário e contexto brasileiro.
            4. Caso você apresente um codígo, seja didático e utilize Python
            
            Tema pergunta: {tema}
            ''',
            input_variables=['tema']            
        )

        cadeia = template_resposta | llm | StrOutputParser()
        resposta = cadeia.invoke({'tema': tema_parametro})
        return resposta    


