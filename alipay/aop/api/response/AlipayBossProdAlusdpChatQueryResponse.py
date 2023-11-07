#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdAlusdpChatQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAlusdpChatQueryResponse, self).__init__()
        self._data = None
        self._message = None
        self._status_code = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAlusdpChatQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'message' in response:
            self.message = response['message']
        if 'status_code' in response:
            self.status_code = response['status_code']
