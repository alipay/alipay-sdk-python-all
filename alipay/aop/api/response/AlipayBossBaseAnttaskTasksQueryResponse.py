#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaskOperateResult import TaskOperateResult
from alipay.aop.api.domain.AntTask import AntTask


class AlipayBossBaseAnttaskTasksQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossBaseAnttaskTasksQueryResponse, self).__init__()
        self._boolean_result = None
        self._entities = None
        self._total_count = None

    @property
    def boolean_result(self):
        return self._boolean_result

    @boolean_result.setter
    def boolean_result(self, value):
        if isinstance(value, TaskOperateResult):
            self._boolean_result = value
        else:
            self._boolean_result = TaskOperateResult.from_alipay_dict(value)
    @property
    def entities(self):
        return self._entities

    @entities.setter
    def entities(self, value):
        if isinstance(value, list):
            self._entities = list()
            for i in value:
                if isinstance(i, AntTask):
                    self._entities.append(i)
                else:
                    self._entities.append(AntTask.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossBaseAnttaskTasksQueryResponse, self).parse_response_content(response_content)
        if 'boolean_result' in response:
            self.boolean_result = response['boolean_result']
        if 'entities' in response:
            self.entities = response['entities']
        if 'total_count' in response:
            self.total_count = response['total_count']
