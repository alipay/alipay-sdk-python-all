#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpSceneFulfillmentSyncResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpSceneFulfillmentSyncResponse, self).__init__()
        self._fulfillment_order_no = None

    @property
    def fulfillment_order_no(self):
        return self._fulfillment_order_no

    @fulfillment_order_no.setter
    def fulfillment_order_no(self, value):
        self._fulfillment_order_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpSceneFulfillmentSyncResponse, self).parse_response_content(response_content)
        if 'fulfillment_order_no' in response:
            self.fulfillment_order_no = response['fulfillment_order_no']
