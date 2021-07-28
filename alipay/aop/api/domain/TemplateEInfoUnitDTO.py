#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TemplateEInfoMoreDTO import TemplateEInfoMoreDTO


class TemplateEInfoUnitDTO(object):

    def __init__(self):
        self._icon = None
        self._key = None
        self._label = None
        self._more = None
        self._type = None
        self._value = None

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value
    @property
    def more(self):
        return self._more

    @more.setter
    def more(self, value):
        if isinstance(value, TemplateEInfoMoreDTO):
            self._more = value
        else:
            self._more = TemplateEInfoMoreDTO.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.label:
            if hasattr(self.label, 'to_alipay_dict'):
                params['label'] = self.label.to_alipay_dict()
            else:
                params['label'] = self.label
        if self.more:
            if hasattr(self.more, 'to_alipay_dict'):
                params['more'] = self.more.to_alipay_dict()
            else:
                params['more'] = self.more
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
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
        o = TemplateEInfoUnitDTO()
        if 'icon' in d:
            o.icon = d['icon']
        if 'key' in d:
            o.key = d['key']
        if 'label' in d:
            o.label = d['label']
        if 'more' in d:
            o.more = d['more']
        if 'type' in d:
            o.type = d['type']
        if 'value' in d:
            o.value = d['value']
        return o


