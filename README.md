# MAX33
1. Pilha (Login e Logout)
No contexto do e-commerce de transportes, a pilha é usada para gerenciar o processo de login e logout dos usuários, aplicando a lógica do último a entrar, primeiro a sair (LIFO). Isso significa que o último usuário que fez login será o primeiro a efetuar logout, simulando um controle simples da sessão ativa. Essa estrutura ajuda a organizar quem está atualmente usando o sistema e permite desfazer operações recentes, garantindo que o sistema mantenha um fluxo organizado de acesso.

2. Lista (Lista de Compras)
A lista é utilizada para armazenar os itens selecionados pelos usuários para compra, como passagens ou serviços adicionais. No e-commerce de transportes, essa lista representa o conjunto de produtos que o usuário deseja adquirir antes de adicioná-los ao carrinho. Ela permite adicionar novos produtos, visualizar o que foi selecionado e remover itens indesejados, refletindo a dinâmica real de seleção de produtos em um ambiente de compras online.

3. Vetor (Carrinho de Compras)
O vetor organiza o carrinho de compras, onde cada elemento contém detalhes específicos do produto — nome, quantidade e preço. No sistema de transporte, isso permite que o usuário controle suas passagens ou serviços escolhidos, visualize o custo total e faça ajustes conforme necessário antes de finalizar a compra. Essa estrutura facilita o armazenamento de dados detalhados de cada item e a realização de cálculos como o valor total da compra.

4. Matriz (Métodos de Pagamento)
A matriz armazena as opções de pagamento disponíveis, associando cada método com suas características, como taxa de juros e número máximo de parcelas. Para o e-commerce de transportes, isso permite oferecer ao cliente diferentes formas de pagamento, incluindo cartão de crédito parcelado, PIX e boleto, simulando condições reais de pagamento. Essa organização facilita a apresentação e o processamento dessas opções durante a finalização da compra.

5. Fila (Dados de Usuários Logados)
A fila é empregada para controlar a ordem de usuários logados no sistema, seguindo a lógica do primeiro a entrar, primeiro a sair (FIFO). Isso reflete a fila de atendimento típica em sistemas online, onde os usuários são processados na ordem em que acessam o e-commerce de transportes. Essa estrutura assegura que o sistema gerencie as conexões e sessões de forma justa e organizada, especialmente em ambientes com múltiplos acessos simultâneos.

Com essas estruturas, o projeto simula um e-commerce tradicional de transportes, modelando as operações básicas de login, seleção de produtos, gerenciamento do carrinho, opções de pagamento e controle de usuários, tudo isso com a eficiência e organização que cada estrutura de dados oferece.
