from sales_person import SalesPerson
class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, 'r')
        lines = file.readlines()
        for line in lines:
            self.sales_people.append(line)

    def quota_report(self, quota):
        for i in self.sales_people:
            self.sales_people += [SalesPerson.get_id(), SalesPerson.get_name(),
                           SalesPerson.total_sales(), SalesPerson.met_quota(quota)]
        return self.sales_people

    def top_seller(self):
        for i in self.sales_people:
            self.sales_people.sort(key=i[2])
        return self.sales_people[0]

    def individual_sales(self, employer_id):
