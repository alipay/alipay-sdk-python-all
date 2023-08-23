#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseDatabaseTaskApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseDatabaseTaskApplyResponse, self).__init__()
        self._download_url = None
        self._task_id = None
        self._upload_id = None
        self._upload_url = None

    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def upload_id(self):
        return self._upload_id

    @upload_id.setter
    def upload_id(self, value):
        self._upload_id = value
    @property
    def upload_url(self):
        return self._upload_url

    @upload_url.setter
    def upload_url(self, value):
        self._upload_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseDatabaseTaskApplyResponse, self).parse_response_content(response_content)
        if 'download_url' in response:
            self.download_url = response['download_url']
        if 'task_id' in response:
            self.task_id = response['task_id']
        if 'upload_id' in response:
            self.upload_id = response['upload_id']
        if 'upload_url' in response:
            self.upload_url = response['upload_url']
