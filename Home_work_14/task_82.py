# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

from user_module import User, Project, LevelError, AccessError
import pytest

@pytest.fixture
def project():
    return Project("user_data.json", access_level=2)

def test_successful_enter_system(project):
    assert project.enter_system("alex", "123") == 0

def test_access_denied_enter_system(project):
    with pytest.raises(AccessError):
        project.enter_system("Unknown User", "user456")

def test_add_user_with_valid_access_level(project):
    new_user = User("Alice", "user789", 2)
    project.add_user(new_user)
    assert new_user in project.users

def test_add_user_with_insufficient_access_level(project):
    user_with_low_access = User("Bob", "user999", 1)
    with pytest.raises(LevelError):
        project.add_user(user_with_low_access)

def test_add_existing_user(project):
    existing_user = next(iter(project.users))
    with pytest.raises(LevelError):
        project.add_user(existing_user)

def test_read_users_from_json(project):
    assert len(project.users) == 12  # Зависит от содержимого вашего JSON-файла

def test_users_equality_by_id():
    user1 = User("Alice", "user123", 1)
    user2 = User("Bob", "user123", 2)
    assert user1 == user2



