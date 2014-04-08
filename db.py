class DBO():
    '''
    {
        id, #
    }
    '''
    def __init__(self, id=None):
        self.id = id

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
        self.col = None
        self.db = None
        self.data = None

    def __getitme__(self, key):
        return self.data()[key]

    def collection(self):
        pass

    def database(self):
        pass

    def data(self):
        '''Raw dictionary returned from the database'''
        pass


class Participant(MongoDBO):
    '''
    {
        parent: MongoDBO,
        contributors: listof Participants?,
        name: string,
        username: string,
        uptime: #,
        computers: listof Computers,
        requests: listof Participants
    }
    '''
    def __init__(self, username=None, name=None):
        MongoDBO.__init__(self)
        self.computers = []
        self.username = username
        self.name = name
        self.requests = []

    def __gt__(self, other):
        '''Compares uptime'''
        return self.uptime() > other.uptime()

    def contributors(self):
        '''List of all the contributors for the given entity'''
        pass

    def is_name_unique(self):
        '''Checks if any other entities have the same name'''
        pass

    def name(self):
        '''Unique name for a given entity'''
        pass

    def uptime(self):
        '''The aggregated time in seconds of all the users computers uptimes'''
        with 0 as total:
            for computer in computers:
                total += computer.uptime()

    def computers(self):
        '''List of all the comptuers associated with that participant'''


    def save_participant(self):
        '''Method to convert Participant into a dictionary'''
        self.data = {'username': self.username,
                        'name' : self.name }
        return participant


    def request(self):
        '''Method to obtain the requests that
           have been sent to this participant
        '''
        return self.requests





class Person(Participant):
    '''
    {
        participant: Participant
    }
    '''
    def __init__(self, username=None, name=None):
        Participant.__init__(self, username, name)


class Organization(Participant):
    '''
    {
        participant: Participant,
        leaders: listof Participants
    }
    '''
    def __init__(self, name=None):
        Participant.__init__(self)
        self.leaders = []

    def leaders(self):
        '''List of all the project leaders (users)'''
        return self.leaders


class Computer(MongoDBO):
    '''
    {
        'uptime': int, #  (seconds),
        'info': {
            'os': str,
            'ram': str,
            'cores': int,
            ...
        },
        address: string
    }
    '''
    def __init__(self):
        MongoDBO.__init__(self)
        self.uptime = 0

    def uptime(self):
        '''Computers uptime (seconds)'''
        return self.uptime

    def info(self):
        '''Dictionary containing useful information about that computer'''
        return self.info

    def connect_info(self):
        '''
        Dictionary containing information necessary for users to
        authenticate with and send commands to.
        '''
        return self.connect_info


class Job(MongoDBO):
    '''
    {
        object: MongoDBO,
        ...
    }
    '''
    def __init__(self):
        MongoDBO.__init__(self)
        pass

    def participant(self):
        pass


class Request(MongoDB0):
    '''
    {
        object: MongoDBO,
        sender: Participant,
        receiver: Participant,
        data: Date,
        status: str,
        ...
    }
    '''

    def __init__(self):
        MongoDBO.__init__(self)
        pass

