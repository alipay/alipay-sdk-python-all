#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HonorRepayApplyTermDTO import HonorRepayApplyTermDTO


class HonorRepayApplyResultDTO(object):

    def __init__(self):
        self._channel_customer_id = None
        self._loan_apply_no = None
        self._out_order_no = None
        self._out_repay_no = None
        self._repay_amount = None
        self._repay_no = None
        self._repay_result = None
        self._repay_source = None
        self._repay_status = None
        self._repay_terms = None
        self._repay_time = None

    @property
    def channel_customer_id(self):
        return self._channel_customer_id

    @channel_customer_id.setter
    def channel_customer_id(self, value):
        self._channel_customer_id = value
    @property
    def loan_apply_no(self):
        return self._loan_apply_no

    @loan_apply_no.setter
    def loan_apply_no(self, value):
        self._loan_apply_no = value
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
    def repay_no(self):
        return self._repay_no

    @repay_no.setter
    def repay_no(self, value):
        self._repay_no = value
    @property
    def repay_result(self):
        return self._repay_result

    @repay_result.setter
    def repay_result(self, value):
        self._repay_result = value
    @property
    def repay_source(self):
        return self._repay_source

    @repay_source.setter
    def repay_source(self, value):
        self._repay_source = value
    @property
    def repay_status(self):
        return self._repay_status

    @repay_status.setter
    def repay_status(self, value):
        self._repay_status = value
    @property
    def repay_terms(self):
        return self._repay_terms

    @repay_terms.setter
    def repay_terms(self, value):
        if isinstance(value, list):
            self._repay_terms = list()
            for i in value:
                if isinstance(i, HonorRepayApplyTermDTO):
                    self._repay_terms.append(i)
                else:
                    self._repay_terms.append(HonorRepayApplyTermDTO.from_alipay_dict(i))
    @property
    def repay_time(self):
        return self._repay_time

    @repay_time.setter
    def repay_time(self, value):
        self._repay_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_customer_id:
            if hasattr(self.channel_customer_id, 'to_alipay_dict'):
                params['channel_customer_id'] = self.channel_customer_id.to_alipay_dict()
            else:
                params['channel_customer_id'] = self.channel_customer_id
        if self.loan_apply_no:
            if hasattr(self.loan_apply_no, 'to_alipay_dict'):
                params['loan_apply_no'] = self.loan_apply_no.to_alipay_dict()
            else:
                params['loan_apply_no'] = self.loan_apply_no
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
        if self.repay_no:
            if hasattr(self.repay_no, 'to_alipay_dict'):
                params['repay_no'] = self.repay_no.to_alipay_dict()
            else:
                params['repay_no'] = self.repay_no
        if self.repay_result:
            if hasattr(self.repay_result, 'to_alipay_dict'):
                params['repay_result'] = self.repay_result.to_alipay_dict()
            else:
                params['repay_result'] = self.repay_result
        if self.repay_source:
            if hasattr(self.repay_source, 'to_alipay_dict'):
                params['repay_source'] = self.repay_source.to_alipay_dict()
            else:
                params['repay_source'] = self.repay_source
        if self.repay_status:
            if hasattr(self.repay_status, 'to_alipay_dict'):
                params['repay_status'] = self.repay_status.to_alipay_dict()
            else:
                params['repay_status'] = self.repay_status
        if self.repay_terms:
            if isinstance(self.repay_terms, list):
                for i in range(0, len(self.repay_terms)):
                    element = self.repay_terms[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.repay_terms[i] = element.to_alipay_dict()
            if hasattr(self.repay_terms, 'to_alipay_dict'):
                params['repay_terms'] = self.repay_terms.to_alipay_dict()
            else:
                params['repay_terms'] = self.repay_terms
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
        o = HonorRepayApplyResultDTO()
        if 'channel_customer_id' in d:
            o.channel_customer_id = d['channel_customer_id']
        if 'loan_apply_no' in d:
            o.loan_apply_no = d['loan_apply_no']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_repay_no' in d:
            o.out_repay_no = d['out_repay_no']
        if 'repay_amount' in d:
            o.repay_amount = d['repay_amount']
        if 'repay_no' in d:
            o.repay_no = d['repay_no']
        if 'repay_result' in d:
            o.repay_result = d['repay_result']
        if 'repay_source' in d:
            o.repay_source = d['repay_source']
        if 'repay_status' in d:
            o.repay_status = d['repay_status']
        if 'repay_terms' in d:
            o.repay_terms = d['repay_terms']
        if 'repay_time' in d:
            o.repay_time = d['repay_time']
        return o


