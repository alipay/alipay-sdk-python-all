#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AdConversion import AdConversion


class AlipayDataDataserviceAdconversionConversionpageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdconversionConversionpageQueryResponse, self).__init__()
        self._current = None
        self._list = None
        self._page_size = None
        self._total = None

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value
    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, AdConversion):
            self._list = value
        else:
            self._list = AdConversion.from_alipay_dict(value)
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
        response = super(AlipayDataDataserviceAdconversionConversionpageQueryResponse, self).parse_response_content(response_content)
        if 'current' in response:
            self.current = response['current']
        if 'list' in response:
            self.list = response['list']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
