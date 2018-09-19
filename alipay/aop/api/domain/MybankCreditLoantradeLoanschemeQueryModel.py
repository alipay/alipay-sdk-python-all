#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoantradeLoanschemeQueryModel(object):

    def __init__(self):
        self._biz = None
        self._biz_no = None
        self._entity_code = None
        self._entity_name = None
        self._entity_type = None
        self._loan_policy_code = None
        self._out_uni_code = None
        self._sale_pd_code = None
        self._scen = None

    @property
    def biz(self):
        return self._biz

    @biz.setter
    def biz(self, value):
        self._biz = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def entity_code(self):
        return self._entity_code

    @entity_code.setter
    def entity_code(self, value):
        self._entity_code = value
    @property
    def entity_name(self):
        return self._entity_name

    @entity_name.setter
    def entity_name(self, value):
        self._entity_name = value
    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value
    @property
    def loan_policy_code(self):
        return self._loan_policy_code

    @loan_policy_code.setter
    def loan_policy_code(self, value):
        self._loan_policy_code = value
    @property
    def out_uni_code(self):
        return self._out_uni_code

    @out_uni_code.setter
    def out_uni_code(self, value):
        self._out_uni_code = value
    @property
    def sale_pd_code(self):
        return self._sale_pd_code

    @sale_pd_code.setter
    def sale_pd_code(self, value):
        self._sale_pd_code = value
    @property
    def scen(self):
        return self._scen

    @scen.setter
    def scen(self, value):
        self._scen = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz:
            if hasattr(self.biz, 'to_alipay_dict'):
                params['biz'] = self.biz.to_alipay_dict()
            else:
                params['biz'] = self.biz
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.entity_code:
            if hasattr(self.entity_code, 'to_alipay_dict'):
                params['entity_code'] = self.entity_code.to_alipay_dict()
            else:
                params['entity_code'] = self.entity_code
        if self.entity_name:
            if hasattr(self.entity_name, 'to_alipay_dict'):
                params['entity_name'] = self.entity_name.to_alipay_dict()
            else:
                params['entity_name'] = self.entity_name
        if self.entity_type:
            if hasattr(self.entity_type, 'to_alipay_dict'):
                params['entity_type'] = self.entity_type.to_alipay_dict()
            else:
                params['entity_type'] = self.entity_type
        if self.loan_policy_code:
            if hasattr(self.loan_policy_code, 'to_alipay_dict'):
                params['loan_policy_code'] = self.loan_policy_code.to_alipay_dict()
            else:
                params['loan_policy_code'] = self.loan_policy_code
        if self.out_uni_code:
            if hasattr(self.out_uni_code, 'to_alipay_dict'):
                params['out_uni_code'] = self.out_uni_code.to_alipay_dict()
            else:
                params['out_uni_code'] = self.out_uni_code
        if self.sale_pd_code:
            if hasattr(self.sale_pd_code, 'to_alipay_dict'):
                params['sale_pd_code'] = self.sale_pd_code.to_alipay_dict()
            else:
                params['sale_pd_code'] = self.sale_pd_code
        if self.scen:
            if hasattr(self.scen, 'to_alipay_dict'):
                params['scen'] = self.scen.to_alipay_dict()
            else:
                params['scen'] = self.scen
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeLoanschemeQueryModel()
        if 'biz' in d:
            o.biz = d['biz']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'entity_code' in d:
            o.entity_code = d['entity_code']
        if 'entity_name' in d:
            o.entity_name = d['entity_name']
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        if 'loan_policy_code' in d:
            o.loan_policy_code = d['loan_policy_code']
        if 'out_uni_code' in d:
            o.out_uni_code = d['out_uni_code']
        if 'sale_pd_code' in d:
            o.sale_pd_code = d['sale_pd_code']
        if 'scen' in d:
            o.scen = d['scen']
        return o


