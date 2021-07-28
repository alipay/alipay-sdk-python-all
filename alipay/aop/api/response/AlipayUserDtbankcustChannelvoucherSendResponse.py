#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserDtbankcustChannelvoucherSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDtbankcustChannelvoucherSendResponse, self).__init__()
        self._activity_id = None
        self._activity_order_id = None
        self._discount_threshold_amt = None
        self._discount_type = None
        self._discount_value = None
        self._send_amount = None
        self._send_status = None
        self._voucher_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_order_id(self):
        return self._activity_order_id

    @activity_order_id.setter
    def activity_order_id(self, value):
        self._activity_order_id = value
    @property
    def discount_threshold_amt(self):
        return self._discount_threshold_amt

    @discount_threshold_amt.setter
    def discount_threshold_amt(self, value):
        self._discount_threshold_amt = value
    @property
    def discount_type(self):
        return self._discount_type

    @discount_type.setter
    def discount_type(self, value):
        self._discount_type = value
    @property
    def discount_value(self):
        return self._discount_value

    @discount_value.setter
    def discount_value(self, value):
        self._discount_value = value
    @property
    def send_amount(self):
        return self._send_amount

    @send_amount.setter
    def send_amount(self, value):
        self._send_amount = value
    @property
    def send_status(self):
        return self._send_status

    @send_status.setter
    def send_status(self, value):
        self._send_status = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserDtbankcustChannelvoucherSendResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'activity_order_id' in response:
            self.activity_order_id = response['activity_order_id']
        if 'discount_threshold_amt' in response:
            self.discount_threshold_amt = response['discount_threshold_amt']
        if 'discount_type' in response:
            self.discount_type = response['discount_type']
        if 'discount_value' in response:
            self.discount_value = response['discount_value']
        if 'send_amount' in response:
            self.send_amount = response['send_amount']
        if 'send_status' in response:
            self.send_status = response['send_status']
        if 'voucher_id' in response:
            self.voucher_id = response['voucher_id']
