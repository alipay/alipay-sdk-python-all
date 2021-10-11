#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskPartnerDTO(object):

    def __init__(self):
        self._name = None
        self._ou = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def ou(self):
        return self._ou

    @ou.setter
    def ou(self, value):
        self._ou = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.ou:
            if hasattr(self.ou, 'to_alipay_dict'):
                params['ou'] = self.ou.to_alipay_dict()
            else:
                params['ou'] = self.ou
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskPartnerDTO()
        if 'name' in d:
            o.name = d['name']
        if 'ou' in d:
            o.ou = d['ou']
        return o


