import json
import sys

users = {'nickpope': 'Nick Pope', 'Bipsy': 'Pete Anderson', 'zygoth': 'Ben Coffman'}
cmd = 'curl -u nickpope https://api.github.com/repos/nickpope/commpute/issues?state=all > ~/tmp.json'


def parseMilestones(data, milestone_title):
    data = json.loads(data)

    def byMilestone(issue):
        if issue['milestone']:
            return issue['milestone']['title'] == milestone_title

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
    parseMilestones(open(sys.argv[1]).read(), 'Milestone 2')


if __name__ == '__main__':
    main()
