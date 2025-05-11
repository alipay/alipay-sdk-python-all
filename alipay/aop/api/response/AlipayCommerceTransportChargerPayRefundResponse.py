#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportChargerPayRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportChargerPayRefundResponse, self).__init__()
        self._refund_id = None

    @property
    def refund_id(self):
        return self._refund_id

    @refund_id.setter
    def refund_id(self, value):
        self._refund_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportChargerPayRefundResponse, self).parse_response_content(response_content)
        if 'refund_id' in response:
            self.refund_id = response['refund_id']
