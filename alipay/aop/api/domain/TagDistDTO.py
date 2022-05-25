#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TagDistDTO(object):

    def __init__(self):
        self._date_format = None
        self._display_name = None
        self._max = None
        self._mix = None
        self._value = None

    @property
    def date_format(self):
        return self._date_format

    @date_format.setter
    def date_format(self, value):
        self._date_format = value
    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, value):
        self._max = value
    @property
    def mix(self):
        return self._mix

    @mix.setter
    def mix(self, value):
        self._mix = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.date_format:
            if hasattr(self.date_format, 'to_alipay_dict'):
                params['date_format'] = self.date_format.to_alipay_dict()
            else:
                params['date_format'] = self.date_format
        if self.display_name:
            if hasattr(self.display_name, 'to_alipay_dict'):
                params['display_name'] = self.display_name.to_alipay_dict()
            else:
                params['display_name'] = self.display_name
        if self.max:
            if hasattr(self.max, 'to_alipay_dict'):
                params['max'] = self.max.to_alipay_dict()
            else:
                params['max'] = self.max
        if self.mix:
            if hasattr(self.mix, 'to_alipay_dict'):
                params['mix'] = self.mix.to_alipay_dict()
            else:
                params['mix'] = self.mix
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TagDistDTO()
        if 'date_format' in d:
            o.date_format = d['date_format']
        if 'display_name' in d:
            o.display_name = d['display_name']
        if 'max' in d:
            o.max = d['max']
        if 'mix' in d:
            o.mix = d['mix']
        if 'value' in d:
            o.value = d['value']
        return o


