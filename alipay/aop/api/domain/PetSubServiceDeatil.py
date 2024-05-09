#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PetSubServiceDeatil(object):

    def __init__(self):
        self._actual_time = None
        self._amount = None
        self._expect_time = None
        self._ext_info = None
        self._period = None
        self._status = None
        self._sub_biz_id = None

    @property
    def actual_time(self):
        return self._actual_time

    @actual_time.setter
    def actual_time(self, value):
        self._actual_time = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def expect_time(self):
        return self._expect_time

    @expect_time.setter
    def expect_time(self, value):
        self._expect_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_biz_id(self):
        return self._sub_biz_id

    @sub_biz_id.setter
    def sub_biz_id(self, value):
        self._sub_biz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_time:
            if hasattr(self.actual_time, 'to_alipay_dict'):
                params['actual_time'] = self.actual_time.to_alipay_dict()
            else:
                params['actual_time'] = self.actual_time
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.expect_time:
            if hasattr(self.expect_time, 'to_alipay_dict'):
                params['expect_time'] = self.expect_time.to_alipay_dict()
            else:
                params['expect_time'] = self.expect_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_biz_id:
            if hasattr(self.sub_biz_id, 'to_alipay_dict'):
                params['sub_biz_id'] = self.sub_biz_id.to_alipay_dict()
            else:
                params['sub_biz_id'] = self.sub_biz_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PetSubServiceDeatil()
        if 'actual_time' in d:
            o.actual_time = d['actual_time']
        if 'amount' in d:
            o.amount = d['amount']
        if 'expect_time' in d:
            o.expect_time = d['expect_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'period' in d:
            o.period = d['period']
        if 'status' in d:
            o.status = d['status']
        if 'sub_biz_id' in d:
            o.sub_biz_id = d['sub_biz_id']
        return o


