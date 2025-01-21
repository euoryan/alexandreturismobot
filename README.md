# Alexandre Turismo Bot

Este é um bot de atendimento automatizado criado para auxiliar os passageiros da Alexandre Turismo. Ele foi desenvolvido para oferecer um direcionamento rápido para os canais de suporte e fornecer informações básicas sobre a empresa de maneira eficiente.

## Sobre o Projeto
O bot foi criado para simplificar o processo de atendimento aos passageiros, oferecendo links rápidos para o suporte via WhatsApp, consulta do ID do usuário e registro das interações para controle e auditoria.

## Funcionalidades
- **Direcionamento ao Suporte**: Links rápidos para WhatsApp e site oficial.
- **Consulta de ID**: Permite que os usuários vejam seu ID do Telegram.
- **Registro de Interações**: Salva logs em Excel com dados das interações para controle e auditoria.
- **Notificações para Administradores**: Envia detalhes das interações diretamente aos administradores.

## Tecnologias
- Python (100%)

## Como Usar
1. Clone o repositório:
   ```bash
   git clone https://github.com/euoryan/alexandreturismobot
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd alexandreturismobot
   ```
3. Configure o token do bot: Solicite o token ao @BotFather e insira-o ao iniciar o programa.
4. Utilize o nome de usuário **admin** e a senha **password** para acessar.
5. Certifique-se de que a pasta `log` exista no diretório para armazenar os registros.

### Executando o Bot
Execute o bot com o comando:
   ```bash
   python aleturbot.py
   ```

## Comandos Disponíveis
- `/start` ou `/help`: Exibe as opções do bot.
- `/suporte`: Link para o WhatsApp do suporte.
- `/site`: Acesso ao site oficial.
- `/meuid`: Exibe o ID do usuário no Telegram.

## Botões Interativos
- **Suporte**: Abre o WhatsApp.
- **Site**: Redireciona ao site oficial.
- **Meu ID**: Mostra o ID do Telegram.

## Logs de Interações
Os registros são armazenados em um arquivo Excel (`log/log.xlsx`) com os seguintes campos:
- **Protocolo**: Número sequencial único para cada interação.
- **Data e Hora**: Registro do momento da interação.
- **Usuário**: Nome de usuário do Telegram.
- **ID**: ID do usuário no Telegram.
- **Mensagem Recebida e Resposta do Bot**: Conteúdo das interações.

<br/>

<div align="center">
Feito com ☕ e código por Ryan ;) Se gostou, deixa uma estrela pra ajudar! ⭐
</div>
