#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPayafteruseCreditagreementQueryModel(object):

    def __init__(self):
        self._credit_agreement_id = None
        self._extra_param = None
        self._out_agreement_no = None
        self._product_code = None
        self._service_id = None

    @property
    def credit_agreement_id(self):
        return self._credit_agreement_id

    @credit_agreement_id.setter
    def credit_agreement_id(self, value):
        self._credit_agreement_id = value
    @property
    def extra_param(self):
        return self._extra_param

    @extra_param.setter
    def extra_param(self, value):
        self._extra_param = value
    @property
    def out_agreement_no(self):
        return self._out_agreement_no

    @out_agreement_no.setter
    def out_agreement_no(self, value):
        self._out_agreement_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_agreement_id:
            if hasattr(self.credit_agreement_id, 'to_alipay_dict'):
                params['credit_agreement_id'] = self.credit_agreement_id.to_alipay_dict()
            else:
                params['credit_agreement_id'] = self.credit_agreement_id
        if self.extra_param:
            if hasattr(self.extra_param, 'to_alipay_dict'):
                params['extra_param'] = self.extra_param.to_alipay_dict()
            else:
                params['extra_param'] = self.extra_param
        if self.out_agreement_no:
            if hasattr(self.out_agreement_no, 'to_alipay_dict'):
                params['out_agreement_no'] = self.out_agreement_no.to_alipay_dict()
            else:
                params['out_agreement_no'] = self.out_agreement_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPayafteruseCreditagreementQueryModel()
        if 'credit_agreement_id' in d:
            o.credit_agreement_id = d['credit_agreement_id']
        if 'extra_param' in d:
            o.extra_param = d['extra_param']
        if 'out_agreement_no' in d:
            o.out_agreement_no = d['out_agreement_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'service_id' in d:
            o.service_id = d['service_id']
        return o


