Este notebook implementa uma análise robusta de intervenções para ansiedade, incorporando técnicas de análise de sensibilidade para avaliar a confiabilidade dos resultados. O framework utiliza uma abordagem de Mistura de Especialistas (MoE) para quantificar a importância das características e determinar relacionamentos causais, tudo isso submetido à análise de sensibilidade para verificar a robustez das conclusões.

## Características Principais

- **Análise de Sensibilidade**: Avalia a robustez dos achados frente a variações nos dados e parâmetros do modelo
- **Explicabilidade via SHAP**: Quantifica a importância das características no modelo
- **Visualizações Avançadas**: KDE, Violin plots, Coordenadas Paralelas e Hipergrafos
- **Bootstrap Estatístico**: Análise via reamostragem para avaliar a confiabilidade das métricas
- **Integração com LLMs**: Utiliza Grok, Claude-3.7-Sonnet e Grok-Enhanced para sintetizar insights

## Fluxo de Trabalho

1. **Carregamento e Validação de Dados**: Carrega dados sintéticos de intervenção em ansiedade, valida estrutura, conteúdo e tipos de dados, tratando erros de maneira elegante.

2. **Pré-processamento**: Realiza codificação one-hot da coluna de grupo e escala características numéricas.

3. **Análise de Valores SHAP**: Quantifica a importância das características usando TreeExplainer.

4. **Visualização de Dados**: Gera visualizações complementares:
   - Gráficos de densidade KDE
   - Violin plots para comparação entre grupos
   - Gráficos de coordenadas paralelas para análise de trajetórias
   - Hipergrafos para visualizar padrões de relacionamento

5. **Resumo Estatístico**: Realiza análise de bootstrap e gera estatísticas descritivas.

6. **Análise de Sensibilidade**: Executa diversas análises de sensibilidade:
   - Perturbação de dados com diferentes níveis de ruído
   - Variação de parâmetros do modelo
   - Análise de subgrupos
   - Remoção de características para avaliar impacto

7. **Relatório de Insights via LLMs**: Sintetiza os achados usando três modelos diferentes, enfatizando a análise de sensibilidade e a robustez das conclusões.

## Requisitos Técnicos

O notebook requer as seguintes bibliotecas Python:
- pandas, matplotlib, seaborn, networkx
- shap, scikit-learn, numpy
- plotly, scipy

## Estrutura de Dados

O conjunto de dados deve conter as seguintes colunas:
- `participant_id`: Identificador único para cada participante
- `group`: Categorização dos participantes (Group A, Group B, Control)
- `anxiety_pre`: Nível de ansiedade pré-intervenção (escala 0-10)
- `anxiety_post`: Nível de ansiedade pós-intervenção (escala 0-10)

## Constantes Configuráveis

O notebook inclui diversas constantes para ajuste da análise:
- `OUTPUT_PATH`: Diretório para os artefatos gerados
- `BOOTSTRAP_RESAMPLES`: Número de reamostragens para análise bootstrap (padrão: 500)
- `LINE_WIDTH`: Largura de linha para visualizações (padrão: 2.5)

## Funções Principais

- `validate_dataframe()`: Verifica a integridade e consistência dos dados
- `calculate_shap_values()`: Computa e visualiza valores SHAP para explicabilidade
- `perform_sensitivity_analysis()`: Executa análises de sensibilidade para verificar robustez
- `create_kde_plot()`, `create_violin_plot()`, etc.: Funções de visualização especializadas
- `perform_bootstrap()`: Calcula intervalos de confiança via bootstrap
- `generate_insights_report()`: Integra análises de LLMs para interpretação dos resultados

## Análise de Sensibilidade

A análise de sensibilidade incorpora:
1. **Perturbação de Dados**: Adição de ruído aleatório para simular variações nos dados
2. **Variação de Parâmetros**: Testes com diferentes configurações do modelo
3. **Análise de Subgrupos**: Cálculo de métricas específicas para cada grupo de intervenção
4. **Variabilidade de Features**: Teste de remoção de características para avaliar impacto
5. **Reamostragem**: Análise estatística via bootstrap para verificar a estabilidade das métricas

## Segurança

O código inclui placeholders para chaves de API (GROK_API_KEY, CLAUDE_API_KEY) que devem ser gerenciadas com segurança. O código destaca a importância de não compartilhar estas chaves diretamente no código.

## Saídas

O notebook gera diversos artefatos no diretório de saída:
- Gráfico de resumo SHAP (`shap_summary.png`)
- Visualizações KDE, Violin, Coordenadas Paralelas e Hipergrafos
- Arquivo de resumo estatístico (`summary.txt`)
- Relatório de insights combinando análises dos LLMs (`insights.txt`)

## Execução

O notebook verifica automaticamente se está sendo executado no ambiente Google Colab e ajusta os caminhos conforme necessário. A execução principal ocorre através da função `if __name__ == "__main__":` que orquestra todo o fluxo de trabalho.

## Palavras-chave

Análise de Sensibilidade, Robustez, Intervenção em Ansiedade, Inferência Causal, SHAP, LLMs, Visualização de Dados, Aprendizado de Máquina, Validação, Generalização

## Autor
Hélio Craveiro Pessoa Júnior
