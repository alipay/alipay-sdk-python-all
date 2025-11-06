#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHdfrtcVideoconferencetaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfrtcVideoconferencetaskQueryResponse, self).__init__()
        self._source_id = None
        self._source_type = None
        self._task_id = None

    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfrtcVideoconferencetaskQueryResponse, self).parse_response_content(response_content)
        if 'source_id' in response:
            self.source_id = response['source_id']
        if 'source_type' in response:
            self.source_type = response['source_type']
        if 'task_id' in response:
            self.task_id = response['task_id']
