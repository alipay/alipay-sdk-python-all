#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAcommunicationFlowCommissionSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationFlowCommissionSubmitResponse, self).__init__()
        self._commission_state = None
        self._item_code = None

    @property
    def commission_state(self):
        return self._commission_state

    @commission_state.setter
    def commission_state(self, value):
        self._commission_state = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationFlowCommissionSubmitResponse, self).parse_response_content(response_content)
        if 'commission_state' in response:
            self.commission_state = response['commission_state']
        if 'item_code' in response:
            self.item_code = response['item_code']
