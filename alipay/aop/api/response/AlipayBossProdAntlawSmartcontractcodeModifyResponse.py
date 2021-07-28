#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdAntlawSmartcontractcodeModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntlawSmartcontractcodeModifyResponse, self).__init__()
        self._biz_code = None
        self._source_sys = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def source_sys(self):
        return self._source_sys

    @source_sys.setter
    def source_sys(self, value):
        self._source_sys = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntlawSmartcontractcodeModifyResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'source_sys' in response:
            self.source_sys = response['source_sys']
