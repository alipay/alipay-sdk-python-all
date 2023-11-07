#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SettleOrderResponse import SettleOrderResponse


class AlipayCommerceDeductionorderDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceDeductionorderDetailQueryResponse, self).__init__()
        self._card_id = None
        self._certificate_id = None
        self._certificate_serial = None
        self._deduction_amount = None
        self._deduction_fail_reason = None
        self._deduction_fail_times = None
        self._deduction_order_id = None
        self._deduction_plan_id = None
        self._deduction_status = None
        self._deduction_time = None
        self._gmt_create = None
        self._login_id = None
        self._open_id = None
        self._order_id = None
        self._plan_deduction_time = None
        self._settle_order_response = None
        self._sub_order_id = None
        self._trade_no = None
        self._user_id = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def certificate_serial(self):
        return self._certificate_serial

    @certificate_serial.setter
    def certificate_serial(self, value):
        self._certificate_serial = value
    @property
    def deduction_amount(self):
        return self._deduction_amount

    @deduction_amount.setter
    def deduction_amount(self, value):
        self._deduction_amount = value
    @property
    def deduction_fail_reason(self):
        return self._deduction_fail_reason

    @deduction_fail_reason.setter
    def deduction_fail_reason(self, value):
        self._deduction_fail_reason = value
    @property
    def deduction_fail_times(self):
        return self._deduction_fail_times

    @deduction_fail_times.setter
    def deduction_fail_times(self, value):
        self._deduction_fail_times = value
    @property
    def deduction_order_id(self):
        return self._deduction_order_id

    @deduction_order_id.setter
    def deduction_order_id(self, value):
        self._deduction_order_id = value
    @property
    def deduction_plan_id(self):
        return self._deduction_plan_id

    @deduction_plan_id.setter
    def deduction_plan_id(self, value):
        self._deduction_plan_id = value
    @property
    def deduction_status(self):
        return self._deduction_status

    @deduction_status.setter
    def deduction_status(self, value):
        self._deduction_status = value
    @property
    def deduction_time(self):
        return self._deduction_time

    @deduction_time.setter
    def deduction_time(self, value):
        self._deduction_time = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def plan_deduction_time(self):
        return self._plan_deduction_time

    @plan_deduction_time.setter
    def plan_deduction_time(self, value):
        self._plan_deduction_time = value
    @property
    def settle_order_response(self):
        return self._settle_order_response

    @settle_order_response.setter
    def settle_order_response(self, value):
        if isinstance(value, SettleOrderResponse):
            self._settle_order_response = value
        else:
            self._settle_order_response = SettleOrderResponse.from_alipay_dict(value)
    @property
    def sub_order_id(self):
        return self._sub_order_id

    @sub_order_id.setter
    def sub_order_id(self, value):
        self._sub_order_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceDeductionorderDetailQueryResponse, self).parse_response_content(response_content)
        if 'card_id' in response:
            self.card_id = response['card_id']
        if 'certificate_id' in response:
            self.certificate_id = response['certificate_id']
        if 'certificate_serial' in response:
            self.certificate_serial = response['certificate_serial']
        if 'deduction_amount' in response:
            self.deduction_amount = response['deduction_amount']
        if 'deduction_fail_reason' in response:
            self.deduction_fail_reason = response['deduction_fail_reason']
        if 'deduction_fail_times' in response:
            self.deduction_fail_times = response['deduction_fail_times']
        if 'deduction_order_id' in response:
            self.deduction_order_id = response['deduction_order_id']
        if 'deduction_plan_id' in response:
            self.deduction_plan_id = response['deduction_plan_id']
        if 'deduction_status' in response:
            self.deduction_status = response['deduction_status']
        if 'deduction_time' in response:
            self.deduction_time = response['deduction_time']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'login_id' in response:
            self.login_id = response['login_id']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'plan_deduction_time' in response:
            self.plan_deduction_time = response['plan_deduction_time']
        if 'settle_order_response' in response:
            self.settle_order_response = response['settle_order_response']
        if 'sub_order_id' in response:
            self.sub_order_id = response['sub_order_id']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'user_id' in response:
            self.user_id = response['user_id']
