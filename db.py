from ops import mongo
import time
from bson.objectid import ObjectId


def find_participants(q={}):
    return mongo.db.participants.find(q, {'_id': False})


def base_user_template():
    return {
        'username': '',
        'twitter_username': '',
        'profile_pic': 'new_avatar.png',
        'tagline': '',
        'computers': [],
        'contributors': [],
        'updates': []
    }


def find_user(username=None, uid=None, strip_id=False):
    ''':returns: participant object if user exists, None otherwise'''
    if uid:
        if type(uid) is str:
            uid = ObjectId(uid)
        elif type(uid) is ObjectId:
            pass
        else:
            return None
        user_doc = mongo.db.participants.find_one({'_id': uid})

    user_doc = None

    if strip_id:
        user_doc = mongo.db.participants.find_one({'username': username})
        if user_doc:
            user_doc['id'] = str(user_doc['_id'])
            user_doc.pop('_id')
    else:
        user_doc = mongo.db.participants.find_one({'username': username})
    return user_doc


class DBO(object):
    '''
    {
        id, #
    }
    '''
    def __init__(self, _id=None):
        self.id = _id

    def load(self):
        '''Reads the data from the database'''
        pass

    def save(self):
        pass


class MongoDBO(DBO):
    '''
    {
        dbo: DBO,
        col: string,
        db:  string
    }
    '''
    def __init__(self):
        DBO.__init__(self)

    def __getitem__(self, k):
        return self.__dict__[k]

    def collection(self):
        raise NotImplementedError('collection() must be implemented by a subclass')

    def insert(self):
        self.collection().insert(self.__dict__)

    def save(self):
        self.collection().save(self.__dict__)


class Participant(MongoDBO):
    '''
    {
        parent: MongoDBO,
        contributors: listof Participants?,
        name: string,
        username: string,
        uptime: #,
        computers: listof Computers,
        requests: listof Requests
    }
    '''
    def __init__(self, username=None, name=None, load=False):
        MongoDBO.__init__(self)
        self.computers = []
        self.username = username
        self.name = name
        self.requests = []
        self.contributors = []
        if load:
            self.load(find_user(self.username))

    def __gt__(self, other):
        '''Compares uptime'''
        return self.uptime() > other.uptime()

    def collection(self):
        return mongo.db.participants

    def save_participant(self):
        '''Method to convert Participant into a dictionary'''
        return self.__dict__

    def load_participant(self, data):
        '''Method to convert Participant into a dictionary'''
        for k, v in data.items():
            self.__dict__[k] = v

    load = load_participant


class Person(Participant):
    '''
    {
        participant: Participant
    }
    '''
    def __init__(self, username=None, name=None):
        Participant.__init__(self, username, name)

    def save_person(self):
        return self.__dict__

    def load_person(self, data):
        '''Method to convert Participant into a dictionary'''
        if 'username' in data:
            self.username = data['username']
        if 'name' in data:
            self.name = data['name']
        if 'computers' in data:
            self.computers = data['computers']
        if 'requests' in data:
            self.requests = data['requests']
        if 'contributors' in data:
            self.contributors = data['contributors']


class Organization(Participant):
    '''
    {
        participant: Participant,
        leaders: listof Participants
    }
    '''
    def __init__(self, username=None, name=None):
        Participant.__init__(self)
        self.leaders = []

    def save_organization(self):
        return self.__dict__

    def load_organization(self, data):
        if 'username' in data:
            self.username = data['username']
        if 'name' in data:
            self.name = data['name']
        if 'computers' in data:
            self.computers = data['computers']
        if 'requests' in data:
            self.requests = data['requests']
        if 'contributors' in data:
            self.contributors = data['contributors']
        if 'leaders' in data:
            self.leaders = data['leaders']


class Computer(MongoDBO):
    '''
    {
        'uptime': int, #  (hours),
        'info': {
            'os': str,
            'ram': str,
            'cores': int,
            ...
        },
        connection_info: {
            'stuff': ...
        }
    }
    '''
    def __init__(self):
        MongoDBO.__init__(self)
        self.uptime = 0
        self.info = {}
        self.connection_info = {}

    def save_computer(self):
        return self.__dict__

    def load_computer(self, data):
        if 'name' in data:
            self.name = data['name']
        if 'uptime' in data:
            self.uptime = data['uptime']
        if 'info' in data:
            self.info = data['info']
        if 'connection_info' in data:
            sefl.connection_info = data['connection_info']


class Job(MongoDBO):
    '''
    {
        object: MongoDBO,
        owner: Participant,
        ...
    }
    '''
    def __init__(self):
        MongoDBO.__init__(self)
        pass

    def load_job(self, data):
        if 'owner' in data:
            self.owner = data['owner']

    def save_job(self):
        return self.__dict__


class FriendRequest(MongoDBO):
    '''
    {
        object: MongoDBO,
        sender: Participant,
        receiver: Participant,
        date: Date
    }
    '''

    def __init__(self, sender, receiver):
        MongoDBO.__init__(self)
        self.sender = sender
        self.receiver = receiver
        self.date = time.time()

    def collection(self):
        return mongo.db.requests
