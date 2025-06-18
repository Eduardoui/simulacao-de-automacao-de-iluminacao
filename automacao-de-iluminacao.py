import time
import random


#Função que simula a detecção de presença (sensor PIR)
def detectar_presenca():
    #Retorna aleatoriamente True (tem alguém) ou False (ambiente vazio)
    return random.choice([True, False])


#Função que simula a leitura de luminosidade (sensor LDR)
def medir_luminosidade():
    #Retorna um valor entre 0 (muito escuro) e 100 (muito claro)
    return random.randint(0, 100)


#Função que decide se a luz será ligada ou desligada com base nos sensores
def controlar_luz(presenca, luminosidade):
    #Se houver presença e o ambiente estiver escuro, liga a luz
    if presenca and luminosidade < 40:
        print("💡 Luz ligada (ambiente escuro e presença detectada)")
    #Se não houver ninguém no ambiente, desliga a luz
    elif not presenca:
        print("💤 Ambiente vazio – luz desligada")
    #Se estiver claro, mesmo com presença, mantém a luz desligada
    else:
        print("🌞 Ambiente claro – luz desligada")


#Simula 10 ciclos de monitoramento (como se fosse tempo real)
for _ in range(10):
    #Lê os "valores" dos sensores simulados
    presenca = detectar_presenca()
    luminosidade = medir_luminosidade()

    #Mostra os valores lidos no terminal
    print(f"\n📡 Presença: {presenca}")
    print(f"🔦 Luminosidade: {luminosidade}")

    #Chama a função que toma a decisão e age com base nas leituras
    controlar_luz(presenca, luminosidade)

    #Guarda 2 segundos antes do próximo ciclo (simula tempo real)
    time.sleep(2)
