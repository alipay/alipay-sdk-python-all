#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubTaskInfo import SubTaskInfo


class AlipayOpenSpIsvSignauthQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpIsvSignauthQueryResponse, self).__init__()
        self._order_id = None
        self._status = None
        self._task_infos = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_infos(self):
        return self._task_infos

    @task_infos.setter
    def task_infos(self, value):
        if isinstance(value, list):
            self._task_infos = list()
            for i in value:
                if isinstance(i, SubTaskInfo):
                    self._task_infos.append(i)
                else:
                    self._task_infos.append(SubTaskInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpIsvSignauthQueryResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'status' in response:
            self.status = response['status']
        if 'task_infos' in response:
            self.task_infos = response['task_infos']
