# ⛏️ Nexus Auto-Miner (Mobile Edition)

Um gerenciador inteligente de mineração de criptomoedas em Python com interface gráfica web, desenvolvido especificamente para operar de forma segura em notebooks (Laptops) com GPUs NVIDIA. 

O sistema utiliza o `lolMiner` como motor de mineração em segundo plano e inclui um "Cérebro Térmico" para proteger o hardware contra superaquecimento. Atualmente configurado para minerar **BEAM-III** via [Unmineable](https://unmineable.com/) e receber pagamentos automáticos em **NANO** (taxa zero).

---

## 🌟 Funcionalidades Principais

* **Interface Web Moderna:** Painel de controle construído com Streamlit, oferecendo métricas limpas e um gráfico de estabilidade de hashrate em tempo real.
* **Cérebro Térmico (Thermal Guard):** Monitoramento contínuo da temperatura da placa de vídeo. 
  * *Pausa automática:* Se a GPU atingir **90 °C**, o minerador é desligado instantaneamente.
  * *Retomada automática:* O sistema aguarda a placa resfriar até **65 °C** e reinicia o processo sozinho.
* **Integração Bancária via API:** Consulta automática do saldo de NANO diretamente dos servidores da Unmineable, atualizado a cada 60 segundos.
* **Caçador de Zumbis (Zombie Process Killer):** Escaneia o Windows em busca de processos órfãos do minerador e os encerra antes de iniciar uma nova sessão, evitando sobrecarga no PC.
* **Execução Otimizada com Miniconda:** Script `.bat` automatizado para inicializar o ambiente virtual isolado e subir o servidor web com um clique.

---

## 📁 Estrutura do Projeto

\`\`\`text
nexus_miner/
│
├── bin/
│   └── lolMiner.exe              # Arquivo executável do minerador (v1.8+ recomendado)
│
├── config/
│   ├── pools.json                # Servidores de mineração (stratum+tcp)
│   └── wallets.json              # Suas carteiras e identificação do trabalhador
│
├── core/
│   ├── api_market.py             # Simulador de mercado / Forçador de algoritmo seguro
│   ├── gpu_telemetry.py          # Leitor de sensores da GPU via nvidia-smi
│   └── process_manager.py        # Gerenciador assíncrono do lolMiner e Caçador de Zumbis
│
├── app.py                        # Interface principal em Streamlit
└── iniciar_minerador.bat         # Script de inicialização (Entrypoint)
\`\`\`

---

## ⚙️ Pré-requisitos e Instalação

1. **Hardware:** Placa de vídeo NVIDIA (Testado em RTX 3050 Laptop GPU).
2. **Drivers:** Drivers da NVIDIA instalados e atualizados (para o `nvidia-smi` funcionar).
3. **Ambiente Python:** Recomendado o uso do [Miniconda](https://docs.anaconda.com/free/miniconda/index.html).
4. **Dependências:**
   Crie seu ambiente virtual e instale as bibliotecas necessárias:
   \`\`\`cmd
   conda create -n r2 python=3.10
   conda activate r2
   pip install streamlit psutil requests
   \`\`\`

---

## 🚀 Como Usar

1. Verifique se a sua carteira de NANO está configurada corretamente no arquivo `config/wallets.json` no formato `MOEDA:SuaCarteira.NomeDoTrabalhador`.
2. Dê um duplo clique no arquivo **`iniciar_minerador.bat`**.
3. O painel abrirá automaticamente no seu navegador padrão (`http://localhost:8501`).
4. Clique no botão **▶️ Iniciar** e aguarde de 20 a 30 segundos para o motor carregar o arquivo DAG na memória da GPU e o gráfico de hashrate ser desenhado.

---

## ⚠️ Aviso de Segurança (Laptop Mining)

Mineração em notebooks é uma atividade de risco devido às limitações de dissipação térmica do chassi e à proximidade dos componentes com a bateria de lítio. 
* Este software foi projetado com uma trava de emergência térmica, mas **nunca deixe o notebook minerando sobre superfícies de tecido (camas, cobertores)**. 
* Recomenda-se fortemente o uso de um suporte elevado ou base com cooler (ventoinhas) para garantir o fluxo de ar contínuo por baixo do aparelho.