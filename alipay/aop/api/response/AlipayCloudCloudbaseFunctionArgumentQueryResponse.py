#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Argument import Argument


class AlipayCloudCloudbaseFunctionArgumentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseFunctionArgumentQueryResponse, self).__init__()
        self._arguments = None
        self._page_index = None
        self._page_size = None
        self._total = None

    @property
    def arguments(self):
        return self._arguments

    @arguments.setter
    def arguments(self, value):
        if isinstance(value, list):
            self._arguments = list()
            for i in value:
                if isinstance(i, Argument):
                    self._arguments.append(i)
                else:
                    self._arguments.append(Argument.from_alipay_dict(i))
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
        response = super(AlipayCloudCloudbaseFunctionArgumentQueryResponse, self).parse_response_content(response_content)
        if 'arguments' in response:
            self.arguments = response['arguments']
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
