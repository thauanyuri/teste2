import os
import zipfile

import wget
import tabula
import pandas as pd
from tabula.io import read_pdf

link1 = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN592.pdf'
nome_arquivo = 'Procedimento_ANEXO_I.pdf'
download_primeiro_arquivo = wget.download ( link1 , nome_arquivo )

tb = tabula.read_pdf ( download_primeiro_arquivo , pages='all' )
tb = tabula.convert_into ( 'Procedimento_ANEXO_I.pdf' , 'Procedimento_ANEXO_I.csv' , output_format='csv' , pages='all' )

dataframe = pd.read_csv ( "Procedimento_ANEXO_I.csv" )
dataframe.replace ( to_replace="OD" ,
                    value="Seg. Odontológica" ,
                    inplace=True )
dataframe.replace ( to_replace="AMB" ,
                    value="Seg. Ambulatorial" ,
                    inplace=True )
dataframe.to_csv ( 'Procedimento_ANEXO_I.csv' )

zip = zipfile.ZipFile ( 'Teste_Thauan_Yuri.zip' , 'w' , compression=zipfile.ZIP_DEFLATED )
zip.write ( 'Procedimento_ANEXO_I.csv' )