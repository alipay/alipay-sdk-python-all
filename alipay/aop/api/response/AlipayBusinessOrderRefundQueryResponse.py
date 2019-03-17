#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PaytoolRefundResultDetail import PaytoolRefundResultDetail


class AlipayBusinessOrderRefundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessOrderRefundQueryResponse, self).__init__()
        self._gmt_refund = None
        self._merchant_order_no = None
        self._order_no = None
        self._order_refund_amount = None
        self._refund_paytool_list = None

    @property
    def gmt_refund(self):
        return self._gmt_refund

    @gmt_refund.setter
    def gmt_refund(self, value):
        self._gmt_refund = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_refund_amount(self):
        return self._order_refund_amount

    @order_refund_amount.setter
    def order_refund_amount(self, value):
        self._order_refund_amount = value
    @property
    def refund_paytool_list(self):
        return self._refund_paytool_list

    @refund_paytool_list.setter
    def refund_paytool_list(self, value):
        if isinstance(value, list):
            self._refund_paytool_list = list()
            for i in value:
                if isinstance(i, PaytoolRefundResultDetail):
                    self._refund_paytool_list.append(i)
                else:
                    self._refund_paytool_list.append(PaytoolRefundResultDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayBusinessOrderRefundQueryResponse, self).parse_response_content(response_content)
        if 'gmt_refund' in response:
            self.gmt_refund = response['gmt_refund']
        if 'merchant_order_no' in response:
            self.merchant_order_no = response['merchant_order_no']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_refund_amount' in response:
            self.order_refund_amount = response['order_refund_amount']
        if 'refund_paytool_list' in response:
            self.refund_paytool_list = response['refund_paytool_list']
