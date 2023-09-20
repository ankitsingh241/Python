class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

ankitsApplication = RailwayForm()
ankitsApplication.name = "Ankit"
ankitsApplication.train = "Vande Bharat Express"
ankitsApplication.printData()

