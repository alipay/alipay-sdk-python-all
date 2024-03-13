#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAcommunicationCreditphonePeriodorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationCreditphonePeriodorderQueryResponse, self).__init__()
        self._alipay_biz_no = None
        self._alipay_open_id = None
        self._alipay_order_no = None
        self._alipay_user_id = None
        self._out_biz_no = None
        self._pay_order_amount = None
        self._pay_order_status = None
        self._pay_order_trade_no = None
        self._pay_order_user_actual_amount = None
        self._period_amount = None
        self._period_status = None
        self._step_number = None
        self._user_period_status = None

    @property
    def alipay_biz_no(self):
        return self._alipay_biz_no

    @alipay_biz_no.setter
    def alipay_biz_no(self, value):
        self._alipay_biz_no = value
    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pay_order_amount(self):
        return self._pay_order_amount

    @pay_order_amount.setter
    def pay_order_amount(self, value):
        self._pay_order_amount = value
    @property
    def pay_order_status(self):
        return self._pay_order_status

    @pay_order_status.setter
    def pay_order_status(self, value):
        self._pay_order_status = value
    @property
    def pay_order_trade_no(self):
        return self._pay_order_trade_no

    @pay_order_trade_no.setter
    def pay_order_trade_no(self, value):
        self._pay_order_trade_no = value
    @property
    def pay_order_user_actual_amount(self):
        return self._pay_order_user_actual_amount

    @pay_order_user_actual_amount.setter
    def pay_order_user_actual_amount(self, value):
        self._pay_order_user_actual_amount = value
    @property
    def period_amount(self):
        return self._period_amount

    @period_amount.setter
    def period_amount(self, value):
        self._period_amount = value
    @property
    def period_status(self):
        return self._period_status

    @period_status.setter
    def period_status(self, value):
        self._period_status = value
    @property
    def step_number(self):
        return self._step_number

    @step_number.setter
    def step_number(self, value):
        self._step_number = value
    @property
    def user_period_status(self):
        return self._user_period_status

    @user_period_status.setter
    def user_period_status(self, value):
        self._user_period_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationCreditphonePeriodorderQueryResponse, self).parse_response_content(response_content)
        if 'alipay_biz_no' in response:
            self.alipay_biz_no = response['alipay_biz_no']
        if 'alipay_open_id' in response:
            self.alipay_open_id = response['alipay_open_id']
        if 'alipay_order_no' in response:
            self.alipay_order_no = response['alipay_order_no']
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'pay_order_amount' in response:
            self.pay_order_amount = response['pay_order_amount']
        if 'pay_order_status' in response:
            self.pay_order_status = response['pay_order_status']
        if 'pay_order_trade_no' in response:
            self.pay_order_trade_no = response['pay_order_trade_no']
        if 'pay_order_user_actual_amount' in response:
            self.pay_order_user_actual_amount = response['pay_order_user_actual_amount']
        if 'period_amount' in response:
            self.period_amount = response['period_amount']
        if 'period_status' in response:
            self.period_status = response['period_status']
        if 'step_number' in response:
            self.step_number = response['step_number']
        if 'user_period_status' in response:
            self.user_period_status = response['user_period_status']
