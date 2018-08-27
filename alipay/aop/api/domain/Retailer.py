#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Retailer(object):

    def __init__(self):
        self._name = None
        self._partner_id = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Retailer()
        if 'name' in d:
            o.name = d['name']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        return o


