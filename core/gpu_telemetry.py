import subprocess

def obter_status_gpu():
    """Usa o nvidia-smi nativo do Windows para ler dados da RTX 3050."""
    try:
        # Comando para buscar temperatura e uso de energia
        resultado = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=temperature.gpu,power.draw", "--format=csv,noheader,nounits"],
            encoding='utf-8'
        )
        dados = resultado.strip().split(', ')
        return {
            "temperatura": int(dados[0]),
            "energia_w": float(dados[1])
        }
    except Exception as e:
        return {"temperatura": 0, "energia_w": 0.0, "erro": str(e)}