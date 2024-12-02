#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardBrandInfo(object):

    def __init__(self):
        self._brand_id = None
        self._firstletter = None
        self._logo = None
        self._name = None

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def firstletter(self):
        return self._firstletter

    @firstletter.setter
    def firstletter(self, value):
        self._firstletter = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.firstletter:
            if hasattr(self.firstletter, 'to_alipay_dict'):
                params['firstletter'] = self.firstletter.to_alipay_dict()
            else:
                params['firstletter'] = self.firstletter
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardBrandInfo()
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'firstletter' in d:
            o.firstletter = d['firstletter']
        if 'logo' in d:
            o.logo = d['logo']
        if 'name' in d:
            o.name = d['name']
        return o


