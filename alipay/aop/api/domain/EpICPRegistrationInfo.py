#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpICPRegistrationInfo(object):

    def __init__(self):
        self._domain_name = None
        self._shtgsj = None
        self._web_name = None
        self._wzbaxkzh = None
        self._zbdwmc = None

    @property
    def domain_name(self):
        return self._domain_name

    @domain_name.setter
    def domain_name(self, value):
        if isinstance(value, list):
            self._domain_name = list()
            for i in value:
                self._domain_name.append(i)
    @property
    def shtgsj(self):
        return self._shtgsj

    @shtgsj.setter
    def shtgsj(self, value):
        self._shtgsj = value
    @property
    def web_name(self):
        return self._web_name

    @web_name.setter
    def web_name(self, value):
        self._web_name = value
    @property
    def wzbaxkzh(self):
        return self._wzbaxkzh

    @wzbaxkzh.setter
    def wzbaxkzh(self, value):
        self._wzbaxkzh = value
    @property
    def zbdwmc(self):
        return self._zbdwmc

    @zbdwmc.setter
    def zbdwmc(self, value):
        self._zbdwmc = value


    def to_alipay_dict(self):
        params = dict()
        if self.domain_name:
            if isinstance(self.domain_name, list):
                for i in range(0, len(self.domain_name)):
                    element = self.domain_name[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.domain_name[i] = element.to_alipay_dict()
            if hasattr(self.domain_name, 'to_alipay_dict'):
                params['domain_name'] = self.domain_name.to_alipay_dict()
            else:
                params['domain_name'] = self.domain_name
        if self.shtgsj:
            if hasattr(self.shtgsj, 'to_alipay_dict'):
                params['shtgsj'] = self.shtgsj.to_alipay_dict()
            else:
                params['shtgsj'] = self.shtgsj
        if self.web_name:
            if hasattr(self.web_name, 'to_alipay_dict'):
                params['web_name'] = self.web_name.to_alipay_dict()
            else:
                params['web_name'] = self.web_name
        if self.wzbaxkzh:
            if hasattr(self.wzbaxkzh, 'to_alipay_dict'):
                params['wzbaxkzh'] = self.wzbaxkzh.to_alipay_dict()
            else:
                params['wzbaxkzh'] = self.wzbaxkzh
        if self.zbdwmc:
            if hasattr(self.zbdwmc, 'to_alipay_dict'):
                params['zbdwmc'] = self.zbdwmc.to_alipay_dict()
            else:
                params['zbdwmc'] = self.zbdwmc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpICPRegistrationInfo()
        if 'domain_name' in d:
            o.domain_name = d['domain_name']
        if 'shtgsj' in d:
            o.shtgsj = d['shtgsj']
        if 'web_name' in d:
            o.web_name = d['web_name']
        if 'wzbaxkzh' in d:
            o.wzbaxkzh = d['wzbaxkzh']
        if 'zbdwmc' in d:
            o.zbdwmc = d['zbdwmc']
        return o


