#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QianfanCardComponent import QianfanCardComponent


class QianfanCardItem(object):

    def __init__(self):
        self._card_name = None
        self._card_type = None
        self._card_version = None
        self._components = None
        self._intent = None

    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def card_version(self):
        return self._card_version

    @card_version.setter
    def card_version(self, value):
        self._card_version = value
    @property
    def components(self):
        return self._components

    @components.setter
    def components(self, value):
        if isinstance(value, list):
            self._components = list()
            for i in value:
                if isinstance(i, QianfanCardComponent):
                    self._components.append(i)
                else:
                    self._components.append(QianfanCardComponent.from_alipay_dict(i))
    @property
    def intent(self):
        return self._intent

    @intent.setter
    def intent(self, value):
        self._intent = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_name:
            if hasattr(self.card_name, 'to_alipay_dict'):
                params['card_name'] = self.card_name.to_alipay_dict()
            else:
                params['card_name'] = self.card_name
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.card_version:
            if hasattr(self.card_version, 'to_alipay_dict'):
                params['card_version'] = self.card_version.to_alipay_dict()
            else:
                params['card_version'] = self.card_version
        if self.components:
            if isinstance(self.components, list):
                for i in range(0, len(self.components)):
                    element = self.components[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.components[i] = element.to_alipay_dict()
            if hasattr(self.components, 'to_alipay_dict'):
                params['components'] = self.components.to_alipay_dict()
            else:
                params['components'] = self.components
        if self.intent:
            if hasattr(self.intent, 'to_alipay_dict'):
                params['intent'] = self.intent.to_alipay_dict()
            else:
                params['intent'] = self.intent
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QianfanCardItem()
        if 'card_name' in d:
            o.card_name = d['card_name']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'card_version' in d:
            o.card_version = d['card_version']
        if 'components' in d:
            o.components = d['components']
        if 'intent' in d:
            o.intent = d['intent']
        return o


