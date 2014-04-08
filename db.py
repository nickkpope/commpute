class DBO():
    def __init__(self, id=None):
        self.id = id

    def load(self):
        '''Reads the data from the database'''
        pass

    def save(self):
        pass


class MongoDBO(DBO):
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
    def __init__(self):
        MongoDBO.__init__(self)

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
        pass

    def computers(self):
        '''List of all the comptuers associated with that participant'''


class Person(Participant):
    def __init__(self, name=None):
        Participant.__init__(self)


class Organization(Participant):
    def __init__(self, name=None):
        Participant.__init__(self)

    def leaders(self):
        '''List of all the project leaders (users)'''


class Computer(MongoDBO):
    '''
    {
        'uptime': int, #  (seconds)
        'info': {
            'os': str,
            'ram': str,
            'cores': int,
            ...
        }
    }
    '''
    def __init__(self):
        MongoDBO.__init__(self)

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
        'participant': ObjectId,
        ...
    }
    '''
    def __init__(self):
        MongoDBO.__init__(self)
        pass

    def participant(self):
        pass
