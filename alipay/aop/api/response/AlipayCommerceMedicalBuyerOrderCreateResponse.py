#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalBuyerOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalBuyerOrderCreateResponse, self).__init__()
        self._fulfillment_no = None
        self._order_no = None

    @property
    def fulfillment_no(self):
        return self._fulfillment_no

    @fulfillment_no.setter
    def fulfillment_no(self, value):
        self._fulfillment_no = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalBuyerOrderCreateResponse, self).parse_response_content(response_content)
        if 'fulfillment_no' in response:
            self.fulfillment_no = response['fulfillment_no']
        if 'order_no' in response:
            self.order_no = response['order_no']
