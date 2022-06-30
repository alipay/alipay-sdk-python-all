#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDigitalmgmtEcmcoreDataarchivesCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtEcmcoreDataarchivesCreateResponse, self).__init__()
        self._data_id = None
        self._message_content = None
        self._status = None

    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def message_content(self):
        return self._message_content

    @message_content.setter
    def message_content(self, value):
        self._message_content = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtEcmcoreDataarchivesCreateResponse, self).parse_response_content(response_content)
        if 'data_id' in response:
            self.data_id = response['data_id']
        if 'message_content' in response:
            self.message_content = response['message_content']
        if 'status' in response:
            self.status = response['status']
