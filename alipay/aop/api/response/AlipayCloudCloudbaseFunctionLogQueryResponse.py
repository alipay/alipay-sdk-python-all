#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseFunctionLogQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseFunctionLogQueryResponse, self).__init__()
        self._logs = None
        self._page_index = None
        self._page_size = None
        self._total = None

    @property
    def logs(self):
        return self._logs

    @logs.setter
    def logs(self, value):
        if isinstance(value, list):
            self._logs = list()
            for i in value:
                self._logs.append(i)
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseFunctionLogQueryResponse, self).parse_response_content(response_content)
        if 'logs' in response:
            self.logs = response['logs']
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
