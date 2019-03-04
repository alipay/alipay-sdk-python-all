#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandTradeorderRefundResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandTradeorderRefundResponse, self).__init__()
        self._buyer_id = None
        self._gmt_refund = None
        self._refund_amount = None
        self._refund_order_id = None
        self._refund_status = None
        self._seller_id = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def gmt_refund(self):
        return self._gmt_refund

    @gmt_refund.setter
    def gmt_refund(self, value):
        self._gmt_refund = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_order_id(self):
        return self._refund_order_id

    @refund_order_id.setter
    def refund_order_id(self, value):
        self._refund_order_id = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandTradeorderRefundResponse, self).parse_response_content(response_content)
        if 'buyer_id' in response:
            self.buyer_id = response['buyer_id']
        if 'gmt_refund' in response:
            self.gmt_refund = response['gmt_refund']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'refund_order_id' in response:
            self.refund_order_id = response['refund_order_id']
        if 'refund_status' in response:
            self.refund_status = response['refund_status']
        if 'seller_id' in response:
            self.seller_id = response['seller_id']
