#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiShopMallPageModifyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiShopMallPageModifyResponse, self).__init__()
        self._order_flow_id = None

    @property
    def order_flow_id(self):
        return self._order_flow_id

    @order_flow_id.setter
    def order_flow_id(self, value):
        self._order_flow_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiShopMallPageModifyResponse, self).parse_response_content(response_content)
        if 'order_flow_id' in response:
            self.order_flow_id = response['order_flow_id']
