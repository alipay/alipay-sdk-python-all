#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HonorRepayRecordDTO(object):

    def __init__(self):
        self._out_order_no = None
        self._out_repay_no = None
        self._repay_amount = None
        self._repay_result = None
        self._repay_status = None
        self._repay_time = None

    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_repay_no(self):
        return self._out_repay_no

    @out_repay_no.setter
    def out_repay_no(self, value):
        self._out_repay_no = value
    @property
    def repay_amount(self):
        return self._repay_amount

    @repay_amount.setter
    def repay_amount(self, value):
        self._repay_amount = value
    @property
    def repay_result(self):
        return self._repay_result

    @repay_result.setter
    def repay_result(self, value):
        self._repay_result = value
    @property
    def repay_status(self):
        return self._repay_status

    @repay_status.setter
    def repay_status(self, value):
        self._repay_status = value
    @property
    def repay_time(self):
        return self._repay_time

    @repay_time.setter
    def repay_time(self, value):
        self._repay_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.out_repay_no:
            if hasattr(self.out_repay_no, 'to_alipay_dict'):
                params['out_repay_no'] = self.out_repay_no.to_alipay_dict()
            else:
                params['out_repay_no'] = self.out_repay_no
        if self.repay_amount:
            if hasattr(self.repay_amount, 'to_alipay_dict'):
                params['repay_amount'] = self.repay_amount.to_alipay_dict()
            else:
                params['repay_amount'] = self.repay_amount
        if self.repay_result:
            if hasattr(self.repay_result, 'to_alipay_dict'):
                params['repay_result'] = self.repay_result.to_alipay_dict()
            else:
                params['repay_result'] = self.repay_result
        if self.repay_status:
            if hasattr(self.repay_status, 'to_alipay_dict'):
                params['repay_status'] = self.repay_status.to_alipay_dict()
            else:
                params['repay_status'] = self.repay_status
        if self.repay_time:
            if hasattr(self.repay_time, 'to_alipay_dict'):
                params['repay_time'] = self.repay_time.to_alipay_dict()
            else:
                params['repay_time'] = self.repay_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HonorRepayRecordDTO()
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_repay_no' in d:
            o.out_repay_no = d['out_repay_no']
        if 'repay_amount' in d:
            o.repay_amount = d['repay_amount']
        if 'repay_result' in d:
            o.repay_result = d['repay_result']
        if 'repay_status' in d:
            o.repay_status = d['repay_status']
        if 'repay_time' in d:
            o.repay_time = d['repay_time']
        return o


