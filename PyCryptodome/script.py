import crypten
import torch

def main():
    # Inizializza Crypten (questo avvia un ambiente di calcolo sicuro)
    crypten.init()

    # Crea i dati "segreti" utilizzando Crypten
    # Per l'esempio, useremo numeri secchi (puoi usare i tuoi dati crittografati reali)
    a = crypten.cryptensor(torch.tensor([2]), requires_grad=False)

    # Calcola il massimo tra i numeri secchi
    max_value = a.max()

    # Stampa il risultato (risultato crittografato)
    print(f"massimo = {max_value.get_plain_text()}")  # get_plain_text() per ottenere il valore decifrato

    # Arrestate Crypten
    crypten.shutdown()

if __name__ == '__main__':
    main()
