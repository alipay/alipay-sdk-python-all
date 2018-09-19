#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantOrderRentQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantOrderRentQueryResponse, self).__init__()
        self._admit_state = None
        self._alipay_fund_order_no = None
        self._borrow_time = None
        self._goods_name = None
        self._order_no = None
        self._pay_amount = None
        self._pay_amount_type = None
        self._pay_status = None
        self._pay_time = None
        self._restore_time = None
        self._use_state = None
        self._user_id = None

    @property
    def admit_state(self):
        return self._admit_state

    @admit_state.setter
    def admit_state(self, value):
        self._admit_state = value
    @property
    def alipay_fund_order_no(self):
        return self._alipay_fund_order_no

    @alipay_fund_order_no.setter
    def alipay_fund_order_no(self, value):
        self._alipay_fund_order_no = value
    @property
    def borrow_time(self):
        return self._borrow_time

    @borrow_time.setter
    def borrow_time(self, value):
        self._borrow_time = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
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
    def pay_amount_type(self):
        return self._pay_amount_type

    @pay_amount_type.setter
    def pay_amount_type(self, value):
        self._pay_amount_type = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def restore_time(self):
        return self._restore_time

    @restore_time.setter
    def restore_time(self, value):
        self._restore_time = value
    @property
    def use_state(self):
        return self._use_state

    @use_state.setter
    def use_state(self, value):
        self._use_state = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantOrderRentQueryResponse, self).parse_response_content(response_content)
        if 'admit_state' in response:
            self.admit_state = response['admit_state']
        if 'alipay_fund_order_no' in response:
            self.alipay_fund_order_no = response['alipay_fund_order_no']
        if 'borrow_time' in response:
            self.borrow_time = response['borrow_time']
        if 'goods_name' in response:
            self.goods_name = response['goods_name']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'pay_amount_type' in response:
            self.pay_amount_type = response['pay_amount_type']
        if 'pay_status' in response:
            self.pay_status = response['pay_status']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'restore_time' in response:
            self.restore_time = response['restore_time']
        if 'use_state' in response:
            self.use_state = response['use_state']
        if 'user_id' in response:
            self.user_id = response['user_id']
