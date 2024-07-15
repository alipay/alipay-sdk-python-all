#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoMallRenfundorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMallRenfundorderQueryResponse, self).__init__()
        self._biz_claim_type = None
        self._dispute_create_time = None
        self._dispute_end_time = None
        self._dispute_status = None
        self._order_id = None
        self._order_line_id = None
        self._refund_fee = None
        self._refund_reason = None
        self._refunder_address = None
        self._refunder_name = None
        self._refunder_tel = None
        self._seller_refuse_reason = None

    @property
    def biz_claim_type(self):
        return self._biz_claim_type

    @biz_claim_type.setter
    def biz_claim_type(self, value):
        self._biz_claim_type = value
    @property
    def dispute_create_time(self):
        return self._dispute_create_time

    @dispute_create_time.setter
    def dispute_create_time(self, value):
        self._dispute_create_time = value
    @property
    def dispute_end_time(self):
        return self._dispute_end_time

    @dispute_end_time.setter
    def dispute_end_time(self, value):
        self._dispute_end_time = value
    @property
    def dispute_status(self):
        return self._dispute_status

    @dispute_status.setter
    def dispute_status(self, value):
        self._dispute_status = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_line_id(self):
        return self._order_line_id

    @order_line_id.setter
    def order_line_id(self, value):
        self._order_line_id = value
    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def refunder_address(self):
        return self._refunder_address

    @refunder_address.setter
    def refunder_address(self, value):
        self._refunder_address = value
    @property
    def refunder_name(self):
        return self._refunder_name

    @refunder_name.setter
    def refunder_name(self, value):
        self._refunder_name = value
    @property
    def refunder_tel(self):
        return self._refunder_tel

    @refunder_tel.setter
    def refunder_tel(self, value):
        self._refunder_tel = value
    @property
    def seller_refuse_reason(self):
        return self._seller_refuse_reason

    @seller_refuse_reason.setter
    def seller_refuse_reason(self, value):
        self._seller_refuse_reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMallRenfundorderQueryResponse, self).parse_response_content(response_content)
        if 'biz_claim_type' in response:
            self.biz_claim_type = response['biz_claim_type']
        if 'dispute_create_time' in response:
            self.dispute_create_time = response['dispute_create_time']
        if 'dispute_end_time' in response:
            self.dispute_end_time = response['dispute_end_time']
        if 'dispute_status' in response:
            self.dispute_status = response['dispute_status']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_line_id' in response:
            self.order_line_id = response['order_line_id']
        if 'refund_fee' in response:
            self.refund_fee = response['refund_fee']
        if 'refund_reason' in response:
            self.refund_reason = response['refund_reason']
        if 'refunder_address' in response:
            self.refunder_address = response['refunder_address']
        if 'refunder_name' in response:
            self.refunder_name = response['refunder_name']
        if 'refunder_tel' in response:
            self.refunder_tel = response['refunder_tel']
        if 'seller_refuse_reason' in response:
            self.seller_refuse_reason = response['seller_refuse_reason']
