#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudFundWalletTemplateCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudFundWalletTemplateCreateResponse, self).__init__()
        self._wallet_template_id = None

    @property
    def wallet_template_id(self):
        return self._wallet_template_id

    @wallet_template_id.setter
    def wallet_template_id(self, value):
        self._wallet_template_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudFundWalletTemplateCreateResponse, self).parse_response_content(response_content)
        if 'wallet_template_id' in response:
            self.wallet_template_id = response['wallet_template_id']
