from flask import Flask

FAI=Flask(__name__)

@FAI.route('/stringresponse')

def stringresponse():
    return 'HAI THIS IS THE FIRST VIEW OF FLASK PROJECT'



@FAI.route('/secondstringresponse')
def secondstringresponse():
    return 'HELLO THIS SECOND VIEW OF THIS PROJECT'

if __name__=='__main__':
    
    FAI.run(debug=True)