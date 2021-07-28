#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TbapiQueryAmountBizContent(object):

    def __init__(self):
        self._amt_group = None
        self._amt_prods = None
        self._request_from = None
        self._scene = None

    @property
    def amt_group(self):
        return self._amt_group

    @amt_group.setter
    def amt_group(self, value):
        self._amt_group = value
    @property
    def amt_prods(self):
        return self._amt_prods

    @amt_prods.setter
    def amt_prods(self, value):
        if isinstance(value, list):
            self._amt_prods = list()
            for i in value:
                self._amt_prods.append(i)
    @property
    def request_from(self):
        return self._request_from

    @request_from.setter
    def request_from(self, value):
        self._request_from = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.amt_group:
            if hasattr(self.amt_group, 'to_alipay_dict'):
                params['amt_group'] = self.amt_group.to_alipay_dict()
            else:
                params['amt_group'] = self.amt_group
        if self.amt_prods:
            if isinstance(self.amt_prods, list):
                for i in range(0, len(self.amt_prods)):
                    element = self.amt_prods[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.amt_prods[i] = element.to_alipay_dict()
            if hasattr(self.amt_prods, 'to_alipay_dict'):
                params['amt_prods'] = self.amt_prods.to_alipay_dict()
            else:
                params['amt_prods'] = self.amt_prods
        if self.request_from:
            if hasattr(self.request_from, 'to_alipay_dict'):
                params['request_from'] = self.request_from.to_alipay_dict()
            else:
                params['request_from'] = self.request_from
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TbapiQueryAmountBizContent()
        if 'amt_group' in d:
            o.amt_group = d['amt_group']
        if 'amt_prods' in d:
            o.amt_prods = d['amt_prods']
        if 'request_from' in d:
            o.request_from = d['request_from']
        if 'scene' in d:
            o.scene = d['scene']
        return o


