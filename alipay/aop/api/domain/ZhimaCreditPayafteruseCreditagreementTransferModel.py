#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPayafteruseCreditagreementTransferModel(object):

    def __init__(self):
        self._category_id = None
        self._deduct_agreement_no = None
        self._extend_params = None
        self._out_agreement_no = None
        self._product_code = None
        self._zm_service_id = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def deduct_agreement_no(self):
        return self._deduct_agreement_no

    @deduct_agreement_no.setter
    def deduct_agreement_no(self, value):
        self._deduct_agreement_no = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
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
    def zm_service_id(self):
        return self._zm_service_id

    @zm_service_id.setter
    def zm_service_id(self, value):
        self._zm_service_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.deduct_agreement_no:
            if hasattr(self.deduct_agreement_no, 'to_alipay_dict'):
                params['deduct_agreement_no'] = self.deduct_agreement_no.to_alipay_dict()
            else:
                params['deduct_agreement_no'] = self.deduct_agreement_no
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
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
        if self.zm_service_id:
            if hasattr(self.zm_service_id, 'to_alipay_dict'):
                params['zm_service_id'] = self.zm_service_id.to_alipay_dict()
            else:
                params['zm_service_id'] = self.zm_service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPayafteruseCreditagreementTransferModel()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'deduct_agreement_no' in d:
            o.deduct_agreement_no = d['deduct_agreement_no']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'out_agreement_no' in d:
            o.out_agreement_no = d['out_agreement_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'zm_service_id' in d:
            o.zm_service_id = d['zm_service_id']
        return o


