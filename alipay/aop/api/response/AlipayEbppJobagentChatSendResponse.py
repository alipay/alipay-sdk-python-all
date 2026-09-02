#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppJobagentChatSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJobagentChatSendResponse, self).__init__()
        self._content = None
        self._session_id = None
        self._tpl_code = None
        self._tpl_data = None
        self._type = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def tpl_code(self):
        return self._tpl_code

    @tpl_code.setter
    def tpl_code(self, value):
        self._tpl_code = value
    @property
    def tpl_data(self):
        return self._tpl_data

    @tpl_data.setter
    def tpl_data(self, value):
        self._tpl_data = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppJobagentChatSendResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
        if 'session_id' in response:
            self.session_id = response['session_id']
        if 'tpl_code' in response:
            self.tpl_code = response['tpl_code']
        if 'tpl_data' in response:
            self.tpl_data = response['tpl_data']
        if 'type' in response:
            self.type = response['type']
