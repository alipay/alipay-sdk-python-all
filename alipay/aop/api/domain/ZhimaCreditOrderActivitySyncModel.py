#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditOrderActivitySyncModel(object):

    def __init__(self):
        self._activity_code = None
        self._expected_deduct_time = None
        self._lottery_result = None
        self._open_id = None
        self._out_order_no = None
        self._user_id = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def expected_deduct_time(self):
        return self._expected_deduct_time

    @expected_deduct_time.setter
    def expected_deduct_time(self, value):
        self._expected_deduct_time = value
    @property
    def lottery_result(self):
        return self._lottery_result

    @lottery_result.setter
    def lottery_result(self, value):
        self._lottery_result = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.expected_deduct_time:
            if hasattr(self.expected_deduct_time, 'to_alipay_dict'):
                params['expected_deduct_time'] = self.expected_deduct_time.to_alipay_dict()
            else:
                params['expected_deduct_time'] = self.expected_deduct_time
        if self.lottery_result:
            if hasattr(self.lottery_result, 'to_alipay_dict'):
                params['lottery_result'] = self.lottery_result.to_alipay_dict()
            else:
                params['lottery_result'] = self.lottery_result
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditOrderActivitySyncModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'expected_deduct_time' in d:
            o.expected_deduct_time = d['expected_deduct_time']
        if 'lottery_result' in d:
            o.lottery_result = d['lottery_result']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


