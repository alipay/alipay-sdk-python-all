#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalOuterorderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalOuterorderCreateResponse, self).__init__()
        self._fulfillment_url = None
        self._partner_order_id = None

    @property
    def fulfillment_url(self):
        return self._fulfillment_url

    @fulfillment_url.setter
    def fulfillment_url(self, value):
        self._fulfillment_url = value
    @property
    def partner_order_id(self):
        return self._partner_order_id

    @partner_order_id.setter
    def partner_order_id(self, value):
        self._partner_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalOuterorderCreateResponse, self).parse_response_content(response_content)
        if 'fulfillment_url' in response:
            self.fulfillment_url = response['fulfillment_url']
        if 'partner_order_id' in response:
            self.partner_order_id = response['partner_order_id']
