#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseDatabaseRollbacktaskGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseDatabaseRollbacktaskGetResponse, self).__init__()
        self._archive_time = None
        self._create_time = None
        self._status = None

    @property
    def archive_time(self):
        return self._archive_time

    @archive_time.setter
    def archive_time(self, value):
        self._archive_time = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseDatabaseRollbacktaskGetResponse, self).parse_response_content(response_content)
        if 'archive_time' in response:
            self.archive_time = response['archive_time']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'status' in response:
            self.status = response['status']
