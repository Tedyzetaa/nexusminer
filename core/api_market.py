import requests

def obter_rentabilidade_atual():
    mercado = {
        "kawpow": -1.0,
        "autolykos2": -1.0,
        "karlsenv2": -1.0, 
        "beam-iii": 0.15  # O Rei voltou!
    }
    melhor_algo = max(mercado, key=mercado.get)
    return mercado, melhor_algo