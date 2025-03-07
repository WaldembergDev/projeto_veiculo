from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.database.db import Base

class Avaria(Base):
    __tablename__ ="avarias"

    id = Column(Integer, primary_key=True)

    agua_para_brisa = Column(Boolean, nullable=False)
    adesivos = Column(Boolean, nullable=False)
    alto_falante_saida_de_som = Column(Boolean, nullable=False)
    arranhados = Column(Boolean, nullable=False)
    bancos_encostos_assentos = Column(Boolean, nullable=False)
    buzina = Column(Boolean, nullable=False)
    chave_de_roda = Column(Boolean, nullable=False)
    cintos_de_seguranca = Column(Boolean, nullable=False)
    documentos_de_carro = Column(Boolean, nullable=False)
    farol_alto = Column(Boolean, nullable=False)
    farol_baixo = Column(Boolean, nullable=False)
    fechamento_das_janelas = Column(Boolean, nullable=False)
    lanternas_frente_e_traseira = Column(Boolean, nullable=False)
    lataria_amassados = Column(Boolean, nullable=False)
    limpador_para_brisa = Column(Boolean, nullable=False)
    limpador_para_brisa_traseiro = Column(Boolean, nullable=False)
    luz_da_placa_licenca = Column(Boolean, nullable=False)
    luz_de_freio = Column(Boolean, nullable=False)
    luz_de_re = Column(Boolean, nullable=False)
    luz_interna = Column(Boolean, nullable=False)
    luzes_painel = Column(Boolean, nullable=False)
    macaco = Column(Boolean, nullable=False)
    nivel_da_agua_radiador = Column(Boolean, nullable=False)
    oleo_do_freio = Column(Boolean, nullable=False)
    oleo_do_motor = Column(Boolean, nullable=False)
    para_brisa = Column(Boolean, nullable=False)
    para_choque_dianteiro = Column(Boolean, nullable=False)
    para_choque_traseiro = Column(Boolean, nullable=False)
    pisca_alerta = Column(Boolean, nullable=False)
    pneu_estado_assentos = Column(Boolean, nullable=False)
    pneu_reserva_estepe = Column(Boolean, nullable=False)
    portas_travas = Column(Boolean, nullable=False)
    quebra_sol = Column(Boolean, nullable=False)
    retrovisores_externos = Column(Boolean, nullable=False)
    retrovisores_internos = Column(Boolean, nullable=False)
    seta_direita_e_esquerda = Column(Boolean, nullable=False)
    tapete = Column(Boolean, nullable=False)
    triangulo_de_sinalizacao = Column(Boolean, nullable=False)
    velocimetro_tacografo = Column(Boolean, nullable=False)