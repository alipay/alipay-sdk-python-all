#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubMerchantEnterOpenModel(object):

    def __init__(self):
        self._extend_fields = None
        self._industry = None
        self._pid = None
        self._register_no = None
        self._sub_m_name = None
        self._sub_m_short_name = None

    @property
    def extend_fields(self):
        return self._extend_fields

    @extend_fields.setter
    def extend_fields(self, value):
        self._extend_fields = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
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
        if self.extend_fields:
            if hasattr(self.extend_fields, 'to_alipay_dict'):
                params['extend_fields'] = self.extend_fields.to_alipay_dict()
            else:
                params['extend_fields'] = self.extend_fields
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
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
        if 'extend_fields' in d:
            o.extend_fields = d['extend_fields']
        if 'industry' in d:
            o.industry = d['industry']
        if 'pid' in d:
            o.pid = d['pid']
        if 'register_no' in d:
            o.register_no = d['register_no']
        if 'sub_m_name' in d:
            o.sub_m_name = d['sub_m_name']
        if 'sub_m_short_name' in d:
            o.sub_m_short_name = d['sub_m_short_name']
        return o


