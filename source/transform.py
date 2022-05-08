import requests
import json
import pandas as pd
from pandas import DataFrame
from cep import basecep


def listaCep():
    """
    Tabela refatorada dos CEPs
    """
    tabelaCep: DataFrame = basecep.base()
    tabelaCep["CEP"] = tabelaCep["CEP"].str.replace("-", "")

    return tabelaCep


def apiList():
    """
    Acessando a API de CEP de acordo com os locais da tabela criada

    Returns:
        DataFrame: Tabela com os dados preenchidos pela requisição da API
    """
    url = "https://cep.awesomeapi.com.br/json/"

    emptyData: DataFrame = pd.DataFrame()

    for row in listaCep().itertuples():
        response = requests.get(f"{url}/{row.CEP}").json()

        response_df_json: DataFrame = pd.json_normalize(response)
        emptyData = pd.concat([emptyData, response_df_json], ignore_index=True)

    tabelaFinal: DataFrame = listaCep().merge(
        emptyData[emptyData.columns[1:]],
        how="left",
        left_on="CEP",
        right_on=emptyData["cep"],
    )
    return tabelaFinal


def saveTable():
    """
    Salva a tabela em formato CSV
    """
    return apiList().to_csv('output/data.csv', index=False, sep=',', encoding='utf-8-sig')