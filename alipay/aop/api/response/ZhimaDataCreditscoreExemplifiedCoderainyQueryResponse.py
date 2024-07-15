#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaDataCreditscoreExemplifiedCoderainyQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaDataCreditscoreExemplifiedCoderainyQueryResponse, self).__init__()
        self._data = None
        self._open_id = None
        self._uid = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value

    def parse_response_content(self, response_content):
        response = super(ZhimaDataCreditscoreExemplifiedCoderainyQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'uid' in response:
            self.uid = response['uid']
