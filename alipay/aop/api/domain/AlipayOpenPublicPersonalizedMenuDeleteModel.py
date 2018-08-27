#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicPersonalizedMenuDeleteModel(object):

    def __init__(self):
        self._menu_key = None

    @property
    def menu_key(self):
        return self._menu_key

    @menu_key.setter
    def menu_key(self, value):
        self._menu_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.menu_key:
            if hasattr(self.menu_key, 'to_alipay_dict'):
                params['menu_key'] = self.menu_key.to_alipay_dict()
            else:
                params['menu_key'] = self.menu_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicPersonalizedMenuDeleteModel()
        if 'menu_key' in d:
            o.menu_key = d['menu_key']
        return o


