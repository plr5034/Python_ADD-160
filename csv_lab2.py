'''
csv lab2
Name: Paul Ring 
github link: https://github.com/plr5034/Python_ADD-160/blob/main/csv_lab2.py

Create an application that will read a CSV file containing exam results and 
generate a report.  This will be done with two clases:
1. ExamReader: This class will read the CSV file and store the results in a
   nested dictionary.  Input exam_results.csv
2. ExamReporter: This class will take the nested dictionary from the 
ExamResults class and generate a csv report.  This report will be summarizing
the results of exams in maths, physics and biology. The report should include
the name of the exam, the number of candidates, the number of passed exams,
the number of failed exams, and the best and the worst scores. All the data
necessary to create the report is in the exam_report.csv file.

Note that one candidate may have several results for the same exam. The number
of candidates should express the number of unique people in each exam
identified by Candidate ID. The final report should look like this:

Exam Name,Number of Candidates,Number of Passed Exams,Number of Failed Exams,
Best Score,Worst Score

Maths,8,4,6,90,33
Physics,3,0,3,66,50
Biology,5,2,3,88,23

'''
import csv

class ExamReader:
    '''
    Class to read exam results from a CSV file and store them in a nested dictionary.
    '''
    def __init__(self, filename):
        self.filename = filename
        self.results = {
            'Maths': {
                'candidates': set(),
                'passed': 0,
                'failed': 0,
                'best_score': float('-inf'),
                'worst_score': float('inf')
            },
            'Physics': {
                'candidates': set(),
                'passed': 0,
                'failed': 0,
                'best_score': float('-inf'),
                'worst_score': float('inf')
            },
            'Biology': {
                'candidates': set(),
                'passed': 0,
                'failed': 0,
                'best_score': float('-inf'),
                'worst_score': float('inf')
            }
        }
 
    def read_results(self):
        ''' 
        Read the exam results from the CSV file and populate the results dictionary.
        The CSV file should have the following columns: Name, ID, Score.
        
        args:
            None
        returns:
            results (dict): A nested dictionary containing the exam results.
        '''

        with open(self.filename, encoding='utf-8', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                exam_name = row['Name']
                candidate_id = row['ID']
                score = int(row['Score'])
                grade = row['Grade']
                
                # Add candidate ID to the set of candidates for the exam
                self.results[exam_name]['candidates'].add(candidate_id)
                
                # Update passed and failed counts
                if grade == "Pass":
                    self.results[exam_name]['passed'] += 1
                else:
                    self.results[exam_name]['failed'] += 1
                
                # Update best and worst scores
                if score > self.results[exam_name]['best_score']:
                    self.results[exam_name]['best_score'] = score
                if score < self.results[exam_name]['worst_score']:
                    self.results[exam_name]['worst_score'] = score
        # Convert the set of candidates to its length
        for exam in self.results:
            self.results[exam]['candidates'] = len(self.results[exam]['candidates'])
        return self.results
    
    def get_results(self):
        '''
        Return the results dictionary.

        args:
            None
        returns:
            results (dict): A nested dictionary containing the exam results.
        '''
        return self.results

class ExamReporter:
    '''
    Class to generate a CSV report from the exam results.

    args:
        results (dict): A nested dictionary containing the exam results.
    returns:
        A CSV file named 'exam_report.csv' summarizing the results.
    '''
    def __init__(self, results, output_filename):
        self.results = results
        self.output_filename = output_filename
        self.fieldnames = ['Exam Name', 'Number of Candidates', 'Number of Passed Exams', 
                           'Number of Failed Exams', 'Best Score', 'Worst Score']
    def generate_report(self):
        '''
        Generate a CSV report from the exam results.
        The report includes the name of the exam, the number of candidates,
        the number of passed exams, the number of failed exams, and the best
        and worst scores.
        args:
            None
        returns:
            None
        '''
        with open(self.output_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()
            for exam_name, data in self.results.items():
                writer.writerow({
                    'Exam Name': exam_name,
                    'Number of Candidates': data['candidates'],
                    'Number of Passed Exams': data['passed'],
                    'Number of Failed Exams': data['failed'],
                    'Best Score': data['best_score'],
                    'Worst Score': data['worst_score']
                })
        
if __name__ == "__main__":
    # Define the input CSV file
    input_csv_file = 'exam_results.csv'
    # Define the output CSV file
    output_csv_file = 'exam_report.csv'
    
    # Create an instance of ExamReader and read the results
    exam_reader = ExamReader(input_csv_file)
    exam_results = exam_reader.read_results()
    
    # Create an instance of ExamReporter and generate the report
    exam_reporter = ExamReporter(exam_results, output_csv_file)
    exam_reporter.generate_report()
    # While the report is creating the csv file, print the results to the console
    print()
    print(f"Report generated: {exam_reporter.output_filename}")
    print()
    print("Exam Results:")
    for my_exam_name, data in exam_results.items():
        print(f"{my_exam_name}: {data}")
