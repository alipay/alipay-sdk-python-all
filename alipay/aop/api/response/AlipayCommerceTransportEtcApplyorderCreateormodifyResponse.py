#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcApplyorderCreateormodifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcApplyorderCreateormodifyResponse, self).__init__()
        self._alipay_order_id = None

    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcApplyorderCreateormodifyResponse, self).parse_response_content(response_content)
        if 'alipay_order_id' in response:
            self.alipay_order_id = response['alipay_order_id']
