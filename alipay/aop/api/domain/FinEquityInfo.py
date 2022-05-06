#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QYBMapInfo import QYBMapInfo


class FinEquityInfo(object):

    def __init__(self):
        self._end_time = None
        self._equity_code = None
        self._equity_num = None
        self._equity_type = None
        self._product_code = None
        self._remark = None
        self._start_time = None
        self._status = None
        self._verification_info = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def equity_code(self):
        return self._equity_code

    @equity_code.setter
    def equity_code(self, value):
        self._equity_code = value
    @property
    def equity_num(self):
        return self._equity_num

    @equity_num.setter
    def equity_num(self, value):
        self._equity_num = value
    @property
    def equity_type(self):
        return self._equity_type

    @equity_type.setter
    def equity_type(self, value):
        self._equity_type = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def verification_info(self):
        return self._verification_info

    @verification_info.setter
    def verification_info(self, value):
        if isinstance(value, QYBMapInfo):
            self._verification_info = value
        else:
            self._verification_info = QYBMapInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.equity_code:
            if hasattr(self.equity_code, 'to_alipay_dict'):
                params['equity_code'] = self.equity_code.to_alipay_dict()
            else:
                params['equity_code'] = self.equity_code
        if self.equity_num:
            if hasattr(self.equity_num, 'to_alipay_dict'):
                params['equity_num'] = self.equity_num.to_alipay_dict()
            else:
                params['equity_num'] = self.equity_num
        if self.equity_type:
            if hasattr(self.equity_type, 'to_alipay_dict'):
                params['equity_type'] = self.equity_type.to_alipay_dict()
            else:
                params['equity_type'] = self.equity_type
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.verification_info:
            if hasattr(self.verification_info, 'to_alipay_dict'):
                params['verification_info'] = self.verification_info.to_alipay_dict()
            else:
                params['verification_info'] = self.verification_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FinEquityInfo()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'equity_code' in d:
            o.equity_code = d['equity_code']
        if 'equity_num' in d:
            o.equity_num = d['equity_num']
        if 'equity_type' in d:
            o.equity_type = d['equity_type']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'remark' in d:
            o.remark = d['remark']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'verification_info' in d:
            o.verification_info = d['verification_info']
        return o


