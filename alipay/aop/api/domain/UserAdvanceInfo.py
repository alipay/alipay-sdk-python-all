#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserAdvanceInfo(object):

    def __init__(self):
        self._consult_result = None
        self._user_alipay_parking_allow_advance = None
        self._user_wait_repayment_amount = None
        self._user_wait_repayment_order_count = None

    @property
    def consult_result(self):
        return self._consult_result

    @consult_result.setter
    def consult_result(self, value):
        self._consult_result = value
    @property
    def user_alipay_parking_allow_advance(self):
        return self._user_alipay_parking_allow_advance

    @user_alipay_parking_allow_advance.setter
    def user_alipay_parking_allow_advance(self, value):
        self._user_alipay_parking_allow_advance = value
    @property
    def user_wait_repayment_amount(self):
        return self._user_wait_repayment_amount

    @user_wait_repayment_amount.setter
    def user_wait_repayment_amount(self, value):
        self._user_wait_repayment_amount = value
    @property
    def user_wait_repayment_order_count(self):
        return self._user_wait_repayment_order_count

    @user_wait_repayment_order_count.setter
    def user_wait_repayment_order_count(self, value):
        self._user_wait_repayment_order_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.consult_result:
            if hasattr(self.consult_result, 'to_alipay_dict'):
                params['consult_result'] = self.consult_result.to_alipay_dict()
            else:
                params['consult_result'] = self.consult_result
        if self.user_alipay_parking_allow_advance:
            if hasattr(self.user_alipay_parking_allow_advance, 'to_alipay_dict'):
                params['user_alipay_parking_allow_advance'] = self.user_alipay_parking_allow_advance.to_alipay_dict()
            else:
                params['user_alipay_parking_allow_advance'] = self.user_alipay_parking_allow_advance
        if self.user_wait_repayment_amount:
            if hasattr(self.user_wait_repayment_amount, 'to_alipay_dict'):
                params['user_wait_repayment_amount'] = self.user_wait_repayment_amount.to_alipay_dict()
            else:
                params['user_wait_repayment_amount'] = self.user_wait_repayment_amount
        if self.user_wait_repayment_order_count:
            if hasattr(self.user_wait_repayment_order_count, 'to_alipay_dict'):
                params['user_wait_repayment_order_count'] = self.user_wait_repayment_order_count.to_alipay_dict()
            else:
                params['user_wait_repayment_order_count'] = self.user_wait_repayment_order_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserAdvanceInfo()
        if 'consult_result' in d:
            o.consult_result = d['consult_result']
        if 'user_alipay_parking_allow_advance' in d:
            o.user_alipay_parking_allow_advance = d['user_alipay_parking_allow_advance']
        if 'user_wait_repayment_amount' in d:
            o.user_wait_repayment_amount = d['user_wait_repayment_amount']
        if 'user_wait_repayment_order_count' in d:
            o.user_wait_repayment_order_count = d['user_wait_repayment_order_count']
        return o


