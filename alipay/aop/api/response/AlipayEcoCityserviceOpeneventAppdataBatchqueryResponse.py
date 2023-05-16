#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoCityserviceOpeneventAppdataBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCityserviceOpeneventAppdataBatchqueryResponse, self).__init__()
        self._count = None
        self._data_detail = None
        self._page_num = None
        self._page_size = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def data_detail(self):
        return self._data_detail

    @data_detail.setter
    def data_detail(self, value):
        self._data_detail = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCityserviceOpeneventAppdataBatchqueryResponse, self).parse_response_content(response_content)
        if 'count' in response:
            self.count = response['count']
        if 'data_detail' in response:
            self.data_detail = response['data_detail']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
