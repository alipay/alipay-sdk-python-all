#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CDataJianTestOne import CDataJianTestOne


class AlipayOpenDataquerytwoJianhuiQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenDataquerytwoJianhuiQueryResponse, self).__init__()
        self._czcsone = None
        self._msgone = None

    @property
    def czcsone(self):
        return self._czcsone

    @czcsone.setter
    def czcsone(self, value):
        if isinstance(value, CDataJianTestOne):
            self._czcsone = value
        else:
            self._czcsone = CDataJianTestOne.from_alipay_dict(value)
    @property
    def msgone(self):
        return self._msgone

    @msgone.setter
    def msgone(self, value):
        self._msgone = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenDataquerytwoJianhuiQueryResponse, self).parse_response_content(response_content)
        if 'czcsone' in response:
            self.czcsone = response['czcsone']
        if 'msgone' in response:
            self.msgone = response['msgone']
