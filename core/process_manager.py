import subprocess
import psutil
import os
import time

class GerenciadorMinerador:
    def __init__(self):
        self.processo_atual = None
        self.algo_atual = None
        self.matar_zumbis() 

    def matar_zumbis(self):
        encontrou_zumbi = False
        for proc in psutil.process_iter(['name']):
            try:
                nome = proc.info['name'].lower()
                if nome in ['lolminer.exe', 'gminer.exe']:
                    proc.terminate()
                    encontrou_zumbi = True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        if encontrou_zumbi:
            time.sleep(1) 

    def iniciar(self, algoritmo, carteira, pool):
        self.parar()
        self.matar_zumbis() 
        
        diretorio_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        comando = []
        
        if algoritmo == "karlsenv2":
            caminho_exe = os.path.join(diretorio_base, "bin", "lolMiner.exe")
            comando = [caminho_exe, "--algo", "KARLSENV2", "--pool", pool, "--user", carteira, "--apiport", "4444"]
            
        # NOVA INTEGRAÇÃO: BEAM-III DO UNMINEABLE
        elif algoritmo == "beam-iii":
            caminho_exe = os.path.join(diretorio_base, "bin", "lolMiner.exe")
            comando = [caminho_exe, "--algo", "BEAM-III", "--pool", pool, "--user", carteira, "--apiport", "4444"]
            
        if comando:
            if not os.path.exists(caminho_exe): return False
            try:
                self.processo_atual = subprocess.Popen(
                    comando, 
                    creationflags=subprocess.CREATE_NEW_CONSOLE,
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
                )
                self.algo_atual = algoritmo
                return True
            except: return False
        return False

    def parar(self):
        if self.processo_atual:
            try:
                processo_pai = psutil.Process(self.processo_atual.pid)
                for filho in processo_pai.children(recursive=True): filho.terminate()
                processo_pai.terminate()
                psutil.wait_procs([processo_pai] + processo_pai.children(recursive=True), timeout=3)
            except: pass
            
        self.matar_zumbis() 
        self.processo_atual = None
        self.algo_atual = None