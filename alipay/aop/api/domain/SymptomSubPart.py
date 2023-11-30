#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SymptomSubPart(object):

    def __init__(self):
        self._logo = None
        self._name = None
        self._order = None
        self._symptoms = None

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
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value
    @property
    def symptoms(self):
        return self._symptoms

    @symptoms.setter
    def symptoms(self, value):
        if isinstance(value, list):
            self._symptoms = list()
            for i in value:
                self._symptoms.append(i)


    def to_alipay_dict(self):
        params = dict()
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
        if self.order:
            if hasattr(self.order, 'to_alipay_dict'):
                params['order'] = self.order.to_alipay_dict()
            else:
                params['order'] = self.order
        if self.symptoms:
            if isinstance(self.symptoms, list):
                for i in range(0, len(self.symptoms)):
                    element = self.symptoms[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.symptoms[i] = element.to_alipay_dict()
            if hasattr(self.symptoms, 'to_alipay_dict'):
                params['symptoms'] = self.symptoms.to_alipay_dict()
            else:
                params['symptoms'] = self.symptoms
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SymptomSubPart()
        if 'logo' in d:
            o.logo = d['logo']
        if 'name' in d:
            o.name = d['name']
        if 'order' in d:
            o.order = d['order']
        if 'symptoms' in d:
            o.symptoms = d['symptoms']
        return o


