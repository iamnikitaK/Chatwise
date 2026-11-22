import re
import pandas as pd


def preprocess(data):
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s*\d{1,2}:\d{2}\s*[AP]M\s*-\s*'

    messages=re.split(pattern,data)
    messages=[msg.strip() for msg in messages if msg.strip()]

    dates=re.findall(pattern, data)
    dates=[date.replace('\u202f',' ') for date in dates]
    dates=[date.replace(' - ','').replace('\u202f',' ').strip() for date in dates]

    df = pd.DataFrame({
        'user_message': messages,
        'message_date': dates
    })

    df['message_date']=pd.to_datetime(df['message_date'],format='%m/%d/%y, %I:%M %p');

    # Rename column
    df.rename(columns={'message_date': 'date'}, inplace=True);

    users=[];
    cleaned_message=[];
    for message in df['user_message']:
        entry=re.split('([\w\W]+?):\s',message);
        if entry[1:]:
            users.append(entry[1]);
            cleaned_message.append(entry[2]);
        else:
           users.append('group_notification');
           cleaned_message.append(entry[0]);

    df['user'] = users;
    df['message'] = cleaned_message;
    df.drop(columns=['user_message'], inplace=True)

    df['year'] = df['date'].dt.year;
    df['month'] = df['date'].dt.month_name();
    df['day'] = df['date'].dt.day;
    df['hour'] = df['date'].dt.hour;
    df['minute'] = df['date'].dt.minute;

    return df;
