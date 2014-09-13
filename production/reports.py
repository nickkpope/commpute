import json
import sys

users = {'nickpope': 'Nick Pope', 'Bipsy': 'Pete Anderson', 'zygoth': 'Ben Coffman'}
cmd = 'curl -u nickpope https://api.github.com/repos/nickpope/commpute/issues?state=all > ~/tmp.json'


def parseMilestones(data, milestone_title):
    data = json.loads(data)
    print '# Future Features'
    print

    def byMilestone(issue):
        if issue['milestone']:
            return issue['milestone']['title'] == milestone_title
        else:
            if not issue['assignee']:
                print '*', '%s: %s' % (issue['state'], issue['title'])
                print '  *', '%s' % (issue['body'])

    print '# %s' % milestone_title
    print
    mstone1 = filter(byMilestone, data)
    report = {}
    for issue in mstone1:
        if issue['assignee']:
            try:
                report[issue['assignee']['login']].append(issue)
            except KeyError:
                report[issue['assignee']['login']] = [issue]

    for user, issues in report.items():
        print '## %s' % users[user]
        for issue in issues:
            print '* %s: %s' % (issue['state'], issue['title'])
        print
        print


def main():
    parseMilestones(open(sys.argv[1]).read(), 'Milestone 3')


if __name__ == '__main__':
    main()
