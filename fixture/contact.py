from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.fill_contact_form(contact)
        # submit form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill in contact form
        self.change_field("firstname", contact.name)
        self.change_field("middlename", contact.midname)
        self.change_field("lastname", contact.lastname)
        self.change_field("nickname", contact.nickname)
        self.change_field("title", contact.title)
        self.change_field("company", contact.company)
        self.change_field("address", contact.address)
        self.change_field("home", contact.home)
        self.change_field("mobile", contact.mobile)
        self.change_field("work", contact.work)
        self.change_field("fax", contact.fax)
        self.change_field("email", contact.email1)
        self.change_field("email2", contact.email2)
        self.change_field("email3", contact.email3)
        self.change_field("homepage", contact.homepage)
        self.select_combo("bday", contact.day)
        self.select_combo("bmonth", contact.month)
        self.change_field("byear", contact.year)
        self.select_combo("aday", contact.aday)
        self.select_combo("amonth", contact.amonth)
        self.change_field("ayear", contact.ayear)
        self.change_field("address2", contact.address2)
        self.change_field("phone2", contact.phone2)
        self.change_field("notes", contact.notes)

    def select_combo(self, combo_name, value):
        wd = self.app.wd
        if value is not None:
            select = Select(wd.find_element_by_name(combo_name))
            select.select_by_value(value)

    def change_field(self, attr_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(attr_name).click()
            wd.find_element_by_name(attr_name).clear()
            wd.find_element_by_name(attr_name).send_keys(text)

    def add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, Contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(Contact)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()

