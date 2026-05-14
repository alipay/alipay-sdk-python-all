#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationCreditphoneOnlineadvanceorderNotifyModel(object):

    def __init__(self):
        self._alipay_online_advance_pay_order_no = None
        self._deduction_amount = None
        self._evaluate_fail_reason = None
        self._evaluate_success = None
        self._fine_interest = None
        self._handling_fee = None
        self._inst_pay_order_no = None
        self._interest = None
        self._next_retry_time = None
        self._pay_link_url = None
        self._principal = None
        self._total_amount = None

    @property
    def alipay_online_advance_pay_order_no(self):
        return self._alipay_online_advance_pay_order_no

    @alipay_online_advance_pay_order_no.setter
    def alipay_online_advance_pay_order_no(self, value):
        self._alipay_online_advance_pay_order_no = value
    @property
    def deduction_amount(self):
        return self._deduction_amount

    @deduction_amount.setter
    def deduction_amount(self, value):
        self._deduction_amount = value
    @property
    def evaluate_fail_reason(self):
        return self._evaluate_fail_reason

    @evaluate_fail_reason.setter
    def evaluate_fail_reason(self, value):
        self._evaluate_fail_reason = value
    @property
    def evaluate_success(self):
        return self._evaluate_success

    @evaluate_success.setter
    def evaluate_success(self, value):
        self._evaluate_success = value
    @property
    def fine_interest(self):
        return self._fine_interest

    @fine_interest.setter
    def fine_interest(self, value):
        self._fine_interest = value
    @property
    def handling_fee(self):
        return self._handling_fee

    @handling_fee.setter
    def handling_fee(self, value):
        self._handling_fee = value
    @property
    def inst_pay_order_no(self):
        return self._inst_pay_order_no

    @inst_pay_order_no.setter
    def inst_pay_order_no(self, value):
        self._inst_pay_order_no = value
    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, value):
        self._interest = value
    @property
    def next_retry_time(self):
        return self._next_retry_time

    @next_retry_time.setter
    def next_retry_time(self, value):
        self._next_retry_time = value
    @property
    def pay_link_url(self):
        return self._pay_link_url

    @pay_link_url.setter
    def pay_link_url(self, value):
        self._pay_link_url = value
    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        self._principal = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_online_advance_pay_order_no:
            if hasattr(self.alipay_online_advance_pay_order_no, 'to_alipay_dict'):
                params['alipay_online_advance_pay_order_no'] = self.alipay_online_advance_pay_order_no.to_alipay_dict()
            else:
                params['alipay_online_advance_pay_order_no'] = self.alipay_online_advance_pay_order_no
        if self.deduction_amount:
            if hasattr(self.deduction_amount, 'to_alipay_dict'):
                params['deduction_amount'] = self.deduction_amount.to_alipay_dict()
            else:
                params['deduction_amount'] = self.deduction_amount
        if self.evaluate_fail_reason:
            if hasattr(self.evaluate_fail_reason, 'to_alipay_dict'):
                params['evaluate_fail_reason'] = self.evaluate_fail_reason.to_alipay_dict()
            else:
                params['evaluate_fail_reason'] = self.evaluate_fail_reason
        if self.evaluate_success:
            if hasattr(self.evaluate_success, 'to_alipay_dict'):
                params['evaluate_success'] = self.evaluate_success.to_alipay_dict()
            else:
                params['evaluate_success'] = self.evaluate_success
        if self.fine_interest:
            if hasattr(self.fine_interest, 'to_alipay_dict'):
                params['fine_interest'] = self.fine_interest.to_alipay_dict()
            else:
                params['fine_interest'] = self.fine_interest
        if self.handling_fee:
            if hasattr(self.handling_fee, 'to_alipay_dict'):
                params['handling_fee'] = self.handling_fee.to_alipay_dict()
            else:
                params['handling_fee'] = self.handling_fee
        if self.inst_pay_order_no:
            if hasattr(self.inst_pay_order_no, 'to_alipay_dict'):
                params['inst_pay_order_no'] = self.inst_pay_order_no.to_alipay_dict()
            else:
                params['inst_pay_order_no'] = self.inst_pay_order_no
        if self.interest:
            if hasattr(self.interest, 'to_alipay_dict'):
                params['interest'] = self.interest.to_alipay_dict()
            else:
                params['interest'] = self.interest
        if self.next_retry_time:
            if hasattr(self.next_retry_time, 'to_alipay_dict'):
                params['next_retry_time'] = self.next_retry_time.to_alipay_dict()
            else:
                params['next_retry_time'] = self.next_retry_time
        if self.pay_link_url:
            if hasattr(self.pay_link_url, 'to_alipay_dict'):
                params['pay_link_url'] = self.pay_link_url.to_alipay_dict()
            else:
                params['pay_link_url'] = self.pay_link_url
        if self.principal:
            if hasattr(self.principal, 'to_alipay_dict'):
                params['principal'] = self.principal.to_alipay_dict()
            else:
                params['principal'] = self.principal
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationCreditphoneOnlineadvanceorderNotifyModel()
        if 'alipay_online_advance_pay_order_no' in d:
            o.alipay_online_advance_pay_order_no = d['alipay_online_advance_pay_order_no']
        if 'deduction_amount' in d:
            o.deduction_amount = d['deduction_amount']
        if 'evaluate_fail_reason' in d:
            o.evaluate_fail_reason = d['evaluate_fail_reason']
        if 'evaluate_success' in d:
            o.evaluate_success = d['evaluate_success']
        if 'fine_interest' in d:
            o.fine_interest = d['fine_interest']
        if 'handling_fee' in d:
            o.handling_fee = d['handling_fee']
        if 'inst_pay_order_no' in d:
            o.inst_pay_order_no = d['inst_pay_order_no']
        if 'interest' in d:
            o.interest = d['interest']
        if 'next_retry_time' in d:
            o.next_retry_time = d['next_retry_time']
        if 'pay_link_url' in d:
            o.pay_link_url = d['pay_link_url']
        if 'principal' in d:
            o.principal = d['principal']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


