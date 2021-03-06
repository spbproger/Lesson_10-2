import json

def candidates_info(json_='candidates.json'):
    """
    Загружает сведения о кандидатах в json-формате
    """
    with open(json_, 'r', encoding='utf-8') as f:
        return json.load(f)


def candidates_output(candidates_info_list):
    """
    Выводит сведения о кандидатах в формате: имя, позиция, навыки
    """
    candidates = '<pre>'
    for candidate in candidates_info_list:
        candidates += (f'Имя кандидата - {candidate["name"]}\n'
                       f'Позиция кандидата - {candidate["position"]}\n'
                       f'Навыки - {candidate["skills"]}\n\n')
    candidates += '</pre>'
    return candidates


def candidate_info_by_id(candidates_info_list, candidate_id):
    """
    Выводит сведения о кандидате по порядковому номеру (id) в списке
    """
    for candidate in candidates_info_list:
        if candidate['id'] == candidate_id:
            return candidate


def candidate_info_by_skills(candidates_info_list, skill):
    """
    Выводит сведения о кандидате по его навыкам
    """
    candidates = '<pre>'
    for candidate in candidates_info_list:
        if skill.lower() in candidate['skills'].lower():
            candidates += (f'Имя кандидата - {candidate["name"]}\n'
                           f'Позиция кандидата - {candidate["position"]}\n'
                           f'Навыки - {candidate["skills"]}\n\n')
    candidates += '</pre>'
    return candidates

