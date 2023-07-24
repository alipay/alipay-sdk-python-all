#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TuitionISVPoboBeneficiaryInfo(object):

    def __init__(self):
        self._name = None
        self._website = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def website(self):
        return self._website

    @website.setter
    def website(self, value):
        self._website = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.website:
            if hasattr(self.website, 'to_alipay_dict'):
                params['website'] = self.website.to_alipay_dict()
            else:
                params['website'] = self.website
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TuitionISVPoboBeneficiaryInfo()
        if 'name' in d:
            o.name = d['name']
        if 'website' in d:
            o.website = d['website']
        return o


