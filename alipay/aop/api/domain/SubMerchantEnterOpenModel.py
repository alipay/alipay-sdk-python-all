#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubMerchantEnterOpenModel(object):

    def __init__(self):
        self._register_no = None
        self._sub_m_name = None
        self._sub_m_short_name = None

    @property
    def register_no(self):
        return self._register_no

    @register_no.setter
    def register_no(self, value):
        self._register_no = value
    @property
    def sub_m_name(self):
        return self._sub_m_name

    @sub_m_name.setter
    def sub_m_name(self, value):
        self._sub_m_name = value
    @property
    def sub_m_short_name(self):
        return self._sub_m_short_name

    @sub_m_short_name.setter
    def sub_m_short_name(self, value):
        self._sub_m_short_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.register_no:
            if hasattr(self.register_no, 'to_alipay_dict'):
                params['register_no'] = self.register_no.to_alipay_dict()
            else:
                params['register_no'] = self.register_no
        if self.sub_m_name:
            if hasattr(self.sub_m_name, 'to_alipay_dict'):
                params['sub_m_name'] = self.sub_m_name.to_alipay_dict()
            else:
                params['sub_m_name'] = self.sub_m_name
        if self.sub_m_short_name:
            if hasattr(self.sub_m_short_name, 'to_alipay_dict'):
                params['sub_m_short_name'] = self.sub_m_short_name.to_alipay_dict()
            else:
                params['sub_m_short_name'] = self.sub_m_short_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubMerchantEnterOpenModel()
        if 'register_no' in d:
            o.register_no = d['register_no']
        if 'sub_m_name' in d:
            o.sub_m_name = d['sub_m_name']
        if 'sub_m_short_name' in d:
            o.sub_m_short_name = d['sub_m_short_name']
        return o


