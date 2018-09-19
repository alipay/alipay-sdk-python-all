#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardTypeVO(object):

    def __init__(self):
        self._card_type = None
        self._description = None

    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardTypeVO()
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'description' in d:
            o.description = d['description']
        return o


