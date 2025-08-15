#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TasteMethod(object):

    def __init__(self):
        self._taste_id = None
        self._taste_name = None

    @property
    def taste_id(self):
        return self._taste_id

    @taste_id.setter
    def taste_id(self, value):
        self._taste_id = value
    @property
    def taste_name(self):
        return self._taste_name

    @taste_name.setter
    def taste_name(self, value):
        self._taste_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.taste_id:
            if hasattr(self.taste_id, 'to_alipay_dict'):
                params['taste_id'] = self.taste_id.to_alipay_dict()
            else:
                params['taste_id'] = self.taste_id
        if self.taste_name:
            if hasattr(self.taste_name, 'to_alipay_dict'):
                params['taste_name'] = self.taste_name.to_alipay_dict()
            else:
                params['taste_name'] = self.taste_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TasteMethod()
        if 'taste_id' in d:
            o.taste_id = d['taste_id']
        if 'taste_name' in d:
            o.taste_name = d['taste_name']
        return o


