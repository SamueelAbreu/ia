# Trabalho Prático 06 - Agentes Inteligentes
## GCC 128 - Inteligência Artificial

**Aluno(a):** [Seu Nome]  
**Professor:** Ahmed Ali Abdalla Esmin - Anna Paula Figueiredo  
**Data:** 08/12/2025

---

## 📋 Slide 1: Descrição da Aplicação

### Sistema Multi-Agente para Análise de Textos

**Objetivo:** Processar e analisar textos automaticamente através da colaboração de múltiplos agentes inteligentes.

**Funcionalidades:**
- ✅ Limpeza e organização automática de textos
- ✅ Classificação temática (Tecnologia, Esportes, Política, Economia, Saúde)
- ✅ Análise de credibilidade baseada em características do texto
- ✅ Geração de resumos automáticos
- ✅ Identificação de presença de dados numéricos

**Tecnologia:** Python puro com arquitetura orientada a agentes

---

## 🤖 Slide 2: Desenho dos Agentes

### Arquitetura do Sistema

```
┌─────────────────────────────────────────────────┐
│          COORDINATOR AGENT                      │
│         (Agente Coordenador)                    │
│                                                 │
│  • Gerencia o fluxo de trabalho                │
│  • Coordena comunicação entre agentes          │
│  • Compila resultados finais                   │
└────────────┬──────────────────┬─────────────────┘
             │                  │
             │                  │
             ▼                  ▼
    ┌────────────────┐  ┌──────────────────┐
    │ TEXT PROCESSOR │  │ CONTENT ANALYZER │
    │     AGENT      │  │      AGENT       │
    ├────────────────┤  ├──────────────────┤
    │ • Remove ruído │  │ • Classifica     │
    │ • Formata texto│  │   tema           │
    │ • Organiza     │  │ • Avalia         │
    │   conteúdo     │  │   credibilidade  │
    │                │  │ • Gera resumo    │
    └────────────────┘  └──────────────────┘
```

### Fluxo de Trabalho

1. **Entrada:** Usuário fornece texto bruto
2. **Processamento:** Coordinator envia para TextProcessor
3. **Análise:** Texto limpo vai para ContentAnalyzer
4. **Saída:** Coordinator compila e apresenta resultados

---

## 🎯 Slide 3: Papéis dos Agentes

### 1. CoordinatorAgent (Coordenador)
- **Papel:** Orquestrador principal do sistema
- **Responsabilidades:**
  - Iniciar e gerenciar o fluxo de trabalho
  - Distribuir tarefas para agentes especializados
  - Compilar resultados finais
  - Manter registro de atividades

### 2. TextProcessor (Processador de Texto)
- **Papel:** Especialista em limpeza de dados textuais
- **Responsabilidades:**
  - Remover espaços e caracteres indesejados
  - Normalizar formatação
  - Capitalizar frases corretamente
  - Preparar texto para análise

### 3. ContentAnalyzer (Analisador de Conteúdo)
- **Papel:** Especialista em análise semântica
- **Responsabilidades:**
  - Classificar tema do texto
  - Avaliar credibilidade
  - Contar palavras e identificar dados numéricos
  - Gerar resumos automáticos

---

## 💡 Slide 4: Características da Implementação

### Princípios Utilizados

**1. Separação de Responsabilidades**
- Cada agente tem função específica e bem definida
- Facilita manutenção e extensão do código

**2. Comunicação Entre Agentes**
- Sistema de log de mensagens
- Rastreabilidade de informações
- Timestamps para auditoria

**3. Autonomia**
- Agentes processam dados independentemente
- Decisões baseadas em regras e heurísticas

**4. Escalabilidade**
- Arquitetura permite adicionar novos agentes facilmente
- Fácil extensão de funcionalidades

---

## 📊 Slide 5: Exemplo de Execução

### Entrada
```
A Apple anunciou ontem um novo chip focado em IA generativa,
prometendo reduzir 40% do consumo de energia e aumentar 60% 
da performance. Especialistas afirmam que isso pode alterar 
o mercado global de hardware. A empresa investiu 2 bilhões 
de dólares no desenvolvimento.
```

### Saída
```
📊 ANÁLISE DE CONTEÚDO:
  Tema: Tecnologia
  Credibilidade: ALTA
  Número de palavras: 46
  Possui dados numéricos: Sim
  
  Resumo:
  A apple anunciou ontem um novo chip focado em ia generativa, 
  prometendo reduzir 40 do consumo de energia e aumentar 60 da 
  performance. Especialistas afirmam que isso pode alterar o 
  mercado global de hardware.
```

---

## 🔍 Slide 6: Conclusões

### Pontos Positivos
✅ **Modularidade:** Código organizado e fácil de manter  
✅ **Simplicidade:** Não requer APIs externas ou configurações complexas  
✅ **Funcionalidade:** Sistema funcional e demonstra conceitos de agentes  
✅ **Extensibilidade:** Fácil adicionar novos agentes ou funcionalidades  
✅ **Autonomia:** Agentes tomam decisões independentes  

### Aprendizados
- Compreensão prática de sistemas multi-agentes
- Importância da coordenação entre agentes
- Design de arquiteturas baseadas em agentes
- Comunicação e troca de informações entre componentes

### Melhorias Futuras
- Integração com modelos de IA (GPT, BERT)
- Interface gráfica para usuário
- Análise de sentimentos
- Suporte a múltiplos idiomas
- Verificação de fontes e fact-checking

---

## 🎥 Slide 7: Demonstração

### Como Executar

```bash
# Navegar até a pasta
cd 06_agentes_inteligentes

# Executar o sistema
python main.py
```

### Vídeo de Apresentação

**Link do vídeo:** [Inserir link do YouTube/Google Drive aqui]

**Conteúdo do vídeo:**
- Demonstração ao vivo do sistema
- Explicação da arquitetura
- Exemplos de uso com diferentes textos
- Discussão dos resultados

---

## 📚 Slide 8: Referências

### Conceitos Utilizados

1. **Sistemas Multi-Agentes**
   - Arquitetura baseada em agentes autônomos
   - Coordenação e colaboração entre agentes

2. **Processamento de Linguagem Natural**
   - Limpeza e normalização de texto
   - Classificação temática por palavras-chave

3. **Análise de Conteúdo**
   - Heurísticas para avaliação de credibilidade
   - Resumo automático baseado em sentenças

### Estrutura de Arquivos
```
06_agentes_inteligentes/
├── main.py                  # Aplicação principal
├── SLIDES_RELATORIO.md     # Slides do relatório
└── README.md               # Instruções de uso
```

---

## 🙏 Slide Final

### Agradecimentos

Obrigado pela atenção!

**Professor:** Ahmed Ali Abdalla Esmin - Anna Paula Figueiredo  
**Disciplina:** GCC 128 - Inteligência Artificial  
**Universidade Federal de Lavras - UFLA**

---

**Link do vídeo de apresentação:** [Inserir link aqui]

**Repositório:** [Se aplicável]

---
