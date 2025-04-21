#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcAccountingentityCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcAccountingentityCreateResponse, self).__init__()
        self._accounting_entity_id = None

    @property
    def accounting_entity_id(self):
        return self._accounting_entity_id

    @accounting_entity_id.setter
    def accounting_entity_id(self, value):
        self._accounting_entity_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcAccountingentityCreateResponse, self).parse_response_content(response_content)
        if 'accounting_entity_id' in response:
            self.accounting_entity_id = response['accounting_entity_id']
