#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundBailCollectionFinishModel(object):

    def __init__(self):
        self._agreement_no = None
        self._extra_param = None
        self._out_collection_no = None
        self._principal_user_id = None
        self._product_code = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def extra_param(self):
        return self._extra_param

    @extra_param.setter
    def extra_param(self, value):
        self._extra_param = value
    @property
    def out_collection_no(self):
        return self._out_collection_no

    @out_collection_no.setter
    def out_collection_no(self, value):
        self._out_collection_no = value
    @property
    def principal_user_id(self):
        return self._principal_user_id

    @principal_user_id.setter
    def principal_user_id(self, value):
        self._principal_user_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.extra_param:
            if hasattr(self.extra_param, 'to_alipay_dict'):
                params['extra_param'] = self.extra_param.to_alipay_dict()
            else:
                params['extra_param'] = self.extra_param
        if self.out_collection_no:
            if hasattr(self.out_collection_no, 'to_alipay_dict'):
                params['out_collection_no'] = self.out_collection_no.to_alipay_dict()
            else:
                params['out_collection_no'] = self.out_collection_no
        if self.principal_user_id:
            if hasattr(self.principal_user_id, 'to_alipay_dict'):
                params['principal_user_id'] = self.principal_user_id.to_alipay_dict()
            else:
                params['principal_user_id'] = self.principal_user_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundBailCollectionFinishModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'extra_param' in d:
            o.extra_param = d['extra_param']
        if 'out_collection_no' in d:
            o.out_collection_no = d['out_collection_no']
        if 'principal_user_id' in d:
            o.principal_user_id = d['principal_user_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


