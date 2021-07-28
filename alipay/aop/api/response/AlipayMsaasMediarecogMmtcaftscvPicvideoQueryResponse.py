#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMsaasMediarecogMmtcaftscvPicvideoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogMmtcaftscvPicvideoQueryResponse, self).__init__()
        self._data = None
        self._request_id = None
        self._result = None
        self._transaction_id = None
        self._type = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogMmtcaftscvPicvideoQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'result' in response:
            self.result = response['result']
        if 'transaction_id' in response:
            self.transaction_id = response['transaction_id']
        if 'type' in response:
            self.type = response['type']
