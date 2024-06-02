#pip install chatterbot #for python 3.8 and older
import chatterbot
import random
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import time
import logging
print('Страп Андріана група 2 лаб 4')
def markov_chain(text):
    f = open(text, "r")
    words = f.read().split()
    markov_dict = {}
    for i in range(len(words) - 1):
        if words[i] not in markov_dict:
            markov_dict[words[i]] = []
        markov_dict[words[i]].append(words[i+1])
    return markov_dict

def generate_text(markov_dict, num_words):
    current_word = random.choice(list(markov_dict.keys()))
    result = [current_word]
    for i in range(num_words - 1):
        next_word = random.choice(markov_dict[current_word])
        result.append(next_word)
        current_word = next_word
    return ' '.join(result)

print('Генерація тексту: ', generate_text(markov_chain('melville-moby_dick.txt'), 18))

logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)
time.clock = time.time

bot = ChatBot('MyBot')
bot.storage.drop()
small_talk = [
    'Hello, how are you?',
    'I’m so so',
    'What is your favorite color?',
    'red',
    'What are you doing tonight?',
    'Drinking tea with friends',
    'What is your favorite movie?',
    'Bohemian Rhapsody',
    'What do you think about music?',
    'I love it',
    'What is your favorite sport?',
    'Volleyball',
    'What is your favorite season?',
    'Spring',
    'What is your favorite book genre?',
    'Detective stories',
    'What is your favorite TV show?',
    'I do not watch TV',
    'What are your plans for the weekend?',
    'Have fun and enjoy life'
]

# Тренуємо бота на фразах зі списку small_talk
trainer = ListTrainer(bot)
trainer.train(small_talk)
# Тренуємо бота на корпусі мовою за індивідуальним варіантом
# corpus_trainer = ChatterBotCorpusTrainer(bot)
# corpus_trainer.train("chatterbot.corpus.french")
while True:
    try:
        user_input = input('Ви: ')
        bot_response = bot.get_response(user_input)
        print('Бот:', bot_response)


    except KeyboardInterrupt:
        print('Bye')
        break

