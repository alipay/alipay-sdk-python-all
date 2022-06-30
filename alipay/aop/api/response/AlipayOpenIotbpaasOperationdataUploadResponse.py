#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotbpaasOperationdataUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotbpaasOperationdataUploadResponse, self).__init__()
        self._flag = None
        self._message = None

    @property
    def flag(self):
        return self._flag

    @flag.setter
    def flag(self, value):
        self._flag = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotbpaasOperationdataUploadResponse, self).parse_response_content(response_content)
        if 'flag' in response:
            self.flag = response['flag']
        if 'message' in response:
            self.message = response['message']
