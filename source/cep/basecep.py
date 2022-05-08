import pandas as pd


def base():
    """
    Base dos Ceps que utilizaremos para retornar no acesso da API

    Returns:
        DataFrame: retorna uma tabela com o Local e CEP
    """
    locais: dict[str, str] = {
        "1º Cep do Brasil": "01001-000",
        "Edifício Copan": "01046-010",
        "Edifício Altino Arantes (Banespão)": "01014-900",
        "Centro Cultural Banco do Brasil": "01012-000",
        "Edifício Martinelli": "01011-100",
        "Luz": "01032-001",
        "MASP": "01310-200",
        "Theatro Municipal de São Paulo": "01037-010",
        "Museu do Futebol": "01234-010",
        "Aquário de São Paulo": "04275-000",
    }

    return pd.DataFrame(locais.items(), columns=["Local", "CEP"])
