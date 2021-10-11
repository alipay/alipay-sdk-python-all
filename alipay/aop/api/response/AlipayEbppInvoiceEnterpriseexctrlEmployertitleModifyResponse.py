#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceEnterpriseexctrlEmployertitleModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceEnterpriseexctrlEmployertitleModifyResponse, self).__init__()
        self._code = None
        self._msg = None
        self._success = None
        self._title_id = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def title_id(self):
        return self._title_id

    @title_id.setter
    def title_id(self, value):
        self._title_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceEnterpriseexctrlEmployertitleModifyResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'msg' in response:
            self.msg = response['msg']
        if 'success' in response:
            self.success = response['success']
        if 'title_id' in response:
            self.title_id = response['title_id']
