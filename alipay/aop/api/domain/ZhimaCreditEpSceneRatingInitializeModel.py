#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpSceneRatingInitializeModel(object):

    def __init__(self):
        self._apply_amount = None
        self._biz_ext_param = None
        self._credit_category = None
        self._ep_cert_no = None
        self._ep_name = None
        self._evaluate_type = None
        self._m_category = None
        self._member_type = None
        self._out_order_no = None
        self._product_code = None
        self._user_id = None

    @property
    def apply_amount(self):
        return self._apply_amount

    @apply_amount.setter
    def apply_amount(self, value):
        self._apply_amount = value
    @property
    def biz_ext_param(self):
        return self._biz_ext_param

    @biz_ext_param.setter
    def biz_ext_param(self, value):
        self._biz_ext_param = value
    @property
    def credit_category(self):
        return self._credit_category

    @credit_category.setter
    def credit_category(self, value):
        self._credit_category = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def evaluate_type(self):
        return self._evaluate_type

    @evaluate_type.setter
    def evaluate_type(self, value):
        self._evaluate_type = value
    @property
    def m_category(self):
        return self._m_category

    @m_category.setter
    def m_category(self, value):
        self._m_category = value
    @property
    def member_type(self):
        return self._member_type

    @member_type.setter
    def member_type(self, value):
        self._member_type = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_amount:
            if hasattr(self.apply_amount, 'to_alipay_dict'):
                params['apply_amount'] = self.apply_amount.to_alipay_dict()
            else:
                params['apply_amount'] = self.apply_amount
        if self.biz_ext_param:
            if hasattr(self.biz_ext_param, 'to_alipay_dict'):
                params['biz_ext_param'] = self.biz_ext_param.to_alipay_dict()
            else:
                params['biz_ext_param'] = self.biz_ext_param
        if self.credit_category:
            if hasattr(self.credit_category, 'to_alipay_dict'):
                params['credit_category'] = self.credit_category.to_alipay_dict()
            else:
                params['credit_category'] = self.credit_category
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.evaluate_type:
            if hasattr(self.evaluate_type, 'to_alipay_dict'):
                params['evaluate_type'] = self.evaluate_type.to_alipay_dict()
            else:
                params['evaluate_type'] = self.evaluate_type
        if self.m_category:
            if hasattr(self.m_category, 'to_alipay_dict'):
                params['m_category'] = self.m_category.to_alipay_dict()
            else:
                params['m_category'] = self.m_category
        if self.member_type:
            if hasattr(self.member_type, 'to_alipay_dict'):
                params['member_type'] = self.member_type.to_alipay_dict()
            else:
                params['member_type'] = self.member_type
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpSceneRatingInitializeModel()
        if 'apply_amount' in d:
            o.apply_amount = d['apply_amount']
        if 'biz_ext_param' in d:
            o.biz_ext_param = d['biz_ext_param']
        if 'credit_category' in d:
            o.credit_category = d['credit_category']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'evaluate_type' in d:
            o.evaluate_type = d['evaluate_type']
        if 'm_category' in d:
            o.m_category = d['m_category']
        if 'member_type' in d:
            o.member_type = d['member_type']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


