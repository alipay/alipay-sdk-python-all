#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobilePublicAccountlistGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicAccountlistGetResponse, self).__init__()
        self._account_list = None
        self._code = None
        self._count = None
        self._msg = None

    @property
    def account_list(self):
        return self._account_list

    @account_list.setter
    def account_list(self, value):
        self._account_list = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicAccountlistGetResponse, self).parse_response_content(response_content)
        if 'account_list' in response:
            self.account_list = response['account_list']
        if 'code' in response:
            self.code = response['code']
        if 'count' in response:
            self.count = response['count']
        if 'msg' in response:
            self.msg = response['msg']
