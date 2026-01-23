#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ObjectTaskStatus import ObjectTaskStatus


class RobbyOpenTaskStatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(RobbyOpenTaskStatusQueryResponse, self).__init__()
        self._biz_no = None
        self._object_task_status_list = None
        self._sub_biz_no = None
        self._task_no = None
        self._task_status = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def object_task_status_list(self):
        return self._object_task_status_list

    @object_task_status_list.setter
    def object_task_status_list(self, value):
        if isinstance(value, list):
            self._object_task_status_list = list()
            for i in value:
                if isinstance(i, ObjectTaskStatus):
                    self._object_task_status_list.append(i)
                else:
                    self._object_task_status_list.append(ObjectTaskStatus.from_alipay_dict(i))
    @property
    def sub_biz_no(self):
        return self._sub_biz_no

    @sub_biz_no.setter
    def sub_biz_no(self, value):
        self._sub_biz_no = value
    @property
    def task_no(self):
        return self._task_no

    @task_no.setter
    def task_no(self, value):
        self._task_no = value
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value

    def parse_response_content(self, response_content):
        response = super(RobbyOpenTaskStatusQueryResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'object_task_status_list' in response:
            self.object_task_status_list = response['object_task_status_list']
        if 'sub_biz_no' in response:
            self.sub_biz_no = response['sub_biz_no']
        if 'task_no' in response:
            self.task_no = response['task_no']
        if 'task_status' in response:
            self.task_status = response['task_status']
