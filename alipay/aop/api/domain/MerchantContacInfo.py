#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContactWayItem import ContactWayItem


class MerchantContacInfo(object):

    def __init__(self):
        self._contact_ways = None
        self._name = None
        self._type = None

    @property
    def contact_ways(self):
        return self._contact_ways

    @contact_ways.setter
    def contact_ways(self, value):
        if isinstance(value, list):
            self._contact_ways = list()
            for i in value:
                if isinstance(i, ContactWayItem):
                    self._contact_ways.append(i)
                else:
                    self._contact_ways.append(ContactWayItem.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_ways:
            if isinstance(self.contact_ways, list):
                for i in range(0, len(self.contact_ways)):
                    element = self.contact_ways[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contact_ways[i] = element.to_alipay_dict()
            if hasattr(self.contact_ways, 'to_alipay_dict'):
                params['contact_ways'] = self.contact_ways.to_alipay_dict()
            else:
                params['contact_ways'] = self.contact_ways
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantContacInfo()
        if 'contact_ways' in d:
            o.contact_ways = d['contact_ways']
        if 'name' in d:
            o.name = d['name']
        if 'type' in d:
            o.type = d['type']
        return o


