from App.database import db
import csv

class Word(db.Model):
    word_num = db.Column(db.Integer, primary_key = True)
    difficulty = db.Column(db.String, nullable = False)
    word = db.Column(db.String, nullable = False)


    def toDict(self):
        return{
            'word_num': self.word_num,
            'difficulty': self.difficulty,
            'word' : self.word

        }