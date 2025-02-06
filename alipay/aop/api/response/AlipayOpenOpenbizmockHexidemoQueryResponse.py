#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenOpenbizmockHexidemoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOpenbizmockHexidemoQueryResponse, self).__init__()
        self._echo = None
        self._open_id = None
        self._result = None
        self._user_id = None

    @property
    def echo(self):
        return self._echo

    @echo.setter
    def echo(self, value):
        self._echo = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenOpenbizmockHexidemoQueryResponse, self).parse_response_content(response_content)
        if 'echo' in response:
            self.echo = response['echo']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'result' in response:
            self.result = response['result']
        if 'user_id' in response:
            self.user_id = response['user_id']
