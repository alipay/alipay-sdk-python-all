#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserTaskProgress(object):

    def __init__(self):
        self._progress_time = None
        self._use_discount_amount = None
        self._use_status = None

    @property
    def progress_time(self):
        return self._progress_time

    @progress_time.setter
    def progress_time(self, value):
        self._progress_time = value
    @property
    def use_discount_amount(self):
        return self._use_discount_amount

    @use_discount_amount.setter
    def use_discount_amount(self, value):
        self._use_discount_amount = value
    @property
    def use_status(self):
        return self._use_status

    @use_status.setter
    def use_status(self, value):
        self._use_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.progress_time:
            if hasattr(self.progress_time, 'to_alipay_dict'):
                params['progress_time'] = self.progress_time.to_alipay_dict()
            else:
                params['progress_time'] = self.progress_time
        if self.use_discount_amount:
            if hasattr(self.use_discount_amount, 'to_alipay_dict'):
                params['use_discount_amount'] = self.use_discount_amount.to_alipay_dict()
            else:
                params['use_discount_amount'] = self.use_discount_amount
        if self.use_status:
            if hasattr(self.use_status, 'to_alipay_dict'):
                params['use_status'] = self.use_status.to_alipay_dict()
            else:
                params['use_status'] = self.use_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserTaskProgress()
        if 'progress_time' in d:
            o.progress_time = d['progress_time']
        if 'use_discount_amount' in d:
            o.use_discount_amount = d['use_discount_amount']
        if 'use_status' in d:
            o.use_status = d['use_status']
        return o


