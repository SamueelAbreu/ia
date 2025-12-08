# Trabalho Prático 06 - Agentes Inteligentes

## 📋 Descrição

Sistema Multi-Agente para Análise de Textos desenvolvido para a disciplina GCC 128 - Inteligência Artificial.

### Agentes Implementados

1. **CoordinatorAgent** - Coordena o fluxo entre os agentes
2. **TextProcessor** - Limpa e organiza textos
3. **ContentAnalyzer** - Analisa e classifica conteúdo

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior
- Nenhuma biblioteca externa necessária (usa apenas bibliotecas padrão do Python)

### Execução

```bash
# Navegar até a pasta
cd 06_agentes_inteligentes

# Executar o sistema
python main.py
```

## 💡 Como Usar

### Exemplo Básico

O arquivo `main.py` já vem com um exemplo funcional. Para testar com seu próprio texto:

```python
# Edite a variável texto_exemplo no final do arquivo main.py
texto_exemplo = """
Seu texto aqui para análise...
"""

# Execute o programa
python main.py
```

### Saída Esperada

O sistema irá:
1. Processar e limpar o texto
2. Classificar o tema (Tecnologia, Esportes, Política, Economia, Saúde, Geral)
3. Avaliar credibilidade (ALTA, MÉDIA, BAIXA)
4. Gerar um resumo automático
5. Identificar presença de dados numéricos

## 📊 Exemplo de Execução

```
============================================================
SISTEMA MULTI-AGENTE INICIADO
============================================================

[Etapa 1] Coordinator → TextProcessor
[22:15:30] TextProcessor recebeu mensagem de Controller
✓ TextProcessor: Texto processado com sucesso

[Etapa 2] Coordinator → ContentAnalyzer
[22:15:30] ContentAnalyzer recebeu mensagem de TextProcessor
✓ ContentAnalyzer: Análise concluída

✓ Coordinator: Processamento completo finalizado

============================================================
RESULTADO DA ANÁLISE
============================================================

📄 TEXTO ORIGINAL:
------------------------------------------------------------
[Texto original aqui]

✨ TEXTO PROCESSADO:
------------------------------------------------------------
[Texto limpo e formatado]

📊 ANÁLISE DE CONTEÚDO:
------------------------------------------------------------
  Tema: Tecnologia
  Credibilidade: ALTA
  Número de palavras: 46
  Possui dados numéricos: Sim
  
  Resumo:
  [Resumo gerado automaticamente]
```

## 🏗️ Arquitetura

### Fluxo de Trabalho

```
Usuário
   ↓
CoordinatorAgent
   ├→ TextProcessor → Texto Limpo
   └→ ContentAnalyzer → Análise Completa
   ↓
Resultado Final
```

### Características

- **Modular:** Cada agente tem responsabilidade específica
- **Autônomo:** Agentes tomam decisões independentes
- **Escalável:** Fácil adicionar novos agentes
- **Simples:** Não requer APIs externas

## 📁 Estrutura de Arquivos

```
06_agentes_inteligentes/
├── main.py                 # Aplicação principal com os 3 agentes
├── SLIDES_RELATORIO.md     # Slides do relatório em Markdown
└── README.md               # Este arquivo
```

## 🎓 Informações Acadêmicas

**Disciplina:** GCC 128 - Inteligência Artificial  
**Professor:** Ahmed Ali Abdalla Esmin - Anna Paula Figueiredo  
**Universidade:** UFLA - Universidade Federal de Lavras  
**Data de Entrega:** 09/12/2025

## 📦 Entrega

Para criar o arquivo ZIP de entrega:

```bash
cd ..
zip -r nome1_nome2.zip 06_agentes_inteligentes/
```

O arquivo ZIP deve conter:
- ✅ Código da aplicação (`main.py`)
- ✅ Slides do trabalho (`SLIDES_RELATORIO.md`)
- ✅ README com instruções (`README.md`)

## 🎥 Vídeo de Apresentação

Link do vídeo: [Inserir link aqui após gravar]

O vídeo deve conter:
- Apresentação dos slides
- Demonstração do sistema funcionando
- Explicação da arquitetura dos agentes

## 🔧 Possíveis Extensões

- Adicionar agente de verificação de fontes
- Implementar análise de sentimentos
- Criar interface gráfica
- Integrar com APIs de IA (GPT, Claude)
- Adicionar suporte a múltiplos idiomas

## 📝 Licença

Trabalho acadêmico desenvolvido para fins educacionais.
