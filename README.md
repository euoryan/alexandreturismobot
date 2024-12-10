# Bot de Atendimento

## Sobre o Projeto

Este bot foi criado para auxiliar os passageiros da Alexandre Turismo, oferecendo um atendimento automatizado e prático, com direcionamento para canais de suporte e acesso a informações básicas.

## Funcionalidades

- **Direcionamento ao Suporte**: Links rápidos para WhatsApp e site oficial.
- **Consulta de ID**: Permite que os usuários vejam seu ID do Telegram.
- **Registro de Interações**: Salva logs em Excel com dados das interações para controle e auditoria.
- **Notificações para Administradores**: Envia detalhes das interações diretamente aos administradores.

## Configuração

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/
   cd <diretório>
   ```

2. **Configure o token do bot**:
   Solicite o token ao [@BotFather](https://t.me/BotFather) e insira-o ao iniciar o programa.

3. **Credenciais de Acesso**:
   Utilize o nome de usuário `admin` e senha `password` para acessar.

4. **Diretório de Logs**:
   Certifique-se de que a pasta `log` existe no diretório do projeto para armazenar os registros.

## Como Usar

1. Execute o bot:
   ```bash
   python aleturbot.py
   ```

2. Comandos disponíveis:
   - `/start` ou `/help`: Exibe as opções do bot.
   - `/suporte`: Link para o WhatsApp do suporte.
   - `/site`: Acesso ao site oficial.
   - `/meuid`: Exibe o ID do usuário no Telegram.

3. Botões interativos:
   - **Suporte**: Abre o WhatsApp.
   - **Site**: Redireciona ao site oficial.
   - **Meu ID**: Mostra o ID do Telegram.

## Logs de Interações

Os registros são armazenados em um arquivo Excel (`log/log.xlsx`) com os seguintes campos:
- **Protocolo**: Número sequencial único para cada interação.
- **Data e Hora**: Registro do momento da interação.
- **Usuário**: Nome de usuário do Telegram.
- **ID**: ID do usuário no Telegram.
- **Mensagem Recebida** e **Resposta do Bot**: Conteúdo das interações.

<br/>

<div align="center">

Feito com ☕ e código por Ryan ;) Se gostou, deixa uma estrela pra ajudar! ⭐

</div>