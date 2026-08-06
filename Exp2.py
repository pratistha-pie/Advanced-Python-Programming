# Advanced Class Concepts - Report Generator
def decorate_report(func):
    def wrapper(self):
        print("=" * 40)
        print("        REPORT")
        print("=" * 40)
        func(self)
        print("=" * 40)
    return wrapper

class Report:
    report_count = 0

    def __init__(self, title, content):
        self.title = title
        self.content = content
        Report.report_count += 1

    @classmethod
    def total_reports(cls):
        print("Total Reports Created:", cls.report_count)

    @decorate_report
    def display(self):
        print("Title   :", self.title)
        print("Content :", self.content)

    def __str__(self):
        return f"Report Title: {self.title}"

r1 = Report("Student Report", "Python Practical Completed")
r2 = Report("Library Report", "Books Issued Successfully")

r1.display()
r2.display()
print(r1)
Report.total_reports()