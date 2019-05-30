#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniAppClientVersionInfo(object):

    def __init__(self):
        self._max_client_version = None
        self._min_client_version = None

    @property
    def max_client_version(self):
        return self._max_client_version

    @max_client_version.setter
    def max_client_version(self, value):
        self._max_client_version = value
    @property
    def min_client_version(self):
        return self._min_client_version

    @min_client_version.setter
    def min_client_version(self, value):
        self._min_client_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_client_version:
            if hasattr(self.max_client_version, 'to_alipay_dict'):
                params['max_client_version'] = self.max_client_version.to_alipay_dict()
            else:
                params['max_client_version'] = self.max_client_version
        if self.min_client_version:
            if hasattr(self.min_client_version, 'to_alipay_dict'):
                params['min_client_version'] = self.min_client_version.to_alipay_dict()
            else:
                params['min_client_version'] = self.min_client_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppClientVersionInfo()
        if 'max_client_version' in d:
            o.max_client_version = d['max_client_version']
        if 'min_client_version' in d:
            o.min_client_version = d['min_client_version']
        return o


