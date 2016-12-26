# -*- coding: utf-8 -*-

import re


def make(config, repository, issue):
    match = re.match(r'^issues?[-/]?(\d+)$', issue)
    if match:
        return GitHubIssue(config, repository, match.group(1))


class NotFoundException(Exception):
    pass


class GitHubIssue():
    def __init__(self, config, repository, issue_no):
        self.config     = config
        self.repository = repository
        self.issue_no   = issue_no
        self._load()

    def _load(self):
        print('fetching github issue...')
        self.data = self.repository.issue(self.issue_no)
        if self.data is None:
            raise NotFoundException('issue was not found')

    @property
    def branch(self):
        return 'issues/{0}'.format(self.issue_no)

    @property
    def url(self):
        return self.data.html_url

    @property
    def title(self):
        return self.data.title
