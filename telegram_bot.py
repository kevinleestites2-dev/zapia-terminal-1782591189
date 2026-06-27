import telebot, subprocess, os, traceback

bot = telebot.TeleBot("8959195719:AAFODhpuArbIerPGKBcD5svoQ8fg3W2QDsc")

@bot.message_handler(func=lambda m: True)
def execute(m):
    cmd = m.text
    # Filter out common prefix junk if user pastes from tutorials
    if cmd.startswith("#"):
        cmd = "\n".join([line for line in cmd.split("\n") if not line.strip().startswith("#")])
    
    if not cmd.strip():
        bot.reply_to(m, "Empty command.")
        return

    try:
        # Run command and capture all output
        out = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        if not out.strip(): out = "(Command executed, no output)"
        
        # Try Markdown first, fallback to raw text if it fails (avoids 400 parse errors)
        try:
            bot.reply_to(m, f"```\n{out[:3900]}\n```", parse_mode='Markdown')
        except:
            bot.reply_to(m, out[:4000])
            
    except subprocess.CalledProcessError as e:
        err_msg = f"Error (Exit {e.returncode}):\n{e.output}"
        try:
            bot.reply_to(m, f"```\n{err_msg[:3900]}\n```", parse_mode='Markdown')
        except:
            bot.reply_to(m, err_msg[:4000])
    except Exception as e:
        bot.reply_to(m, f"System Error: {str(e)}")

bot.infinity_polling()
