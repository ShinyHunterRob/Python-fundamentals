estado_civil = input("Insira o seu estado civil ([S]olteiro, [C]asado, [V]iúvo, [D]ivorciado):\t").strip().lower()

match estado_civil:
    case "S": print("Seleccionou Solteiro")
    case "C": print("Seleccionou Casado")
    case "V": print("Seleccionou Viúvo")
    case "D": print("Seleccionou Divorciado")
    case _ : print("Opção inválido")