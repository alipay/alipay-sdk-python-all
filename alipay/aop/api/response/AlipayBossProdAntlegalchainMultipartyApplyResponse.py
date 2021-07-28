#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdAntlegalchainMultipartyApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntlegalchainMultipartyApplyResponse, self).__init__()
        self._bas_data_id = None

    @property
    def bas_data_id(self):
        return self._bas_data_id

    @bas_data_id.setter
    def bas_data_id(self, value):
        self._bas_data_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntlegalchainMultipartyApplyResponse, self).parse_response_content(response_content)
        if 'bas_data_id' in response:
            self.bas_data_id = response['bas_data_id']
