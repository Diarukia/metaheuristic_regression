from regression_framework.admins.base_admin import Base_admin

class Logistic_admin(Base_admin):
    def __init__(self,alpha,beta,models):
        super().__init__(alpha,beta,models)

    def run_admin(self):
        for i in range(2):
            self.models[0].run_model(self.beta)
            if(i % self.alpha == 0):
                self.execute_regression()


    def execute_regression(self):
        pass
        