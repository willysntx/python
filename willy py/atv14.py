conta = float(input("qual o numero da conta:"))
saldo = float(input("saldo da conta:"))
debito = float(input("qual valor do debito:"))
credito = float(input("qual o valor do credito:"))
saldoAtual = (saldo-debito+credito)

print("o valor na conta e",saldoAtual)

if saldoAtual <0:
    print("o saldo e negativo:")

elif saldoAtual >0:
     print("o saldo e positivo")
