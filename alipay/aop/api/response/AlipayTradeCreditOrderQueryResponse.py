#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeCreditOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCreditOrderQueryResponse, self).__init__()
        self._advance_total_fee = None
        self._buyer_pay_time = None
        self._credit_biz_order_id = None
        self._credit_pay_fee = None
        self._credit_quota_confirm_time = None
        self._credit_quota_pay_time = None
        self._credit_refund_fee = None
        self._credit_task_first_exec_time = None
        self._credit_total_fee = None
        self._guarantee_pay_time = None
        self._out_trade_no = None
        self._overdue_time = None
        self._status = None
        self._trade_no = None

    @property
    def advance_total_fee(self):
        return self._advance_total_fee

    @advance_total_fee.setter
    def advance_total_fee(self, value):
        self._advance_total_fee = value
    @property
    def buyer_pay_time(self):
        return self._buyer_pay_time

    @buyer_pay_time.setter
    def buyer_pay_time(self, value):
        self._buyer_pay_time = value
    @property
    def credit_biz_order_id(self):
        return self._credit_biz_order_id

    @credit_biz_order_id.setter
    def credit_biz_order_id(self, value):
        self._credit_biz_order_id = value
    @property
    def credit_pay_fee(self):
        return self._credit_pay_fee

    @credit_pay_fee.setter
    def credit_pay_fee(self, value):
        self._credit_pay_fee = value
    @property
    def credit_quota_confirm_time(self):
        return self._credit_quota_confirm_time

    @credit_quota_confirm_time.setter
    def credit_quota_confirm_time(self, value):
        self._credit_quota_confirm_time = value
    @property
    def credit_quota_pay_time(self):
        return self._credit_quota_pay_time

    @credit_quota_pay_time.setter
    def credit_quota_pay_time(self, value):
        self._credit_quota_pay_time = value
    @property
    def credit_refund_fee(self):
        return self._credit_refund_fee

    @credit_refund_fee.setter
    def credit_refund_fee(self, value):
        self._credit_refund_fee = value
    @property
    def credit_task_first_exec_time(self):
        return self._credit_task_first_exec_time

    @credit_task_first_exec_time.setter
    def credit_task_first_exec_time(self, value):
        self._credit_task_first_exec_time = value
    @property
    def credit_total_fee(self):
        return self._credit_total_fee

    @credit_total_fee.setter
    def credit_total_fee(self, value):
        self._credit_total_fee = value
    @property
    def guarantee_pay_time(self):
        return self._guarantee_pay_time

    @guarantee_pay_time.setter
    def guarantee_pay_time(self, value):
        self._guarantee_pay_time = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def overdue_time(self):
        return self._overdue_time

    @overdue_time.setter
    def overdue_time(self, value):
        self._overdue_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeCreditOrderQueryResponse, self).parse_response_content(response_content)
        if 'advance_total_fee' in response:
            self.advance_total_fee = response['advance_total_fee']
        if 'buyer_pay_time' in response:
            self.buyer_pay_time = response['buyer_pay_time']
        if 'credit_biz_order_id' in response:
            self.credit_biz_order_id = response['credit_biz_order_id']
        if 'credit_pay_fee' in response:
            self.credit_pay_fee = response['credit_pay_fee']
        if 'credit_quota_confirm_time' in response:
            self.credit_quota_confirm_time = response['credit_quota_confirm_time']
        if 'credit_quota_pay_time' in response:
            self.credit_quota_pay_time = response['credit_quota_pay_time']
        if 'credit_refund_fee' in response:
            self.credit_refund_fee = response['credit_refund_fee']
        if 'credit_task_first_exec_time' in response:
            self.credit_task_first_exec_time = response['credit_task_first_exec_time']
        if 'credit_total_fee' in response:
            self.credit_total_fee = response['credit_total_fee']
        if 'guarantee_pay_time' in response:
            self.guarantee_pay_time = response['guarantee_pay_time']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'overdue_time' in response:
            self.overdue_time = response['overdue_time']
        if 'status' in response:
            self.status = response['status']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
