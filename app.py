#obft edfk dkvm clrk

import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

sender_email = "a.r.devs2021@gmail.com"
sender_password = "obft edfk dkvm clrk" 

receiver_emails = ["kumarakash95075@gmail.com", "mr.prathvirajchavan.com"]


tasks_data = [
    {"task": "Study Data Science", "duration": 120},
    {"task": "Work on Power BI project", "duration": 90},
    {"task": "Revise UML diagrams", "duration": 60},
    {"task": "Review Operating Systems", "duration": 150},
    {"task": "Practice Hindi writing", "duration": 45}
]


def assign_task():
    assigned_task = random.choice(tasks_data)
    
    deadline = "2024-10-10"
    assigned_task['deadline'] = deadline
    return assigned_task

def send_email(subject, body, receivers):
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(receivers) 
    msg['Subject'] = subject

    
    msg.attach(MIMEText(body, 'plain'))

   
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Use TLS
    server.login(sender_email, sender_password)

    text = msg.as_string()
    server.sendmail(sender_email, receivers, text)
    server.quit()

    print(f"Email sent to {', '.join(receivers)}!")


def send_task_notification():
    task = assign_task()
    subject = f"Task Reminder: {task['task']}"
    body = f"You have a new task assigned:\n\nTask: {task['task']}\nDuration: {task['duration']} minutes\nDeadline: {task['deadline']}"
    send_email(subject, body, receiver_emails)


schedule.every().day.at("04:00").do(send_task_notification)  # 4 AM
schedule.every().day.at("05:00").do(send_task_notification)  # 5 AM
schedule.every().day.at("06:00").do(send_task_notification)  # 6 AM
schedule.every().day.at("18:00").do(send_task_notification)  # 6 PM
schedule.every().day.at("19:00").do(send_task_notification)  # 7 PM
schedule.every().day.at("22:00").do(send_task_notification)  # 10 PM
schedule.every().day.at("23:00").do(send_task_notification)  # 11 PM


if __name__ == "__main__":
    print("Scheduler started...")

    while True:
        schedule.run_pending()  # Check for scheduled tasks
        time.sleep(60)  # Wait 1 minute before checking again
