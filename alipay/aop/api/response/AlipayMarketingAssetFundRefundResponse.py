#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingAssetFundRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingAssetFundRefundResponse, self).__init__()
        self._refund_order_id = None

    @property
    def refund_order_id(self):
        return self._refund_order_id

    @refund_order_id.setter
    def refund_order_id(self, value):
        self._refund_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingAssetFundRefundResponse, self).parse_response_content(response_content)
        if 'refund_order_id' in response:
            self.refund_order_id = response['refund_order_id']
