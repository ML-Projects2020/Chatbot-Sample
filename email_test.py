import smtplib as sl
print(sl)
server = sl.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
print("6")
server.login('titustraining4@gmail.com','angularjs')
print("7")
server.sendmail('titustraining4@gmail.com',['tituskrupamon@gmail.com',"kjasmine@stratapps.com","tm185173@ncr.com"],'data')