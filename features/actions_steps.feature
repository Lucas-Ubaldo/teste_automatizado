Feature: Login no YouTube
  Scenario: Login bem-sucedido
    Given que estou na página de login do YouTube
    When eu insiro meu email "teste.automatizadoQS@gmail.com"
    And eu insiro minha senha "QS_123456789"
    And eu pesquiso por "corinthians"
    Then eu devo ver os resultados da pesquisa


  
