#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GavintestNewLeveaOne import GavintestNewLeveaOne


class AlipayOpenMiniReleaststBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniReleaststBatchqueryResponse, self).__init__()
        self._des = None
        self._out = None

    @property
    def des(self):
        return self._des

    @des.setter
    def des(self, value):
        if isinstance(value, GavintestNewLeveaOne):
            self._des = value
        else:
            self._des = GavintestNewLeveaOne.from_alipay_dict(value)
    @property
    def out(self):
        return self._out

    @out.setter
    def out(self, value):
        self._out = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniReleaststBatchqueryResponse, self).parse_response_content(response_content)
        if 'des' in response:
            self.des = response['des']
        if 'out' in response:
            self.out = response['out']
