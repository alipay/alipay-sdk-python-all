#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSupplychainFactoringSelleradmitQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainFactoringSelleradmitQueryResponse, self).__init__()
        self._exsit = None
        self._refuse_code = None
        self._refuse_msg = None
        self._refused = None
        self._white = None

    @property
    def exsit(self):
        return self._exsit

    @exsit.setter
    def exsit(self, value):
        self._exsit = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        self._refuse_msg = value
    @property
    def refused(self):
        return self._refused

    @refused.setter
    def refused(self, value):
        self._refused = value
    @property
    def white(self):
        return self._white

    @white.setter
    def white(self, value):
        self._white = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainFactoringSelleradmitQueryResponse, self).parse_response_content(response_content)
        if 'exsit' in response:
            self.exsit = response['exsit']
        if 'refuse_code' in response:
            self.refuse_code = response['refuse_code']
        if 'refuse_msg' in response:
            self.refuse_msg = response['refuse_msg']
        if 'refused' in response:
            self.refused = response['refused']
        if 'white' in response:
            self.white = response['white']
