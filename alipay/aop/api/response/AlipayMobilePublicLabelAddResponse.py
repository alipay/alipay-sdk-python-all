#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobilePublicLabelAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicLabelAddResponse, self).__init__()
        self._code = None
        self._id = None
        self._msg = None
        self._name = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicLabelAddResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'id' in response:
            self.id = response['id']
        if 'msg' in response:
            self.msg = response['msg']
        if 'name' in response:
            self.name = response['name']
