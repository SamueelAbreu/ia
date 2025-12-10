"""
Sistema Multi-Agente para Análise de Textos
GCC 128 - Inteligência Artificial
Trabalho Prático 06 - Agentes Inteligentes

Este sistema utiliza 3 agentes simples baseados em regras:
1. TextProcessor: Limpa e organiza o texto
2. ContentAnalyzer: Analisa e classifica o conteúdo
3. CoordinatorAgent: Coordena a interação entre os agentes
"""

import re
from datetime import datetime

# ---------------------------------------------------------
#  Classe Base para Agentes
# ---------------------------------------------------------

class Agent:
    """Classe base para todos os agentes"""
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.message_log = []
    
    def log_message(self, message, sender="System"):
        """Registra mensagens recebidas"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = {
            "timestamp": timestamp,
            "sender": sender,
            "message": message
        }
        self.message_log.append(log_entry)
        print(f"[{timestamp}] {self.name} recebeu mensagem de {sender}")
    
    def process(self, data):
        """Método abstrato para processar dados"""
        raise NotImplementedError

# ---------------------------------------------------------
#  Agente 1: TextProcessor (Processador de Texto)
# ---------------------------------------------------------

class TextProcessor(Agent):
    """Agente responsável por limpar e organizar textos"""
    
    def __init__(self):
        super().__init__("TextProcessor", "Limpeza e Organização")
    
    def process(self, text):
        """Limpa e organiza o texto"""
        self.log_message(text[:50] + "...", "Controller")
        
        # Remove espaços extras
        text = re.sub(r'\s+', ' ', text)
        
        # Remove caracteres especiais indesejados
        text = re.sub(r'[^\w\s.,!?;:\-áéíóúàèìòùâêîôûãõçÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÇ]', '', text)
        
        # Capitaliza início de frases
        sentences = text.split('.')
        sentences = [s.strip().capitalize() for s in sentences if s.strip()]
        text = '. '.join(sentences) + '.'
        
        print(f"✓ {self.name}: Texto processado com sucesso")
        return text.strip()

# ---------------------------------------------------------
#  Agente 2: ContentAnalyzer (Analisador de Conteúdo)
# ---------------------------------------------------------

class ContentAnalyzer(Agent):
    """Agente responsável por analisar e classificar conteúdo"""
    
    def __init__(self):
        super().__init__("ContentAnalyzer", "Análise de Conteúdo")
        
        # Palavras-chave por categoria
        self.keywords = {
            "tecnologia": ["tecnologia", "chip", "software", "hardware", "ia", "computador", 
                          "internet", "digital", "app", "smartphone"],
            "esportes": ["futebol", "jogo", "time", "campeonato", "atleta", "esporte",
                        "vitória", "gol", "partida"],
            "política": ["governo", "presidente", "eleição", "política", "lei", "congresso",
                        "ministro", "partido"],
            "economia": ["economia", "dinheiro", "mercado", "bolsa", "juros", "inflação",
                        "dólar", "empresas", "negócios"],
            "saúde": ["saúde", "doença", "hospital", "médico", "tratamento", "vacina",
                     "paciente", "sintoma"]
        }
    
    def process(self, text):
        """Analisa o texto e retorna classificação"""
        self.log_message(text[:50] + "...", "TextProcessor")
        
        text_lower = text.lower()
        
        # Classifica o tema
        tema = self._classify_theme(text_lower)
        
        # Conta palavras
        word_count = len(text.split())
        
        # Verifica presença de números (pode indicar dados concretos)
        has_numbers = bool(re.search(r'\d+', text))
        
        # Gera resumo simples (primeiras 3 frases)
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        resumo = '. '.join(sentences[:3]) + '.'
        
        # Análise de credibilidade básica
        credibilidade = "MÉDIA"
        if has_numbers and word_count > 50:
            credibilidade = "ALTA"
        elif word_count < 20:
            credibilidade = "BAIXA"
        
        analysis = {
            "tema": tema,
            "credibilidade": credibilidade,
            "palavras": word_count,
            "resumo": resumo,
            "possui_dados": "Sim" if has_numbers else "Não"
        }
        
        print(f"✓ {self.name}: Análise concluída")
        return analysis
    
    def _classify_theme(self, text):
        """Classifica o tema baseado em palavras-chave"""
        scores = {category: 0 for category in self.keywords}
        
        for category, keywords in self.keywords.items():
            for keyword in keywords:
                if keyword in text:
                    scores[category] += 1
        
        # Retorna categoria com maior score
        max_category = max(scores, key=scores.get)
        if scores[max_category] > 0:
            return max_category.capitalize()
        return "Geral"

# ---------------------------------------------------------
#  Agente 3: CoordinatorAgent (Coordenador)
# ---------------------------------------------------------

class CoordinatorAgent(Agent):
    """Agente coordenador que gerencia o fluxo entre agentes"""
    
    def __init__(self):
        super().__init__("Coordinator", "Coordenação")
        self.text_processor = TextProcessor()
        self.content_analyzer = ContentAnalyzer()
    
    def process(self, raw_text):
        """Coordena o processamento completo"""
        print("\n" + "="*60)
        print("SISTEMA MULTI-AGENTE INICIADO")
        print("="*60 + "\n")
        
        # Etapa 1: Processar texto
        print(f"[Etapa 1] {self.name} → TextProcessor")
        clean_text = self.text_processor.process(raw_text)
        
        print()
        
        # Etapa 2: Analisar conteúdo
        print(f"[Etapa 2] {self.name} → ContentAnalyzer")
        analysis = self.content_analyzer.process(clean_text)
        
        print()
        
        # Compilar resultado final
        result = {
            "texto_original": raw_text,
            "texto_processado": clean_text,
            "analise": analysis
        }
        
        print(f"✓ {self.name}: Processamento completo finalizado\n")
        return result

# ---------------------------------------------------------
#  Função para exibir resultados
# ---------------------------------------------------------

def display_results(result):
    """Exibe os resultados de forma formatada"""
    print("="*60)
    print("RESULTADO DA ANÁLISE")
    print("="*60)
    
    print("\n📄 TEXTO ORIGINAL:")
    print("-" * 60)
    print(result["texto_original"])
    
    print("\n\n✨ TEXTO PROCESSADO:")
    print("-" * 60)
    print(result["texto_processado"])
    
    print("\n\n📊 ANÁLISE DE CONTEÚDO:")
    print("-" * 60)
    analysis = result["analise"]
    print(f"  Tema: {analysis['tema']}")
    print(f"  Credibilidade: {analysis['credibilidade']}")
    print(f"  Número de palavras: {analysis['palavras']}")
    print(f"  Possui dados numéricos: {analysis['possui_dados']}")
    print(f"\n  Resumo:")
    print(f"  {analysis['resumo']}")
    
    print("\n" + "="*60)

# ---------------------------------------------------------
#  Execução Principal
# ---------------------------------------------------------

if __name__ == "__main__":
    # Exemplo de texto para análise
    texto_exemplo = """
    A Apple anunciou ontem um novo chip focado em IA generativa,
    prometendo reduzir 40% do consumo de energia e aumentar 60% da performance.
    Especialistas afirmam que isso pode alterar o mercado global de hardware.
    A empresa investiu 2 bilhões de dólares no desenvolvimento.
    """
    
    # Criar coordenador e processar
    coordinator = CoordinatorAgent()
    resultado = coordinator.process(texto_exemplo)
    
    # Exibir resultados
    display_results(resultado)
    
    print("\n💡 SISTEMA: Experimente com outros textos editando a variável 'texto_exemplo'!")
    print("="*60)
