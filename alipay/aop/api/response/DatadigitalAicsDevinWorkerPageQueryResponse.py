#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WorkerItem import WorkerItem


class DatadigitalAicsDevinWorkerPageQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAicsDevinWorkerPageQueryResponse, self).__init__()
        self._current = None
        self._data = None
        self._total_page = None
        self._total_size = None

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, WorkerItem):
                    self._data.append(i)
                else:
                    self._data.append(WorkerItem.from_alipay_dict(i))
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalAicsDevinWorkerPageQueryResponse, self).parse_response_content(response_content)
        if 'current' in response:
            self.current = response['current']
        if 'data' in response:
            self.data = response['data']
        if 'total_page' in response:
            self.total_page = response['total_page']
        if 'total_size' in response:
            self.total_size = response['total_size']
