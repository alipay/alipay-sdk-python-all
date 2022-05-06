#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseTestplatformTaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseTestplatformTaskQueryResponse, self).__init__()
        self._branch = None
        self._commit_id = None
        self._current_retry = None
        self._git_repo = None
        self._gmt_create = None
        self._player = None
        self._result_type = None
        self._task_id = None
        self._test_cases = None
        self._test_info = None
        self._test_suite = None

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
    def current_retry(self):
        return self._current_retry

    @current_retry.setter
    def current_retry(self, value):
        self._current_retry = value
    @property
    def git_repo(self):
        return self._git_repo

    @git_repo.setter
    def git_repo(self, value):
        self._git_repo = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        self._player = value
    @property
    def result_type(self):
        return self._result_type

    @result_type.setter
    def result_type(self, value):
        self._result_type = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def test_cases(self):
        return self._test_cases

    @test_cases.setter
    def test_cases(self, value):
        self._test_cases = value
    @property
    def test_info(self):
        return self._test_info

    @test_info.setter
    def test_info(self, value):
        self._test_info = value
    @property
    def test_suite(self):
        return self._test_suite

    @test_suite.setter
    def test_suite(self, value):
        self._test_suite = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseTestplatformTaskQueryResponse, self).parse_response_content(response_content)
        if 'branch' in response:
            self.branch = response['branch']
        if 'commit_id' in response:
            self.commit_id = response['commit_id']
        if 'current_retry' in response:
            self.current_retry = response['current_retry']
        if 'git_repo' in response:
            self.git_repo = response['git_repo']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'player' in response:
            self.player = response['player']
        if 'result_type' in response:
            self.result_type = response['result_type']
        if 'task_id' in response:
            self.task_id = response['task_id']
        if 'test_cases' in response:
            self.test_cases = response['test_cases']
        if 'test_info' in response:
            self.test_info = response['test_info']
        if 'test_suite' in response:
            self.test_suite = response['test_suite']
