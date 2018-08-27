#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCityfacilitatorScriptQueryModel(object):

    def __init__(self):
        self._card_type = None
        self._script_type = None

    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def script_type(self):
        return self._script_type

    @script_type.setter
    def script_type(self, value):
        self._script_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.script_type:
            if hasattr(self.script_type, 'to_alipay_dict'):
                params['script_type'] = self.script_type.to_alipay_dict()
            else:
                params['script_type'] = self.script_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCityfacilitatorScriptQueryModel()
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'script_type' in d:
            o.script_type = d['script_type']
        return o


