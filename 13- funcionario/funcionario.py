class Funcionario:
    def __init__(self, nome, sal):
        self.nome = nome
        self.salario = sal
    '''
    @property
    def sal(self):
        return self.salario

    @sal.setter
    def sal(self, sal):
        if self.sal != string:
            self._sal = sal
        else:
            return 'erro'
    '''
    def retorna_nome(self):
        return self.nome

    def retorna_salario(self):
        return self.salario

    def aumentar_salario(self, percent):
        percent = ((100 + percent) /100) * self.retorna_salario()
        return percent
        
