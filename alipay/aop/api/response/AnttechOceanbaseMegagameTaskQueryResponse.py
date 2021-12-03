#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseMegagameTaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseMegagameTaskQueryResponse, self).__init__()
        self._branch = None
        self._commit_id = None
        self._git_repo = None
        self._id = None
        self._team_id = None

    @property
    def branch(self):
        return self._branch

    @branch.setter
    def branch(self, value):
        self._branch = value
    @property
    def commit_id(self):
        return self._commit_id

    @commit_id.setter
    def commit_id(self, value):
        self._commit_id = value
    @property
    def git_repo(self):
        return self._git_repo

    @git_repo.setter
    def git_repo(self, value):
        self._git_repo = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def team_id(self):
        return self._team_id

    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseMegagameTaskQueryResponse, self).parse_response_content(response_content)
        if 'branch' in response:
            self.branch = response['branch']
        if 'commit_id' in response:
            self.commit_id = response['commit_id']
        if 'git_repo' in response:
            self.git_repo = response['git_repo']
        if 'id' in response:
            self.id = response['id']
        if 'team_id' in response:
            self.team_id = response['team_id']
