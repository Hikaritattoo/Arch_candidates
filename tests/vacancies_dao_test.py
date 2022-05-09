from app.vacancies.dao.vacancies_dao import VacancyDAO
import pytest

# Задаем, какие ключи ожидаем получать в вакансии
keys_should_be = {'pk', 'company', 'position', 'salary'}


# Готовим фикстуру, которая даст нам экземпляр DAO
@pytest.fixture()
def vacancies_dao():
    vacancies_dao_instance = VacancyDAO('./data/vacancies.json')
    return vacancies_dao_instance


# Начинаем писать тесты


class TestVacancyDAO:

    def test_get_all(self, vacancies_dao):
        """ Проверяем получение всех вакансий"""
        vacancies = vacancies_dao.get_all()
        assert type(vacancies) == list, 'возвращается не список'
        assert len(vacancies) > 0, 'возвращается пустой список'
        assert set(vacancies[0].keys()) == keys_should_be, 'неверный список ключей'

    def test_get_by_pk(self, vacancies_dao):
        """ Проверяем получение одной вакансии"""
        vacancy = vacancies_dao.get_by_pk(1)
        assert type(vacancy) == dict
        assert (vacancy['pk'] == 1), 'возвращается неправильная вакансия'
        assert set(vacancy.keys()) == keys_should_be, 'неверный список ключей'
