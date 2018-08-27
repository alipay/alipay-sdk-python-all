#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiRetailWmsInboundorderCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsInboundorderCreateResponse, self).__init__()
        self._inbound_order_id = None

    @property
    def inbound_order_id(self):
        return self._inbound_order_id

    @inbound_order_id.setter
    def inbound_order_id(self, value):
        self._inbound_order_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsInboundorderCreateResponse, self).parse_response_content(response_content)
        if 'inbound_order_id' in response:
            self.inbound_order_id = response['inbound_order_id']
