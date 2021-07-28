#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniQrcodeUnbindModel(object):

    def __init__(self):
        self._route_group = None

    @property
    def route_group(self):
        return self._route_group

    @route_group.setter
    def route_group(self, value):
        self._route_group = value


    def to_alipay_dict(self):
        params = dict()
        if self.route_group:
            if hasattr(self.route_group, 'to_alipay_dict'):
                params['route_group'] = self.route_group.to_alipay_dict()
            else:
                params['route_group'] = self.route_group
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniQrcodeUnbindModel()
        if 'route_group' in d:
            o.route_group = d['route_group']
        return o


