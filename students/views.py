from django.shortcuts import render
import random
def generate_students_data():
    names = ["ლევანი", "მიხეილი", "ლევანი", "რეზი", "sabaking69", "ტატო", "ნიკა", "ანდრია", "აჩი", "დიტო"]
    surnames = ["კობახიძე", "ზანგი", "ნიგერი", "კინგი", "ნარმანია", "თუ", "რაც", "არი", "69", "ვაი"]
    
    students = {
        f"Student {i+1}": {
            "name": random.choice(names),
            "surname": random.choice(surnames),
            "gpa": round(random.uniform(1.0, 4.0), 2),
            "course": random.randint(1, 4)
        }
        for i in range(100)
    }
    return students

def main_page_view(request):
    students_data = generate_students_data()
    students_count = len(students_data)
    return render(request, 'students/main_page.html', {'students_count': students_count})

def students_page_view(request):
    students_data = generate_students_data()
    return render(request, 'students/students_page.html', {'students': students_data})
