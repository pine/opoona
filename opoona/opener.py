# -*- coding: utf-8 -*-

import six
import github3

from . import git
from .tickets.github import make as make_github_ticket


class InvalidConfigException(Exception):
    pass


class InvalidStatusException(Exception):
    pass


class Opener():
    def __init__(self, config):
        self.config     = config
        self.repository = self._get_repository()

    def open(self, issue):
        # self._check_git_status()
        ticket = self._make_ticket(issue)
        base   = git.get_branch()
        self._check_branch_exists(base, ticket.branch)

        git.checkout(ticket.branch)
        git.commit(ticket.branch)
        git.push(ticket.branch)

        pull = self._create_pull_request(base, ticket)
        print('done! {0}'.format(pull.html_url))

    def _get_repository(self):
        token = self.config['github']['token']
        if not token:
            raise InvalidConfigException("\n".join([
                'github token is required',
                'check your config file',
            ]))
        owner, repository = git.get_owner_repository()
        github = github3.login(token = token)
        return github.repository(owner, repository)

    def _make_ticket(self, issue):
        ticket = make_github_ticket(self.config, self.repository, issue)
        if not ticket:
            raise InvalidStatusException('invalid issue format: {0}'.format(issue))
        return ticket

    def _create_pull_request(self, base, ticket):
        print('creating pull request...')
        print('  {0} <- {1}'.format(base, ticket.branch))
        pull = self.repository.create_pull(
            title = ticket.title,
            base  = base,
            head  = ticket.branch,
            body  = six.u('{0}\n\n### Tasks\n\n- [ ] ').format(ticket.url),
        )
        issue = self.github.issue(pull.number)
        issue.add_labels('WIP')
        return pull

    def _check_git_status(self):
        if not git.is_inside_work_tree():
            raise InvalidStatusException("\n".join([
                'current directory is not inside git work tree.',
                'check current directory',
            ]))
        if git.is_dirty():
            raise InvalidStatusException("\n".join([
                'repository is dirty.',
                'check `git status`',
            ]))

    def _check_branch_exists(self, base, branch):
        if base == branch:
            raise InvalidStatusException("\n".join([
                'try to create {0} branch, but it is current branch.'.format(branch),
                'check `git status`',
            ]))
        if git.has_branch(branch):
            raise InvalidStatusException("\n".join([
                'try to create {0} branch, but it is already exists.'.format(branch),
                'check `git branch`',
            ]))

