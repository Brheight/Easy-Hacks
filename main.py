
saluted = ['Good Job!!', 'Awesome!!', 'Fantastic', 'Okay, Moving on', 'Lovely!!', 'Great!!', 'Amazing!!', 'Excellent!!',
'Good Job!!', 'Awesome!!', 'Fantastic', 'Okay, Moving on', 'Lovely!!', 'Great!!', 'Amazing!!', 'Excellent!!','Okay, Moving on', 'Lovely!!', 'Great!!', 'Amazing!!', 'Excellent!!']
task = ['Click the profile button to view available profiles','Click the notification button to view messages',
'Click the about button to view available learn about Easy Eacks',
'Click the contact button to send us a message','Click the settings button to view available profiles','Click the Exit button if you want to leave Easy Hacks']
#'Click the Data Refinery button'] , 'Click the Extractor Plus button ','Click the Image Reader button ', 'Click the Nomineogen button']
pos_x = [1]
pos_y = [.77, .545,.46,.39,.31,.23,.155, .77, .59, .44,.29,.14]
tool_btn = ['data_refine','extract_plus','neogen','img2txt']
options = ['profiles','notification', 'settings',  'help','about','contact']

mo_x = [.9,.9,.6,.5, .5,.2,.5,.2,.2,.2]
mo_y =  [.35,-35,-.47,-.47, -.4,-.4 -.4,-.4,-.47,-.47,-.47]
tp =  [0,0,0,0,0,0,0,0,0 ,1,1,1]
btm = [1,1,1,1,1,1,1,1, 1,1,1,1]


move_x =[.9,.5,.05,.05,.8, .8, .8,.8,.8]

move_y= [.35, .15,.25,.25,.25, .25,.25,.25,.25]
mov_x = [.6,.6,.6,.5, .5,.2,.5,.2,.2]
mov_y =  [-.47,-.47,-.47,-.47, -.4,-.4 -.4,-.4,-.47]
top =    [1,1,0,1,0,1,0,0,0 ]
bottom = [0,0,1,0,1,0,1,1, 1]


hos_x = [.9,.9,.6,.5, .5,.2,.5,.2,.2]
hos_y =  [.35,-35,-.47,-.47, -.4,-.4 -.4,-.4,-.47]

ho_x = [.9,.9,.6,.5, .5,.2,.5,.2,.2]
ho_y =  [.35,-35,-.47,-.47, -.4,-.4 -.4,-.4,-.47]

screen = []
capture = None
tools = ['Data Refinery','Nomineogen','Extractor Plus']
result_mode = False
image_names = []
resume_result = ''
fn_dir=None
contacts={}
time_stamped={}
name = ''
email = ''
MediaStore_Images_Media_DATA = "_data"
screen =[]
address = ''
file_uri='me'
link = ''
profile_picture = ''
phone = ''
stamped_item = None
msg=None
result_open= ''
use = ''
emass = {}
f = ''
from kivy.storage.jsonstore import JsonStore
store = JsonStore('rating.json')
#store.put('saved' ,name=msg)
if store.exists('rating'):
    rated = store.get('rating')['name']
    rating=rated
else:
    store.put('rating' ,name='not_rated')
    rating='not_rated'

contact_name = ''
created = ''
input_enter=''
back_home=False
capture =10
login_pref='offline'
licensecode = ['850B3605-C881-43AD-9C21-A944379098B3','856C7575-1724-46C3-8B7A-28248F1F45ED']
LicenseCode =licensecode[1]
username=['BENJAMINAD','BRHEIGHTADEWOLE']
current_tul=''
UserName =username[1]
month = {'01':'January', '02':'February', '03':'March','04':'April','05':'May','06':'June',
        '07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
import mobile_apps
quicklessons =mobile_apps.lessons
easyhacks_intro=mobile_apps.easyhacks_intro
#from kivy.properties import BooleanProperty,NumericProperty, StringProperty, 

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition    
#from kivy.uix.floatlayout import FloatLayout
from kivy.properties import BooleanProperty,NumericProperty, StringProperty,OptionProperty, ObjectProperty
from kivy.clock import Clock

#import asyncio
from kivy.lang import Builder
#Builder.load_file('preload.kv')

#def background():
from kivy.uix.image import Image
from kivy.uix.label import Label    
#from kivy.properties import OptionProperty, ObjectProperty
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.compat import string_types
from plyer import notification
import time

from kivy.properties import BooleanProperty,NumericProperty, StringProperty,OptionProperty, ObjectProperty
from  textfield import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.modalview import ModalView

from kivy.uix.button import Button, ButtonBehavior

from kivy.lang import Builder
from kivy.uix.treeview import TreeView, TreeViewLabel,TreeViewNode
from kivy.uix.carousel import Carousel
from kivy.animation import Animation

from kivy.uix.popup import Popup

from kivy.uix.rst import RstDocument
import neogenesis

from sys import argv
from kivy.factory import Factory
import os
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from functools import partial
import json
from kivy.core.window import Window
from kivy.uix.label import Label

from kivy.uix.tabbedpanel import TabbedPanel
#import shutil


Builder.load_file('EasyHacks.kv')
try:
    import requests
except ImportError:
    print("You need the requests library to be installed in order to use this sample.")
    print("Run 'pip install requests' to fix it.")




class TransBtn(Button):
    primary_color = [
        0.12941176470588237,
        0.5882352941176471,
        0.9529411764705882,
        1
    ]
    primary_color_=[0.9764705882352941, 0.1764705882352941, 0.1764705882352941, 1]


class Alert(Popup):
    def __init__(self, **kwargs):
        super(Alert, self).__init__(**kwargs)
        self.e =er
        msg_ = FloatLayout()
        document = RstDocument(text=self.e, pos_hint={'center_x':.5, 'center_y':.6}, size_hint=(.9,.6)) #, opacity=0)
        butn = TransBtn(text='Close', size_hint=(.8,.2), pos_hint={'center_y':.1, 'center_x':.5}, on_press=self.pop_close)
        msg_.add_widget(document)
        msg_.add_widget(butn)
        self.title='Alert!'
        self.content=msg_
        self.title_align='center'
        self.background='images/trans.png' #grey_shade.jpg'
        self.title_color=(0,0,0,1)
        self.size_hint=(.7,.3)
        self.auto_dismiss=False
        #self.open()
    def pop_close(self, instance):
        self.dismiss()

class QuitUs(Popup):
    def __init__(self, **kwargs):
        super(QuitUs, self).__init__(**kwargs)
        #self.e ='images/no_rated.png' #'images/not_rated.png'
        msg_ = FloatLayout()
        self.document = RstDocument(text='Do you want to close Easy Hacks?', pos_hint={'center_x':.5, 'top':.9}, size_hint=(1,.5)) #, opacity=0)
        
        
        abutn = TransBtn(text='No', size_hint=(.4,.2), pos_hint={'center_y':.1, 'center_x':.25}, on_press=self.dismiss)
        butn = TransBtn(text='Yes', size_hint=(.4,.2), pos_hint={'center_y':.1, 'center_x':.75}, on_release=self.submit)
        msg_.add_widget(self.document)
        
        msg_.add_widget(butn)
        msg_.add_widget(abutn)
        self.auto_dismiss=False
        self.title="Quit!!"
        #'images/rated_us.png'
        #rated_us_2.png
        #rated_us_1.png
        #rated_us_4.png
        #rated_us_3.png
        self.content=msg_
        self.title_align='center'
        self.background='images/trans.png'
        #self.title_color=(0,0,0,1)
        self.size_hint=(.7,.3)
        #self.open()
    
    def submit(self, instance):
        #store = JsonStore('rating.json')
        #global rating
        #store.put('rating' ,name=self.document.source)
        notification.notify(title='test', message='Closing Easy Hacks...')
        print(self.document.source,'source')
        #rating = self.document.source
        p.close()
        #self.dismiss()


class RateUs(Popup):
    def __init__(self, **kwargs):
        super(RateUs, self).__init__(**kwargs)
        self.e ='images/no_rated.png' #'images/not_rated.png'
        msg_ = FloatLayout()
        self.document = Image(source=self.e, pos_hint={'center_x':.5, 'top':.9}, size_hint=(1,.6)) #, opacity=0)
        first = restB(source='images/effect_empty.png', pos_hint={'center_x':.1, 'y':.43}, size_hint=(.2,.2), on_press=self.first)
        second = restB(source='images/effect_empty.png', pos_hint={'center_x':.3, 'y':.43}, size_hint=(.2,.2),on_press=self.second)
        third = restB(source='images/effect_empty.png', pos_hint={'center_x':.5, 'y':.43}, size_hint=(.2,.2),on_press=self.third) #, opam city=0)
        fourth = restB(source='images/effect_empty.png', pos_hint={'center_x':.7, 'y':.43}, size_hint=(.2,.2),on_press=self.fourth)
        fifth = restB(source='images/effect_empty.png', pos_hint={'center_x':.9, 'y':.43}, size_hint=(.2,.2),on_press=self.fifth)
        #butn = TransBtn(text='Close', size_hint=(.8,.2), pos_hint={'center_y':.1, 'center_x':.5}, on_press=self.pop_close)
        abutn = TransBtn(text='Submit', size_hint=(.4,.2), pos_hint={'center_y':.1, 'center_x':.25}, on_press=self.submit)
        butn = TransBtn(text='Cancel', size_hint=(.4,.2), pos_hint={'center_y':.1, 'center_x':.75}, on_press=self.pop_close)
        msg_.add_widget(self.document)
        msg_.add_widget(first)
        msg_.add_widget(second)
        msg_.add_widget(third)
        msg_.add_widget(fourth)
        msg_.add_widget(fifth)
        msg_.add_widget(butn)
        msg_.add_widget(abutn)
        self.auto_dismiss=False
        self.title="Let's know what you think!"
        #'images/rated_us.png'
        #rated_us_2.png
        #rated_us_1.png
        #rated_us_4.png
        #rated_us_3.png
        self.content=msg_
        self.title_align='center'
        self.background='images/grey_shade.jpg'
        self.title_color=(0,0,0,1)
        self.size_hint=(.7,.3)
        self.open()
    def first(self, instance):
        self.document.source='images/rated_us_1.png'
    def second(self, instance):
        self.document.source='images/rated_us_2.png'
    def third(self, instance):
        self.document.source='images/rated_us_3.png'
    def fourth(self, instance):
        self.document.source='images/rated_us_4.png'
    def fifth(self, instance):
        self.document.source='images/rated_us_5.png'
    def pop_close(self, instance):
        self.dismiss()
    def submit(self, instance):
        #store = JsonStore('rating.json')
        global rating
        store.put('rating' ,name=self.document.source)
        print(self.document.source,'source')
        rating = self.document.source
        self.dismiss()


class Tip(Popup):
    def __init__(self, **kwargs):
        super(Tip, self).__init__(**kwargs)
        self.e =er
        msg_ = FloatLayout()
        document = RstDocument(text=self.e, pos_hint={'center_x':.5, 'center_y':.6}, size_hint=(.9,.6)) #, opacity=0)
        butn = TransBtn(text='Close', size_hint=(.8,.2), pos_hint={'center_y':.1, 'center_x':.5}, on_press=self.pop_close)
        msg_.add_widget(document)
        msg_.add_widget(butn)
        self.title='Invalid items removed'
        self.content=msg_
        self.title_align='center'
        self.background='images/grey_shade.jpg'
        self.title_color=(0,0,0,1)
        self.size_hint=(.7,.3)
        self.auto_dismiss=False
        self.open()
    def pop_close(self, instance):
        self.dismiss()

me = '''Bright Adewole 
brightoadewole@gmail.com 
2a Salami Close, Off Kokumo Close, Iyana Ipaja, Lagos State
tabdevelopers.org
+23470366282414'''



class TreeViewButton(ButtonBehavior, TreeViewLabel):
    def __init__(self, **kwargs):
        super(TreeViewButton, self).__init__(**kwargs)
        #self.background_normal='images/effect_empty.png'
        #self.background_normal='images/effect_empty.png'
        self.background_down='images/contact_board.png'
class treed(FloatLayout):
    def __init__(self, **kwargs):
        super(treed, self).__init__(**kwargs)
        self.pos_hint={'center_x':.5,'top':.95}
        tv= self.ids['tv']
        eml = tv.add_node(TreeViewLabel(text='Email'))
        lnk = tv.add_node(TreeViewLabel(text='Link'))
        phon = tv.add_node(TreeViewLabel(text='Phone'))
        oth = tv.add_node(TreeViewLabel(text='Others'))
        for item in msg.split('\n'):
            if '@' in item:
                #e.append(item)
                tv.add_node(TreeViewButton(text='{}'.format(item), is_open=True,on_press=partial(self.emailing, item)),eml)
            elif 'http' in item or 'url' in item or '.com' in item or '.org' in item or '.net' in item:
                #l.append(item)
                tv.add_node(TreeViewButton(text='{}'.format(item),is_open=True, on_press=partial(self.linking, item)),lnk)
            elif len(item) >6:
                if item.isnumeric() or  '+' in item:
                    #p.append(item)
                    tv.add_node(TreeViewButton(text='{}'.format(item),is_open=True, on_press=partial(self.phoning, item)),phon)
            else:
                #o.append(item)
                tv.add_node(TreeViewLabel(text='{}'.format(item),is_open=True),oth)
    def emailing(self, instance,*args):
        try:
            from android.permissions import request_permissions, Permission, check_permission
            if check_permission('android.permission.WRITE_EXTERNAL_STORAGE'):
                if check_permission('android.permission.READ_EXTERNAL_STORAGE'):
                    if check_permission('android.permission.CAMERA'):
                        pass
            else:
                Clock.schedule_once(lambda dt:take_permission(),.2)
            from android.storage import app_storage_path
            settings_path = app_storage_path()
            self.fn = settings_path +    '/keys.txt'
            if os.path.exists(self.fn):
                f = open(self.fn, 'r')
            
                a = f.read()
            
                data = a.split('\n')
            for item in data:
                if 'email' in item:
                    mail = item.split('=')[1]
                    #print(emails,'email')
                if 'pass' in item:
                    passw = item.split('=')[1]
                    #print('passw', pass_key)
                    #print('user', user.text)
                if 'user' in item:
                    user = item.split('=')[1]
                    #print('passw', user_name)
                    #print('user', user.text)
                if 'first' in item:
                    first = item.split('=')[1]
                    #print('passw', first)
                    #print('user', user.text)
                if 'last' in item:
                    last = item.split('=')[1]
                    #print('passw', last)
                    #print('user', user.text)
            requests.put('https://easy-hacks-4eca2.firebaseio.com/users/{}/details.json'.format(mail),'{"name":"%s","last":"%s","pass":"%s","user":"%s","rating":"%s"}' %(first,last,passw,user, rating))
        except:
            pass
        global er
        try:
            if instance!='' and '@' in instance:
                from plyer import email
                recipient = instance
                subject = None
                text = None
                create_chooser = False
                email.send(recipient= recipient, subject= subject, text=text, create_chooser=create_chooser)
            else:
                er = 'Invalid Link'
                Alert().open()
        except Exception as e:
            
            er = str(e)
            Alert().open()
    def phoning(self, instance, *args):
        try:
            global er
            #from plyer import call
            #phone = self.ids['phone']
            #call.makecall(tel =phone.text)
            inst= ''.join(instance.split('+'))
            if inst.isnumeric():
                from android import activity, mActivity
                from jnius import autoclass, cast
                String = autoclass('java.lang.String')
                Intent = autoclass('android.content.Intent')
                Uri = autoclass('android.net.Uri')
                Environment=autoclass('android.os.Environment')
                intent = Intent()
                self.msg='tel:'+'{}'.format(instance)
                intent.setAction(Intent.ACTION_DIAL)
                intent.setData(Uri.parse(self.msg))
                
                mActivity.startActivityForResult(intent,0x123)
            else:
                er = "Invalid Contact"
                Alert().open()
        except Exception as e:
            er = str(e)
            
            Alert().open()

    def linking(self, instance, *args):
        try:
            from android.permissions import request_permissions, Permission, check_permission
            if check_permission('android.permission.WRITE_EXTERNAL_STORAGE'):
                if check_permission('android.permission.READ_EXTERNAL_STORAGE'):
                    if check_permission('android.permission.CAMERA'):
                        pass
            else:
                Clock.schedule_once(lambda dt:take_permission(),.2)
            from android.storage import app_storage_path
            settings_path = app_storage_path()
            self.fn = settings_path +    '/keys.txt'
            if os.path.exists(self.fn):
                f = open(self.fn, 'r')
            
                a = f.read()
            
                data = a.split('\n')
            for item in data:
                if 'email' in item:
                    mail = item.split('=')[1]
                    #print(emails,'email')
                if 'pass' in item:
                    passw = item.split('=')[1]
                    #print('passw', pass_key)
                    #print('user', user.text)
                if 'user' in item:
                    user = item.split('=')[1]
                    #print('passw', user_name)
                    #print('user', user.text)
                if 'first' in item:
                    first = item.split('=')[1]
                    #print('passw', first)
                    #print('user', user.text)
                if 'last' in item:
                    last = item.split('=')[1]
                    #print('passw', last)
                    #print('user', user.text)
            requests.put('https://easy-hacks-4eca2.firebaseio.com/users/{}/details.json'.format(mail),'{"name":"%s","last":"%s","pass":"%s","user":"%s","rating":"%s"}' %(first,last,passw,user, rating))
        except:
            pass
        try:
            global er
            if instance!='' and '.' in instance:
                from android import activity, mActivity
                from jnius import autoclass, cast
                if 'http' in instance:
                    url = '{}'.format(instance)    
                else:
                    url = 'https:{}'.format(instance) #+
                String = autoclass('java.lang.String')
                Intent = autoclass('android.content.Intent')
                Uri = autoclass('android.net.Uri')
                
                intent = Intent()
                
                
                intent.setAction(Intent.ACTION_VIEW)
                intent.setData(Uri.parse(url))
                mActivity.startActivityForResult(intent,0x123)
            else:
                er='Invalid link'
                Alert().open()
        except Exception as e:
            print(e)
            
            er = str(e)            
            Alert().open()
class Call(Popup):
    def __init__(self, **kwargs):
        super(Call, self).__init__(**kwargs)
        self.e =er
        msg_ = FloatLayout()
        butn = RectangleFlatButton(text='Close',  size_hint=(.8,.1), pos_hint={'center_y':.1, 'center_x':.5}, on_press=self.pop_close)
        msg_.add_widget(treed()) #Tripod())
        msg_.add_widget(butn)
        self.title='Call, Email or Browse'
        self.content=msg_
        self.title_align='center'
        #self.background='images/grey_shade.jpg'
        #self.title_color=(0,0,0,1)
        self.size_hint=(.7,.8)
        
        self.auto_dismiss=False
        
        self.open()
    def pop_close(self, instance):
        self.dismiss()




notes = ['Be advised to go through the tutorials', 'New contacts have been added to profiles','Check settings to select prefereces', 
        'would like to learn about us? go to our about page', 'Contact us through the contact page and air your views']
def take_permission():
    global er
    try:
        from android.permissions import request_permissions, Permission, check_permission
        request_permissions(
            [Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.CAMERA])
    except Exception as e:
        
        er =str(e)
        Alert().open()

class restB(ButtonBehavior, Image):
    pass


class cust_btn(ButtonBehavior, Image):
    cust_pos = NumericProperty(.5)
    def __init__(self, **kwargs):
        super(cust_btn, self).__init__(**kwargs)
        self.size_hint = (.5,.1)

    def on_press(self):
        

        anim = Animation(cust_pos=.515, duration=.0001)
        anim += Animation(cust_pos=.49, duration=.0001)
        anim += Animation(cust_pos=.51, duration=.0001)
        anim += Animation(cust_pos=.495, duration=.0001)
        anim += Animation(cust_pos=.505, duration=.0001)
        anim += Animation(cust_pos=.5, duration=.0001)
        anim.start(self)
        

    def delay(self, instance):
        a = 'delay'
        b='checks'
        c=a +' '+b
        return 


class lbl_btn(ButtonBehavior, Label):
    pass

#Screens start here


class RectangleFlatButton(Button):
    primary_color=[1,1,1,1]
    afgs = [0.12941176470588237,
        0.5882352941176471,
        0.9529411764705882,
        1
    ]
    primary_color_=[0.9764705882352941, 0.1764705882352941, 0.1764705882352941, 1]


class contact_btn(ButtonBehavior, Image):
    pass



class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    dir = StringProperty()

    def __init__(self, **kwargs):
        super(LoadDialog, self).__init__(**kwargs)
        try:
            from jnius import autoclass
            Environment=autoclass('android.os.Environment')
            self.dir = Environment.getExternalStorageDirectory().getPath()
        except Exception as e:
            print(e)
            global er
            er = str(e)
            Alert().open()




policy_notice = mobile_apps.policy

class Menu(Screen):
    
    def __init__(self,**kwargs):
        super(Menu, self).__init__(**kwargs)
        content = FloatLayout()
        document = RstDocument(text='Please note that if you do not select a preference, offline login is implied', pos_hint={'center_x':.5, 'top':.95}, size_hint=(.9,.3)) #, opacity=0)
        self.single = TransBtn(text='Login Online',size_hint=(.7,.1), pos_hint={'center_x':.5,'y':.4}, on_press=self.pref_online )
        self.multiple = TransBtn(text='Login Offline', size_hint=(.7, .1), pos_hint={'center_x': .5, 'y': .15}, on_press=self.pref_offline)
        content.add_widget(document)
        content.add_widget(self.single)
        
        content.add_widget(self.multiple)
        
        self.login_preference = Popup(title='Login Preference',background='images/grey_shade.png',title_color=(0,0,0,1),
                        content=content,auto_dismiss=False,
                        size_hint=(.7,.7))
        
    def pref_online(self, instance):
        global login_pref
        login_pref ='online'
        print('login',login_pref)
        self.login_preference.dismiss()
    def pref_offline(self, instance):
        print('login',login_pref)
        self.login_preference.dismiss()
    def policy(self):
        
        
        self.add_policy()
        
    
    def add_policy(self):
        message = FloatLayout()
        document = RstDocument(text=policy_notice, pos_hint={'center_x':.5, 'center_y':.55}, size_hint=(.9,.8))
        message.add_widget(document)
        butn = TransBtn(text='Done', size_hint=(.8,.1), pos_hint={'center_y':.05, 'center_x':.5}, on_press=self.pop_close)
    
        message.add_widget(butn)
        #self.modal.on_dismiss = self.dismal
        
        self.popup = Popup(title='Our Policy',background='images/trans.png',auto_dismiss=False,
                        content=message,
                        size_hint=(.8,.7))
        #self.modal.dismiss()
        self.popup.open()
    
    def contact(self):
        
        
        if rating=='not_rated':
            RateUs()
        
        sm.switch_to(screen[9])
        
    def about(self):
        sm.switch_to(screen[14])
        
    def mane(self,instance):
        self.dismiss()
        sm.switch_to(screen[1])
    def login(self):
        from android.storage import app_storage_path
        settings_path = app_storage_path()
        self.e =e = settings_path
        global er
        er = str(e)            
        Alert().open()
    def ocr(self, instance):
        OCR(rslt='')
    def neo(self, instance):
        Neogenesis(rslt='')
    def sort(self, instance):
        OCR(rslt='')
    def email_x(self, instance):
        EmailExtractor(rslt='')
    
        
            
            
    
    def home(self):
        
        Clock.schedule_once(self.open_menu, .4)    
    def login_page(self):
        self.processing()
        def me():
            self.login_preference.open()
            sm.switch_to(screen[13])
        Clock.schedule_once(lambda dt: me(), .6)
    def awareness(self):
        note_info=['Generate profiles and Build contacts with Easy Hacks',
        'Quickly copy links, emails or numbers from images with Easy Hacks',
        'Do you have email(s) without name(s)? Use Easy Hacks Nomineogen',
        'Call, email and view links from result generated with Easy Hacks',
        'Extract emails, link and/or phone numbers from text with Easy Hacks',
        'Get location of indivuals through profile addresses on Google Map']
        import random
        salute =['Hey', 'Hello', 'Howdy', 'Holla','Hallo']
        pre =random.randrange(5)
        pr =random.randrange(4)        
        try:
            from android.storage import app_storage_path
            settings_path = app_storage_path() # 
        except:
            settings_path ='/home/ben/Videos/apk/' #
        name =''
        self.fn_dir = settings_path +    '/keys.txt'
        if os.path.exists(self.fn_dir):
            f = open(self.fn_dir, 'r').read()
            print(f)
            data = f.split('\n')
            for item in data:
                if 'name' in item:
                    name = item.split('=')[1]
        
        notification.notify(title='{} {}!!'.format(salute[pr],name.capitalize()), message='{}'.format(note_info[pre]),
            app_name='Easy Hacks')    
    def open_menu(self, instance):
        #path_pic = '/home/ben/Music'
        
        try:
            from android.permissions import request_permissions, Permission, check_permission
            if check_permission('android.permission.WRITE_EXTERNAL_STORAGE'):
                if check_permission('android.permission.READ_EXTERNAL_STORAGE'):
                    if check_permission('android.permission.CAMERA'):
                        pass
            else:
                Clock.schedule_once(lambda dt:take_permission(),.2)
            from android.storage import app_storage_path
            settings_path = app_storage_path()
            self.fn = settings_path +    '/keys.txt'
            if os.path.exists(self.fn):
                f = open(self.fn, 'r')
            
                a = f.read()
            
                data = a.split('\n')
                for item in data:
                    if 'loggedin' in item:
                        
                        try:
                            for item in data:
                                
                                if 'email' in item:
                                    mail = item.split('=')[1]
                                    print(emails,'email')
                                if 'pass' in item:
                                    passw = item.split('=')[1]
                                    print('passw', pass_key)
                                    print('user', user.text)
                                    
                                if 'user' in item:
                                    user = item.split('=')[1]
                                    print('passw', user_name)
                                    print('user', user.text)
                                    
                                    
                                if 'first' in item:
                                    first = item.split('=')[1]
                                    print('passw', first)
                                    print('user', user.text)
                                if 'last' in item:
                                    last = item.split('=')[1]
                                    print('passw', last)
                                    print('user', user.text)
                            requests.put('https://easy-hacks-4eca2.firebaseio.com/users/{}/details.json'.format(mail),'{"name":"%s","last":"%s","pass":"%s","user":"%s","rating":"%s"}' %(first,last,passw,user, rating))
                        except:
                            pass
                        f.close()
                        
                        self.awareness()
                        sm.switch_to(screen[1])
            
                        return
                
                
                self.login_preference.open()
                sm.switch_to(screen[13])
            else:
                
                self.login_preference.open()
                sm.switch_to(screen[13])
        except Exception as e:
            
            self.awareness()
            sm.switch_to(screen[1])
            
            global er
            er = str(e)
            
            Alert().open()
    def dissapear(self, instance):
        self.regards.opacity = 0
    def apear(self, instance):
        self.regards.opacity = 1
        
    def saluted(self):
        Clock.schedule_once(self.salute)
        Clock.schedule_once(self.salute_ret,1)
        Clock.schedule_once(self.change,1)
        Clock.schedule_once(self.salute,1.2)
        Clock.schedule_once(self.salute_ret,1.7)
        
        
    def salute(self,instance):
        self.regards = self.ids['regards']
        
        Animation(y=self.height/2, d=1).start(self.regards)
    def salute_ret(self,instance):
        
        print('move up')
        Animation(y=self.height*2, d=.1).start(self.regards)

    
    def pop_greet(self):
        
        Animation(y=self.height*.2, d=.1).start(self.greet)

    def pop_close(self, instance):
        print('closed pop')
        self.popup.dismiss()
    def change(self, intance):
        self.sal = 'How'
        self.day = 'are'
        self.user = 'you today?'


class VaultWheel(FloatLayout):
    angle = NumericProperty(0)
    speed = NumericProperty(0)
    


class Wheel(FloatLayout):
    angle = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super(Wheel, self).__init__(**kwargs)
        self.rotate()

    def on_angle(self, item, angle):
        if angle == 360:
            item.angle = 0

    def change_speed(self):
        anim = Animation(angle=360, duration=1)
        anim.start(self)
            
    def rotate(self):
        anim = Animation(angle=360, duration=20)
        anim += Animation(angle=360, duration=20)
        anim.repeat = True
        anim.start(self)


class InnerWheel(FloatLayout):
    angle = NumericProperty(0)
    def __init__(self, **kwargs):
        super(InnerWheel, self).__init__(**kwargs)
        self.dur = 20
        self.rotate()

    def on_angle(self, item, angle):
        if angle == -360:
            item.angle = 0

    def change_speed(self):
        anim = Animation(angle=-360, duration=1)
        anim.start(self)

    def rotate(self):
        anim = Animation(angle=-360, duration=20)
        anim += Animation(angle=-360, duration=20)
        anim.repeat = True
        anim.start(self)

summary ="""\nHere's a run down of the tools
\nand respective functions
\nData Refinery: Handles 
\ntext and text files. """

sum="""Emails Extractor: Extracts
\n emails, phone numbers
\nand links from text. 
\nImage Reader: Extracts 
\ntext from images. 
\nNomineogen: Generates 
\nlikely names from email 
\naddress.
\n\nWould you like some 
\nlight tutorials to 
\nhelp you get started?"""
#"""Easy Hacks offers you several tools all wrapped in one convenient and user friendly package. This tools help you hack data, hence the name. It's capabilities ranges from handling text to files and images. You'll find four tool links on the home screen:  With sort you can sort words in text into logical order, be it, alpha or numeric. Shrink simple likes you remove duplicates of multiples of words from text. Both sort and shrink options take the liberty to remove gibberish symbols. Click the tip button in data refinery for details""",
#"""Extractor Plus also  handles text files and text. It extract specific information from text such as emails, numbers, links and a partern you can choose to specify.""",
#"""Neogenesis also handles text files and text. It type of text it handles though are strictly emails. It generates possible names from emails provided by you. And has an accuracy of 70% based on the similar of the email provide to the actually name. Because of the failings of this too we have provided you with an option to edit the result before saving the profiles of the individual emails. Hence, you can input bulk emails and get a list of names and contacts which you can edit before saving. Also we have provided options for you to include links, phone contact and physical address in the individual contacts before saving""",
#"""The image reader strictly handles images. It extracts text from images as long as they are text-embedded"""
#''''''

class LoginScreen(Screen):
    
    blur = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        
        super(LoginScreen, self).__init__(**kwargs)
        self.size_hint = (1, 1)
        message = FloatLayout()
        self.document = TextInput(pos_hint={'center_x':.5, 'center_y':.8}, size_hint=(.9,.1), hint_text='Enter email')
        self.document_1 = TextInput(pos_hint={'center_x':.5, 'center_y':.6}, size_hint=(.9,.1), hint_text='Enter username', on_text_validate=self.validate)
        self.document_2 = TextInput(pos_hint={'center_x':.5, 'center_y':.4}, size_hint=(.9,.1), hint_text='Enter new password', disabled=True)
        message.add_widget(self.document)
        message.add_widget(self.document_1)
        message.add_widget(self.document_2)
        self.butn = TransBtn(text='Submit', size_hint=(.8,.1), pos_hint={'center_y':.1, 'center_x':.5}, on_press=self.change_password, disabled=True)
        abutn = TransBtn(text='Close', size_hint=(.8,.1), pos_hint={'center_y':.1, 'center_x':.5}, on_press=self.pop_close)
        message.add_widget(self.butn)
        message.add_widget(abutn)
        
        self.popup = Popup(title='Change password',background='images/grey_shade.png',title_color=(0,0,0,1),auto_dismiss=False,
                        content=message,
                        size_hint=(.7,.7))
    def validate(self, instance):
        try:
            from android.permissions import request_permissions, Permission, check_permission
            if check_permission('android.permission.WRITE_EXTERNAL_STORAGE'):
                if check_permission('android.permission.READ_EXTERNAL_STORAGE'):
                    if check_permission('android.permission.CAMERA'):
                        pass
            else:
                Clock.schedule_once(lambda dt:take_permission(),.2)
            from android.storage import app_storage_path
            settings_path = app_storage_path()
            self.fn = settings_path +    '/keys.txt'
            if os.path.exists(self.fn):
                f = open(self.fn, 'r')
            
                a = f.read()
            
                data = a.split('\n')
            for item in data:
                if 'email' in item:
                    mail = item.split('=')[1]
                    #print(emails,'email')
                if 'pass' in item:
                    passw = item.split('=')[1]
                    #print('passw', pass_key)
                    #print('user', user.text)
                if 'user' in item:
                    user = item.split('=')[1]
                    #print('passw', user_name)
                    #print('user', user.text)
                if 'first' in item:
                    first = item.split('=')[1]
                    #print('passw', first)
                    #print('user', user.text)
                if 'last' in item:
                    last = item.split('=')[1]
                    #print('passw', last)
                    #print('user', user.text)
                if self.document.text==mail and self.document.text_1==user:
                    notification.notify(title='test', message='Please enter a new password and click Submit then login with your new password')
                    self.document_2.disabled=False
                    self.butn.disabled=False
                else:
                    notification.notify(title='test', message='Sorry, account not found. You can reset Easy Hacks in settings and create a new account')
        
        except:
            pass
        
    def change_password(self, instance):
        try:
            from android.permissions import request_permissions, Permission, check_permission
            if check_permission('android.permission.WRITE_EXTERNAL_STORAGE'):
                if check_permission('android.permission.READ_EXTERNAL_STORAGE'):
                    if check_permission('android.permission.CAMERA'):
                        pass
            else:
                Clock.schedule_once(lambda dt:take_permission(),.2)
            from android.storage import app_storage_path
            settings_path = app_storage_path()
            self.fn = settings_path +    '/keys.txt'
            if os.path.exists(self.fn):
                f = open(self.fn, 'r')
            
                a = f.read()
            
                data = a.split('\n')
            for item in data:
                if 'email' in item:
                    mail = item.split('=')[1]
                    #print(emails,'email')
                if 'pass' in item:
                    passw = item.split('=')[1]
                    #print('passw', pass_key)
                    #print('user', user.text)
                if 'user' in item:
                    user = item.split('=')[1]
                    #print('passw', user_name)
                    #print('user', user.text)
                if 'first' in item:
                    first = item.split('=')[1]
                    #print('passw', first)
                    #print('user', user.text)
                if 'last' in item:
                    last = item.split('=')[1]
                    #print('passw', last)
                    #print('user', user.text)
                f.close()
                data = 'name={}\nlast={}\nemail={}\npass={}\nuser={}'.format(first, last, mail, passw, user)
                            
                #first = first_name.text
                #last = last_name.text
                #mail =' '.join(email.text.split('.'))

                #passw = password.text
                #user = username.text

                #dicto ='{"name":"%s","last":"%s","pass":"%s","user":"%s"}' %(first_name.text, last_name.text, password.text, username.text)
                #print(dicto)
                #try:
                #    r =requests.put('https://easy-hacks-4eca2.firebaseio.com/users/{}/details.json'.format(mail),'{"name":"%s","last":"%s","pass":"%s","user":"%s","rating":"%s"}' %(first,last,passw,user, rating))
                #    #print('request', r)
                #except:
                #    print('Not sent')
                #jobj = json.loads(r.content)
                #requests.get('https://easy-hacks-4eca2.firebaseio.com/users/{}/details.json'.format(email.text))
                p = open(self.fn, 'w')
                p.write(data)
                p.close()
                self.popup.dismiss()
        except Exception as e:
            print(str(e))
            self.popup.dismiss()
        
    def forgot(self):
        self.popup.open()
    def pop_close(self, instance):
        self.popup.dismiss()

    def pop_up(self):
        
        try:
            from android.storage import app_storage_path
            settings_path =app_storage_path() # '/home/ben/Videos' #
            self.fn = settings_path +    '/keys.txt'
            user= self.ids['user']
            
            password = self.ids['pass']
            global er
            #r =requests.get('https://easy-hacks-4eca2.firebaseio.com/users/{}/details.json'.format(user.text))
            if os.path.exists(self.fn):
                f = open(self.fn, 'r').read()
                #print(f)
                self.data =data= f.split('\n')
                print(data)
                for item in self.data:
                    print('printing', item)
                    if 'email' in item:
                        emails = item.split('=')[1]
                        print(emails,'email')
                    if 'pass' in item:
                        pass_key = item.split('=')[1]
                        print('passw', pass_key)
                        print('user', user.text)
                    if 'user' in item:
                        user_name = item.split('=')[1]
                        print('passw', user_name)
                        print('user', user.text)
                    if 'first' in item:
                        first = item.split('=')[1]
                        print('passw', first)
                        print('user', user.text)
                    if 'last' in item:
                        last = item.split('=')[1]
                        print('passw', last)
                        print('user', user.text)
                if user.text!='' or password.text!='':
                    print('entering')
                    print('self data', self.data)
                    print('pass', pass_key)
                    if user.text.lower() == emails.lower():
                        print('entered')
                        if password.text == pass_key:
                            #if r.status_code!=200:
                            #notification.notify(title='test', 
                            #message='https://easy-hacks-4eca2.firebaseio.com/users/{}/details.json {"name":"{}","last":"{}","pass":"{}","user":"{}"}'.format(emails,first, last, pass_key, user_name))
                            #requests.put('https://easy-hacks-4eca2.firebaseio.com/users/{}/details.json'.format(emails),'{"name":"{}","last":"{}","pass":"{}","user":"{}"}'.format(first, last, pass_key, user_name))
                            print('locked')
                            f += '\nloggedin'
                            a = open(self.fn, 'w')
                            a.write(f)
                            a.close
                            self.man()
                        else:
                            self.e= e = "Sorry, password wrong password. Did you forget your password?"
                            global er
                            er = str(e)            
                            Alert().open()
                    else:
                        self.e = e ='email not found. Try another email or create a fresh account'
                        #global er
                        er = str(e)            
                        Alert().open()
                    
                else:
                    self.e = e = 'Please fill all entries'
                    #global er
                    er = str(e)            
                    Alert().open()
            elif requests.get('https://easy-hacks-4eca2.firebaseio.com/users/{}/details.json'.format(user.text)).status_code==200:
                r=requests.get('https://easy-hacks-4eca2.firebaseio.com/users/{}/details.json'.format(user.text))
                jobj = json.loads(r.content)
                pass_key= jobj['pass']
                if user.text!='':
                    print('entering')
                    
                    if password.text == pass_key:
                        print('locked')
                        f += '\nloggedin'
                        a = open(self.fn, 'w')
                        a.write(f)
                        a.close()
                        self.man()
                    else:
                        self.e= e = "Sorry, password wrong password. Did you forget your password?"
                        #global er
                        er = str(e)            
                        Alert().open()
                else:
                    self.e = e ='email not found. Try another email or create a fresh account'
                    #global er
                    er = str(e)            
                    Alert().open()
                
            
            else:
                self.e =e= "Your haven't created an account yet! Click the create account button to generate one"    
                #global er
                er = str(e)            
                Alert().open()
        except Exception as e:
            print(e)
            self.e =e= 'Sorry, something went wrong'
            #global er
            er = str(e)            
            Alert().open()
    def dis(self):
        sm.switch_to(screen[0])
    def man(self):
        self.modal = ModalView(size_hint=(1, 1))
        self.modal.on_open = self.true_blur
        self.modal.background ='images/effect_empty.png'
        content = FloatLayout()
        content_1 = FloatLayout()
        data =self.data
        print('new dat', data)
        for item in data:
            if 'name' in item:
                name = item.split('=')[1]
                print(name)
        
        self.name= name.capitalize() #+' '+last.capitalize()
        print(self.name)
        self.carousel = Carousel(size_hint=(1,1), pos_hint={'center_x':.5,'center_y':.5})
        content.add_widget(
        Label(text = 'Hello {}!!\n\nWelcome to Easy Hacks\n{}'.format(self.name, summary),size_hint=(.5,.1), pos_hint={'center_x':.5,'y':.5}, font_size=30))
        
        content.add_widget(RectangleFlatButton(text='Skip',size_hint=(.3,.05), pos_hint={'center_x':.2,'y':.05}, on_press=self.pop_up_close))
        #self.clo = RectangleFlatButton(text='No',size_hint=(.3,.05), pos_hint={'center_x':.5,'y':.05})
        content.add_widget(RectangleFlatButton(text='Next',size_hint=(.3,.05), pos_hint={'center_x':.8,'y':.05}, on_press=self.next))
        
        content_1.add_widget(
        Label(text = '{}'.format(sum),size_hint=(.5,.1), pos_hint={'center_x':.5,'y':.5}, font_size=30))
        content_1.add_widget(RectangleFlatButton(text='Back',size_hint=(.25,.05), pos_hint={'center_x':.2,'y':.05}, on_press=self.last))
        #self.clo = RectangleFlatButton(text='No',size_hint=(.3,.05), pos_hint={'center_x':.5,'y':.05})
        content_1.add_widget(RectangleFlatButton(text='Yes',size_hint=(.25,.05), pos_hint={'center_x':.8,'y':.05}, on_press=self.tutr))
        
        content_1.add_widget(
        RectangleFlatButton(text='No',size_hint=(.25,.05), pos_hint={'center_x':.5,'y':.05}, on_press=self.pop_up_close))
        #self.clo = RectangleFlatButton(text='No',size_hint=(.3,.05), pos_hint={'center_x':.5,'y':.05})
        #self.tut = RectangleFlatButton(text='Yes',size_hint=(.3,.05), pos_hint={'center_x':.8,'y':.05} )
        #elf.close.bind(on_press=self.pop_up_close)
        
        #self.tut.bind(on_press=self.tutr)
        #content.add_widget(self.close)
        #content.add_widget(self.tut)
        self.carousel.add_widget(content)
        self.carousel.add_widget(content_1)
        self.modal.add_widget(self.carousel)
        self.modal.open()
        self.modal.on_dismiss = self.dismal
    def last(self, instance):
        self.carousel.load_previous()
    def next(self, instance):
        self.carousel.load_next()
    def tutr(self,instance):
        self.modal.dismiss()
        global back_home
        back_home =True
        global screen
        screen.pop()
        screen.append(About(name='14'))
        sm.switch_to(screen[6])
    def true_blur(self):
        self.blur = True
        return self.blur
    def false_blur(self):
        self.blur = False
        return self.blur
    def pop_up_close(self, instance):
        self.false_blur()
        self.modal.dismiss()
        global screen
        screen.pop()
        screen.append(About(name='14'))
        sm.switch_to(screen[1])
    def dismal(self):
        self.false_blur()
        
    def account(self):
        
        sm.switch_to(screen[12])


class EmailExtractor(Screen):
    emails = ObjectProperty(None)
    result_mod = BooleanProperty(None)
    loadfile = ObjectProperty(None)
    
    def __init__(self,  **kwargs):
        super(EmailExtractor, self).__init__(**kwargs)
        try:
            self.result_mod = result_mode
            
            self.resume_result = ''
            
            
            
        except Exception as e:
            global er
            er = str(e)            
            Alert().open()
    def tip_info(self):
        message = FloatLayout()
        document = RstDocument(text=tip_mode, pos_hint={'center_x':.5, 'center_y':.55}, size_hint=(.9,.8))
        message.add_widget(document)
        butn = TransBtn(text='Close', size_hint=(.8,.1), pos_hint={'center_y':.05, 'center_x':.5}, on_press=self.pop_close)
    
        message.add_widget(butn)
        
        self.popup = Popup(title='Tip',background='images/trans.png',title_color=(0,0,0,1),auto_dismiss=False,
                    content=message,
                    size_hint=(.7,.6))
        
        self.popup.open()
    
    
    def pop_close(self, instance):
        self.popup.dismiss()
    def home(self):
        self.emails.text = ''
        global tools
        tools = ['Data Refinery','Nomineogen','Extractor Plus']
        sm.switch_to(screen[1])
    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Choose Text File", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        try:
            with open(os.path.join(path, filename[0])) as stream:
                self.emails.text = stream.read()
        except Exception as e:
            self.e = str(e)
            self.error()
        self.dismiss_popup()
    def seat(self, instance):
        self.modal = ModalView(size_hint=(1, 1))
        self.modal.background ='images/effect_empty.png'
        box = FloatLayout()
        box.add_widget(Image(source='images/tab_rotate.gif',pos_hint={'center_x':.5,'center_y':.5},size_hint=(.5,.5)))
        box.add_widget(Label(text='Loading... Please Wait...',pos_hint={'center_x':.5,'center_y':.3},size_hint=(.5,.5)))
        self.modal.add_widget(box)
        
        self.modal.open()
    def stand(self, instance):
        self.modal.dismiss()
    
    def dismiss_popup(self):
        self._popup.dismiss()

    def camera(self):
        try:
            from android.permissions import request_permissions, Permission
            request_permissions(
                [Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.CAMERA])
        except:
            print('android storage permission')

        try:
            CamBox()
            sm.switch_to(screen[5])
        except Exception as e:
            self.e = str(e)
            self.error()

    def close(self):
        self.dismiss()
    
    def pattern_extract(self):
        try:
            print('regex')
            #import re
            regex_input = self.ids['regex']
            reg =regex_input.text
            
            pattern = []
            st = self.emails.text
            #print(st)
            s = st.split()
            for item in s:
                if item.find(reg)!=-1: #re.match([reg],item):
                    #tail =item.index('@')
                    #print(item[tail+1:])
                    pattern.append(item)
                    print(pattern)
            self.resume_result = '\n'.join(pattern)
        except Exception as e:
            print(e)
            self.e = str(e)
            self.e= e=self.e+' regex'
            global er
            er = str(e)            
            Alert().open()

    def mode(self, instance):
        try:
            extract_btn = self.ids['extract']
            

            if self.emails.text:
                if '@Extract' in extract_btn.source:
                    self.email_extract()
                elif 'link' in extract_btn.source:
                    self.extract_link()
                elif 'phone' in extract_btn.source:
                    self.extract_phone()
                elif 'pattern' in extract_btn.source:
                    self.pattern_extract()
                else:
                    self.extract_plus()
            else:
                self.emails.focus
        
        except Exception as e:
            print(e)
            self.e = str(e)
            self.e=e=self.e+' select mode'
            global er
            er = str(e)            
            Alert().open()
        Clock.schedule_once(self.stand, 0)
        print('dismissed')

    def extract_plus(self):
        try:
            st = self.emails.text
            compare = 'gmail.comyahoo.comymail.comhotmail.comicloud.com.net.microsoftoutlook.com.org.co.ca.ng.com.ng'
            #print(st)
            s = st.split()
            xtract = []
            link_tract = []
            phone = []
            for item in s:
                if '@' in item:
                    tail =item.index('@')
                    #print(item[tail+1:])
                    if len(item[:tail])>1:
                        if item[tail+1:] in compare and '.' in item[tail+1:] and len(item[tail+1:])>4:
                            ree =item[tail+1:]
                            
                            
                            
                            if len(ree.split('.')[-1])>1 and len(ree.split('.')[0])>2:
                                #append ='Tru'
                                #print(len(ree.split('.')[-1])>1)
                                #print(ree)
                                #print(ree.split('.'))
                                #print(len(ree.split('.')[0])>2)
                                xtract.append(item)
                        elif '.' in item[tail+1:] and len(item[tail+1:])>4:
                            #print('synthatically valid')
                            ree =item[tail+1:]
                            
                            if len(ree.split('.')[-1])>1 and len(ree.split('.')[0])>2:
                                #append ='Tru'
                                #print(len(ree.split('.')[-1])>1)
                                #print(ree)
                                #print(ree.split('.'))
                                #print(len(ree.split('.')[0])>2)
                                xtract.append(item)
                    
            for item in s:
                if '@' not in item:
                    if 'www' in item or 'http' in item or 'url' in item:
                        link_tract.append(item)
                    elif '.' in item:
                        xtract.append(item)
            
            for item in s:
                if item.isnumeric() and len(item)>6:
                    phone.append(item)
                elif '+' in item and len(item)>6:
                    phone.append(item)
                else:
                    pass

            
            #print(xtract)
            #print(len(xtract))
            #global resume_result
            self.resume_result ='\n'.join(xtract) + '\n' + '\n'.join(link_tract) + '\n' + '\n'.join(phone)
            
            #self.display.text ='\n\n'.join(xtract)
        
        except Exception as e:
            print(e)
            self.e = str(e)
            self.e=e =self.e+' extract plus'
            global er
            er = str(e)            
            Alert().open()
    
    def extract_phone(self):
        try:
            st = self.emails.text
            s = st.split()
            xtract = []
            phone = []
            print(s)
            for item in s:
                if item.isnumeric() and len(item)>6:
                    xtract.append(item)
                elif '+' in item and len(item)>6:
                    xtract.append(item)
                else:
                    pass

            self.resume_result ='\n'.join(xtract)
        
        except Exception as e:
            print(e)
            self.e = str(e)
            self.e=e= self.e+' extract phone'
            global er
            er = str(e)            
            Alert().open()
    
    def extract_link(self):
        try:
            st = self.emails.text
            compare = 'gmail.comya/hoo.comymail.comhotmail.comicloud.com.net.microsoftoutlook.com.org.co.ca.ng.com.ng'
            #print(st)
            s = st.split()
            xtract = []
            for item in s:
                if '@' not in item:
                    if 'www' in item or 'http' in item or 'url' in item:
                        xtract.append(item)
                    elif '.' in item:
                        xtract.append(item)
            #print(xtract)
            #print(len(xtract))
            #global resume_result
            print(len(xtract), 'link(s) found')
            self.resume_result = '\n'.join(xtract)
            #self.display.text ='\n\n'.join(xtract)
        
        except Exception as e:
            print(e)
            self.e = str(e)
            self.e=e= self.e+' extract link'
            global er
            er = str(e)            
            Alert().open()
    
    def email_extract(self):
        try:
            '''This function extradts emails from jubiris information'''
            st = self.emails.text
            compare = 'gmail.comyahoo.comymail.comhotmail.comicloud.com.net.microsoftoutlook.com.org.co.ca.ng.com.ng'
            #print(st)
            s = st.split()
            xtract = []
            for item in s:
                if '@' in item:
                    tail =item.index('@')
                    #print(item[tail+1:])
                    if len(item[:tail])>1:
                        if item[tail+1:] in compare and '.' in item[tail+1:] and len(item[tail+1:])>4:
                            ree =item[tail+1:]
                            
                            
                            
                            if len(ree.split('.')[-1])>1 and len(ree.split('.')[0])>2:
                                #append ='Tru'
                                #print(len(ree.split('.')[-1])>1)
                                #print(ree)
                                #print(ree.split('.'))
                                #print(len(ree.split('.')[0])>2)
                                xtract.append(item)
                        elif '.' in item[tail+1:] and len(item[tail+1:])>4:
                            #print('synthatically valid')
                            ree =item[tail+1:]
                            
                            if len(ree.split('.')[-1])>1 and len(ree.split('.')[0])>2:
                                #append ='Tru'
                                #print(len(ree.split('.')[-1])>1)
                                #print(ree)
                                #print(ree.split('.'))
                                #print(len(ree.split('.')[0])>2)
                                xtract.append(item)
            #print(xtract)
            #print(len(xtract))
            #global resume_result
            print(len(xtract), 'email(s) found')
            self.resume_result = '\n'.join(xtract)
            #self.display.text ='\n\n'.join(xtract)
        
        except Exception as e:
            print(e)
            self.e = str(e)
            self.e=e =self.e+' extract email'
            global er
            er = str(e)            
            Alert().open()

    def other_tools(self, instance):
        #self.close()
        #self.blur = True
        global total_search
        total_search=self.emails.text.split()
        result_open=self.emails.text.split()
        global done
        global input_enter
        input_enter = self.emails.text
        done =self.resume_result.split()

        for item in done:
            result_open.remove(item)
        global invalid
        invalid = result_open
        result_analysis = '{} items search, \n{} found, {} are invalid'.format(total_search, done,invalid)
        
        """notification.notify(title='Reminder!!', message='Quick copy links, emails or phone numbers from images with Easy Hacks',
            app_name='Easy Hacks')
        notification.notify(title='Reminder!!', message='Do you have email(s) without name(s)? Use Easy Hacks Nomineogen tool to fix this ',
            app_name='Easy Hacks')
        notification.notify(title='Reminder!!', message='Make calls, send emails and view web links from result generate with Easy Hacks',
            app_name='Easy Hacks')
        notification.notify(title='Reminder!!', message='Extract emails, link and/or phone numbers from large volume of text with Easy Hacks',
            app_name='Easy Hacks')"""
        OtherTools(current_tool='Extractor Plus', result_q=self.resume_result).open()


        #deff = '{} items screened'.format(len(self.emails.text.split('\n')))
        deff =' '.join(self.emails.text.split('\n'))
        ew=[]
        for item in deff.split(' '):
            if item:
                ew.append(item)
        total = '{} items screened'.format(len(ew))

        rep =' '.join(self.resume_result.split('\n'))
        usable = rep.split(' ')
        use=[]
        for item in usable:
            if item:
                use.append(item)
        
        e =len(ew)-len(use)
        minus=   '{} Invalid item(s) removed'.format(e)
        deff ='{} item(s) in result'.format(len(use))
        global er 
        #er = deff+'\n'+minus+'\n'+total
        er = '\n'.join(('{}.'.format(deff),'\n{}.'.format(minus),'\n{}.'.format(total)))
        Clock.schedule_once(lambda dt:Alert().open(), 0)

    
    def eliminator(self):
        'Tis function helps remove unwanted emails like @info etc'
        print(len(dic))
        for item in dic.keys():
            # if len(item.split())>3:
            if 'sales' in dic[item]:
                ch.append(item)
                print(item)
                print(dic[item])
            elif 'career' in dic[item]:
                ch.append(item)
                print(item)
                print(dic[item])
            elif 'info' in dic[item]:
                ch.append(item)
                print(item)
                print(dic[item])
            elif 'enquiry' in dic[item]:
                ch.append(item)
                print(item)
                print(dic[item])
            else:
                pass
        print(len(ch))
        for item in ch:
            dic.pop(item)
        print(dic)
        print(len(dic))

class ExtractPlus(EmailExtractor,ModalView):
    emails = ObjectProperty(None)
    result_mod = BooleanProperty(False)
    def __init__(self,rslt,**kwargs):
        super(EmailExtractor, self).__init__(**kwargs)
        try:
            
            #self.size_hint = (1, 1)
            print('rslt', rslt)
            self.rslt = rslt
            self.emails.text = rslt
            self.result_mod = result_mode
            self.background = 'images/effect.png'
            self.resume_result = ''
            #self.open()
            #self.modal = ModalView(size_hint=(1, 1))
            #self.modal.background ='images/effect_empty.png'
            #box = FloatLayout()
            #box.add_widget(Image(source='images/tab_rotate.gif',pos_hint={'center_x':.5,'center_y':.5},size_hint=(.5,.5)))
            #box.add_widget(Label(text='Loading... Please Wait...',pos_hint={'center_x':.5,'center_y':.3},size_hint=(.5,.5)))
            #self.modal.add_widget(box)
        except Exception as e:
            self.e = str(e)
            #self.error()
            global er
            er = self.e
            Alert().open()
    def home(self):
        
        global tools
        tools = ['Data Refinery','Nomineogen','Extractor Plus']
        self.dismiss()
        sm.switch_to(screen[1])
    def other_tools(self, instance):
        #self.close()
        #self.blur = True
        self.dismiss()
        global total_search
        total_search=self.emails.text.split()
        result_open=self.emails.text.split()
        global done
        done =self.resume_result.split()

        for item in done:
            result_open.remove(item)
        global invalid
        invalid = result_open
        result_analysis = '{} items search, \n{} found, {} are invalid'.format(total_search, done,invalid)
        OtherTools(current_tool='Extractor Plus', result_q=self.resume_result).open()


class CreateAccount(Screen):

    def __init__(self, **kwargs):
        super(CreateAccount, self).__init__(**kwargs)
        self.size_hint = (1, 1)
        #self.background = 'images/effect_empty.png'
        #self.open()

    def error(self):
        msg = FloatLayout()
        document = RstDocument(text='Sorry, account already exist. Sign in with said account or create another account.', pos_hint={'center_x':.5, 'center_y':.5}, size_hint=(.9,.8))
        msg.add_widget(document)
        popup = Popup(title='Alert!!',auto_dismiss=False,
                    content=msg,background = 'images/grey_shade.jpg',title_color=(0,0,0,1),
                    size_hint=(.7,.5))
        popup.open()
    def dis(self):
        sm.switch_to(screen[13])
    def congrats(self):
        msg_ = FloatLayout()
        document = RstDocument(text='Account Created Successfully', pos_hint={'center_x':.5, 'center_y':.6}, size_hint=(.9,.6)) #, opacity=0)
        butn = TransBtn(text='Close', size_hint=(.8,.2), pos_hint={'center_y':.1, 'center_x':.5}, on_press=self.pop_close)
        msg_.add_widget(document)
        msg_.add_widget(butn)
        self.popup = Popup(title='Congratulations!!',auto_dismiss=False,
                    content=msg_,background = 'images/grey_shade.jpg',title_color=(0,0,0,1),
                    size_hint=(.7,.3))
        
        self.popup.open()
    def pop_close(self, instance):
        self.popup.dismiss()
    def close(self):
        self.e = 'Invalid Action'
        try:
            from android.permissions import request_permissions, Permission
            request_permissions(
                [Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.CAMERA])
        except:
            print('android storage permission')
            
        try:
            first_name = self.ids['first_name']
            last_name = self.ids['last_name']
            username = self.ids['username']
            email = self.ids['email']
            password = self.ids['pass']
            
            from android.storage import app_storage_path
            #settings_path = '/home/ben/Videos' #app_storage_path()
            settings_path = app_storage_path() #'/home/ben/Videos' #
            self.fn = settings_path +    '/keys.txt'
            global er
            mail =' '.join(email.text.split('.'))
            try:
                r =requests.get('https://easy-hacks-4eca2.firebaseio.com/users/{}/details.json'.format(mail))
            except:
                print('skipped first check')
            try:
                if os.path.exists(self.fn):
                    er = 'Account Already exists'            
                    Alert().open()
                else:
                    if r.status_code==200:
                        er = 'Account Already exists'
                        prin(mail)            
                        Alert().open()
            except:
                try:
                    
                    if email.text!='' and first_name.text!='' and password.text!='' and username.text!='':
                        
                        if len(email.text)> 1 and '@' in email.text:
                            data = 'name={}\nlast={}\nemail={}\npass={}\nuser={}'.format(first_name.text, last_name.text, email.text, password.text, username.text)
                            
                            first = first_name.text
                            last = last_name.text
                            mail =' '.join(email.text.split('.'))

                            passw = password.text
                            user = username.text

                            #dicto ='{"name":"%s","last":"%s","pass":"%s","user":"%s"}' %(first_name.text, last_name.text, password.text, username.text)
                            #print(dicto)
                            try:
                                r =requests.put('https://easy-hacks-4eca2.firebaseio.com/users/{}/details.json'.format(mail),'{"name":"%s","last":"%s","pass":"%s","user":"%s","rating":"%s"}' %(first,last,passw,user, rating))
                                #print('request', r)
                            except:
                                print('Not sent')
                            #jobj = json.loads(r.content)
                            #requests.get('https://easy-hacks-4eca2.firebaseio.com/users/{}/details.json'.format(email.text))
                            f = open(self.fn, 'w')
                            f.write(data)
                            f.close()
                            print(data)
                            self.congrats()
                            sm.switch_to(screen[13])
                        else:
                            self.e = e= 'Please enter a valid email'
                            #global er
                            er = str(e)            
                            Alert().open()
                            #print(e)
                    else:
                        self.e = e = "Please fill all forms"
                        #global er
                        er = str(e)            
                        Alert().open()
                        #print(e)
                except Exception as e:
                    print(e)
                    #global er
                    er = str(e)            
                    Alert().open()        
                    #print(e)
        except Exception as e:
            print(e)
            #global er
            er = str(e)            
            #Alert()
            print(e)

    def error_(self):
        msg = FloatLayout()
        document = RstDocument(text='\n'.join(self.e.split(' ')), pos_hint={'center_x':.5, 'center_y':.5}, size_hint=(.9,.8))
        msg.add_widget(document)
        popup = Popup(title='Error!!',background = 'images/grey_shade.jpg',title_color=(0,0,0,1),
                    content=msg, auto_dismiss=False,
                    size_hint=(.7,.5))
        popup.open()

text_string= mobile_apps.text
#life_hacks = mobile_apps.life_hacks
#easyhacks_intro = mobile_apps.easyhacks_intro
#tutorials= mobile_apps.lessons

class but(ButtonBehavior, Image):
    pass


class Scroll_A(ScrollView):
    scroll_b = ObjectProperty(None)
    pass

class Scroll_B(ScrollView):
    pass
class Scroll_C(ScrollView):
    pass
class Profiles(ModalView):
    def __init__(self,**kwargs):
        super(Profiles, self).__init__(**kwargs)
        self.size_hint = (1, 1)
        self.background = 'images/effect_black.png'
        #message = FloatLayout()
        #'20200910_103756'
        
        
        try:
            root = ScrollView(size_hint=(.9, .7),
                    pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
            layout = GridLayout(cols=2,  spacing=root.width,padding=root.width*.8,
                    size_hint=(1, None))
            layout.bind(minimum_height=layout.setter('height'))
            from jnius import autoclass
            Environment=autoclass('android.os.Environment')
            path = Environment.getExternalStorageDirectory().getPath() + '/Easy Hacks'
            path_pic =Environment.getExternalStorageDirectory().getPath() + '/Easy Hacks' +'/create profiles'
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                print('Already Created')
            if not os.path.exists(path_pic):
                os.mkdir(path_pic)
            else:
                print('Already Created')
            #path_pic = '/home/ben/Music'            
            self.fn = path_pic +    '/keys.txt'
            
            from android.storage import app_storage_path
            settings_path = app_storage_path() # '/home/ben/Videos/apk/' #
            
            self.fn_dir = settings_path +    '/keys.txt'
            if os.path.exists(self.fn_dir):
                f = open(self.fn_dir, 'r').read()
                print(f)
                data = f.split('\n')
                for item in data:
                    if 'name' in item:
                        name = item.split('=')[1]
                    if 'last' in item:
                        last = item.split('=')[1]
                
            self.name= name.capitalize() +' '+last.capitalize()
            #path_pic='/home/ben/Videos/apk/timed'

            files = os.listdir(path_pic)
            #print(files)
            #print(f)
            #data = f.split('\n')
            global emass
            for item in files:
                we =open(path_pic+'/'+item,'r').read()
                emass[item] = we
            
            #print(emass)
            #self.emass = {}
            
            for timestamp in files:
                actual_month= month[timestamp[4:6]]
                year =timestamp[:4]
                day =timestamp[6:8]
                hour = timestamp[9:11]
                minute = timestamp[11:13]
                second = timestamp[13:15]
                timed = '\n\n{} {}, {} \n{}:{}:{}'.format(actual_month,day,year,hour,minute,second)
                
                saved_contact = BoxLayout(orientation='vertical',size=(root.width*2,root.width*2),
                            size_hint=(None, None))
                self.rest = contact_btn(source='images/time_stamped.png') #, text=timestamp)
                #self.emass[self.rest] = timestamp
                self.rest.bind(on_press= partial(self.open_saved_contact, timestamp))
                saved_contact.add_widget(self.rest)
                saved_contact.add_widget(Label(text=timed,size_hint_y=None, height='10dp', halign='center', font_size=20))
                layout.add_widget(saved_contact)
            
            root.add_widget(layout)
            #self.add_widget(root)
            #print(emass)
            box = BoxLayout(orientation='vertical',padding=10, spacing=10)
            username_contact = BoxLayout(orientation='vertical', size_hint_y=30)
            other_contacts = BoxLayout(orientation='vertical', size_hint_y= 70)
            #name_store = JsonStore('name.json')
            #if name_store.exists('account'):
            #    user = name_store.get('account')['name']
            #else:
            #    user=''
            username_contact.add_widget(Label(text=self.name, size_hint_y=None, height='20dp'))
            username_contact.add_widget(Image(source='images/contact_block.png')) #,size_hint_y=None,height='200dp'))
            #username_contact.add_widget(Label(text='Esther Benson', size_hint_y=None, height='40dp'))
            box.add_widget(username_contact)
            other_contacts.add_widget(Image(source='images/other saved contacts.png', size_hint_y=None,height='20dp'))
            other_contacts.add_widget(root)
            close = Button(text='Close',size_hint_y=None, height= '40dp', on_press=self.dismiss)
            other_contacts.add_widget(close)
            #box.add_widget(root)
            box.add_widget(other_contacts)
            self.add_widget(box)
            #self.open()
            self.bind(on_dismiss=self.empty_msg)
            #notification.notify(title='test', message='scrollview width:{}, grid width:{}, item width:{}'.format(root.width,layout.width,'200'),
            #toast=True)

        except Exception as e:
            print(e)
            global er
            er = str(e)            
            Alert().open()
    def empty_msg(self, instance):
        global msg
        msg =''
    def refine(self, raw):
        char = '[ ] * { } # ! $ % ^ & ( \' ) + = | " \\ ` ~ - _'
        raw = raw.split(',')
        for junk in char.split(' '):
            raw = (' '.join(raw)).split('{}'.format(junk))
        return raw
    def open_saved_contact(self, instance, *args):
        #print(self.emass[self.rest])
        print(instance)
        global f
        global created

        created = instance
        f = emass[instance]
        print('create',f[10:])
        #global current_tul
        #current_tul = 'General'
        OpenProfile().open()
        #stamped_item = rest.tx


class CreateProfiles(ModalView):
    def __init__(self,**kwargs):
        super(CreateProfiles, self).__init__(**kwargs)
        self.size_hint = (1, 1)
        self.background = 'images/effect_black.png'
        try:
            layout = GridLayout(cols=2,  padding=100, spacing=100,
                size_hint=(1, None), width=500)
            layout.bind(minimum_height=layout.setter('height'))
            count =0
            global contacts
            contacts={}
            print('msg',msg)
            data = msg.split('\n')
            print('data', data)
            for item in data:
                if item != '':
                    if '@' not in item:
                        capLock = [w for w in item.split()]
                        name = ' '.join(capLock)
                        count= 0
                    elif '@' in item:
                        count += 1
                        if count > 1:
                            email = ''.join(item.split())
                            name = '{}{}'.format(' ', name)
                            contacts[name] = email
                        else:
                            email = ''.join(item.split())
                            contacts[name] = email
                    else:
                        print('Error')
                        contacts[name] = email
            print('contact',contacts)
            for contact in contacts.keys():
                saved_contact = BoxLayout(orientation='vertical',size=(150, 150),
                            size_hint=(None, None))
                self.rest =contact_btn(source='images/contact_block.png') #, text=timestamp)
                #self.emass[self.rest] = timestamp
                self.rest.bind(on_press= partial(self.open_profile_details, contact))
                saved_contact.add_widget(self.rest)
                if len(self.refine(contact))> 1:
                    contact=self.refine(contact)
                    contact ='{} {}'.format(contact[0],contact[1])
                ellipses= '{}'.format(contact)
                if len(ellipses)>15:
                    ellipses='{}...'.format(ellipses[:15])
                saved_contact.add_widget(Label(text=ellipses, font_size=20))
                layout.add_widget(saved_contact)
            root = ScrollView(size_hint=(1, .9), 
                    pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
            root.add_widget(layout)
            box = BoxLayout(orientation='vertical',padding=10, spacing=10)
            box.add_widget(Image(source='images/generate_contacts.png', size_hint_y=None,height='40dp'))
            box.add_widget(root)
            box.add_widget(Button(text='Close',size_hint_y=None, height= '40dp', on_press = self.dismiss))
            self.add_widget(box)
            

        except Exception as e:
            print(e)
            self.e = str(e)
            self.e =e=self.e+'profile'
            global er
            er = str(e)            
            Alert().open()
        #self.on_dismiss = self.save_profiles()
        self.bind(on_dismiss=self.save_profiles)
        #self.open()

    def save_profiles(self, instance):
        from jnius import autoclass
        Environment=autoclass('android.os.Environment')
        path = Environment.getExternalStorageDirectory().getPath() + '/Easy Hacks'
        path_pic =Environment.getExternalStorageDirectory().getPath() + '/Easy Hacks' +'/create profiles'
        
        time_stamp=time.strftime("%Y%m%d_%H%M%S")+'.txt'
        
        #path_pic='/home/ben/Videos/apk/timed'
        f = open(path_pic+'/'+time_stamp, 'w')
        f.write(msg)
        notification.notify(title='test', message='Profile(s) saved {}'.format(msg),
            toast=True)
        
    def refine(self, raw):
        char = '[ ] * { } # ! $ % ^ & ( \' ) + = | " \\ ` ~ - _'
        raw = raw.split(',')
        for junk in char.split(' '):
            raw = (' '.join(raw)).split('{}'.format(junk))
        return raw
    def open_profile_details(self, instance, *args):
        try:
            #print(self.emass[self.rest])
            #print(instance)
            global contact_name
            contact_name = instance
            #print('create',f[10:])
            #ProfileDetails()
            #if current_tul=='General':
            #ProfileDetails()
            #else:
            ProfileAnalyse().open()
        except Exception as e:
            print(e)
            self.e = str(e)
            self.e =e=self.e+'profile'
            global er
            er = str(e)            
            Alert().open()


class OpenProfile(ModalView):
    def __init__(self,**kwargs):
        super(OpenProfile, self).__init__(**kwargs)
        self.size_hint = (1, 1)
        self.background = 'images/effect_black.png'
        #message = FloatLayout()
        
        layout = GridLayout(cols=2,  padding=100, spacing=100,
                size_hint=(None, None), width=500)
        layout.bind(minimum_height=layout.setter('height'))
        count =0
        global contacts
        contacts ={}
        try:
            #print('open profiles',f[10:])
            
            data = f.split('\n')
            #contacts = {}
            for item in data:
                if item != '':
                    if '@' not in item:
                        capLock = [w for w in item.split()]
                        name = ' '.join(capLock)
                        count= 0
                    elif '@' in item:
                        count += 1
                        if count > 1:
                            email = item
                            name = '{}{}'.format(' ', name)
                            contacts[name] = email
                        else:
                            email = item
                            contacts[name] = email
                    else:
                        print('Error')
                        contacts[name] = email
            print(contacts)
            for contact in contacts.keys():
                saved_contact = BoxLayout(orientation='vertical',size=(150, 150),
                            size_hint=(None, None))
                self.rest =contact_btn(source='images/contact_block.png') #, text=timestamp)
                #self.emass[self.rest] = timestamp
                self.rest.bind(on_press= partial(self.open_profile_details, contact))
                saved_contact.add_widget(self.rest)
                if len(self.refine(contact))> 1:
                    contact=self.refine(contact)
                    contact ='{} {}'.format(contact[0],contact[1])
                ellipses= '{}'.format(contact)
                if len(ellipses)>15:
                    ellipses='{}...'.format(ellipses[:15])
                saved_contact.add_widget(Label(text=ellipses, font_size=20))
                layout.add_widget(saved_contact)
            root = ScrollView(size_hint=(1, .9), 
                    pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
            root.add_widget(layout)
            box = BoxLayout(orientation='vertical',padding=10, spacing=10)
            timestamp =created
            actual_month= month[timestamp[4:6]]
            year =timestamp[:4]
            day =timestamp[6:8]
            hour = timestamp[9:11]
            minute = timestamp[11:13]
            second = timestamp[13:15]
            timed = '{} {}, {} {}:{}:{}'.format(actual_month,day,year,hour,minute,second)
            box.add_widget(Label(text='Created on {}'.format(timed), size_hint_y=None,height='40dp'))
            box.add_widget(root)
            box.add_widget(Button(text='Close',size_hint_y=None, height= '40dp', on_press = self.dismiss))
            self.add_widget(box)
            #self.open()

        except Exception as e:
            print(e)
            self.e = str(e)
            self.e =e=self.e+'profile'
            global er
            er = str(e)            
            Alert().open()
    def save_profiles(self):
        from jnius import autoclass
        Environment=autoclass('android.os.Environment')
        path = Environment.getExternalStorageDirectory().getPath() + '/Easy Hacks'
        path_pic =Environment.getExternalStorageDirectory().getPath() + '/Easy Hacks' +'/create profiles'
        time_stamp=time.strftime("%Y%m%d_%H%M%S")+'.txt'
        #path_pic ='/home/ben/Videos/apk'
        f = open(path_pic+'/'+time_stamp, 'w')
        f.write(msg)
        notification.notify(title='test', message='Profile(s) saved',
            toast=True)
        
    def refine(self, raw):
        char = '[ ] * { } # ! $ % ^ & ( \' ) + = | " \\ ` ~ - _'
        raw = raw.split(',')
        for junk in char.split(' '):
            raw = (' '.join(raw)).split('{}'.format(junk))
        return raw
    def open_profile_details(self, instance, *args):
        try:
            #print(self.emass[self.rest])
            #print(instance)
            global contact_name
            contact_name = instance
            #print('create',f[10:])
            ProfileDetails().open()
        except Exception as e:
            print(e)
            self.e = str(e)
            self.e =e=self.e+'profile'
            global er
            er = str(e)            
            Alert().open()

class ProfileAnalyse(ModalView):
    name = StringProperty('')
    email = StringProperty('')
    address =StringProperty('')
    phone =StringProperty('')
    link = StringProperty('')    
    def __init__(self,**kwargs):
        super(ProfileAnalyse, self).__init__(**kwargs)
        self.size_hint = (1, 1)
        self.background = 'images/effect_black.png'
        try:
            #message = FloatLayout()
            if current_tul=='Image Reader':
                e =[]
                l =[]
                o =[]
                p =[]
                n =[]
                
                for item in me.split('\n'):
                    if '@' in item:
                        e.append(item)
                    elif 'email' in item or 'http' in item or 'url' in item or '.com' in item or '.org' in item or '.net' in item:
                        l.append(item)
                    elif item.isnumeric()  and len(item)>6:
                        p.append(item)
                    elif  '+' in item and len(item)>6:
                        p.append(item)
                    elif item.isalpha and len(item.split())<4:
                        n.append(item)
                    elif ',' in item or len(item.split(','))>2:
                        o.append(item)
                        print('physical address', item)
                        notification.notify(title='test', message='{} saved with comma first section'.format(item),toast=True)        
                    else:
                        o.append(item)
                        print('physical address', item)
                        notification.notify(title='test', message='{} saved with without comma firsy section'.format(item),toast=True)        

                    
                self.link= '\n'.join(l)
                self.email='\n'.join(e)
                self.phone= '\n'.join(p)
                self.address='\n'.join(o)
                self.name = '\n'.join(n)
            else:
                self.name =contact_name
                if ',' in contacts[contact_name]:
                    sae =contacts[contact_name]
                    self.email = sae.split(',')[0]
                    self.link= sae.split(',')[1]
                    self.phone= sae.split(',')[2]
                    self.address=','.join(sae.split(',')[3:])
                    
                else:
                    self.email = contacts[contact_name]
                    self.link= ''
                    self.phone= ''
                    self.address=''
                #self.open()
                
            
            
            
            
            
            #self.name =contact_name
            #self.email = contacts[contact_name]
            #self.link = ''
            #self.phone =''
            #self.address =''
            #self.open()
        except Exception as e:
            print(e)
            self.e = str(e)
            self.e =e='Sorry, you can not edit twice!!'
            global er
            er = str(e)            
            Alert().open()
    def save_profile(self):
        
        n =(self.ids['name'].text)
        e =(self.ids['email'].text)
        a= (self.ids['address'].text)
        print('a value',a)
        l =(self.ids['link'].text)
        p= (self.ids['phone'].text)
        result =''
        if e!='':
            result += e
        if p!='':
            result += ','+p
            print('edited phone')
        if l!='':
            result += ','+l
        if a!='':
            result += ','+a
            print('edited add')
            notification.notify(title='test', message='{} agreein to existence result'.format(result),toast=True)        
        if current_tul=='Image Reader':
            from jnius import autoclass
            import time
            #time_stamp=time.strftime("%Y%m%d_%H%M%S")
            Environment=autoclass('android.os.Environment')
            path = Environment.getExternalStorageDirectory().getPath() + '/Easy Hacks'
            path_pic =Environment.getExternalStorageDirectory().getPath() + '/Easy Hacks' +'/create profiles'
            time_stamp=time.strftime("%Y%m%d_%H%M%S")+'.txt'
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                print('Already Created')
            if not os.path.exists(path_pic):
                os.mkdir(path_pic)
            else:
                print('Already Created')
            
            self.fn = (path_pic +    '/{}.py'.format(time_stamp))
            result = n + '\n' + result
            f = open(self.fn, 'w')
            f.write(result)
            f.close()
        else:
            global msg
            print(msg)
            msg =''
            print('result', result)
            contacts.pop(contact_name)
            contacts[n] = result
            print('cotact', contacts)
            notification.notify(title='test', message='{} result'.format(result),toast=True)        
            for item in contacts:
                msg+=item
                msg+= '\n'+contacts[item]
                msg+='\n'+'\n'
            print('after', msg)
            notification.notify(title='test', message='{}'.format(msg),toast=True)        


    
class ProfileDetails(ModalView):
    name = StringProperty('')
    email = StringProperty('')
    link = StringProperty('')
    phone = StringProperty('')
    address = StringProperty('')
    
    def __init__(self,**kwargs):
        super(ProfileDetails, self).__init__(**kwargs)
        self.size_hint = (1, 1)
        self.background = 'images/effect_black.png'
        try:
            #message = FloatLayout()
            self.name =contact_name
            if ',' in contacts[contact_name]:
                sae =contacts[contact_name]
                if len(sae.split(','))>3:
                    self.email = sae.split(',')[0]
                    self.link= sae.split(',')[1]
                    self.phone= sae.split(',')[2]
                    self.address=','.join(sae.split(',')[3:])
                else:
                    isolate =sae.split(',')
                    self.email = isolate.pop(0)
                    for item in isolate:
                        if 'http' in item or 'url' in item or '.com' in item or '.org' in item or '.net' in item:
                            
                            self.link= item
                        elif item.isnumeric() or '+' in item:
                            self.phone= item
                        else:
                            self.address=item
            else:
                self.email = contacts[contact_name]
                self.link= ''
                self.phone= ''
                self.address=''
            #self.open()
        
            #self.name =contact_name
            #self.email = contacts[contact_name]
            #self.open()
        except Exception as e:
            print(e)
            self.e = str(e)
            self.e =e=self.e+'profile'
            global er
            er = str(e)            
            Alert().open()
                
    def msg(self, instance):
        global er
        try:
            from android.permissions import request_permissions, Permission, check_permission
            if check_permission('android.permission.WRITE_EXTERNAL_STORAGE'):
                if check_permission('android.permission.READ_EXTERNAL_STORAGE'):
                    if check_permission('android.permission.CAMERA'):
                        pass
            else:
                Clock.schedule_once(lambda dt:take_permission(),.2)
            from android.storage import app_storage_path
            settings_path = app_storage_path()
            self.fn = settings_path +    '/keys.txt'
            if os.path.exists(self.fn):
                f = open(self.fn, 'r')
            
                a = f.read()
            
                data = a.split('\n')
            for item in data:
                if 'email' in item:
                    mail = item.split('=')[1]
                    print(emails,'email')
                if 'pass' in item:
                    passw = item.split('=')[1]
                    print('passw', pass_key)
                    print('user', user.text)
                if 'user' in item:
                    user = item.split('=')[1]
                    print('passw', user_name)
                    print('user', user.text)
                if 'first' in item:
                    first = item.split('=')[1]
                    print('passw', first)
                    print('user', user.text)
                if 'last' in item:
                    last = item.split('=')[1]
                    print('passw', last)
                    print('user', user.text)
            requests.put('https://easy-hacks-4eca2.firebaseio.com/users/{}/details.json'.format(mail),'{"name":"%s","last":"%s","pass":"%s","user":"%s","rating":"%s"}' %(first,last,passw,user, rating))
        except:
            pass
        try:
            if instance!='' and '@' in instance:
                from plyer import email
                recipient = instance
                subject = None
                text = 'Dear {}'.format(self.name)
                create_chooser = False
                email.send(recipient= recipient, subject= subject, text=text, create_chooser=create_chooser)
            else:
                er = 'Invalid Link'
                Alert().open()
        except Exception as e:
            
            er = str(e)
            Alert().open()
    def copy_to_click(self):
        pass
    def call(self, instance):
        try:
            global er
            #from plyer import call
            #phone = self.ids['phone']
            #call.makecall(tel =phone.text)
            inst= ''.join(instance.split('+'))
            if inst.isnumeric():
                from android import activity, mActivity
                from jnius import autoclass, cast
                String = autoclass('java.lang.String')
                Intent = autoclass('android.content.Intent')
                Uri = autoclass('android.net.Uri')
                Environment=autoclass('android.os.Environment')
                intent = Intent()
                self.msg='tel:'+'{}'.format(instance)
                intent.setAction(Intent.ACTION_DIAL)
                intent.setData(Uri.parse(self.msg))
                
                mActivity.startActivityForResult(intent,0x123)
            else:
                er = "Invalid Contact"
                Alert().open()
        except Exception as e:
            er = str(e)
            
            Alert().open()
    def open_link(self, instance):
        try:
            from android.permissions import request_permissions, Permission, check_permission
            if check_permission('android.permission.WRITE_EXTERNAL_STORAGE'):
                if check_permission('android.permission.READ_EXTERNAL_STORAGE'):
                    if check_permission('android.permission.CAMERA'):
                        pass
            else:
                Clock.schedule_once(lambda dt:take_permission(),.2)
            from android.storage import app_storage_path
            settings_path = app_storage_path()
            self.fn = settings_path +    '/keys.txt'
            if os.path.exists(self.fn):
                f = open(self.fn, 'r')
            
                a = f.read()
            
                data = a.split('\n')
            for item in data:
                if 'email' in item:
                    mail = item.split('=')[1]
                    print(emails,'email')
                if 'pass' in item:
                    passw = item.split('=')[1]
                    print('passw', pass_key)
                    print('user', user.text)
                if 'user' in item:
                    user = item.split('=')[1]
                    print('passw', user_name)
                    print('user', user.text)
                if 'first' in item:
                    first = item.split('=')[1]
                    print('passw', first)
                    print('user', user.text)
                if 'last' in item:
                    last = item.split('=')[1]
                    print('passw', last)
                    print('user', user.text)
            requests.put('https://easy-hacks-4eca2.firebaseio.com/users/{}/details.json'.format(mail),'{"name":"%s","last":"%s","pass":"%s","user":"%s","rating":"%s"}' %(first,last,passw,user, rating))
        except:
            pass
        
        try:
            global er
            if instance!='' and '.' in instance:
                from android import activity, mActivity
                from jnius import autoclass, cast
                if 'http' in instance:
                    url = '{}'.format(instance)    
                else:
                    url = 'https:{}'.format(instance) #'https://api.whatsapp.com/send?phone='+'+234 814 940 2614'+"&text="+'hello'
                String = autoclass('java.lang.String')
                Intent = autoclass('android.content.Intent')
                Uri = autoclass('android.net.Uri')
                
                intent = Intent()
                
                
                intent.setAction(Intent.ACTION_VIEW)
                intent.setData(Uri.parse(url))
                mActivity.startActivityForResult(intent,0x123)
            else:
                er='Invalid link'
                Alert().open()
        except Exception as e:
            print(e)
            
            er = str(e)            
            Alert().open()
    def map_direction(self, direction):
        try:
            from android import activity, mActivity
            from jnius import autoclass, cast
            #String = autoclass('java.lang.String')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            
            uri = Uri.parse("geo:0,0?q={}".format(direction))  #.format(direction)) #"google.navigation:q=Taronga+Zoo,+Sydney+Australia") #"geo:37.7749,-122.4194");
            intent = Intent(Intent.ACTION_VIEW, uri);
            if intent.setPackage("com.google.android.apps.maps") != None:
                mActivity.startActivity(intent)
            else:
                notification.notify(title='test', message='Please install Google Maps'.format(str(e)),toast=True)        
            
        except Exception as e:

            notification.notify(title='test', message='{}'.format(str(e)),toast=True)        
    
from kivy.app import App as pas

class Notification(pas):
    display_type = OptionProperty('normal', options=['normal', 'popup'])

    settings_popup = ObjectProperty(None, allownone=True)

    def create_settings(self):
        
        if self.settings_cls is None:
            from notification_optoins import SettingsWithNoMenu #SettingsWithSpinner #
            self.settings_cls = SettingsWithNoMenu #
        elif isinstance(self.settings_cls, string_types):
            self.settings_cls = Factory.get(self.settings_cls)
        s = self.settings_cls()
        self.build_settings(s)
        if self.use_kivy_settings:
            s.add_kivy_panel()
        s.bind(on_close=self.close_settings,
            on_config_change=self._on_config_change)
        return s
    def destroy_settings(self):
        '''.. versionadded:: 1.8.0

        Dereferences the current settings panel if one
        exists. This means that when :meth:`App.open_settings` is next
        run, a new panel will be created and displayed. It doesn't
        affect any of the contents of the panel, but lets you (for
        instance) refresh the settings panel layout if you have
        changed the settings widget in response to a screen size
        change.

        If you have modified :meth:`~App.open_settings` or
        :meth:`~App.display_settings`, you should be careful to
        correctly detect if the previous settings widget has been
        destroyed.

        '''
        if self._app_settings is not None:
            self._app_settings = None


    def sett(self):
        try:
            self.set_display_type('popup')
            self.open_settings()
        except Exception as e:
            global er
            
            er = str(e)+'Restart is required'
            Alert()
            
    def on_pause(self):
        return True
    def on_settings_cls(self, *args):
        self.destroy_settings()

    def set_settings_cls(self, panel_type):
        self.settings_cls = panel_type

    def set_display_type(self, display_type):
        self.destroy_settings()
        self.display_type = display_type
    def on_resume(self):
        pass
    def display_settings(self, settings):
        if self.display_type == 'popup':
            p = self.settings_popup
            
            
            if p is None:
                #self.btn=Button(text='Close',on_press=self.close_settings)    
                #settings.add_widget(self.btn)
                #box = BoxLayout(orientation='vertical')
                #box.add_widget(settings)
                #box.add_widget(self.btn)
                self.settings_popup = p = Popup(content=settings,
                                                title='Notifications',
                                                size_hint=(0.7, 0.5))
            if p.content is not settings:
                p.content = settings
            p.open()
        else:
            super(Notification, self).display_settings(settings)
    def close_settings(self, *args):
        if self.display_type == 'popup':
            p = self.settings_popup
            if p is not None:
                p.dismiss()
        else:
            super(Notification, self).close_settings()

class Settings(App):
    
    display_type = OptionProperty('normal', options=['normal', 'popup'])
    settings_popup = ObjectProperty(None, allownone=True)
    
        
    def create_settings(self):
        
        if self.settings_cls is None:
            from easyhacks_settings import SettingsWithSpinner #SettingsWithNoMenu
            self.settings_cls = SettingsWithSpinner #SettingsWithNoMenu
        elif isinstance(self.settings_cls, string_types):
            self.settings_cls = Factory.get(self.settings_cls)
        s = self.settings_cls()
        self.build_settings(s)
        if self.use_kivy_settings:
            s.add_kivy_panel()
        s.bind(on_close=self.close_settings,
            on_config_change=self._on_config_change)
        return s

    def sett(self):
        try:
            self.set_display_type('popup')
            self.open_settings()
        except Exception as e:
            #global er
            print('error')
            #er = 'Restart is required'
            #Alert()
            
    def on_pause(self):
        return True
    def on_settings_cls(self, *args):
        self.destroy_settings()

    def set_settings_cls(self, panel_type):
        self.settings_cls = panel_type

    def set_display_type(self, display_type):
        self.destroy_settings()
        self.display_type = display_type
    def on_resume(self):
        pass
    def display_settings(self, settings):
        if self.display_type == 'popup':
            p = self.settings_popup
            if p is None:
                self.settings_popup = p = Popup(content=settings,auto_dismiss=False,
                                                title='Settings',
                                                size_hint=(0.8, 0.8))
            if p.content is not settings:
                p.content = settings
            p.open()
        else:
            super(Settings, self).display_settings(settings)

    def close_settings(self, *args):
        if self.display_type == 'popup':
            p = self.settings_popup
            if p is not None:
                p.dismiss()
        else:
            super(Settings, self).close_settings()




class Home(Screen):
    img=ObjectProperty(None)
    cont=ObjectProperty(None)
    cont1=ObjectProperty(None)
    cont2=ObjectProperty(None)
    cont3=ObjectProperty(None)
    tools=ObjectProperty(None)
    Blur =ObjectProperty(None)
    footer = ObjectProperty(None)
    
    def __init__(self,**kwargs):
        super(Home, self).__init__(**kwargs)
        global result_mode
        global tools
        
        tools = ['Data Refinery','Nomineogen','Extractor Plus']
        result_mode = False
        self.val=False
        
        try:
            pass
            
        except                                                                                                                                                                                                                                         Exception as e:
            print(e)
            global er
            er = str(e)
            
            Alert().open()
    def dely(self):
        print('daley')
        #Clock.schedule_once(self.start_delay,.5)
        
    def start_delay(self, instance):

        self.modal = ModalView(size_hint=(1, 1))
        self.modal.background ='images/effect_empty.png'
        box = FloatLayout()
        box.add_widget(Image(source='images/tab_rotate.gif',pos_hint={'center_x':.5,'center_y':.5},size_hint=(.5,.5)))
        box.add_widget(Label(text='Loading... Please Wait...',pos_hint={'center_x':.5,'center_y':.3},size_hint=(.5,.5)))
        self.modal.add_widget(box)
        self.modal.open()
    def delay_stop(self, instance):
        self.modal.dismiss()
    

        
    def onpress(self):
        if self.val ==False:
            self.cont.opacity = 0
            self.cont1.opacity = 0
            self.cont2.opacity = 0
            self.cont3.opacity = 0
            Clock.create_trigger(Animation(x=self.width/1.65, d=.1).start(self.tools))
            #SoundLoader.load('images/vault_move.mp3').play()
            Clock.create_trigger(Animation(x=self.vault.width/ 1.83).start(self.vault))
            self.val=True

        else:
            Clock.create_trigger(Animation(x=0).start(self.vault))
            Clock.schedule_once(lambda dt: self.return_pos(),1)
            Clock.schedule_once(lambda dt: self.visible(),1.5)
            self.val =False
    
    def return_pos(self):
        Animation(x=0, d=.1).start(self.tools)
        

    def visible(self):
        if self.val ==False:
            self.cont.opacity = 1
            self.cont1.opacity = 1
            self.cont2.opacity = 1
            self.cont3.opacity = 1
    
    def contact(self):
        global result_mode
        result_mode=True
        global back_home
        back_home =True
        sm.switch_to(screen[9])
        if rating=='not_rated':
            RateUs()

    def about(self):
        result_mode
        global back_home
        back_home =True
        sm.switch_to(screen[14])
    def help(self):
        #sm.switch_to(screen[15])
        #QuitApp()
        QuitUs().open()
    def ocr(self, isinstance):
        #Clock.schedule_once(self.delay_stop, 1)
        #OCR(rslt='')*
        sm.switch_to(screen[5])

    def email_x(self, isinstance):
        #Clock.schedule_once(self.delay_stop, 1)
        #EmailExtractor(rslt='')
        sm.switch_to(screen[3])
    def neogen(self, isinstance):
        #Clock.schedule_once(self.delay_stop, 1)
        #Neogenesis(rslt='')
        sm.switch_to(screen[4])

    def shorkt(self, instance): 
        #Clock.schedule_once(self.delay_stop, 1)
        sm.switch_to(screen[2])
        

    def profile(self):
        Profiles().open()
        
    def notification(self):
        Notification().sett()
    def settings(self):
        Settings().sett()


class pointer(Image):
    cust_pos = NumericProperty(.5)
    def __init__(self, **kwargs):
        super(pointer, self).__init__(**kwargs)
        self.size_hint = (.5,.1)
        
        anim = Animation(cust_pos=.49, duration=.1)
        anim += Animation(cust_pos=.515, duration=.5)
        anim += Animation(cust_pos=.49, duration=.1)
        anim += Animation(cust_pos=.515, duration=.5)
        anim += Animation(cust_pos=.49, duration=.1)
        anim += Animation(cust_pos=.515, duration=.5)
        anim.repeat=True
        anim.start(self)
        
class pointer1(Image):
    cust_pos = NumericProperty(.5)
    def __init__(self, **kwargs):
        super(pointer1, self).__init__(**kwargs)
        self.size_hint = (.5,.1)
        
        anim = Animation(cust_pos=.49, duration=.1)
        anim += Animation(cust_pos=.515, duration=.5)
        anim += Animation(cust_pos=.49, duration=.1)
        anim += Animation(cust_pos=.515, duration=.5)
        anim += Animation(cust_pos=.49, duration=.1)
        anim += Animation(cust_pos=.515, duration=.5)
        anim.repeat=True
        anim.start(self)







class Tutorial1(Home):
    salute = saluted[0]
    task = task[0]
    pos_x = pos_x[0]
    pos_y = pos_y[0]
    mo_x = mo_x[0]
    mo_y = mo_y[0]
    value = 0
    def __init__(self,**kwargs):
        super(Tutorial1, self).__init__(**kwargs)
        #print('df',self.ids['profiles'].state)
        for item in self.ids:
            if item=='data_refine':
                self.ids[item].disabled=True
            if item=='extract_plus':
                self.ids[item].disabled=True
            if item=='neogen':
                self.ids[item].disabled=True
            if item=='img2txt':
                self.ids[item].disabled=True
        toppin = self.ids['toppin']
        print('down', bottom[self.val])
        downpin = self.ids['downpin']
        toppin.opacity =tp[self.val]
        downpin.opacity = btm[self.val]
        #self.pointer = Image(source='images/pointer.png', size_hint=(.4,.2), pos_hint={'x':.2,'y':.6})
        #self.pointer = pointer(size_hint=(.4,.2), pos_hint={'x':.3,'y':.8})
        #self.add_widget(cust_btn(source='images/pointer.png', size_hint=(1,1), pos_hint={'x':cust_btn().cust_pos,'y':.6}))
    def active(self):
        
        sm.switch_to(screen[14])
    def next_task(self):
        try:
            print(self.val)
            '''for item in self.ids:
                if item!='inneer':
                    if item!='outer':
                        if item!='next':
                            if item!='active':
                                self.ids[item].disabled=False                                                        
            print('after',self.ids['profiles'].disabled)
            for item in self.ids:
                self.ids[item].disabled=False
            
            for item in self.ids:
                if item!='profiles':
                    if item!='active':
                        self.ids[item].disabled=True'''
            global er
            if self.val==True and self.value<6:
                #print('start val', self.value)
                
                #if self.num == 3:
                #    self.num =0
                print('still before')
                er = saluted[self.value] + ',' +'\n'+task[self.value]
                Clock.schedule_once(lambda dt:Alert().open(), .2)
                self.value += 1
                #self.salute = saluted[self.value]
                self.task = task[self.value]
                self.pos_x = pos_x[0]
                print('increase val', self.value)
                self.pos_y = pos_y[self.value]
                print(self.pos_y)

                self.mov_x = mo_x[self.val]
                self.mov_y = mo_y[self.val]
                print('top',top[self.val])
                toppin = self.ids['toppin']
                print('down', bottom[self.val])
                downpin = self.ids['downpin']
                toppin.opacity =tp[self.val]
                downpin.opacity = btm[self.val]
            elif self.val and self.value>6:
                er = 'Please Bright, \n'+'Click the rotating wheel to continue'
                Clock.schedule_once(lambda dt:Alert().open(), .2)
                print(self.value,'value')
                print(self.val, 'val')
            elif self.val==False and self.value>6:
                print('now after thank')
                er = saluted[self.value] + ',' +'\n'+task[self.value]
                Clock.schedule_once(lambda dt:Alert().open(), .2)
                self.value += 1
                #self.salute = saluted[self.value]
                self.task = task[self.value]
                self.pos_x = pos_x[0]
                print('increase val', self.value)
                self.pos_y = pos_y[self.value]
                print(self.pos_y)

                self.mov_x = mo_x[self.val]
                self.mov_y = mo_y[self.val]
                print('top',top[self.val])
                toppin = self.ids['toppin']
                print('down', bottom[self.val])
                downpin = self.ids['downpin']
                toppin.opacity =tp[self.val]
                downpin.opacity = btm[self.val]
            else:
                #if self.num == 3:
                #    self.num =0
                if self.value >6:
                    er = 'Please larger, \n'+'Click the rotating wheel to continue'
                    Clock.schedule_once(lambda dt:Alert().open(), .2)
                else:
                    er = 'Please, \n'+'Click the rotating wheel to continue'
                    Clock.schedule_once(lambda dt:Alert().open(), .2)
        except:
            er = 'Tutorial session ended. Go back to the tutorial section in About Page to learn how to use the Data Refinery, Extractor Plus, Nomineogen and Image Reader'
            Clock.schedule_once(lambda dt:Alert().open(), .2)


class Neogenesis(Screen):
    emails = ObjectProperty(None)
    result_mod = BooleanProperty(False)
    rslt = StringProperty(msg)
    def __init__(self,**kwargs):
        try:
            super(Neogenesis, self).__init__(**kwargs)
            #self.size_hint = (1, 1)
            #print('rslt', rslt)
            self.result_mod = result_mode
            #self.background = 'images/effect.png'
            self.resume_result = ''
            #self.open()
            
        except Exception as e:
            self.e = str(e)
            #self.error()
            global er
            er = self.e
            Alert().open()
    
    def tip_info(self):
        message = FloatLayout()
        document = RstDocument(text=tip_neo, pos_hint={'center_x':.5, 'center_y':.55}, size_hint=(.9,.8))
        message.add_widget(document)
        butn = TransBtn(text='Close', size_hint=(.8,.1), pos_hint={'center_y':.05, 'center_x':.5}, on_press=self.pop_close)
    
        message.add_widget(butn)
        
        self.popup = Popup(title='Tip',background='trans.png',title_color=(0,0,0,1),
                    content=message,auto_dismiss=False,
                    size_hint=(.7,.6))
        

        self.popup.open()
    def pop_close(self, instance):
        self.popup.dismiss()
    
    def close(self):
        self.dismiss()
    def home(self):
        self.emails.text =''
        global tools
        tools = ['Data Refinery','Nomineogen','Extractor Plus']
        sm.switch_to(screen[1])
    def email_extract(self):
        '''This function extradts emails from jubiris information'''
        st = self.emails.text
        compare = 'gmail.comyahoo.comymail.comhotmail.comicloud.com.net.microsoftoutlook.com.org.co.ca.ng.com.ng'
        #print(st)
        s = st.split()
        xtract = []
        for item in s:
            if '@' in item:
                tail =item.index('@')
                #print(item[tail+1:])
                if len(item[:tail])>1:
                    if item[tail+1:] in compare and '.' in item[tail+1:] and len(item[tail+1:])>4:
                        ree =item[tail+1:]
                        
                        
                        
                        if len(ree.split('.')[-1])>1 and len(ree.split('.')[0])>2:
                            #append ='Tru'
                            #print(len(ree.split('.')[-1])>1)
                            #print(ree)
                            #print(ree.split('.'))
                            #print(len(ree.split('.')[0])>2)
                            xtract.append(item.lower())
                    elif '.' in item[tail+1:] and len(item[tail+1:])>4:
                        #print('synthatically valid')
                        ree =item[tail+1:]
                        
                        if len(ree.split('.')[-1])>1 and len(ree.split('.')[0])>2:
                            #append ='Tru'
                            #print(len(ree.split('.')[-1])>1)
                            #print(ree)
                            #print(ree.split('.'))
                            #print(len(ree.split('.')[0])>2)
                            xtract.append(item.lower())
        self.resume_result = '\n'.join(xtract)
        return self.resume_result
    def seat(self, instance):
        self.modal = ModalView(size_hint=(1, 1))
        self.modal.background ='images/effect_empty.png'
        box = FloatLayout()
        box.add_widget(Image(source='images/tab_rotate.gif',pos_hint={'center_x':.5,'center_y':.5},size_hint=(.5,.5)))
        box.add_widget(Label(text='Loading... Please Wait...',pos_hint={'center_x':.5,'center_y':.3},size_hint=(.5,.5)))
        self.modal.add_widget(box)
        
        self.modal.open()
    def stand(self, instance):
        self.modal.dismiss()
    
    
    def generate_emails(self, instance):
        try:
            email= self.email_extract()
            #print('extracted', email)
            global contacts
            if email:
                #email = self.emails.text
                result=''
                #print('before',result)
                result = neogenesis.magnus(email)
                #print('after',result)
                final_names = ''
                #print(r'result',result)
                
                if result:
                    if len(result)<2:
                        for item in result:
                            work = item.split(' ')
                            print('work', work)
                            email_ = work.pop()
                            name = ' '.join(work)
                            contacts[name]=email
                            #msg = '\n {}, {}'.format(msg, name, email_)
                            final_names = '{}\n\n{}\n{}'.format(final_names, name, email_)
                            #final_names = '{}\n'.format(final_names)
                        
                    else:
                        for item in result:
                            work = item.split(' ')
                            email_ = work.pop()
                            name = ' '.join(work)
                            contacts[name]=email
                            #msg = '\n {}, {}'.format(name, email_)
                            final_names = '{}\n\n{}\n{}'.format(final_names, name, email_)
                            #final_names = '{}\n'.format(final_names)
                        

                else:
                    self.alert()
                #print('final names', final_names)
                #global resume_result
                a= final_names.split('\n')
                #print('final_names',final_names)
                #print('a',a)
                a.pop(0)
                #print('first pop',a)
                a.pop(0)
                #print('second pop', a)
                print('contacts',len(contacts))
                final_names = '\n'.join(a)
                self.resume_result = final_names
                Clock.schedule_once(self.stand, 2.1)
                #print('resume result', resume_result)
                
                final_names= ''''''
                #self.display.text = final_names
            else:
                print('Please type something')
                Clock.schedule_once(self.stand, 2.1)
        
        except Exception as e:
            print(e)
            global er
            er = str(e)
            Alert().open()
    def check_result(self,instance):
        if len(self.resume_result) > 2:
            #self.dismiss()
            self.other_tools()
        else:
            Clock.schedule_once(self.stand, 2.1)
    def check_msg(self):
        print('checking')
        print('rslt', self.rslt)
        print('msg', msg)
        self.display.text = msg
        print('dislay', self.display.text)
        return self.display.text
    def camera(self):
        try:
            Clock.schedule_once(self.stand,2)
            CamBox()
            sm.switch_to(screen[5])
        except Exception as e:
            global er
            er = str(e)
            Alert().open()
    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Choose Text File", content=content,auto_dismiss=False,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        try:
            with open(os.path.join(path, filename[0])) as stream:
                self.emails.text = stream.read()
        except Exception as e:
            global er
            er = str(e)
            Alert().open()
        self.dismiss_popup()
    def dismiss_popup(self):
        self._popup.dismiss()


    def alert(self):
        popup = Popup(title='Alert!!',auto_dismiss=False,
                    content=Label(text='Please enter valid email(s)'),
                    size_hint=(.5,.3))
        popup.open()


    def other_tools(self):
        #self.close()
        #print('neo', resume_result)
        #self.blur = True
        global input_enter
        input_enter = self.emails.text
        global er
        
        deff = '{} items screened'.format(len(self.emails.text.split('\n')))
        e =len(self.emails.text.split('\n'))-len(self.resume_result.split('\n'))/2
        minus=   '{} Invalid items removed'.format(int(e))
        total ='{} items in result'.format(len(self.resume_result.split('\n')))

        er = '\n'.join(('{}.'.format(deff),'\n{}.'.format(minus),'\n{}.'.format(total)))
        global result_open
        result_open = self.emails.text
        OtherTools(current_tool='Nomineogen', result_q= self.resume_result).open()
        Clock.schedule_once(lambda dt:Alert().open(), 0)

move_x =[.9,.8]
move_y= [.35, .25]
x_task = ['Click the textbox to type the emails you want to handle. This session handles only emails','Click the attach file button to choose a file',
'Click the settings button to view available profiles','Click the camera button to open the camera to scan and extract text', 'Click the mode button to select the mode of extraction. Note: if you do not select mode, Extractor Plus will automatically extract all possible emails, phone numbers and links from your input','Note this page will leave this current page and take you to the image reader so you can process the image', 
'Click the generate button to generate possible emails from the text provided']

neo_task = ['Click the textbox to type the emails you want to handle. This session handles only emails','Click the attach file button to choose a file',
'Click the settings button to view available profiles','Click the camera button to open the camera to scan and extract text, Note this page will leave this current page and take you to the image reader so you can process the image', 
'Click the generate button to generate possible emails from the text provided']
img_task = ['Click the gallery button open your gallery and pick a picture', 
'Click the camera button to open the camera to scan and extract text', 'click the scan button to extract the text from the image or file you have provided ']

m_x =[.9,.5,.05,.05,.8, .8, .8,.8,.8]

m_y= [.35, .15,.25,.25,.25, .25,.25,.25,.25]
neo_x = [.6,.6,.5,.8, .5,.2,.5,.2,.2]
neo_y =  [-.47,-.47,-.47,-.47, -.4,-.4 -.4,-.4,-.47]
neo_top =    [1,1,0,0,0,0,0,0,0 ]
neo_bottom = [0,0,1,1,1,1,1,1, 1]
class Tutorial3(Neogenesis):
    salute = saluted[0]
    task = neo_task[0]
    pos_x = m_x[0]
    pos_y = m_y[0]
    mov_x = neo_x[0]
    mov_y = neo_y[0]
    top = neo_top[0]
    bottom = neo_bottom[0]
    val = 0
    def __init__(self,**kwargs):
        super(Tutorial3, self).__init__(**kwargs)
        '''for item in self.ids:
            if item!='':
                if item!='':
                    if item!='next':
                        self.ids[item].disabled=True
        
        '''
        self.num = 0
        #self.pointer = Image(source='images/pointer.png', size_hint=(.4,.2), pos_hint={'x':.2,'y':.6})
        #self.pointer = pointer(size_hint=(.4,.2), pos_hint={'x':.3,'y':.8})
        #self.add_widget(cust_btn(source='images/pointer.png', size_hint=(1,1), pos_hint={'x':cust_btn().cust_pos,'y':.6}))
    def active(self):
        '''previous_screen = sm.previous()
        if previous_screen =='menu':
            sm.switch_to(screen[0])
        else:
            sm.switch_to(screen[1])'''
        sm.switch_to(screen[14])
    def next_task(self):
        global er
        self.salute = saluted[self.val]
        self.task = neo_task[self.val]
        er = self.salute + self.task
        #if self.num == 3:
        #    self.num =0
        #er = saluted[self.num]
        Clock.schedule_once(lambda dt:Alert().open(), .2)
        self.val += 1
        self.pos_x = m_x[self.val]
        self.pos_y = m_y[self.val]
        self.mov_x = neo_x[self.val]
        self.mov_y = neo_y[self.val]
        #print('top',top[self.val])
        toppin = self.ids['toppin']
        #print('down', bottom[self.val])
        downpin = self.ids['downpin']
        toppin.opacity =neo_top[self.val]
        downpin.opacity = neo_bottom[self.val]

tip = '''Note: Dashes, underscores and forward slashes are ignored during refinery processes because they are commonly used in names, emails and links'''
tip_mode = '''Click the mode button by the left to get three options: Email, Link, Phone and Regex.
\n Use email to extract email address
\n Use link to extract web links
\n Use phone to extract phone numbers
\n Use regex to specify a pattern to extract. Type the pattern you wish to extract in the search box and click search. For Example: Searching for "080", "@company.com" or "www" will give you result of strings that contain "080", "@company.com" and "www" respectively.
\nNo9te:If you do not select a mode, Extractor Plus will extract all email,phone number and/or links found in your input'''

tip_neo ='''Nomineogen is a tool for handling strictly emails. It takes email input and generates potential names from it. It can also help you save the profiles created and build contacts'''

class NeogenResult(Neogenesis,ModalView):
    emails = ObjectProperty(None)
    result_mod = BooleanProperty(False)
    def __init__(self,rslt,**kwargs):
        super(Neogenesis, self).__init__(**kwargs)
        try:
            
            #self.size_hint = (1, 1)
            print('rslt', rslt)
            self.rslt = rslt
            self.emails.text = rslt
            self.result_mod = result_mode
            self.background = 'images/effect.png'
            self.resume_result = ''
            #self.open()
            #self.modal = ModalView(size_hint=(1, 1))
            #self.modal.background ='images/effect_empty.png'
            #box = FloatLayout()
            #box.add_widget(Image(source='images/tab_rotate.gif',pos_hint={'center_x':.5,'center_y':.5},size_hint=(.5,.5)))
            #box.add_widget(Label(text='Loading... Please Wait...',pos_hint={'center_x':.5,'center_y':.3},size_hint=(.5,.5)))
            #self.modal.add_widget(box)
        except Exception as e:
            self.e = str(e)
            #self.error()
            global er
            er = self.e
            Alert().open()
    def home(self):
        global tools
        tools = ['Data Refinery','Nomineogen','Extractor Plus']
        self.dismiss()
        sm.switch_to(screen[1])
    def other_tools(self):
        #self.close()
        #print('neo', resume_result)
        #self.blur = True
        self.dismiss()
        global result_open
        result_open = self.emails.text
        OtherTools(current_tool='Nomineogen', result_q= self.resume_result).open()

class Sort(Screen):
    sort_input = ObjectProperty(None)
    strin = ObjectProperty(None)
    result_mod = BooleanProperty(False)
    def __init__(self, **kwargs):
        super(Sort, self).__init__(**kwargs)
        self.result_mod = result_mode
    
        self.resume_result = ''
    
    def tip_info(self):
        message = FloatLayout()
        document = RstDocument(text=tip, pos_hint={'center_x':.5, 'center_y':.55}, size_hint=(.9,.8))
        message.add_widget(document)
        butn = TransBtn(text='Close', size_hint=(.8,.1), pos_hint={'center_y':.05, 'center_x':.5}, on_press=self.pop_close)
    
        message.add_widget(butn)
        
        self.popup = Popup(title='Tip',background='images/trans.png',title_color=(0,0,0,1),auto_dismiss=False,
                    content=message,
                    size_hint=(.7,.6))
        

        self.popup.open()
    def pop_close(self, instance):
        self.popup.dismiss()
    def close(self):
        self.dismiss()
    def clear(self):
        pass
    def tip_popup(self, instance):
        message = FloatLayout()
        document = RstDocument(text=text, pos_hint={'center_x':.5, 'center_y':.5}, size_hint=(.9,.8))
        #self.pop = Popup(Title='Tip', content=message, size_hint=(None, None), size=(400, 400))
        #message.add_widget(Label(text= msg,size_hint=(.3,.3), pos_hint={'center_x':.5,'y':.5},halign='center'))
        message.add_widget(document)
        #close = Button(text='Dismiss',size_hint=(.5,.3), pos_hint={'center_x':.5,'y':.1}, font_size=30)
        #close.bind(on_press=self.pop_close())
        #message.add_widget(close)
        popup = Popup(title='Tip',
                    content=message,auto_dismiss=False,
                    size_hint=(.7,.5))
        popup.open()
    def seat(self, instance):
        self.modal = ModalView(size_hint=(1, 1))
        self.modal.background ='images/effect_empty.png'
        box = FloatLayout()
        box.add_widget(Image(source='images/tab_rotate.gif',pos_hint={'center_x':.5,'center_y':.5},size_hint=(.5,.5)))
        box.add_widget(Label(text='Loading... Please Wait...',pos_hint={'center_x':.5,'center_y':.3},size_hint=(.5,.5)))
        self.modal.add_widget(box)
        
        self.modal.open()
    def stand(self, instance):
        
        self.modal.dismiss()
    def home(self):
        self.sort_input.text = ''
        self.strin.text = ''
        global tools
        tools = ['Data Refinery','Nomineogen','Extractor Plus']
        sm.switch_to(screen[1])
    def error_(self):
        global er
        er = 'No result found'
        
        Alert().open()
    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Choose Text File", content=content,auto_dismiss=False,
                            size_hint=(0.9, 0.9))
        self._popup.open()
    def load(self, path, filename):
        try:
            with open(os.path.join(path, filename[0])) as stream:
                self.sort_input.text = stream.read()
                self.strin.text = self.sort_input.text
                #Clock.schedule_once(lambda dt:wait(),0)
        except Exception as e:
            self.e = str(e)
            self.error()
        self.dismiss_popup()
    
    def dismiss_popup(self):
        self._popup.dismiss()
    def refine(self, raw):
        char = '[ ] * { } # ! $ % ^ & ( \' ) + = | " \\ ` ~'
        raw = raw.split(',')
        for junk in char.split(' '):
            raw = (' '.join(raw)).split('{}'.format(junk))
        return raw
    def sort_data(self, instance):
        in_data = self.sort_input.text
        process =self.refine(in_data)
        process = '\n'.join(process)
        process = process.split()
        process.sort()
        self.resume_result = '\n'.join(process)
        Clock.schedule_once(self.stand, 2)
    def shrink(self, instance):
        string_val = self.strin.text
        process = self.refine(string_val)
        process=' '.join(process)
        data =process.split()
        #data = process.split()
        result = list(dict.fromkeys(data))
        self.resume_result = '\n'.join(result)
        Clock.schedule_once(self.stand, 2)
    def camera(self):
        try:
            CamBox()
            sm.switch_to(screen[5])
        except Exception as e:
            self.e = str(e)
            self.error()
    def other_tools(self, instance):
        #self.close()
        #value = True
        #Cache.append('keys', name_key, value)
        #retry = Cache.get('keys', name_key)
        #print('retry 1',retry)
        #self.blur = retry
        
        #self.blur = True
        #sm.switch_to(screen[0])
        global result_open
        global input_enter
        input_enter = self.sort_input.text
        result_open = self.sort_input.text
        OtherTools(current_tool='Data Refinery', result_q=self.resume_result).open()

        deff = '{} items screened'.format(len(self.sort_input.text.split('\n')))
        e =len(self.sort_input.text.split('\n'))-len(self.resume_result.split('\n'))
        minus=   '{} Invalid items removed'.format(e)
        total ='{} items in result'.format(len(self.resume_result.split('\n')))
        global er 
        #er = deff+'\n'+minus+'\n'+total
        er = '\n'.join(('{}.'.format(deff),'\n{}.'.format(minus),'\n{}.'.format(total)))
        Clock.schedule_once(lambda dt:Alert().open(), 0)



    def error(self):
        global er
        er = self.e
        Alert().open()
        

class Tutorial2(Sort):
    salute = saluted[0]
    task = task[0]
    pos_x = move_x[0]
    pos_y = move_y[0]
    mov_x = mov_x[0]
    mov_y = mov_y[0]
    top = top[0]
    bottom = bottom[0]
    val = 0
    def __init__(self,**kwargs):
        super(Sort, self).__init__(**kwargs)
        '''for item in self.ids:
            if item!='':
                if item!='':
                    if item!='next':
                        self.ids[item].disabled=True
        
        '''
        self.num = 0
        #self.pointer = Image(source='images/pointer.png', size_hint=(.4,.2), pos_hint={'x':.2,'y':.6})
        #self.pointer = pointer(size_hint=(.4,.2), pos_hint={'x':.3,'y':.8})
        #self.add_widget(cust_btn(source='images/pointer.png', size_hint=(1,1), pos_hint={'x':cust_btn().cust_pos,'y':.6}))
    def active(self):
        '''previous_screen = sm.previous()
        if previous_screen =='menu':
            sm.switch_to(screen[0])
        else:
            sm.switch_to(screen[1])'''
        sm.switch_to(screen[14])
    def next_task(self):
        global er
        #if self.num == 3:
        #    self.num =0
        #er = saluted[self.num]
        Clock.schedule_once(lambda dt:Alert().open(), .2)
        self.val += 1
        self.salute = saluted[self.val]
        self.task = task[self.val]
        self.pos_x = move_x[self.val]
        self.pos_y = move_y[self.val]
        self.mov_x = mov_x[self.val]
        self.mov_y = mov_y[self.val]
        print('top',top[self.val])
        toppin = self.ids['toppin']
        print('down', bottom[self.val])
        downpin = self.ids['downpin']
        toppin.opacity =top[self.val]
        downpin.opacity = bottom[self.val]

class SortResult(Sort,ModalView):
    def __init__(self,rslt,**kwargs):
        super(Sort, self).__init__(**kwargs)
        try:
            
            #self.size_hint = (1, 1)
            print('rslt', rslt)
            self.rslt = rslt
            self.sort_input.text = rslt
            self.strin.text = rslt
            self.result_mod = result_mode
            self.background = 'images/effect.png'
            self.resume_result = ''
            #self.open()
            #self.modal = ModalView(size_hint=(1, 1))
            #self.modal.background ='images/effect_empty.png'
            #box = FloatLayout()
            #box.add_widget(Image(source='images/tab_rotate.gif',pos_hint={'center_x':.5,'center_y':.5},size_hint=(.5,.5)))
            #box.add_widget(Label(text='Loading... Please Wait...',pos_hint={'center_x':.5,'center_y':.3},size_hint=(.5,.5)))
            #self.modal.add_widget(box)
        except Exception as e:
            self.e = str(e)
            #self.error()
            global er
            er = self.e
            Alert().open()
    def other_tools(self, instance):
        #self.close()
        #value = True
        #Cache.append('keys', name_key, value)
        #retry = Cache.get('keys', name_key)
        #print('retry 1',retry)
        #self.blur = retry
        
        #self.blur = True
        self.dismiss()
        global result_open
        result_open = self.sort_input.text
        OtherTools(current_tool='Data Refinery', result_q=self.resume_result).open()
    def home(self):
        self.dismiss()
        global tools
        tools = ['Data Refinery','Nomineogen','Extractor Plus']
        sm.switch_to(screen[1])


class CamBox(ModalView):
    def __init__(self,**kwargs):
        super(CamBox, self).__init__(**kwargs)        
        global image_names
        image_names = []
        self.index = 0
        self.fn = None
        self.size_hint = (1, 1)
        self.title='Capture Image'
        self.background = 'images/black.png'
        #self.result_mod = result_mode
        self.open()
        self.root = ScrollView(size_hint=(1, .25),
                            pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_y=False)
        box =self.ids['imgs']
        self.layout = GridLayout(rows=1, padding=5, spacing=20,
                            size_hint=(None, None), height=50)
                    
        # when we add children to the grid layout, its size doesn't change at
        # all. we need to ensure that the height will be the minimum required
        # to contain all the childs. (otherwise, we'll child outside the
        # bounding box of the childs)
        self.layout.bind(minimum_width=self.layout.setter('width'))
        self.root.add_widget(self.layout)
        box.add_widget(self.root)
        
    def flash_release(self):
        try:
            from plyer import flash
            flash.release()
        except Exception as e:
            global er
            er = str(e)
            Alert().open()
    def flash_on(self):
        try:
            from plyer import flash
            flash.on()
        except Exception as e:
            global er
            er = str(e)
            Alert().open()
    def flash_off(self):
        try:
            from plyer import flash
            flash.off()
        except Exception as e:
            global er
            er = str(e)
            Alert().open()
    def aftermat(self):
        self.onCameraClick()
        #self.dismiss()
        #print('dismissed')
        #self.add_picture()
    def onCameraClick(self):
        global image_names
        
        try:
            self.index += 1
            from jnius import autoclass
            time_stamp=time.strftime("%Y%m%d_%H%M%S")
            Environment=autoclass('android.os.Environment')
            path = Environment.getExternalStorageDirectory().getPath() + '/Easy Hacks'
            path_pic =Environment.getExternalStorageDirectory().getPath() + '/Easy Hacks' +'/images'
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                print('Already Created')
            if not os.path.exists(path_pic):
                os.mkdir(path_pic)
            else:
                print('Already Created')
            
            self.fn = (path_pic +    '/{}.jpg'.format(time_stamp))
            #self.fn ='/home/ben/Music/Easy Hacks/selfie_{}.png'.format(time_stamp)
            cameraObject=self.ids['cam']
            #print(self.fn,'onCamera')
            global fn_dir
            fn_dir =self.fn
            global image_names
            cameraObject.export_to_png(self.fn) 
            #print('picture taking')
            #print('saving in', self.fn)
            #OCR(rslt='').fn = self.fn
            global er
            if capture<2:
                pass
            else:
                try:
                    #carls = self.ids['car_info']
                    #carls.clear_widgets()
                    image_names.append(fn_dir)
                    #print(image_names)
                    #carls.add_widget(Image(source=fn_dir,pos_hint={'center_y':.5,'center_x':.5}))
                    self.layout.clear_widgets()
                    # add button into that grid
                    for img in image_names:
                        btn = Image(source=img, size=(100, 80),size_hint=(None, None))
                        self.layout.add_widget(btn)
                except Exception as e:
                    print(e)
                    #global er
                    er = str(e)            
                    Alert().open()

        except Exception as e:
            print(e)
            #global er
            er = str(e)            
            Alert().open()
        
    def add_image(self):
        notification.notify(title='test', message='Please click the view image(s) button to see image',toast=True)        
        self.layout.clear_widgets()
        global image_names
        image_names=[]
        #OCR(rslt='').add_picture()
        
    def pop_close(self):
        notification.notify(title='test', message='Please click the view image(s) button to see image',toast=True)        
        self.layout.clear_widgets()
        #self.dismiss()
        #OCR().add_picture()
        
    

#layout = BoxLayout(orientation='vertical')
class Img(Image):
    pass
text = '''
.. _top:
Single Capture takes one picture and allows you to crop. With 
Bulk Capture you can take as many shot at a go. On 
completion img2txt will convert the bulk images into a single
file of text for you
'''

class OCR(Screen):
    path = StringProperty()
    capture = NumericProperty(capture)
    fn = ObjectProperty(None)
    result_mod = BooleanProperty(False)
    

    def __init__(self, **kwargs):
        super(OCR, self).__init__(**kwargs)        
        self.index = 0
        self.result_mod = result_mode
        self.fn = None
        self.res_resume = "Sorry!! You haven't performed any action"
        self.clear = None
        self.modals = ModalView(size_hint=(1, 1))
        self.modals.background ='images/effect_empty.png'
        self.rect =RectangleFlatButton(text='View Image(s)', size_hint=(.5,.05), pos_hint={'y':.08,'center_x':.5}, on_press=self.add_picture, disabled=True, opacity=0)
        self.add_widget(self.rect)
        box = FloatLayout()
        box.add_widget(Image(source='images/tab_rotate.gif',pos_hint={'center_x':.5,'center_y':.5},size_hint=(.5,.5)))
        box.add_widget(Label(text='Loading... Please Wait...',pos_hint={'center_x':.5,'center_y':.3},size_hint=(.5,.5)))
        self.modals.add_widget(box)

    def close(self):
        try:
            self.dismiss()
        except Exception as e:
            global er
            er = str(e)            
            Alert().open()
    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Choose an Image File", content=content,auto_dismiss=False,
                            size_hint=(0.9, 0.9))
        self._popup.open()
    def filechooser(self):
        try:
            from jnius import autoclass,cast
            from android import activity, mActivity
            # python-for-android provides this
            #from android import activity

            #PythonActivity = autoclass('org.renpy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')

            # Value of MediaStore.Images.Media.DATA
            MediaStore_Images_Media_DATA = "_data"

            # Custom request codes
            RESULT_LOAD_IMAGE = 1

            Activity = autoclass('android.app.Activity')
            
            
            #from jnius import autoclass
            #Environment=autoclass('android.os.Environment')
            #self.dir = Environment.getExternalStorageDirectory().getPath()
            
            #import gallery
            #gallery
            #fn_dir =gallery.user_select_image(self.dir)
            
            
            '''Open Gallery Activity and call callback with absolute image filepath of image user selected.
            None if user canceled.
            '''

            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our
            # PythonActivity.
            # We need to cast our class into an activity and use it
            #currentActivity = cast('android.app.Activity', mActivity.mActivity)

            # Forum discussion: https://groups.google.com/forum/#!msg/kivy-users/bjsG2j9bptI/-Oe_aGo0newJ
            def on_activity_result(request_code, result_code, intent):
                if request_code != RESULT_LOAD_IMAGE:
                    #Logger.warning('user_select_image: ignoring activity result that was not RESULT_LOAD_IMAGE')
                    return

                if result_code == Activity.RESULT_CANCELED:
                    #Clock.schedule_once(lambda dt: callback(None), 0)
                    return

                if result_code != Activity.RESULT_OK:
                    # This may just go into the void...
                    raise NotImplementedError('Unknown result_code "{}"'.format(result_code))

                selectedImage = intent.getData();  # Uri
                filePathColumn = ['data'] #[MediaStore_Images_Media_DATA]; # String[]
                # Cursor
                #cursor = mActivity.getContentResolver().query(selectedImage,
                #        filePathColumn, None, None, None);
                cursor = mActivity.getContentResolver().openOutputStream(selectedImage)
                #        filePathColumn, None, None, None);
                #cursor.moveToFirst();

                # int
                #columnIndex = cursor.getColumnIndex(filePathColumn[0]);
                # String
                picturePath = cursor.getString(columnIndex);
                #cursor.close();
                #Logger.info('android_ui: user_select_image() selected %s', picturePath)

                # This is possibly in a different thread?
                #Clock.schedule_once(lambda dt: callback(picturePath), 0)
                
                
                global image_names
                image_names =[]
                image_names.append(picturePath)
                self.rect.disabled=False
                self.rect.opacity= 1
                notification.notify(title='test', message='Please click the view image(s) button to see image',toast=True)        
                notification.notify(title='test', message='cursor:{}'.format(cursor),toast=True)        
                

            
            activity.bind(on_activity_result=on_activity_result)

            intent = Intent()
            Environment=autoclass('android.os.Environment')
            
            intent.setAction(Intent.ACTION_GET_CONTENT)
            
            #intent.setData(Uri.parse(Environment.getExternalStorageDirectory().getPath()))
            #intent.setData(Uri.parse('content://media/internal/images/media'))
            intent.setType("*/*")

            mActivity.startActivityForResult(intent, RESULT_LOAD_IMAGE)

            
        except Exception as e:
            global er
            er = str(e)            
            Alert().open()
    def file_picker(self):
        content = FloatLayout()
        
        self.single = TransBtn(text='Default Explorer',size_hint=(.7,.1), pos_hint={'center_x':.5,'y':.65}, on_press=self.pref_online )
        self.multiple = TransBtn(text='Provisional Explorer', size_hint=(.7, .1), pos_hint={'center_x': .5, 'y': .4}, on_press=self.pref_offline)
        self.cancel = TransBtn(text='Cancel', size_hint=(.7, .1), pos_hint={'center_x': .5, 'y': .15}, on_press=self.close_load)
        content.add_widget(self.single)
        
        content.add_widget(self.multiple)
        content.add_widget(self.cancel)
        self.login_preference = Popup(title='Image Picker Preference',background='images/grey_shade.png',title_color=(0,0,0,1),
                        content=content,auto_dismiss=False,
                        size_hint=(.7,.7))
        self.login_preference.open()
    def pref_online(self, instance):
        self.filechooser()
        self.login_preference.dismiss()
    def pref_offline(self, instance):
        
        self.show_load()
        self.login_preference.dismiss()
    def close_load(self, instance):
        
        self.login_preference.dismiss()
    def seat(self, instance):
        self.modals.open()
    def stand(self, instance):
        self.modals.dismiss()
    
    def load(self, path, filename):
        try:
            global fn_dir
            fn_dir = filename[0]
            global image_names
            image_names=[]
            image_names.append(fn_dir)
            
            carls = self.ids['car_info']
            carls.clear_widgets()
            
            notification.notify(title='test', message='path: {}'.format(str(fn_dir)),toast=True)        
            carls.add_widget(Image(source=fn_dir,pos_hint={'center_y':.5,'center_x':.5}, size_hint=(.7,.7)))
            with open(os.path.join(path, filename[0])) as stream:
                pass
            notification.notify(title='test', message='Path: {}, filename:{}, stream:{}'.format(path, filename, stream),toast=True)        
        except Exception as e:
            self.e = str(e)
            self.error()
        self.dismiss_popup()
    def dismiss_popup(self):
        self._popup.dismiss()
    def home(self):

        global tools
        tools = ['Data Refinery','Nomineogen','Extractor Plus']
        sm.switch_to(screen[1])
    
    def expiry_date(self, instance):
        from datetime import date
        from dateutil.relativedelta import relativedelta
        commission_date= date(2020, 9, 19)
        expiry_date = commission_date+ relativedelta(days=+29)
        current_date = date.today() 
        if current_date<expiry_date:
            #'licenced'
            self.image2txt()
        else:
            #'expired'
            Clock.schedule_once(self.stand, 2)
            global er
            er = 'Sorry, Easy Hacks requires an update for you to continue using this feature. We apologise for any inconvenience'
            Clock.schedule_once(lambda dt:Alert().open(), 2.1)

        #+ relativedelta(days=+29)


    def cam(self, instance):
        try:
            #self.blur = True
            self.rect.disabled=False
            self.rect.opacity= 1
            
            Clock.schedule_once(self.stand, 2)
            CamBox()
            
        except Exception as e:
            global er
            er = str(e)            
            Alert().open()
    def add_picture(self, instance):
        try:
            if len(image_names)==0:
                notification.notify(title='test', message='Sorry, No available image(s) to view',toast=True)        
            elif len(image_names)==1:
                
                carls = self.ids['car_info']
                carls.clear_widgets()
                try:
                    self.layout.clear_widgets()
                except:
                    pass
                #notification.notify(title='test', message='path: {}'.format(str(fn_dir)),toast=True)        
                carls.add_widget(Image(source=image_names[0],pos_hint={'center_y':.5,'center_x':.5},size_hint=(.7,.7)))
            else:
                carls = self.ids['car_info']
                carls.clear_widgets()
                #for img in image_names:
                #    carls.add_widget(Image(source=img,pos_hint={'center_y':.5,'center_x':.5}))
                flot =self.ids['float']
                self.root = ScrollView( do_scroll_y=False,size_hint=(1,.15),
                    pos_hint={'center_y':.25,'center_x':.5})
                self.layout = GridLayout(rows=1,spacing=20,
                                    size_hint=(None, None), height=100)
                self.layout.bind(minimum_width=self.layout.setter('width'))
                self.root.add_widget(self.layout)
                #image_names.append(fn_dir)
                #print(image_names)
                #carls.add_widget(Image(source=fn_dir,pos_hint={'center_y':.5,'center_x':.5}))
                self.layout.clear_widgets()
                # add button into that grid
                
                for img in image_names:
                    btn = Image(source=img, size=(100, 80),size_hint=(None, None))
                    self.layout.add_widget(btn)
                #box.add_widget(self.root)
                flot.add_widget(self.root)
        except Exception as e:
            print(e)
            global er
            er = str(e)            
            Alert().open()

    def gallery(self):
        try:
            from jnius import autoclass,cast
            from android import activity, mActivity
            # python-for-android provides this
            #from android import activity

            #PythonActivity = autoclass('org.renpy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')

            # Value of MediaStore.Images.Media.DATA
            MediaStore_Images_Media_DATA = "_data"

            # Custom request codes
            RESULT_LOAD_IMAGE = 1

            Activity = autoclass('android.app.Activity')
            
            
            #from jnius import autoclass
            #Environment=autoclass('android.os.Environment')
            #self.dir = Environment.getExternalStorageDirectory().getPath()
            
            #import gallery
            #gallery
            #fn_dir =gallery.user_select_image(self.dir)
            
            
            '''Open Gallery Activity and call callback with absolute image filepath of image user selected.
            None if user canceled.
            '''

            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our
            # PythonActivity.
            # We need to cast our class into an activity and use it
            #currentActivity = cast('android.app.Activity', mActivity.mActivity)

            # Forum discussion: https://groups.google.com/forum/#!msg/kivy-users/bjsG2j9bptI/-Oe_aGo0newJ
            def on_activity_result(request_code, result_code, intent):
                if request_code != RESULT_LOAD_IMAGE:
                    #Logger.warning('user_select_image: ignoring activity result that was not RESULT_LOAD_IMAGE')
                    return

                if result_code == Activity.RESULT_CANCELED:
                    #Clock.schedule_once(lambda dt: callback(None), 0)
                    return

                if result_code != Activity.RESULT_OK:
                    # This may just go into the void...
                    raise NotImplementedError('Unknown result_code "{}"'.format(result_code))

                selectedImage = intent.getData();  # Uri
                filePathColumn = [MediaStore_Images_Media_DATA]; # String[]
                # Cursor
                cursor = mActivity.getContentResolver().query(selectedImage,
                        filePathColumn, None, None, None);
                cursor.moveToFirst();

                # int
                columnIndex = cursor.getColumnIndex(filePathColumn[0]);
                # String
                picturePath = cursor.getString(columnIndex);
                cursor.close();
                #Logger.info('android_ui: user_select_image() selected %s', picturePath)

                # This is possibly in a different thread?
                #Clock.schedule_once(lambda dt: callback(picturePath), 0)
                
                
                global image_names
                image_names =[]
                image_names.append(picturePath)
                self.rect.disabled=False
                self.rect.opacity= 1
                notification.notify(title='test', message='Please click the view image(s) button to see image',toast=True)        
                notification.notify(title='test', message='Path: {}, columnIndex:{}, cursor:{},selectedImage:{}'.format(picturePath, columnIndex, cursor,selectedImage),toast=True)        
                

            # See: http://pyjnius.readthedocs.org/en/latest/android.html
            activity.bind(on_activity_result=on_activity_result)

            intent = Intent()

            # http://programmerguru.com/android-tutorial/how-to-pick-image-from-gallery/
            # http://stackoverflow.com/questions/18416122/open-gallery-app-in-android
            intent.setAction(Intent.ACTION_PICK)
            # TODO internal vs external?
            intent.setData(Uri.parse('content://media/internal/images/media'))
            #intent.setData(Uri.parse('*.*'))
            #setType(Image)

            mActivity.startActivityForResult(intent, RESULT_LOAD_IMAGE)
            
        except Exception as e:
            global er
            er = str(e)            
            Alert().open()
    
    def pop_up(self):
        self.modal = ModalView(size_hint=(1, 1))
        self.modal.background ='images/effect_empty.png'
        content = FloatLayout()
        content.add_widget(Label(text = 'Select your preference',size_hint=(.5,.3), pos_hint={'center_x':.5,'y':.55}, font_size=50))
        self.single = Button(text='Single Capture',size_hint=(.5,.05), pos_hint={'center_x':.5,'y':.5} )
        self.multiple = Button(text='Bulk Capture', size_hint=(.5, .05), pos_hint={'center_x': .5, 'y': .35})
        self.close = Button(text='Dismiss', size_hint=(.5, .05), pos_hint={'center_x': .5, 'y': .2})
        self.tip = Button(text='Tip', size_hint=(.1, .05), pos_hint={'right': 1, 'top': 1})
        self.single.bind(on_press=self.single_capture)
        self.multiple.bind(on_press=self.multiple_capture)
        self.tip.bind(on_press=self.tip_popup)
        self.close.bind(on_press=self.pop_close)
        content.add_widget(self.single)
        content.add_widget(self.multiple)
        content.add_widget(self.tip)
        content.add_widget(self.close)
        self.modal.add_widget(content)
        
        
        self.modal.open()
        self.res_resume = "Sorry!! You haven't performed any action"
        #self.modal.on_dismiss = self.dismal
    def other_tools(self):
        #self.dismiss()
        #self.blur = True
        #global result_open
        #result_open = self.sort_input.text
        OtherTools(current_tool='Image Reader', result_q=self.res_resume).open()    
        return self.capture
    def single_capture(self, instance):
        self.capture=1
        self.set_capture()
        self.modal.dismiss()
        # sm.switch_to(Menu())
        #self.modal_capture.open()
    def set_capture(self):
        global capture
        capture =self.capture
    def multiple_capture(self, instance):
        self.capture=4
        self.set_capture()
        self.modal.dismiss()
    def tip_popup(self, instance):
        message = FloatLayout()
        document = RstDocument(text=text, pos_hint={'center_x':.5, 'center_y':.5}, size_hint=(.9,.8))
        #self.pop = Popup(Title='Tip', content=message, size_hint=(None, None), size=(400, 400))
        #message.add_widget(Label(text= msg,size_hint=(.3,.3), pos_hint={'center_x':.5,'y':.5},halign='center'))
        message.add_widget(document)
        #close = Button(text='Dismiss',size_hint=(.5,.3), pos_hint={'center_x':.5,'y':.1}, font_size=30)
        #close.bind(on_press=self.pop_close())
        #message.add_widget(close)
        popup = Popup(title='Tip',auto_dismiss=False,
                    content=message,
                    size_hint=(.7,.5))
        popup.open()
    def pop_close(self, instance):
        self.capture=1
        self.set_capture()
        self.modal.dismiss()
    def close(self):
        #self.blur = False
        self.dismiss()
    def anypro(self, instance):
        #AnaPro()
        global current_tul
        current_tul='Image Reader'
        ProfileAnalyse().open()
    def image2txt(self):
        print(fn_dir)
        try:
            self.resume_result =''
            self.result_record =''
            RequestUrl = "http://www.ocrwebservice.com/restservices/processDocument?gettext=true";

            # Extract text with English and german language using zonal OCR
            #RequestUrl = 'http://www.ocrwebservice.com/restservices/processDocument?language=english,german&zone=0:0:600:400,500:1000:150:400';

            # Convert first 5 pages of multipage document into doc and txt
            # RequestUrl = 'http://www.ocrwebservice.com/restservices/processDocument?language=english&pagerange=1-5&outputformat=doc,txt';

            #Full path to uploaded document
            FilePath = fn_dir #'/home/ben/Documents/MASTERCARD FOUNDATION SCHOLARS PROGRAM APPLICATION FORM.pdf' #"C:\\test_image.jpg"

            with open(FilePath, 'rb') as image_file:
                image_data = image_file.read()
                
            r = requests.post(RequestUrl, data=image_data, auth=(UserName, LicenseCode))

            if r.status_code == 401:
                #Please provide valid username and license code
                print("Unauthorized request")
                exit()

            # Decode Output response
            jobj = json.loads(r.content)

            ocrError = str(jobj["ErrorMessage"])

            if ocrError != '':
                    #Error occurs during recognition
                    print ("Recognition Error: " + ocrError)
                    exit()

            print('first',self.resume_result)
            # Task description
            
            a ="Task Description:" + str(jobj["TaskDescription"])
            self.result_record += a
            # Available pages 
            b ="Available Pages:" + str(jobj["AvailablePages"])
            self.result_record += '\n'+b
            # Processed pages 
            c = "Processed Pages:" + str(jobj["ProcessedPages"])
            self.result_record += '\n'+c
            # For zonal or multipage OCR: OCRText[z][p]    z - zone, p - pages
            print('second',self.resume_result)
            # Extracted text from first or single page
            d = str(jobj["OCRText"][0][0])
            self.resume_result += '\n'+d
            print('third',self.resume_result)
            # Extracted text from second page (if multipage doc converted)
            #print("Extracted Text:" + str(jobj["OCRText"][0][1]))

            # Get extracted text from First zone for each page
            e =str(jobj["OCRText"][0][0])
            self.resume_result += '\n'+e
            f = str(jobj["OCRText"][0][1])
            self.resume_result += '\n'+f
            # Get extracted text from Second zone for each page
            #print("Zone 2 Page 1 Text:" + str(jobj["OCRText"][1][0]))
            #print("Zone 2 Page 2 Text:" + str(jobj["OCRText"][1][1]))

            #Download output file (if outputformat was specified)
            #file_response = requests.get(jobj["OutputFileUrl"], stream=True)
            #with open("outputDoc.doc", 'wb') as output_file:
            #   shutil.copyfileobj(file_response.raw, output_file)
            self.resume_result = '{} \n{} \n{} \n{} \n{} \n{}'.format(a,b,c,d,e,f)
            Clock.schedule_once(self.stand, 2)
            Clock.schedule_once(lambda dt:self.other_tools(), 2.1)
        except Exception as e:
        
            Clock.schedule_once(self.stand, 2)
            self.e = str(e)
            print(fn_dir)
            print(self.resume_result)
            global er
            er = 'Please ensure you have internet access\n' +  str(e)
            print(self.result_record)
            #self.other_tools()
            if len(self.resume_result)>2:
                Clock.schedule_once(lambda dt:self.other_tools(), 2.01)
                er = self.result_record
                Clock.schedule_once(lambda dt:Alert().open(), 2.01)
                
            
    def other_tools(self, instance):
        global result_open
        self.resume_result=''
        OtherTools(current_tool='Image Reader', result_q= self.resume_result).open


class ResultMode(FloatLayout):
    def open_link(self):
        try:
            from android import activity, mActivity
            from jnius import autoclass, cast
            url = 'http://www.google.com' #'https://api.whatsapp.com/send?phone='+'+234 814 940 2614'+"&text="+'hello'
            String = autoclass('java.lang.String')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            
            intent = Intent()
            
            
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse(url))
            mActivity.startActivityForResult(intent,0x123)
        except Exception as e:
            print(e)
            global er
            er = str(e)            
            Alert().open()
    def show_errors(self):
        input_e = input_enter.split()
        print(input_e)
        print(msg)
        result = msg.split()
        invalids = []
        for item in input_e:
            for ite in result:
                if item!= ite:
                    invalids.append(item)
        global er
        if len(invalids)> 0:
            er = ' '.join(invalids)
        else:
            er= 'No invalids found'
        Tip()

    def notify(self):
        try:
            
            #notification.notify(title='test', message='brightoadewole@gmail.com,tabdevelopers@yahoo.com,tabdeveloperscorrespondence@gmail.com',
            #app_name='Easy Hacks', app_icon='pad.png', ticker='hi',timeout=10,toast='Easy Hacks has messaged you')
            #notification.notify(title='test', message='brightoadewole@gmail.com,tabdevelopers@yahoo.com,tabdeveloperscorrespondence@gmail.com',
            #toast=True)
            notification.notify(title='Your result is ready', message='brightoadewole@gmail.com,tabdevelopers@yahoo.com,tabdeveloperscorrespondence@gmail.com',
            app_name='Easy Hacks')
            notification.notify(title='test', message='brightoadewole@gmail.com,tabdevelopers@yahoo.com,tabdeveloperscorrespondence@gmail.com',
            app_name='Easy Hacks', app_icon='images/pad.png', ticker='We know',timeout=10)
            
        except Exception as e:
            global er
            er = str(e)
            Alert().open()
    def screenshot(self):
        try:
            from plyer import screenshot
        
            from jnius import autoclass
            Environment=autoclass('android.os.Environment')
            self.dir = Environment.getExternalStorageDirectory().getPath()
            #a= '/home/ben/Music/Easy Hacks/selfie_34.jpg'
            screenshot.file_path=self.dir+'/screenshot.png'
            screenshot.capture()
        except Exception as e:
            global er
            er = str(e)
            Alert().open()
    def file_choose(self):
        try:
            from plyer import filechooser
            from jnius import autoclass
            Environment=autoclass('android.os.Environment')
            self.dir = Environment.getExternalStorageDirectory().getPath()
            filechooser.choose_dir(file_path=self.dir)
        except Exception as e:
            global er
            er = str(e)
            Alert().open()
    def new_email(self):
        try:
            from android import activity, mActivity
            from jnius import autoclass, cast
            String = autoclass('java.lang.String')
            Intent = autoclass('android.content.Intent')
            #Uri = autoclass('android.net.Uri')
            #Environment=autoclass('android.os.Environment')
            intent = Intent()
            self.msg='{}'.format('brightoadewole@gmail.com')
            #uri =Uri.parse("smsto:"+'+2348149402614')
            intent.setAction(Intent.ACTION_SEND)
            #smsText='hi'
            #intent(Intent.ACTION_SENDTO, uri)
            #intent.setPackage("com.whatsapp")
            #intent.putExtra("sms_body", smsText)
            intent.putExtra(Intent.EXTRA_SUBJECT, cast('java.lang.CharSequence', String('Hello')))
            intent.putExtra(Intent.EXTRA_EMAIL, 'Thanks for trying')
            intent.putExtra(Intent.EXTRA_TEXT, cast('java.lang.CharSequence', String('{}'.format(self.msg))))
            intent.setType('text/html') #text message
            
            #global fn_dir
            #self.e =intent.setAction(Intent.ACTION_PICK)
            #intent.setData(Uri.parse('content://media/internal/images/media'))
            mActivity.startActivityForResult(intent,0x123)
        except Exception as e:
            print(e)
            global er
            er = str(e)            
            Alert().open()

    def whatsapp(self):
        try:
            from android import activity, mActivity
            from jnius import autoclass, cast
            url = 'https://api.whatsapp.com/send?phone='+'+2348149402614'+"&text="+'hello'
            String = autoclass('java.lang.String')
            Intent = autoclass('android.content.Intent')
            #Uri = autoclass('android.net.Uri')
            #Environment=autoclass('android.os.Environment')
            intent = Intent()
            self.msg='{}'.format(msg)
            #uri =Uri.parse("smsto:"+'+2348149402614')
            intent.setAction(Intent.ACTION_VIEW)
            #smsText='hi'

            #intent(Intent.ACTION_SENDTO, uri)
            #intent.setPackage("com.whatsapp")
            #intent.putExtra("sms_body", smsText)
            #intent.putExtra(Intent.EXTRA_SUBJECT, cast('java.lang.CharSequence', String('Fast Perception')))
            #intent.putExtra(Intent.EXTRA_TEXT, cast('java.lang.CharSequence', String('{}'.format(self.msg))))
            #intent.setType('text/plain') #text message
            
            #global fn_dir
            #self.e =intent.setAction(Intent.ACTION_PICK)
            intent.setData(Uri.parse(url))
            mActivity.startActivityForResult(intent,0x123)
        except Exception as e:
            print(e)
            global er
            er = str(e)            
            Alert().open()

    def share(self):
        try:
            from android import activity, mActivity
            from jnius import autoclass, cast
            String = autoclass('java.lang.String')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            Environment=autoclass('android.os.Environment')
            intent = Intent()
            self.msg='{}'.format(msg)
            intent.setAction(Intent.ACTION_SEND)
            #intent.setPackage("com.instagram.android") #"com.truecaller") 
            intent.putExtra(Intent.EXTRA_SUBJECT, cast('java.lang.CharSequence', String('Fast Perception')))
            intent.putExtra(Intent.EXTRA_TEXT, cast('java.lang.CharSequence', String('{}'.format(self.msg))))
            intent.setType('text/plain') #text message

            #global fn_dir
            #self.e =intent.setAction(Intent.ACTION_PICK)
            #intent.setData(Uri.parse('content://media/internal/images/media'))
            mActivity.startActivityForResult(intent,0x123)
        except Exception as e:
            print(e)
            global er
            er = str(e)            
            Alert().open()

    def delete_(self):
        global er
        try:
            #contact = JsonStore('contact.json')
            #we = contact.get('dict')['name']
            #self.e =we
            #self.error_()
            e ='Still under construction'
            #global er
            er = e
            Alert().open()
        except Exception as e:
            print(e)
            #global er
            er = str(e)            
            Alert().open()
    def save_result(self):
        try:
            from android.permissions import request_permissions, Permission
            request_permissions(
                [Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.CAMERA, Permission.CALL_PHONE,Permission.SEND_SMS])
        except:
            print('android storage permission')
        
        try:
            #store = JsonStore('save_num.json')
            #store.put('saved' ,name=msg)
            from jnius import autoclass
            import time
            time_stamp=time.strftime("%Y%m%d_%H%M%S")
            Environment=autoclass('android.os.Environment')
            path = Environment.getExternalStorageDirectory().getPath() + '/Easy Hacks'
            path_pic =Environment.getExternalStorageDirectory().getPath() + '/Easy Hacks' +'/saved items'
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                print('Already Created')
            if not os.path.exists(path_pic):
                os.mkdir(path_pic)
            else:
                print('Already Created')
            self.fn = (path_pic +    '/{}.py'.format(time_stamp))
            f = open(self.fn, 'w')
            f.write(msg)
            f.close
            #self.fn ='/home/ben/Music/Easy Hacks/selfie_{}.png'.format(time_stamp)
            #cameraObject=self.ids['cam']
            #print(self.fn,'onCamera')
            #global fn_dir
            #fn_dir =self.fn
            #cameraObject.export_to_png(self.fn) 
            #print('picture taking')
            #print('saving in', self.fn)
            #OCR(rslt='').fn = self.fn
        except Exception as e:
            print(e)
            global er
            er = str(e)            
            Alert().open()


quick_tip = '\n'.join(("The page below displays your result. You can click the Nomineogen button to generate possible names for emails.", 
"Use Data Refinery to, Sort:arrange the data in logical order or Shrink: button to remove duplicates. Extractor Plus can extract emails from your result", 
"\nFYI: Should you choose to proceed with screening the data using other tools, you wont",
"be allow to return to previously used tools. If you want to end the current session of screening or start a new session click the 'Return Home' button below"))


class ResultHead(BoxLayout):
    pass





class OtherTools(ModalView):
    def __init__(self, current_tool,result_q, **kwargs):
        super(OtherTools, self).__init__(**kwargs)
        self.size_hint=(1, 1)
        global tools
        global result_open
        result_open = True
        #print('total searched',result_open)
        #print('first',result_q)class Other
        #print(tools)
        print(tools)
        print(current_tool)
        if current_tool != 'Image Reader':
            tools.remove(current_tool)
        self.background ='images/grey_shade.jpg' #'images/new_back.png' #
        content = FloatLayout()
        #content = self.ids['content']
        #print(result_q)
        self.result_q = result_q
        global msg
        #effect_tool=self.ids['tools']
        msg = result_q
        global current_tul
        if result_q=='':
            print('empty')
            txt = "Sorry!! You haven't performed any action"
            self.document = TextInput(text ='',hint_text=txt, pos_hint={'x': .2, 'center_y': .525}, size_hint=(.75, .7))
        elif "Sorry!! You haven't performed any action" in result_q:
            print('message')
            self.result_q = ''
            self.document = TextInput(text ='',hint_text=result_q, pos_hint={'x': .2, 'center_y': .525}, size_hint=(.75, .7))
        else:
            #print('go')
            self.document = TextInput(text=result_q, pos_hint={'x': .2, 'center_y': .525}, size_hint=(.75, .7)) #,input_type='text',keyboard_suggestion=True,use_bubble=True,allow_copy=True)
        #content.add_widget(self.document)
        calc = '\n'.join(
            [str(n + 1) for n in range(len(self.document.text.split('\n')))]) if self.document.focus else '\n'.join(
            [str(n + 1) for n in range(len(self.document.text.split('\n')))])
        number_line = TextInput(text=calc, pos_hint={'x': .05, 'center_y': .525}, size_hint=(.15, .7), disabled=True, halign='center')
        #content.add_widget(number_line)
        do_more = 'You have reach the limit of this feature.\nIf you would like to do more please click the more button'

        if len(tools)>0:
            lab_text = 'Info'
        else:
            lab_text = do_more
        #content.add_widget(
        #        Image(source='images/result1.png', size_hint=(.5, .1), pos_hint={'center_x': .5, 'top': 1})) #, font_size=50))
        content.add_widget(ResultHead())
        content.add_widget(ResultBody())
                
        if len(tools) == 3:
            self.single = TransBtn(text=tools[0], size_hint=(.28, .05), pos_hint={'x': .05, 'y': .1}, font_size=25) #,ripple_color=(0.8, 0.8, 0.8, 0.5))
            self.double = TransBtn(text=tools[1], size_hint=(.28, .05), pos_hint={'center_x': .5, 'y': .1},font_size=25) #,on_press=self.dbl)
            self.triple = TransBtn(text=tools[2], size_hint=(.28, .05), pos_hint={'right': .95, 'y': .1}, font_size=25) #,on_press=self.tpl)
            self.single.bind(on_release=self.sgl)
            self.double.bind(on_release=self.dbl)
            self.triple.bind(on_release=self.tpl)
            content.add_widget(self.single)
            content.add_widget(self.double)
            content.add_widget(self.triple)

        elif len(tools) == 2:
            self.single = TransBtn(text=tools[0], size_hint=(.43, .05), pos_hint={'x': .05, 'y': .1})
            self.double = TransBtn(text=tools[1], size_hint=(.43, .05), pos_hint={'right': .95, 'y': .1})
            self.single.bind(on_release=self.sgl)
            self.double.bind(on_release=self.dbl)
            content.add_widget(self.single)
            content.add_widget(self.double)
        elif len(tools) == 1:
            self.single = TransBtn(text=tools[0], size_hint=(.9, .05), pos_hint={'center_x': .5, 'y': .1})
            self.single.bind(on_release=self.sgl)
            content.add_widget(self.single)

        else:
            self.single = TransBtn(text='More', size_hint=(.9, .05), pos_hint={'center_x': .5, 'y': .1})
            self.single.bind(on_release=self.sgl)
            content.add_widget(self.single)
        if current_tool=='Nomineogen':
            current_tul='Nomineogen'
            #eff = EffectWidget()
            self.create_profile = TransBtn(text='Create Profile(s)', size_hint=(.43, .05), pos_hint={'x': .05, 'y': .025})
            #self.effect_reference = EffectBase(glsl=effect_string_colors_)
            self.create_profile.bind(on_press=self.open_profiles)
            #eff.add_widget(self.create_profile)
            #eff.effects=[self.effect_reference]
            #self.create_profile.bind(on_press = self.open_profiles)
            content.add_widget(self.create_profile)
            #content.add_widget(eff)
            self.close = TransBtn(text='Return Home', size_hint=(.43, .05), pos_hint={'right': .95, 'y': .025},on_press=self.dis)
        elif current_tool=='Extractor Plus':
            #eff = EffectWidget()
            self.create_profile = TransBtn(text='Call, Email or Browse', size_hint=(.43, .05), pos_hint={'x': .05, 'y': .025}, font_size=20)
            #self.effect_reference = EffectBase(glsl=effect_string_colors_)
            self.create_profile.bind(on_press=self.contact)
            #eff.add_widget(self.create_profile)
            #eff.effects=[self.effect_reference]
            #self.create_profile.bind(on_press = self.open_profiles)
            content.add_widget(self.create_profile)
            #content.add_widget(eff)
            self.close = TransBtn(text='Return Home', size_hint=(.43, .05), pos_hint={'right': .95, 'y': .025},on_press=self.dis)
        elif current_tool=='Image Reader':
            #global current_tul
            current_tul='Image Reader'
            self.create_profile = TransBtn(text='Create Profile', size_hint=(.43, .05), pos_hint={'x': .05, 'y': .025})
            #self.effect_reference = EffectBase(glsl=effect_string_colors_)
            self.create_profile.bind(on_press=self.analyse)
            #eff.add_widget(self.create_profile)
            #eff.effects=[self.effect_reference]
            #self.create_profile.bind(on_press = self.open_profiles)
            content.add_widget(self.create_profile)
            #content.add_widget(eff)
            self.close = TransBtn(text='Return Home', size_hint=(.43, .05), pos_hint={'right': .95, 'y': .025},on_press=self.dis)
            

        else:
            self.close = TransBtn(text='Return Home', size_hint=(.9, .05), pos_hint={'center_x': .5, 'y': .025},on_release=self.dis)
        self.tip = RectangleFlatButton(text='Tip', size_hint=(.15, .05), pos_hint={'right': 1, 'top': 1}, on_release=self.tip_popup)
        self.current_tool = current_tool
        #self.tip.bind()
        #self.close.bind()
        content.add_widget(self.tip)
        content.add_widget(self.close)
        self.add_widget(content)
        #effect_tool.add_widget(content)
        content.add_widget(ResultMode())
        #effect_tool.add_widget(ResultMode())
        #self.modal.add_widget(content)
        

        #self.add_widget(self.modal)
        #self.open()
        #Clock.schedule_once(self.delay, .5)
        #self.modal.open()
    def result_set(self):
        global result_mode
        result_mode =True
    
    def contact(self, contact):
        
        Call()
    def analyse(self, instance):
        global current_tul
        current_tul='Image Reader'
        ProfileAnalyse().open()
    def dis(self, instance):
        #tools.append(self.current_tool)
        value = False
        self.dismiss()
        global tools
        global contacts
        contacts={}
        tools = ['Data Refinery','Nomineogen','Extractor Plus']
        sm.switch_to(screen[1])
        


    def open_profiles(self, instance):
        CreateProfiles().open()

        


    def tip_popup(self, instance):
        message = FloatLayout()
        document = RstDocument(text=quick_tip, pos_hint={'center_x':.5, 'center_y':.55}, size_hint=(.9,.7))
        message.add_widget(document)

        butn = TransBtn(text='Close', size_hint=(.8,.1), pos_hint={'center_y':.05, 'center_x':.5}, on_press=self.pop_close)
    
        message.add_widget(butn)
        
        self.popup = Popup(title='Tip',background = 'images/grey_shade.jpg',auto_dismiss=False,
                    content=message,title_color=(0,0,0,1),
                    size_hint=(.7,.5))
        self.popup.open()
    def pop_close(self, instance):
        self.popup.dismiss()

    def sgl(self, instance):
        print(instance)
        self.result_set()
        self.dismiss()
        global contacts
        contacts={}
        
        if self.single.text=='Nomineogen':
            #self.dismiss()
            NeogenResult(rslt=self.result_q).open()
            
            
        elif self.single.text=='Extractor Plus':
            #self.dismiss()
            ExtractPlus(rslt = self.result_q).open()
            #sm.switch_to(screen[2])
        
        elif self.single.text=='More':
            #self.dismiss()
            #Contact()
            sm.switch_to(screen[14])
            print('here')
        elif self.single.text == 'Data Refinery':
            SortResult(rslt = self.result_q).open()
        else:
            pass


    def dbl(self, instance):
        global contacts
        contacts={}
        self.result_set()
        self.dismiss()
        if self.double.text=='Data Refinery':
            SortResult(rslt = self.result_q).open()
        elif self.double.text=='Nomineogen':
            NeogenResult(rslt= self.result_q).open()
        elif self.double.text=='Extractor Plus':
            ExtractPlus(rslt = self.result_q).open()
        
        else:
            pass

    def tpl(self, instance):
        self.result_set()
        self.dismiss()
        global contacts
        contacts={}
        
        if self.triple.text=='Data Refinery':
            SortResult(rslt = self.result_q).open()
        elif self.triple.text=='Nomineogen':
            NeogenResult(rslt=self.result_q).open()
        elif self.triple.text=='Extractor Plus':
            ExtractPlus(rslt= self.result_q)
        else:
            pass

class ResultBody(BoxLayout):
    result_info = StringProperty('')
    def __init__(self, **kwargs):
        super(ResultBody, self).__init__(**kwargs)
        self.result_info =msg
    

class CarlView(Carousel):
    def on_touch_move(self, touch):
        pass

class Contact(Screen):
    result_mod = BooleanProperty(False)
    def __init__(self, **kwargs):
        super(Contact, self).__init__(**kwargs)
        self.size_hint=(1, 1)
        self.background = 'images/effect.png'
        
        #self.open()
        self.result_mod = result_mode
        #RateUs()
    def close(self):
        #self.dismiss()
        previous_screen = sm.previous()
        
    def home(self):
        global back_home
        print(back_home, 'check value')
        if back_home==True:
            print('going home')
            sm.switch_to(screen[1])
            
            back_home = False
        else:
            sm.switch_to(screen[0])
        
    def whatsapp(self):
        try:
            '''from android import activity, mActivity
            from jnius import autoclass, cast
            String = autoclass('java.lang.String')
            Intent = autoclass('android.content.Intent')
            #Uri = autoclass('android.net.Uri')
            #Environment=autoclass('android.os.Environment')
            intent = Intent()
            self.msg='{}'.format(msg)
            #uri =Uri.parse("smsto:"+'+2348149402614')
            intent.setAction(Intent.ACTION_SEND)
            #smsText='hi'
            #intent(Intent.ACTION_SENDTO, uri)
            intent.setPackage("com.whatsapp")
            #intent.putExtra("sms_body", smsText)
            intent.putExtra(Intent.EXTRA_SUBJECT, cast('java.lang.CharSequence', String('Fast Perception')))
            intent.putExtra(Intent.EXTRA_TEXT, cast('java.lang.CharSequence', String('{}'.format(self.msg))))
            intent.setType('text/plain') #text message
            
            #global fn_dir
            #self.e =intent.setAction(Intent.ACTION_PICK)
            #intent.setData(Uri.parse('content://media/internal/images/media'))
            mActivity.startActivityForResult(intent,0x123)'''
            from android import activity, mActivity
            from jnius import autoclass, cast
            url = 'https://api.whatsapp.com/send?phone='+'+2347066282414'+"&text="+'hello'
            String = autoclass('java.lang.String')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            #Environment=autoclass('android.os.Environment')
            intent = Intent()
            self.msg='{}'.format(msg)
            #uri =Uri.parse("smsto:"+'+2348149402614')
            intent.setAction(Intent.ACTION_VIEW)
            #smsText='hi'

            #intent(Intent.ACTION_SENDTO, uri)
            #intent.setPackage("com.whatsapp")
            #intent.putExtra("sms_body", smsText)
            #intent.putExtra(Intent.EXTRA_SUBJECT, cast('java.lang.CharSequence', String('Fast Perception')))
            #intent.putExtra(Intent.EXTRA_TEXT, cast('java.lang.CharSequence', String('{}'.format(self.msg))))
            #intent.setType('text/plain') #text message
            
            #global fn_dir
            #self.e =intent.setAction(Intent.ACTION_PICK)
            intent.setData(Uri.parse(url))
            mActivity.startActivityForResult(intent,0x123)
        except Exception as e:
            print(e)
            global er
            er = str(e)            
            Alert().open()
    def insta(self):
        try:
            '''from android import activity, mActivity
            from jnius import autoclass, cast
            String = autoclass('java.lang.String')
            Intent = autoclass('android.content.Intent')
            #Uri = autoclass('android.net.Uri')
            #Environment=autoclass('android.os.Environment')
            intent = Intent()
            self.msg='{}'.format(msg)
            #uri =Uri.parse("smsto:"+'+2348149402614')
            intent.setAction(Intent.ACTION_SEND)
            #smsText='hi'
            #intent(Intent.ACTION_SENDTO, uri)
            intent.setPackage("com.instagram.android")
            #intent.putExtra("sms_body", smsText)
            intent.putExtra(Intent.EXTRA_SUBJECT, cast('java.lang.CharSequence', String('Fast Perception')))
            intent.putExtra(Intent.EXTRA_TEXT, cast('java.lang.CharSequence', String('{}'.format(self.msg))))
            intent.setType('text/plain') #text message
            
            #global fn_dir
            #self.e =intent.setAction(Intent.ACTION_PICK)
            #intent.setData(Uri.parse('content://media/internal/images/media'))
            mActivity.startActivityForResult(intent,0x123)'''
            from android import activity, mActivity
            from jnius import autoclass, cast
            url = 'http://instagram.com/_u/tab_developers' #'https://api.whatsapp.com/send?phone='+'+234 814 940 2614'+"&text="+'hello'
            String = autoclass('java.lang.String')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            #Environment=autoclass('android.os.Environment')
            intent = Intent()
            self.msg='{}'.format(msg)
            #uri =Uri.parse("smsto:"+'+2348149402614')
            intent.setAction(Intent.ACTION_VIEW)
            #smsText='hi'

            #intent(Intent.ACTION_SENDTO, uri)
            #intent.setPackage("com.whatsapp")
            #intent.putExtra("sms_body", smsText)
            #intent.putExtra(Intent.EXTRA_SUBJECT, cast('java.lang.CharSequence', String('Fast Perception')))
            #intent.putExtra(Intent.EXTRA_TEXT, cast('java.lang.CharSequence', String('{}'.format(self.msg))))
            #intent.setType('text/plain') #text message
            
            #global fn_dir
            #self.e =intent.setAction(Intent.ACTION_PICK)
            intent.setData(Uri.parse(url))
            mActivity.startActivityForResult(intent,0x123)
        except Exception as e:
            print(e)
            global er
            er = str(e)            
            Alert().open()

    def phone(self):
        try:
            from android import activity, mActivity
            from jnius import autoclass, cast
            String = autoclass('java.lang.String')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            Environment=autoclass('android.os.Environment')
            intent = Intent()
            self.msg='tel:'+'+2347066282414'
            intent.setAction(Intent.ACTION_DIAL)
            intent.setData(Uri.parse(self.msg))
            mActivity.startActivityForResult(intent,0x123)
        except Exception as e:
            global er
            er = str(e)
            Alert().open()
    def send_message(self):
        try:
            from android.permissions import request_permissions, Permission, check_permission
            if check_permission('android.permission.WRITE_EXTERNAL_STORAGE'):
                if check_permission('android.permission.READ_EXTERNAL_STORAGE'):
                    if check_permission('android.permission.CAMERA'):
                        pass
            else:
                Clock.schedule_once(lambda dt:take_permission(),.2)
            from android.storage import app_storage_path
            settings_path = app_storage_path()
            self.fn = settings_path +    '/keys.txt'
            if os.path.exists(self.fn):
                f = open(self.fn, 'r')
            
                a = f.read()
            
                data = a.split('\n')
            for item in data:
                if 'email' in item:
                    mail = item.split('=')[1]
                    #print(emails,'email')
                if 'pass' in item:
                    passw = item.split('=')[1]
                    #print('passw', pass_key)
                    #print('user', user.text)
                if 'user' in item:
                    user = item.split('=')[1]
                    #print('passw', user_name)
                    #print('user', user.text)
                if 'first' in item:
                    first = item.split('=')[1]
                    #print('passw', first)
                    #print('user', user.text)
                if 'last' in item:
                    last = item.split('=')[1]
                    #print('passw', last)
                    #print('user', user.text)
            requests.put('https://easy-hacks-4eca2.firebaseio.com/users/{}/details.json'.format(mail),'{"name":"%s","last":"%s","pass":"%s","user":"%s","rating":"%s"}' %(first,last,passw,user, rating))
        except:
            pass
        
        try:
            global er
            from plyer import email
            recipient = 'tabdevelopers@yahoo.com,tabdeveloperscorrespondence@gmail.com'
            subject = self.ids['subject'].text
            text = self.ids['message'].text
            create_chooser = False
            if len(subject.split())>0 and len(text.split())>0:
                email.send(recipient= recipient, subject= 'Easy Hacks Feedback: '+subject, text='Dear TAB DEVELOPERS,\n'+text, create_chooser=create_chooser)
                Clock.schedule_once(lambda dt:self.empty_form(), .3)
            else:
                
                er ='Please fill the forms properly'
                Alert().open()
        except Exception as e:
            
            er = str(e)
            Alert().open()
    def empty_form(self):
        self.ids['subject'].text=''
        self.ids['message'].text=''


class SortText(TextInput):
    pass


class About(Screen):

    txt = StringProperty(None)
    quicklessons= StringProperty(quicklessons)
    txt2 = StringProperty(easyhacks_intro)
    #txt3 = StringProperty(None)
    def __init__(self, **kwargs):
        super(About, self).__init__(**kwargs)
        self.txt = text_string
        try:
            from android.permissions import request_permissions, Permission, check_permission
            if check_permission('android.permission.WRITE_EXTERNAL_STORAGE'):
                if check_permission('android.permission.READ_EXTERNAL_STORAGE'):
                    if check_permission('android.permission.CAMERA'):
                        pass
            else:
                Clock.schedule_once(lambda dt:take_permission(),.2)
            from android.storage import app_storage_path
            settings_path =app_storage_path()
            self.fn = settings_path +    '/keys.txt'
            if os.path.exists(self.fn):
                f = open(self.fn, 'r')
                #print('before')
                a = f.read()
                #print('after')
                data = a.split('\n')
            
                if 'loggedin' in data:
                    f.close()
                    
                else:
                    for item in self.ids:
                        if item=='d' or item =='i' or item =='n' or item=='h' or item =='e':
                            self.ids[item].disabled=True
            else:
                for item in self.ids:
                    if item=='d' or item =='i' or item =='n' or item=='h' or item =='e':
                        self.ids[item].disabled=True
        except:
            for item in self.ids:
                if item=='d' or item =='i' or item =='n' or item=='h' or item =='e':
                    self.ids[item].disabled=True        
    def close(self):
        #self.dismiss()
        global back_home
        if back_home==True:
            sm.switch_to(screen[1])
            print('going home')
            
            back_home = False
        else:
            sm.switch_to(screen[0])
            print('going menu')
    def insta(self):
        try:
            '''from android import activity, mActivity
            from jnius import autoclass, cast
            String = autoclass('java.lang.String')
            Intent = autoclass('android.content.Intent')
            #Uri = autoclass('android.net.Uri')
            #Environment=autoclass('android.os.Environment')
            intent = Intent()
            self.msg='{}'.format(msg)
            #uri =Uri.parse("smsto:"+'+2348149402614')
            intent.setAction(Intent.ACTION_SEND)
            #smsText='hi'
            #intent(Intent.ACTION_SENDTO, uri)
            intent.setPackage("com.instagram.android")
            #intent.putExtra("sms_body", smsText)
            intent.putExtra(Intent.EXTRA_SUBJECT, cast('java.lang.CharSequence', String('Fast Perception')))
            intent.putExtra(Intent.EXTRA_TEXT, cast('java.lang.CharSequence', String('{}'.format(self.msg))))
            intent.setType('text/plain') #text message
            
            #global fn_dir
            #self.e =intent.setAction(Intent.ACTION_PICK)
            #intent.setData(Uri.parse('content://media/internal/images/media'))
            mActivity.startActivityForResult(intent,0x123)'''
            from android import activity, mActivity
            from jnius import autoclass, cast
            url = 'http://instagram.com/_u/tab_developers' #'https://api.whatsapp.com/send?phone='+'+234 814 940 2614'+"&text="+'hello'
            String = autoclass('java.lang.String')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            #Environment=autoclass('android.os.Environment')
            intent = Intent()
            self.msg='{}'.format(msg)
            #uri =Uri.parse("smsto:"+'+2348149402614')
            intent.setAction(Intent.ACTION_VIEW)
            #smsText='hi'

            #intent(Intent.ACTION_SENDTO, uri)
            #intent.setPackage("com.whatsapp")
            #intent.putExtra("sms_body", smsText)
            #intent.putExtra(Intent.EXTRA_SUBJECT, cast('java.lang.CharSequence', String('Fast Perception')))
            #intent.putExtra(Intent.EXTRA_TEXT, cast('java.lang.CharSequence', String('{}'.format(self.msg))))
            #intent.setType('text/plain') #text message
            
            #global fn_dir
            #self.e =intent.setAction(Intent.ACTION_PICK)
            intent.setData(Uri.parse(url))
            mActivity.startActivityForResult(intent,0x123)
        except Exception as e:
            print(e)
            global er
            er = str(e)            
            Alert().open()

        
    def home_tutor(self):
        global er
        #if self.num == 3:
        #    self.num =0
        
        er = 'Welcome, \n'+'Click the rotating wheel to view options and then click next for further instructions'
        Clock.schedule_once(lambda dt:Alert().open(), .2)
        sm.switch_to(screen[6])
    def neogen_tutor(self):
        global er
        #if self.num == 3:
        #    self.num =0
        er = 'Welcome, \n'+'Click the Tip button  to get important information about this page and then click next for further instructions'
        Clock.schedule_once(lambda dt:Alert().open(), .3)
        sm.switch_to(screen[7])
    def data_tutor(self):
        global er
        #if self.num == 3:
        #    self.num =0
        er = 'Welcome, \n'+'Click the Tip button  to get important information about this page and then click next for further instructions'
        Clock.schedule_once(lambda dt:Alert().open(), .2)
        sm.switch_to(screen[8])
    def extract_tutor(self):
        global er
        #if self.num == 3:
        #    self.num =0
        er = 'Welcome, \n'+'Click the Tip button  to get important information about this page and then click next for further instructions'
        Clock.schedule_once(lambda dt:Alert().open(), .2)
        sm.switch_to(screen[11])
    def ocr_tutor(self):
        global er
        #if self.num == 3:
        #    self.num =0
        er = 'Welcome, \n'+'Click the attach file button to choose a file'
        Clock.schedule_once(lambda dt:Alert().open(), .2)
        sm.switch_to(screen[10])


    


i_x =[.3,.5,.05,.05,.8, .8, .8,.8,.8]

i_y= [.2, .15,.25,.25,.25, .25,.25,.25,.25]
img_x = [.1,.2,.8,.5,.8, .5,.2,.5,.2,.2]
img_y =  [-.47,.17,.17,-.47, -.4,-.4 -.4,-.4,-.47]
img_top =    [1,0,0,0,0,0,0,0,0 ]
img_bottom = [0,1,1,1,1,1,1,1, 1]

class Tutorial4(OCR):
    salute = saluted[0]
    task = img_task[0]
    pos_x = i_x[0]
    pos_y = i_y[0]
    mov_x = img_x[0]
    mov_y = img_y[0]
    top = img_top[0]
    bottom = img_bottom[0]
    val = 0
    def __init__(self,**kwargs):
        super(Tutorial4, self).__init__(**kwargs)
        '''for item in self.ids:
            if item!='':
                if item!='':
                    if item!='next':
                        self.ids[item].disabled=True
        
        '''
        self.num = 0
        #self.pointer = Image(source='images/pointer.png', size_hint=(.4,.2), pos_hint={'x':.2,'y':.6})
        #self.pointer = pointer(size_hint=(.4,.2), pos_hint={'x':.3,'y':.8})
        #self.add_widget(cust_btn(source='images/pointer.png', size_hint=(1,1), pos_hint={'x':cust_btn().cust_pos,'y':.6}))
    def active(self):
        '''previous_screen = sm.previous()
        if previous_screen =='menu':
            sm.switch_to(screen[0])
        else:
            sm.switch_to(screen[1])'''
        sm.switch_to(screen[14])
    def next_task(self):
        global er
        #if self.num == 3:
        #    self.num =0
        #er = saluted[self.num]
        self.salute = saluted[self.val]
        self.task = img_task[self.val]
        er = self.salute + self.task
        Clock.schedule_once(lambda dt:Alert().open(), .2)
        self.val += 1
        
        self.pos_x = m_x[self.val]
        self.pos_y = m_y[self.val]
        self.mov_x = img_x[self.val]
        self.mov_y = img_y[self.val]
        #print('top',top[self.val])
        toppin = self.ids['toppin']
        #print('down', bottom[self.val])
        downpin = self.ids['downpin']
        toppin.opacity =img_top[self.val]
        downpin.opacity = img_bottom[self.val]



px_x =[.9,.5,.05,.05,.8, .8, .8,.8,.8]

px_y= [.35, .15,.25,.25,.25, .25,.25,.25,.25]
xt_x = [.6,.6,.5,.1, .5,.1,.2,.5,.2,.2]
xt_y =  [-.47,-.47,-.47,-.2,-.47, -.4,-.4 -.4,-.4,-.47]
xt_top =    [1,1,0,0,0,0,0,0,0 ]
xt_bottom = [0,0,1,1,1,1,1,1, 1]
class Tutorial5(EmailExtractor):
    salute = saluted[0]
    task = x_task[0]
    pos_x = px_x[0]
    pos_y = px_y[0]
    mov_x = xt_x[0]
    mov_y = xt_y[0]
    top = xt_top[0]
    bottom = xt_bottom[0]
    val = 0
    def __init__(self,**kwargs):
        super(Tutorial5, self).__init__(**kwargs)
        '''for item in self.ids:
            if item!='':
                if item!='':
                    if item!='next':
                        self.ids[item].disabled=True
        
        '''
        self.num = 0
        #self.pointer = Image(source='images/pointer.png', size_hint=(.4,.2), pos_hint={'x':.2,'y':.6})
        #self.pointer = pointer(size_hint=(.4,.2), pos_hint={'x':.3,'y':.8})
        #self.add_widget(cust_btn(source='images/pointer.png', size_hint=(1,1), pos_hint={'x':cust_btn().cust_pos,'y':.6}))
    def active(self):
        '''previous_screen = sm.previous()
        if previous_screen =='menu':
            sm.switch_to(screen[0])
        else:
            sm.switch_to(screen[1])'''
        sm.switch_to(screen[14])
    def next_task(self):
        global er
        #if self.num == 3:
        #    self.num =0
        #er = saluted[self.num]
        self.salute = saluted[self.val]
        self.task = x_task[self.val]
        er = self.salute + self.task
        Clock.schedule_once(lambda dt:Alert().open(), .2)
        self.val += 1
        
        self.pos_x = m_x[self.val]
        self.pos_y = m_y[self.val]
        self.mov_x = neo_x[self.val]
        self.mov_y = neo_y[self.val]
        #print('top',top[self.val])
        toppin = self.ids['toppin']
        #print('down', bottom[self.val])
        downpin = self.ids['downpin']
        toppin.opacity =neo_top[self.val]
        downpin.opacity = neo_bottom[self.val]



Factory.register('EmailExtractor', cls=EmailExtractor)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('Neogenesis', cls=Neogenesis)
Factory.register('Sort', cls=Sort)
Factory.register('OCR', cls=OCR)


sm =ScreenManager(transition=FadeTransition())

class ActivityNote(Screen):
    time = NumericProperty(0)
    def __init__(self, **kwargs):
        super(ActivityNote, self).__init__(**kwargs)
        
        self.start = 0
        Clock.schedule_interval(self._update_clock, 1/15)
        
        
    def _update_clock(self, dt):
        
        global screen
        self.start += 1
        if self.start ==1:
        
            screen =[]
            screen.append(Menu(name='0'))
        if self.start ==2:
            self.add_widget(Image(source='images/easy_hacks_splash.png', size_hint=(.8,.6), pos_hint={'center_x':.5, 'y':.5}))
            screen.append(Home(name='1'))
        if self.start ==3:
            #self.add_widget(Image(source='images/new_back.png', size_hint=(1,1), pos_hint={'center_x':.5, 'center_y':.5}, allow_stretch=True, keep_ratio=False))
            self.add_widget(Image(source='images/tab_rotate.gif', size_hint=(.3,.4), pos_hint={'center_x':.5, 'y':.3}))
            screen.append(Sort(name='2') )
        if self.start ==4:
            
            screen.append(EmailExtractor(name='3'))
        if self.start ==5:
            
            screen.append(Neogenesis(name='4'))
        if self.start ==6:
            #notification.notify(title='test', message='{}'.format(file_uri))
            
            screen.append( OCR(name='5'))
        if self.start ==7:
            
            screen.append(Tutorial1(name='6'))
        if self.start ==8:
            
            screen.append(Tutorial3(name='7'))
        if self.start ==9:
            
            screen.append(Tutorial2(name='8'))
        if self.start ==10:
            
            screen.append(Contact(name='9'))
            
        if self.start ==11:
            
            screen.append(Tutorial4(name='10'))
        if self.start ==12:
            
            screen.append(Tutorial5(name='11'))
        if self.start ==13:
            
            screen.append(CreateAccount(name='12'))
        if self.start ==14:
            
            screen.append(LoginScreen(name='13'))
        if self.start ==15:
            
            screen.append(About(name='14'))
            Clock.unschedule(self._update_clock, 1/16)
            sm.switch_to(screen[0])
        
            


        self.time = len(screen)


class EasyHacks(App):
    def build(self):
        sm.add_widget(ActivityNote(name='activity')) 
        from kivy.core.window import Window
        Window.bind(on_keyboard=self.key_input)
        return sm
    
    def key_input(self, window, key, *args):
        if key == 27:
            QuitUs().open()
            return True  # override the default behaviour
        else:           # the key now does nothing
            return False
        
if __name__ == '__main__':
    try:
        
    
        #from jnius import cast
        #from jnius import autoclass
        #import android
        #import android.activity
        #PythonActivity = autoclass('org.renpy.android')
        #activity = PythonActivity.mActivity
        #intent = activity.getIntent()
        from android import activity, mActivity
        from jnius import autoclass, cast
        #String = autoclass('java.lang.String')
        Intent = autoclass('android.content.Intent')
        Uri = autoclass('android.net.Uri')
        #Environment=autoclass('android.os.Environment')
        intent = Intent()
        #self.msg='tel:'+'{}'.format(instance)
        #intent.setAction(Intent.ACTION_DIAL)
        #intent.setData(Uri.parse(self.msg)
        intent_data = intent.getData()
        def de():
            global file_uri
            try:

                file_uri = intent_data.toString()
            except Exception as e:
                file_uri = str(intent_data)
        #de()
    except:
        print('Not android')
        #file_uri = 'mue out'
    EasyHacks().run()


