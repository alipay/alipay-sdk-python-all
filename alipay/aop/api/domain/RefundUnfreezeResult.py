#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RefundUnfreezeResult(object):

    def __init__(self):
        self._freeze_no = None
        self._result_code = None
        self._status = None
        self._unfreeze_amount = None
        self._unfreeze_no = None
        self._unfreeze_time = None

    @property
    def freeze_no(self):
        return self._freeze_no

    @freeze_no.setter
    def freeze_no(self, value):
        self._freeze_no = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def unfreeze_amount(self):
        return self._unfreeze_amount

    @unfreeze_amount.setter
    def unfreeze_amount(self, value):
        self._unfreeze_amount = value
    @property
    def unfreeze_no(self):
        return self._unfreeze_no

    @unfreeze_no.setter
    def unfreeze_no(self, value):
        self._unfreeze_no = value
    @property
    def unfreeze_time(self):
        return self._unfreeze_time

    @unfreeze_time.setter
    def unfreeze_time(self, value):
        self._unfreeze_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.freeze_no:
            if hasattr(self.freeze_no, 'to_alipay_dict'):
                params['freeze_no'] = self.freeze_no.to_alipay_dict()
            else:
                params['freeze_no'] = self.freeze_no
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.unfreeze_amount:
            if hasattr(self.unfreeze_amount, 'to_alipay_dict'):
                params['unfreeze_amount'] = self.unfreeze_amount.to_alipay_dict()
            else:
                params['unfreeze_amount'] = self.unfreeze_amount
        if self.unfreeze_no:
            if hasattr(self.unfreeze_no, 'to_alipay_dict'):
                params['unfreeze_no'] = self.unfreeze_no.to_alipay_dict()
            else:
                params['unfreeze_no'] = self.unfreeze_no
        if self.unfreeze_time:
            if hasattr(self.unfreeze_time, 'to_alipay_dict'):
                params['unfreeze_time'] = self.unfreeze_time.to_alipay_dict()
            else:
                params['unfreeze_time'] = self.unfreeze_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundUnfreezeResult()
        if 'freeze_no' in d:
            o.freeze_no = d['freeze_no']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'status' in d:
            o.status = d['status']
        if 'unfreeze_amount' in d:
            o.unfreeze_amount = d['unfreeze_amount']
        if 'unfreeze_no' in d:
            o.unfreeze_no = d['unfreeze_no']
        if 'unfreeze_time' in d:
            o.unfreeze_time = d['unfreeze_time']
        return o


