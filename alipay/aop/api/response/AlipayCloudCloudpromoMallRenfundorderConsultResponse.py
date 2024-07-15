#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MpcRefundReason import MpcRefundReason


class AlipayCloudCloudpromoMallRenfundorderConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMallRenfundorderConsultResponse, self).__init__()
        self._biz_claim_type = None
        self._max_refund_fee = None
        self._min_refund_fee = None
        self._order_line_id = None
        self._refund_reason_list = None

    @property
    def biz_claim_type(self):
        return self._biz_claim_type

    @biz_claim_type.setter
    def biz_claim_type(self, value):
        self._biz_claim_type = value
    @property
    def max_refund_fee(self):
        return self._max_refund_fee

    @max_refund_fee.setter
    def max_refund_fee(self, value):
        self._max_refund_fee = value
    @property
    def min_refund_fee(self):
        return self._min_refund_fee

    @min_refund_fee.setter
    def min_refund_fee(self, value):
        self._min_refund_fee = value
    @property
    def order_line_id(self):
        return self._order_line_id

    @order_line_id.setter
    def order_line_id(self, value):
        self._order_line_id = value
    @property
    def refund_reason_list(self):
        return self._refund_reason_list

    @refund_reason_list.setter
    def refund_reason_list(self, value):
        if isinstance(value, MpcRefundReason):
            self._refund_reason_list = value
        else:
            self._refund_reason_list = MpcRefundReason.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMallRenfundorderConsultResponse, self).parse_response_content(response_content)
        if 'biz_claim_type' in response:
            self.biz_claim_type = response['biz_claim_type']
        if 'max_refund_fee' in response:
            self.max_refund_fee = response['max_refund_fee']
        if 'min_refund_fee' in response:
            self.min_refund_fee = response['min_refund_fee']
        if 'order_line_id' in response:
            self.order_line_id = response['order_line_id']
        if 'refund_reason_list' in response:
            self.refund_reason_list = response['refund_reason_list']
