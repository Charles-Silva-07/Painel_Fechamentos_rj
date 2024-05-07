import pandas as pd
import streamlit as st
import pyodbc


@st.cache_data
def load_data(ano=2024, semana=18):
    # Substitua com os detalhes da sua conexão com o SQL Server
    server = '192.168.10.10'
    database = 'BI'
    username = 'web_solutions'
    password = '32s48#41dF24ss87'

    # String de conexão
    conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    # Estabelece a conexão
    connection = pyodbc.connect(conn_str)

    # Substitua esta parte com sua consulta SQL, usando os parâmetros ano e semana conforme necessário
    query = f"""
        SELECT
            REPLACE(CAST({ano} AS VARCHAR), ',', '') AS ano,
            {semana} AS semana,
            d.pc_secao_descr_,            
            d.pc_grupo_descr_,
            d.pc_descricao,
            REPLACE(CAST(c.pr_codigo AS VARCHAR), ',', '') AS pr_codigo,
            c.pr_descricao, 
            CONVERT(DECIMAL(10,1), SUM(b.vi_qtd)) AS qnt_vendida,
            CONVERT(DECIMAL(15,2), SUM(b.vi_qtd * b.vi_valorunit)) AS valor, 
            COUNT(pos.conta_cli) AS pos,
            COUNT(cob.conta_cli_cob) AS cob
        FROM
            WiBiERP_CAR.dbo.t_vendas a
            LEFT JOIN WiBiERP_CAR.dbo.t_vendas_itens b ON a.vd_codigo = b.vd_codigo
            LEFT JOIN WiBiERP_CAR.dbo.t_produtos c ON b.pr_codigo = c.pr_codigo
            LEFT JOIN WiBiERP_CAR.dbo.t_produtos_class d ON c.pc_codigo = d.pc_codigo
            LEFT JOIN (
                SELECT COUNT(t.cl_codigo) AS conta_cli, u.pr_codigo
                FROM WiBiERP_CAR.dbo.t_vendas t, WiBiERP_CAR.dbo.t_vendas_itens u			
                WHERE t.vd_codigo = u.vd_codigo
                    AND t.vd_status <> 12
                    AND t.vd_bonif = 0
                    AND t.vd_data_venda IN (SELECT cal_data FROM WiBiERP_CAR.dbo.t_calendar WHERE cal_ano = 2024 AND cal_semana = 2)
                GROUP BY u.pr_codigo
            ) AS pos ON pos.pr_codigo = b.pr_codigo
            LEFT JOIN (
                SELECT COUNT(x.cl_codigo) AS conta_cli_cob, z.pr_codigo
                FROM WiBiERP_CAR.dbo.t_vendas x, WiBiERP_CAR.dbo.t_vendas_itens z
                WHERE x.vd_codigo = z.vd_codigo
                    AND x.vd_status <> 12
                    AND x.vd_bonif = 0
                    AND x.vd_data_venda BETWEEN
                        (SELECT MAX(cal_data) - 28 FROM WiBiERP_CAR.dbo.t_calendar WHERE cal_ano = 2024 AND cal_semana = 2) AND
                        (SELECT MAX(cal_data) FROM WiBiERP_CAR.dbo.t_calendar WHERE cal_ano = 2024 AND cal_semana = 2)
                GROUP BY z.pr_codigo
            ) AS cob ON cob.pr_codigo = b.pr_codigo
        WHERE
            a.vd_status <> 12
            AND a.vd_bonif = 0
            AND a.vd_data_venda IN (SELECT cal_data FROM WiBiERP_CAR.dbo.t_calendar WHERE cal_ano = {ano} AND cal_semana = {semana})
        GROUP BY
            d.pc_secao_descr_, d.pc_grupo_descr_, d.pc_descricao, c.pr_codigo, c.pr_descricao
        ORDER BY
            d.pc_secao_descr_, d.pc_grupo_descr_, c.pr_descricao;
    """

    # Carrega os dados em um DataFrame
    df_original = pd.read_sql_query(query, connection)

    # Fecha a conexão
    connection.close()

    return df_original

# Chama a função load_data
df = load_data()

# Imprime o DataFrame na tela
st.write(df)
