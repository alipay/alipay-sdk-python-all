#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdAntlegalchainFilenotaryCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntlegalchainFilenotaryCreateResponse, self).__init__()
        self._biz_bas_id = None

    @property
    def biz_bas_id(self):
        return self._biz_bas_id

    @biz_bas_id.setter
    def biz_bas_id(self, value):
        self._biz_bas_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntlegalchainFilenotaryCreateResponse, self).parse_response_content(response_content)
        if 'biz_bas_id' in response:
            self.biz_bas_id = response['biz_bas_id']
