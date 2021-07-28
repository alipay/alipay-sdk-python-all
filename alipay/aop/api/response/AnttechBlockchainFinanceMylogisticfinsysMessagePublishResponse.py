#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceMylogisticfinsysMessagePublishResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceMylogisticfinsysMessagePublishResponse, self).__init__()
        self._data = None
        self._extra_info = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def extra_info(self):
        return self._extra_info

    @extra_info.setter
    def extra_info(self, value):
        self._extra_info = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceMylogisticfinsysMessagePublishResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'extra_info' in response:
            self.extra_info = response['extra_info']
