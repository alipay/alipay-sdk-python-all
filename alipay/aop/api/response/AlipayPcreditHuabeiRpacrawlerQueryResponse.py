#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RpaCrawlerTaskVO import RpaCrawlerTaskVO


class AlipayPcreditHuabeiRpacrawlerQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiRpacrawlerQueryResponse, self).__init__()
        self._task_list = None
        self._total_count = None

    @property
    def task_list(self):
        return self._task_list

    @task_list.setter
    def task_list(self, value):
        if isinstance(value, list):
            self._task_list = list()
            for i in value:
                if isinstance(i, RpaCrawlerTaskVO):
                    self._task_list.append(i)
                else:
                    self._task_list.append(RpaCrawlerTaskVO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiRpacrawlerQueryResponse, self).parse_response_content(response_content)
        if 'task_list' in response:
            self.task_list = response['task_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
