#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CollaborateTask import CollaborateTask


class AlipayOfflineProviderCollaborateTaskPullResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderCollaborateTaskPullResponse, self).__init__()
        self._count = None
        self._tasks = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, value):
        if isinstance(value, list):
            self._tasks = list()
            for i in value:
                if isinstance(i, CollaborateTask):
                    self._tasks.append(i)
                else:
                    self._tasks.append(CollaborateTask.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderCollaborateTaskPullResponse, self).parse_response_content(response_content)
        if 'count' in response:
            self.count = response['count']
        if 'tasks' in response:
            self.tasks = response['tasks']
