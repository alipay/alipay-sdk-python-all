#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpRatingInnerInitializeModel(object):

    def __init__(self):
        self._credit_category = None
        self._ep_cert_no = None
        self._ep_name = None
        self._m_category = None
        self._member_type = None
        self._out_order_no = None
        self._user_id = None

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
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
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
        o = ZhimaCreditEpRatingInnerInitializeModel()
        if 'credit_category' in d:
            o.credit_category = d['credit_category']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'm_category' in d:
            o.m_category = d['m_category']
        if 'member_type' in d:
            o.member_type = d['member_type']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


