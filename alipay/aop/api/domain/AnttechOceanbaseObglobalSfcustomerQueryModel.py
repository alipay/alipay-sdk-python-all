#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalSfcustomerQueryModel(object):

    def __init__(self):
        self._country = None
        self._ep_full_name = None
        self._ep_name = None

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value
    @property
    def ep_full_name(self):
        return self._ep_full_name

    @ep_full_name.setter
    def ep_full_name(self, value):
        self._ep_full_name = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.country:
            if hasattr(self.country, 'to_alipay_dict'):
                params['country'] = self.country.to_alipay_dict()
            else:
                params['country'] = self.country
        if self.ep_full_name:
            if hasattr(self.ep_full_name, 'to_alipay_dict'):
                params['ep_full_name'] = self.ep_full_name.to_alipay_dict()
            else:
                params['ep_full_name'] = self.ep_full_name
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalSfcustomerQueryModel()
        if 'country' in d:
            o.country = d['country']
        if 'ep_full_name' in d:
            o.ep_full_name = d['ep_full_name']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        return o


