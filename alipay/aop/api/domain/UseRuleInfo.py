#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UseRuleInfo(object):

    def __init__(self):
        self._suitable_shops = None
        self._use_mode = None

    @property
    def suitable_shops(self):
        return self._suitable_shops

    @suitable_shops.setter
    def suitable_shops(self, value):
        if isinstance(value, list):
            self._suitable_shops = list()
            for i in value:
                self._suitable_shops.append(i)
    @property
    def use_mode(self):
        return self._use_mode

    @use_mode.setter
    def use_mode(self, value):
        if isinstance(value, list):
            self._use_mode = list()
            for i in value:
                self._use_mode.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.suitable_shops:
            if isinstance(self.suitable_shops, list):
                for i in range(0, len(self.suitable_shops)):
                    element = self.suitable_shops[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.suitable_shops[i] = element.to_alipay_dict()
            if hasattr(self.suitable_shops, 'to_alipay_dict'):
                params['suitable_shops'] = self.suitable_shops.to_alipay_dict()
            else:
                params['suitable_shops'] = self.suitable_shops
        if self.use_mode:
            if isinstance(self.use_mode, list):
                for i in range(0, len(self.use_mode)):
                    element = self.use_mode[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.use_mode[i] = element.to_alipay_dict()
            if hasattr(self.use_mode, 'to_alipay_dict'):
                params['use_mode'] = self.use_mode.to_alipay_dict()
            else:
                params['use_mode'] = self.use_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UseRuleInfo()
        if 'suitable_shops' in d:
            o.suitable_shops = d['suitable_shops']
        if 'use_mode' in d:
            o.use_mode = d['use_mode']
        return o


