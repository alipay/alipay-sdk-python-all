#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoActivityAttrOptionVO import PromoActivityAttrOptionVO


class PromoActivityAttrVO(object):

    def __init__(self):
        self._attr_key = None
        self._multi = None
        self._name = None
        self._options = None
        self._required = None

    @property
    def attr_key(self):
        return self._attr_key

    @attr_key.setter
    def attr_key(self, value):
        self._attr_key = value
    @property
    def multi(self):
        return self._multi

    @multi.setter
    def multi(self, value):
        self._multi = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        if isinstance(value, list):
            self._options = list()
            for i in value:
                if isinstance(i, PromoActivityAttrOptionVO):
                    self._options.append(i)
                else:
                    self._options.append(PromoActivityAttrOptionVO.from_alipay_dict(i))
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value


    def to_alipay_dict(self):
        params = dict()
        if self.attr_key:
            if hasattr(self.attr_key, 'to_alipay_dict'):
                params['attr_key'] = self.attr_key.to_alipay_dict()
            else:
                params['attr_key'] = self.attr_key
        if self.multi:
            if hasattr(self.multi, 'to_alipay_dict'):
                params['multi'] = self.multi.to_alipay_dict()
            else:
                params['multi'] = self.multi
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.options:
            if isinstance(self.options, list):
                for i in range(0, len(self.options)):
                    element = self.options[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.options[i] = element.to_alipay_dict()
            if hasattr(self.options, 'to_alipay_dict'):
                params['options'] = self.options.to_alipay_dict()
            else:
                params['options'] = self.options
        if self.required:
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoActivityAttrVO()
        if 'attr_key' in d:
            o.attr_key = d['attr_key']
        if 'multi' in d:
            o.multi = d['multi']
        if 'name' in d:
            o.name = d['name']
        if 'options' in d:
            o.options = d['options']
        if 'required' in d:
            o.required = d['required']
        return o


