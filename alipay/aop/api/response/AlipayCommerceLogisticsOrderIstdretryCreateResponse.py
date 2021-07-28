#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsOrderIstdretryCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsOrderIstdretryCreateResponse, self).__init__()
        self._coupon_fee = None
        self._deliver_fee = None
        self._dispatch_duration = None
        self._distance = None
        self._fee = None
        self._finish_code = None
        self._insurance_fee = None
        self._order_no = None
        self._pay_amount = None
        self._pickup_code = None
        self._status = None
        self._waybill_no = None

    @property
    def coupon_fee(self):
        return self._coupon_fee

    @coupon_fee.setter
    def coupon_fee(self, value):
        self._coupon_fee = value
    @property
    def deliver_fee(self):
        return self._deliver_fee

    @deliver_fee.setter
    def deliver_fee(self, value):
        self._deliver_fee = value
    @property
    def dispatch_duration(self):
        return self._dispatch_duration

    @dispatch_duration.setter
    def dispatch_duration(self, value):
        self._dispatch_duration = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        self._fee = value
    @property
    def finish_code(self):
        return self._finish_code

    @finish_code.setter
    def finish_code(self, value):
        self._finish_code = value
    @property
    def insurance_fee(self):
        return self._insurance_fee

    @insurance_fee.setter
    def insurance_fee(self, value):
        self._insurance_fee = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pickup_code(self):
        return self._pickup_code

    @pickup_code.setter
    def pickup_code(self, value):
        self._pickup_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsOrderIstdretryCreateResponse, self).parse_response_content(response_content)
        if 'coupon_fee' in response:
            self.coupon_fee = response['coupon_fee']
        if 'deliver_fee' in response:
            self.deliver_fee = response['deliver_fee']
        if 'dispatch_duration' in response:
            self.dispatch_duration = response['dispatch_duration']
        if 'distance' in response:
            self.distance = response['distance']
        if 'fee' in response:
            self.fee = response['fee']
        if 'finish_code' in response:
            self.finish_code = response['finish_code']
        if 'insurance_fee' in response:
            self.insurance_fee = response['insurance_fee']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'pickup_code' in response:
            self.pickup_code = response['pickup_code']
        if 'status' in response:
            self.status = response['status']
        if 'waybill_no' in response:
            self.waybill_no = response['waybill_no']
