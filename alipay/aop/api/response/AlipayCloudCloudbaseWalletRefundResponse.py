#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseWalletRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseWalletRefundResponse, self).__init__()
        self._refund_order_no = None

    @property
    def refund_order_no(self):
        return self._refund_order_no

    @refund_order_no.setter
    def refund_order_no(self, value):
        self._refund_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseWalletRefundResponse, self).parse_response_content(response_content)
        if 'refund_order_no' in response:
            self.refund_order_no = response['refund_order_no']
