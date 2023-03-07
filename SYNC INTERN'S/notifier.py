#import the necessary module!
from plyer import notification

#specify the parameters
title = 'Heyy!'
message= 'Hope you have a fantastic day! Take care!'

notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 10,
                    toast=False)