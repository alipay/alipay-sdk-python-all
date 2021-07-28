#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardInstanceDO(object):

    def __init__(self):
        self._card_id = None
        self._level = None
        self._max_level = None
        self._name = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def max_level(self):
        return self._max_level

    @max_level.setter
    def max_level(self, value):
        self._max_level = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.max_level:
            if hasattr(self.max_level, 'to_alipay_dict'):
                params['max_level'] = self.max_level.to_alipay_dict()
            else:
                params['max_level'] = self.max_level
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
        o = CardInstanceDO()
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'level' in d:
            o.level = d['level']
        if 'max_level' in d:
            o.max_level = d['max_level']
        if 'name' in d:
            o.name = d['name']
        return o


