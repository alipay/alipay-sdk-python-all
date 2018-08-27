#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiRetailWmsOutboundorderCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsOutboundorderCreateResponse, self).__init__()
        self._outbound_order_id = None

    @property
    def outbound_order_id(self):
        return self._outbound_order_id

    @outbound_order_id.setter
    def outbound_order_id(self, value):
        self._outbound_order_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsOutboundorderCreateResponse, self).parse_response_content(response_content)
        if 'outbound_order_id' in response:
            self.outbound_order_id = response['outbound_order_id']
