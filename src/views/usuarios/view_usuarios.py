import streamlit as st
from src.controller.controller_usuario import ControllerUsuario
import pandas as pd
# Status e Permissao
from src.models.usuario import Status, PermissaoEnum

st.title("Consulta de Usuários")
st.subheader("Pesquisa:")
nome = st.text_input("Nome do Usuário")


@st.cache_data
def carregar_dataframe():
    dataframe = ControllerUsuario.carregar_dataframe_usuarios()
    return dataframe
# Carrega o DataFrame
df_usuarios = carregar_dataframe()
st.dataframe(df_usuarios.reset_index(drop=True), use_container_width=True)

if nome:
    df_usuarios = df_usuarios[df_usuarios['Nome'].str.contains(nome, case=False, na=False)]

# Exibe o resultado
st.subheader("Resultados da Consulta:")
st.dataframe(df_usuarios, use_container_width=True)
# @st.dialog(title='Editar Usuário')
# def editar_usuario(dados_usuario):
#     st.text(f'Id: {dados_usuario['id']}')
#     novo_nome = st.text_input('Nome')
#     novo_login = st.text_input('Login')
#     nova_senha = st.text_input('Senha')

#     novo_status = st.selectbox('Status', list(Status), format_func=lambda x: x.value)
#     permissao = st.selectbox('Permissao', list(PermissaoEnum), format_func=lambda x: x.value)
#     atualizar_dados = st.button('Atualizar Dados')

#     if atualizar_dados:
#         atualizacao_usuario = ControllerUsuario.atualizar_usuario_pelo_id
@st.dialog(title='Criar Usuário')
def criar_usuario():
    nome = st.text_input('Nome')
    login = st.text_input('Login')
    senha = st.text_input('Senha')
    
    status = st.selectbox('Status', list(Status), format_func=lambda x: x.value) # format_func foi ChatGPT
    permissao = st.selectbox('Permissao', list(PermissaoEnum), format_func=lambda x: x.value)# format_func foi ChatGPt
    botao_cadastrar = st.button('Cadastrar Cliente', key='botao_cadastrar_usuario')
    if botao_cadastrar:
        usuario_salvo = ControllerUsuario.cadastrar_usuario(nome = nome , 
                                                            login = login, 
                                                            senha = senha, 
                                                            permissao = permissao.name, 
                                                            status = status.name)
        st.success('Usuário Cadastrado com Sucesso!')
if st.button("Novo Usuário"):
    criar_usuario()
        
