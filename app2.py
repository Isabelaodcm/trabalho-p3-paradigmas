import streamlit as st
from consultor import SistemaConsultores

sistema = SistemaConsultores()

# Título do aplicativo
st.title("Plataforma de Consultoria On-line")
st.write('''**Especialistas em diversas áreas oferecem consultorias via uma plataforma online, que permite
aos clientes agendar sessões de videoconferência, acessar materiais de apoio, e avaliar os serviços
recebidos. O sistema gerencia os perfis dos consultores, disponibilidade de horários, e pagamentos.
Os clientes podem buscar especialistas com base em suas necessidades e classificações anteriores. **''')

menu = ["Cadastrar Consultor", "Listar Consultores", "Editar Perfil Consultor", "Excluir Perfil de Consultor", "Localizar Consultor pelo Código", "Buscar Consultor por Especialidade"]
escolha = st.sidebar.selectbox("Menu", menu)

if escolha == "Cadastrar Consultor":
    st.subheader("Cadastrar Consultor")
    with st.form(key='cadastrar_consultor'):
        nome = st.text_input("Nome do Consultor")
        especialidade = st.text_input("Área de Especialidade")
        pagamento = st.text_input("Preço por sessão")
        nota = st.text_input("Avaliação de 1 a 5")
        horario = st.text_input("Horário Disponível (manhã ou tarde)")
        submit_button = st.form_submit_button(label='Cadastrar')

        if submit_button:
            sistema.cadastrar_consultor(nome, especialidade, pagamento, nota, horario)
            st.success("Consultor cadastrado com sucesso")

elif escolha == "Listar Consultores":
    st.subheader("Lista de Consultores")
    consultores = sistema.listar_consultores()
    for consultor in consultores:
        st.write(consultor)

elif escolha == "Editar Perfil Consultor":
    st.subheader("Editar Perfil Consultor")
    codigo = st.number_input("Código do Consultor", min_value=1)
    consultor = sistema.localizar_pelo_codigo(codigo)
    if consultor:
        st.write(f"Dados atuais do Consultor:\n{consultor}")
        with st.form(key='editar_perfil'):
            nome = st.text_input("Nome", consultor.nome)
            profissao = st.text_input("Profissão", consultor.profissao)
            pagamento = st.text_input("Pagamento", consultor.pagamento)
            nota = st.text_input("Nota", consultor.nota)
            horario = st.text_input("Horário", consultor.horario)
            submit_button = st.form_submit_button(label='Atualizar')

            if submit_button:
                novos_valores = {"nome": nome, "profissao": profissao, "pagamento": pagamento, "nota": nota, "horario": horario}
                sistema.atualizar_profissional_por_codigo(codigo, novos_valores)
                st.success("Perfil atualizado com sucesso")
    else:
        st.error("Consultor não encontrado")

elif escolha == "Excluir Perfil de Consultor":
    st.subheader("Excluir Perfil de Consultor")
    codigo = st.number_input("Código do Consultor", min_value=1)
    if st.button("Excluir"):
        sistema.excluir_profissional_por_codigo(codigo)
        st.success("Consultor excluído com sucesso")

elif escolha == "Localizar Consultor pelo Código":
    st.subheader("Localizar Consultor pelo Código")
    codigo = st.number_input("Código do Consultor", min_value=1)
    if st.button("Localizar"):
        consultor = sistema.localizar_pelo_codigo(codigo)
        if consultor:
            st.write(consultor)
        else:
            st.error("Consultor não encontrado")

elif escolha == "Buscar Consultor por Especialidade":
    st.subheader("Buscar Consultor por Especialidade")
    especialidade = st.text_input("Especialidade")
    if st.button("Buscar"):
        consultores = sistema.buscar_profissional_por_profissao(especialidade)
        if consultores:
            for consultor in consultores:
                st.write(consultor)
        else:
            st.error("Nenhum consultor encontrado com essa especialidade")
        