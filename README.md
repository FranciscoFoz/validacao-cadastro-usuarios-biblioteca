# Validação do cadastro de usuários da biblioteca

Neste repositório você encontrará as informações do meu projeto que elaborei para reforçar os conhecimentos do curso da Alura, [Python Brasil: validação de dados no padrão nacional](https://www.alura.com.br/curso-online-python-validacao-dados). 

O objetivo desse projeto foi validar os dados de cadastro do número de celular de uma biblioteca, para que se possa manter a qualidade do cadastro e relacionamento com os usuários da biblioteca.



| :placard: Vitrine.Dev |     |
| -------------  | --- |
| :sparkles: Nome        | **Validação do cadastro de usuários da biblioteca**
| :label: Tecnologias | python
| :rocket: URL         | https://github.com/FranciscoFoz/validacao-cadastro-usuarios-biblioteca
| :fire: Desafio     | 

<!-- Inserir imagem com a #vitrinedev ao final do link -->
![](https://images.unsplash.com/photo-1564981797816-1043664bf78d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80#vitrinedev)

photo by [Drahomír Posteby-Mach](https://unsplash.com/@postebymach) on [Unsplash](https://unsplash.com/)


Elaborado por Francico Foz

<a href="https://img.shields.io/badge/author-gustavolq-blue.svg)](https://www.linkedin.com/in/francisco-tadeu-foz/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>  

---

Olá! 

Neste repositório você encontrará o projeto do meu [artigo](https://franciscofoz.medium.com/validando-dados-de-usu%C3%A1rios-da-biblioteca-com-regex-no-python-792c19c1715f) 


## Resumo
Uma biblioteca universitária, no Brasil, está validando os dados do cadastro de seus usuários, para que possam entrar em contato.
O e-mail é a comunicação ideal para entrar em contato, por isso já foi feita a validação. Entretanto nem todos os usuários possuem no cadastro um e-mail válido e a segunda opção seria o número de celular.
Mas o número de celular não é validado inteiramente no formulário da página web do cadastro e números repetidos ou incorretos podem aparecer. 

Quais são os usuários da biblioteca que não possuem um número de celular válido?
Com essas informações a equipe da direção da biblioteca poderá montar um plano de ação para de alguma forma corrigir o cadastro.

Também está disponível a tabela destes usuários no banco de dados da matrícula da universidade e do cadastro inicial do comercial. Para verificar se não estão corretos nestes outros.

### Dataset

Os conjuntos de dados são fictícios e criados por mim. 

Você poderá acessar os dados utilizados nesta análise [aqui](https://github.com/FranciscoFoz/validacao-cadastro-usuarios-biblioteca/blob/main/Notebook/Validacao_cadastro_usuario_biblioteca.ipynb) no [Kaggle](https://www.kaggle.com/datasets/franciscotadeufoz/validacao-cadastro-usuarios-biblioteca).


### Desenvolvimento do projeto

Desenvolvi uma classe que pudesse validar os números de celular com Regex e me retornar o número formatado ou se ele era inválido.

Dentre os números inválidos, verifiquei nas demais tabelas (matrícula e comercial) quais estariam corretos. 
Desta forma obtive uma lista de 22 números inválidos para que possam montar um plano de ação de correção.

Você pode conferir o projeto completo no notebook do repositório.

## Considerações finais

A validação de dados é uma forma de se garantir a sua acuracidade.
O ideal é que ela seja realizada no "input" (entrada) dos dados, entretanto nem sempre é a realidade e é necessário realizar uma validação nos dados já preenchidos.
