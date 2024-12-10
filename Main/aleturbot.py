import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import getpass
import os
import pandas as pd
from datetime import datetime

# Inicializa o contador de protocolo
protocolo_counter = 0

def create_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.row(InlineKeyboardButton("Suporte", url="https://wa.me/5548992104426"))
    keyboard.row(InlineKeyboardButton("Site", url="https://alexandreturismo.com.br"))
    keyboard.row(InlineKeyboardButton("Meu ID", callback_data="show_id"))
    return keyboard

def log_interaction(user_id, username, message_text, bot_response):
    global protocolo_counter
    protocolo_counter += 1
    
    log_entry = {
        "Protocolo": protocolo_counter,
        "Data e Hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Usuário": username,
        "ID": user_id,
        "Mensagem Recebida": message_text,
        "Resposta do Bot": bot_response
    }
    
    # Cria a pasta de log se não existir
    if not os.path.exists("log"):
        os.makedirs("log")
    
    # Cria ou atualiza o arquivo Excel
    log_file = "log/log.xlsx"
    if os.path.exists(log_file):
        df = pd.read_excel(log_file)
        new_row = pd.DataFrame([log_entry])  # Cria um DataFrame a partir do log_entry
        df = pd.concat([df, new_row], ignore_index=True)  # Usa concat para adicionar a nova linha
    else:
        df = pd.DataFrame([log_entry])
    
    df.to_excel(log_file, index=False)
    
    # Envia log para os IDs especificados
    log_message = f"""Nova Interação - Protocolo: {protocolo_counter}
📅 Data e Hora: {log_entry['Data e Hora']}
👤 Usuário: {log_entry['Usuário']}
🆔 ID: {log_entry['ID']}
📥 Mensagem Recebida: {log_entry['Mensagem Recebida']}
📤 Resposta do Bot: {log_entry['Resposta do Bot']}"""
    
    return log_message

def main():
    token = input("Digite o token do seu bot: ")
    username = input("Digite o nome de usuário: ")
    password = getpass.getpass("Digite a senha: ")

    if username != "admin" or password != "password":
        print("Credenciais inválidas. Encerrando o programa.")
        return

    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start', 'help'])
    @bot.message_handler(func=lambda message: True)
    def send_welcome(message):
        keyboard = create_keyboard()
        response = "Sou apenas um bot de comunicado da Alexandre, não tenho autorização para conversar com nenhum usuário. Qualquer dúvida, fale com nosso suporte, veja suas opções 💙"
        bot.reply_to(message, response, reply_markup=keyboard)
        
        log_message = log_interaction(message.from_user.id, message.from_user.username, message.text, response)
        for admin_id in [1312054516, 7320952120]:
            bot.send_message(admin_id, log_message)

    @bot.message_handler(commands=['suporte'])
    def handle_support(message):
        response = "Você pode entrar em contato com nosso suporte através do WhatsApp: https://wa.me/5548992104426"
        bot.reply_to(message, response)
        
        log_message = log_interaction(message.from_user.id, message.from_user.username, "/suporte", response)
        for admin_id in [1312054516, 7320952120]:
            bot.send_message(admin_id, log_message)

    @bot.message_handler(commands=['site'])
    def handle_site(message):
        response = "Visite nosso site: https://alexandreturismo.com.br"
        bot.reply_to(message, response)
        
        log_message = log_interaction(message.from_user.id, message.from_user.username, "/site", response)
        for admin_id in [1312054516, 7320952120]:
            bot.send_message(admin_id, log_message)

    @bot.message_handler(commands=['meuid'])
    def handle_meu_id(message):
        response = f"Seu ID é: {message.from_user.id}"
        bot.reply_to(message, response)
        
        log_message = log_interaction(message.from_user.id, message.from_user.username, "/meuid", response)
        for admin_id in [1312054516, 7320952120]:
            bot.send_message(admin_id, log_message)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        if call.data == "show_id":
            response = f"Seu ID é: {call.from_user.id}"
            bot.answer_callback_query(call.id, response, show_alert=True)
            
            # Pergunta ao usuário se deseja receber o ID no chat
            confirmation_keyboard = InlineKeyboardMarkup()
            confirmation_keyboard.row(
                InlineKeyboardButton("Sim", callback_data="confirm_id"),
                InlineKeyboardButton("Não", callback_data="cancel_id")
            )
            
            bot.send_message(call.from_user.id, "Você deseja receber seu ID no chat?", reply_markup=confirmation_keyboard)

            log_message = log_interaction(call.from_user.id, call.from_user.username, "Solicitou ID", response)
            for admin_id in [1312054516, 7320952120]:
                bot.send_message(admin_id, log_message)

        elif call.data == "confirm_id":
            response = f"Seu ID é: {call.from_user.id}"
            bot.send_message(call.from_user.id, response)

        elif call.data == "cancel_id":
            bot.send_message(call.from_user.id, "Você optou por não receber seu ID no chat.")

    print("Bot está rodando...")
    bot.polling()

if __name__ == "__main__":
    main()
