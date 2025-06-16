from src.db.connection import SessionLocal
from src.models.ipca_model import IPCAModel

def save_ipca_data(data_list):
   db = SessionLocal()
   try:
      for i,item in enumerate(data_list):
         db_item = IPCAModel(
               valor=item.valor,
               unidade_da_federacao_codigo=item.unidade_da_federacao_codigo,
               unidade_da_federacao=item.unidade_da_federacao,
               periodo=item.periodo,
               tipo_de_projeto=item.tipo_de_projeto,
               padrao_de_acabamento=item.padrao_de_acabamento
            )
         db.add(db_item)
      db.commit()
   except Exception as e:
      db.rollback()
      print(f"Erro ao salvar dados: {e}")
   finally:
      db.close()
