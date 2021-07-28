#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniMiniappServiceconfigModifyModel(object):

    def __init__(self):
        self._home_open = None
        self._service_config = None

    @property
    def home_open(self):
        return self._home_open

    @home_open.setter
    def home_open(self, value):
        self._home_open = value
    @property
    def service_config(self):
        return self._service_config

    @service_config.setter
    def service_config(self, value):
        self._service_config = value


    def to_alipay_dict(self):
        params = dict()
        if self.home_open:
            if hasattr(self.home_open, 'to_alipay_dict'):
                params['home_open'] = self.home_open.to_alipay_dict()
            else:
                params['home_open'] = self.home_open
        if self.service_config:
            if hasattr(self.service_config, 'to_alipay_dict'):
                params['service_config'] = self.service_config.to_alipay_dict()
            else:
                params['service_config'] = self.service_config
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniMiniappServiceconfigModifyModel()
        if 'home_open' in d:
            o.home_open = d['home_open']
        if 'service_config' in d:
            o.service_config = d['service_config']
        return o


