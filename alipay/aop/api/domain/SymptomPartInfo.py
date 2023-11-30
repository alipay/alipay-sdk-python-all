#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SymptomSubPart import SymptomSubPart


class SymptomPartInfo(object):

    def __init__(self):
        self._logo = None
        self._name = None
        self._order = None
        self._sub_parts = None
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
    def sub_parts(self):
        return self._sub_parts

    @sub_parts.setter
    def sub_parts(self, value):
        if isinstance(value, list):
            self._sub_parts = list()
            for i in value:
                if isinstance(i, SymptomSubPart):
                    self._sub_parts.append(i)
                else:
                    self._sub_parts.append(SymptomSubPart.from_alipay_dict(i))
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
        if self.sub_parts:
            if isinstance(self.sub_parts, list):
                for i in range(0, len(self.sub_parts)):
                    element = self.sub_parts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_parts[i] = element.to_alipay_dict()
            if hasattr(self.sub_parts, 'to_alipay_dict'):
                params['sub_parts'] = self.sub_parts.to_alipay_dict()
            else:
                params['sub_parts'] = self.sub_parts
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
        o = SymptomPartInfo()
        if 'logo' in d:
            o.logo = d['logo']
        if 'name' in d:
            o.name = d['name']
        if 'order' in d:
            o.order = d['order']
        if 'sub_parts' in d:
            o.sub_parts = d['sub_parts']
        if 'symptoms' in d:
            o.symptoms = d['symptoms']
        return o


