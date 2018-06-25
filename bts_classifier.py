from sklearn.naive_bayes import GaussianNB
import pickle

def word_count(text):
    keywords = ["ปกติ", "ได้รับการแก้ไข", "นำออกจากระบบให้บริการ", "เคลื่อนที่ได้แล้ว", "สรุป",
        "ใช้งานได้แล้ว", "มีความล่าช้า", "ส่งผลกระทบ", "ความเร็วต่ำ",
        "เกิดเหตุ", "ขัดข้อง", "จะล่าช้า", "แก้ไข", "เผื่อเวลา", "ช่วยเหลือ"]
    return [text.count(keyword) for keyword in keywords]

def classify(text):
    labels = [None, 'normal', 'delay', 'disrupted']
    x = [word_count(text)]
    clf = pickle.load(open('model.pkl', 'rb'))	
    return labels[clf.predict(x)[0]]