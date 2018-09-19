#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantBaseEnterOpenModel(object):

    def __init__(self):
        self._logo_info = None
        self._m_name = None
        self._m_short_name = None

    @property
    def logo_info(self):
        return self._logo_info

    @logo_info.setter
    def logo_info(self, value):
        self._logo_info = value
    @property
    def m_name(self):
        return self._m_name

    @m_name.setter
    def m_name(self, value):
        self._m_name = value
    @property
    def m_short_name(self):
        return self._m_short_name

    @m_short_name.setter
    def m_short_name(self, value):
        self._m_short_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.logo_info:
            if hasattr(self.logo_info, 'to_alipay_dict'):
                params['logo_info'] = self.logo_info.to_alipay_dict()
            else:
                params['logo_info'] = self.logo_info
        if self.m_name:
            if hasattr(self.m_name, 'to_alipay_dict'):
                params['m_name'] = self.m_name.to_alipay_dict()
            else:
                params['m_name'] = self.m_name
        if self.m_short_name:
            if hasattr(self.m_short_name, 'to_alipay_dict'):
                params['m_short_name'] = self.m_short_name.to_alipay_dict()
            else:
                params['m_short_name'] = self.m_short_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantBaseEnterOpenModel()
        if 'logo_info' in d:
            o.logo_info = d['logo_info']
        if 'm_name' in d:
            o.m_name = d['m_name']
        if 'm_short_name' in d:
            o.m_short_name = d['m_short_name']
        return o


