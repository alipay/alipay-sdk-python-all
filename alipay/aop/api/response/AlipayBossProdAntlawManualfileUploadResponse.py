#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdAntlawManualfileUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntlawManualfileUploadResponse, self).__init__()
        self._biz_code = None
        self._smart_contract_id = None
        self._source_sys = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def smart_contract_id(self):
        return self._smart_contract_id

    @smart_contract_id.setter
    def smart_contract_id(self, value):
        self._smart_contract_id = value
    @property
    def source_sys(self):
        return self._source_sys

    @source_sys.setter
    def source_sys(self, value):
        self._source_sys = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntlawManualfileUploadResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'smart_contract_id' in response:
            self.smart_contract_id = response['smart_contract_id']
        if 'source_sys' in response:
            self.source_sys = response['source_sys']
