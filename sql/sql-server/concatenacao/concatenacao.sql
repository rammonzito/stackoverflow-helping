/* ATUALIZANDO VARIAVEL VARCHAR COM VALORES EXISTENTES (SOMENTE PARA ILUSTRACAO) */
DECLARE @UNIDADE VARCHAR(100) = ''
SELECT @UNIDADE += @UNIDADE + ', ' FROM UNIDADES WHERE CODIGO_UNIDADE IN (/* Códigos informados*/)

SELECT @UNIDADE