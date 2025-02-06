#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ObjectData import ObjectData


class AlipayIserviceCcmCrmClueQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmCrmClueQueryResponse, self).__init__()
        self._current_page = None
        self._page_size = None
        self._total_page = None
        self._value = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, list):
            self._value = list()
            for i in value:
                if isinstance(i, ObjectData):
                    self._value.append(i)
                else:
                    self._value.append(ObjectData.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmCrmClueQueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_page' in response:
            self.total_page = response['total_page']
        if 'value' in response:
            self.value = response['value']
