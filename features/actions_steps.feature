Feature: Acoes no YouTube
  Scenario: Acoes bem-sucedidas
    Given que estou na página de login do YouTube
    When eu insiro meu email "lzzk1910@gmail.com"
    And eu insiro minha senha "corinthianszl07"
    And eu pesquiso por "corinthians"
    When eu clico e reproduzo o primeiro vídeo
    When eu clico no botão de Inscrever-se
    When eu clico no botão de Gostei
    When eu clico no botão de Salvar em "Assistir mais tarde"
    Then eu devo ver o vídeo sendo reproduzido
    And o vídeo deve ser salvo em "Assistir mais tarde"

  Scenario: Clicar no botão de upload de vídeo
    Given que estou na página de login do YouTube
    When eu insiro meu email "lzzk1910@gmail.com"
    And eu insiro minha senha "corinthianszl07"
    And eu clico no botão de upload de vídeo 
    When eu escolho o vídeo "C:\Users\LUCAS UBALDO\Documents\teste-automatizado\video\teste.mp4" para enviar
    And eu insiro o título do vídeo "Teste automatizado"
    When eu clico no botão de próximo
    When eu clico no botão de publicar
    When eu sou redirecionado para a página de upload após a publicação