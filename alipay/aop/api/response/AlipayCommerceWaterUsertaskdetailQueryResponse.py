#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceWaterUsertaskdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceWaterUsertaskdetailQueryResponse, self).__init__()
        self._credit_no = None
        self._last_date = None
        self._out_order_no = None
        self._pay_count = None
        self._prize_name = None
        self._send_shop_name = None
        self._sign_date = None
        self._task_id = None
        self._uid = None
        self._uid_open_id = None
        self._user_task_id = None
        self._user_task_pay_status = None
        self._user_task_status = None

    @property
    def credit_no(self):
        return self._credit_no

    @credit_no.setter
    def credit_no(self, value):
        self._credit_no = value
    @property
    def last_date(self):
        return self._last_date

    @last_date.setter
    def last_date(self, value):
        self._last_date = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def pay_count(self):
        return self._pay_count

    @pay_count.setter
    def pay_count(self, value):
        self._pay_count = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def send_shop_name(self):
        return self._send_shop_name

    @send_shop_name.setter
    def send_shop_name(self, value):
        self._send_shop_name = value
    @property
    def sign_date(self):
        return self._sign_date

    @sign_date.setter
    def sign_date(self, value):
        self._sign_date = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def uid_open_id(self):
        return self._uid_open_id

    @uid_open_id.setter
    def uid_open_id(self, value):
        self._uid_open_id = value
    @property
    def user_task_id(self):
        return self._user_task_id

    @user_task_id.setter
    def user_task_id(self, value):
        self._user_task_id = value
    @property
    def user_task_pay_status(self):
        return self._user_task_pay_status

    @user_task_pay_status.setter
    def user_task_pay_status(self, value):
        self._user_task_pay_status = value
    @property
    def user_task_status(self):
        return self._user_task_status

    @user_task_status.setter
    def user_task_status(self, value):
        self._user_task_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceWaterUsertaskdetailQueryResponse, self).parse_response_content(response_content)
        if 'credit_no' in response:
            self.credit_no = response['credit_no']
        if 'last_date' in response:
            self.last_date = response['last_date']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'pay_count' in response:
            self.pay_count = response['pay_count']
        if 'prize_name' in response:
            self.prize_name = response['prize_name']
        if 'send_shop_name' in response:
            self.send_shop_name = response['send_shop_name']
        if 'sign_date' in response:
            self.sign_date = response['sign_date']
        if 'task_id' in response:
            self.task_id = response['task_id']
        if 'uid' in response:
            self.uid = response['uid']
        if 'uid_open_id' in response:
            self.uid_open_id = response['uid_open_id']
        if 'user_task_id' in response:
            self.user_task_id = response['user_task_id']
        if 'user_task_pay_status' in response:
            self.user_task_pay_status = response['user_task_pay_status']
        if 'user_task_status' in response:
            self.user_task_status = response['user_task_status']
