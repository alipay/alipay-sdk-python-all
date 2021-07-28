#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderExtInfo import OrderExtInfo


class JourneyMerchantInfo(object):

    def __init__(self):
        self._ext_info = None
        self._logo = None
        self._name = None
        self._short_name = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, OrderExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(OrderExtInfo.from_alipay_dict(i))
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def short_name(self):
        return self._short_name

    @short_name.setter
    def short_name(self, value):
        self._short_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.short_name:
            if hasattr(self.short_name, 'to_alipay_dict'):
                params['short_name'] = self.short_name.to_alipay_dict()
            else:
                params['short_name'] = self.short_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JourneyMerchantInfo()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'logo' in d:
            o.logo = d['logo']
        if 'name' in d:
            o.name = d['name']
        if 'short_name' in d:
            o.short_name = d['short_name']
        return o


