class StudyService:
    def get_disciplines(self, user_id):
        return [
            {'id': 1, 'name': 'Matemática', 'color': '#3498db', 'presences': 10, 'total': 20},
            {'id': 2, 'name': 'Português', 'color': '#e74c3c', 'presences': 15, 'total': 20}
        ]

    def add_discipline(self, name, color, user_id):
        print(f"Salvando disciplina {name} para o usuario {user_id}")
        return True