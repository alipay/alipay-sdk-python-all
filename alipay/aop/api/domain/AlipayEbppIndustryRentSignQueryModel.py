#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryRentSignQueryModel(object):

    def __init__(self):
        self._cert_num = None
        self._cert_type = None
        self._draw_item = None
        self._enterprise_credit_no = None
        self._enterprise_name = None
        self._enterprise_proof = None
        self._is_available = None
        self._online_state = None
        self._org_code = None
        self._user_name = None

    @property
    def cert_num(self):
        return self._cert_num

    @cert_num.setter
    def cert_num(self, value):
        self._cert_num = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def draw_item(self):
        return self._draw_item

    @draw_item.setter
    def draw_item(self, value):
        self._draw_item = value
    @property
    def enterprise_credit_no(self):
        return self._enterprise_credit_no

    @enterprise_credit_no.setter
    def enterprise_credit_no(self, value):
        self._enterprise_credit_no = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def enterprise_proof(self):
        return self._enterprise_proof

    @enterprise_proof.setter
    def enterprise_proof(self, value):
        self._enterprise_proof = value
    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, value):
        self._is_available = value
    @property
    def online_state(self):
        return self._online_state

    @online_state.setter
    def online_state(self, value):
        self._online_state = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_num:
            if hasattr(self.cert_num, 'to_alipay_dict'):
                params['cert_num'] = self.cert_num.to_alipay_dict()
            else:
                params['cert_num'] = self.cert_num
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.draw_item:
            if hasattr(self.draw_item, 'to_alipay_dict'):
                params['draw_item'] = self.draw_item.to_alipay_dict()
            else:
                params['draw_item'] = self.draw_item
        if self.enterprise_credit_no:
            if hasattr(self.enterprise_credit_no, 'to_alipay_dict'):
                params['enterprise_credit_no'] = self.enterprise_credit_no.to_alipay_dict()
            else:
                params['enterprise_credit_no'] = self.enterprise_credit_no
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = self.enterprise_name.to_alipay_dict()
            else:
                params['enterprise_name'] = self.enterprise_name
        if self.enterprise_proof:
            if hasattr(self.enterprise_proof, 'to_alipay_dict'):
                params['enterprise_proof'] = self.enterprise_proof.to_alipay_dict()
            else:
                params['enterprise_proof'] = self.enterprise_proof
        if self.is_available:
            if hasattr(self.is_available, 'to_alipay_dict'):
                params['is_available'] = self.is_available.to_alipay_dict()
            else:
                params['is_available'] = self.is_available
        if self.online_state:
            if hasattr(self.online_state, 'to_alipay_dict'):
                params['online_state'] = self.online_state.to_alipay_dict()
            else:
                params['online_state'] = self.online_state
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryRentSignQueryModel()
        if 'cert_num' in d:
            o.cert_num = d['cert_num']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'draw_item' in d:
            o.draw_item = d['draw_item']
        if 'enterprise_credit_no' in d:
            o.enterprise_credit_no = d['enterprise_credit_no']
        if 'enterprise_name' in d:
            o.enterprise_name = d['enterprise_name']
        if 'enterprise_proof' in d:
            o.enterprise_proof = d['enterprise_proof']
        if 'is_available' in d:
            o.is_available = d['is_available']
        if 'online_state' in d:
            o.online_state = d['online_state']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


