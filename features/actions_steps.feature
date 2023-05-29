Feature: Acoes no YouTube
  Scenario: Acoes bem-sucedidas
    Given que estou na página de login do YouTube
    When eu insiro meu email "teste.automatizadoQS@gmail.com"
    And eu insiro minha senha "QS_123456789"
    And eu pesquiso por "corinthians"
    When eu clico e reproduzo o primeiro vídeo
    Then eu devo ver o vídeo sendo reproduzido
    