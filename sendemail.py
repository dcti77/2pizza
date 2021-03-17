import smtplib

def sendmail(*args, **kwargs):
    smtpObj = smtplib.SMTP("smtp.mailgun.org", 587)
    smtpObj.login("postmaster@sandbox9f691658a7a34e5ea6478cc871c7befe.mailgun.org", "cbc9976c2438ef75edb53433e6f5b1bd-73e57fef-a08e34cb")

    msg = ""
    sendto_list = ["driversapp@outlook.com"]

    smtpObj.sendmail("postmaster@sandbox9f691658a7a34e5ea6478cc871c7befe.mailgun.org",sendto_list,msg)

    smtpObj.quit()






