#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneEcommercePurchaseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneEcommercePurchaseResponse, self).__init__()
        self._purchase_contract_id = None

    @property
    def purchase_contract_id(self):
        return self._purchase_contract_id

    @purchase_contract_id.setter
    def purchase_contract_id(self, value):
        self._purchase_contract_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneEcommercePurchaseResponse, self).parse_response_content(response_content)
        if 'purchase_contract_id' in response:
            self.purchase_contract_id = response['purchase_contract_id']
