#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundIndustryOperationQueryModel(object):

    def __init__(self):
        self._operation_id = None
        self._pay_out_request_no = None
        self._refund_out_request_no = None

    @property
    def operation_id(self):
        return self._operation_id

    @operation_id.setter
    def operation_id(self, value):
        self._operation_id = value
    @property
    def pay_out_request_no(self):
        return self._pay_out_request_no

    @pay_out_request_no.setter
    def pay_out_request_no(self, value):
        self._pay_out_request_no = value
    @property
    def refund_out_request_no(self):
        return self._refund_out_request_no

    @refund_out_request_no.setter
    def refund_out_request_no(self, value):
        self._refund_out_request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.operation_id:
            if hasattr(self.operation_id, 'to_alipay_dict'):
                params['operation_id'] = self.operation_id.to_alipay_dict()
            else:
                params['operation_id'] = self.operation_id
        if self.pay_out_request_no:
            if hasattr(self.pay_out_request_no, 'to_alipay_dict'):
                params['pay_out_request_no'] = self.pay_out_request_no.to_alipay_dict()
            else:
                params['pay_out_request_no'] = self.pay_out_request_no
        if self.refund_out_request_no:
            if hasattr(self.refund_out_request_no, 'to_alipay_dict'):
                params['refund_out_request_no'] = self.refund_out_request_no.to_alipay_dict()
            else:
                params['refund_out_request_no'] = self.refund_out_request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundIndustryOperationQueryModel()
        if 'operation_id' in d:
            o.operation_id = d['operation_id']
        if 'pay_out_request_no' in d:
            o.pay_out_request_no = d['pay_out_request_no']
        if 'refund_out_request_no' in d:
            o.refund_out_request_no = d['refund_out_request_no']
        return o


