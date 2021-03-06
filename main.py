from flask import Flask
from utils import candidates_info, candidates_output, candidate_info_by_id, candidate_info_by_skills


app = Flask(__name__)

# Опишем декораторы


@app.route("/")     # Основная страница
def main():
    candidates_info_list = candidates_info()
    return candidates_output(candidates_info_list)


@app.route("/candidates/<int:candidate_id>/")       # Страница со сведениями о кандидате
def candidates(candidate_id):
    candidates_info_list = candidates_info()
    candidate = candidate_info_by_id(candidates_info_list, candidate_id)
    scrn = f'<img src="{candidate["picture"]}">'
    candidate_info = scrn + candidates_output([candidate])
    return candidate_info



@app.route("/skills/<skill>/")      # Страница со сведениями о навыках андидатов
def skills(skill):
    candidates_info_list = candidates_info()
    candidate = candidate_info_by_skills(candidates_info_list, skill)
    return candidate

#Теперь стартуем сервер, чтобы обрабатывать запросы от пользователей

app.run(host='127.0.0.2', port=80)