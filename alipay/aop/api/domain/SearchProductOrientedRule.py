#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchProductOrientedRule(object):

    def __init__(self):
        self._client_platform = None
        self._end_version = None
        self._start_version = None

    @property
    def client_platform(self):
        return self._client_platform

    @client_platform.setter
    def client_platform(self, value):
        self._client_platform = value
    @property
    def end_version(self):
        return self._end_version

    @end_version.setter
    def end_version(self, value):
        self._end_version = value
    @property
    def start_version(self):
        return self._start_version

    @start_version.setter
    def start_version(self, value):
        self._start_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_platform:
            if hasattr(self.client_platform, 'to_alipay_dict'):
                params['client_platform'] = self.client_platform.to_alipay_dict()
            else:
                params['client_platform'] = self.client_platform
        if self.end_version:
            if hasattr(self.end_version, 'to_alipay_dict'):
                params['end_version'] = self.end_version.to_alipay_dict()
            else:
                params['end_version'] = self.end_version
        if self.start_version:
            if hasattr(self.start_version, 'to_alipay_dict'):
                params['start_version'] = self.start_version.to_alipay_dict()
            else:
                params['start_version'] = self.start_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchProductOrientedRule()
        if 'client_platform' in d:
            o.client_platform = d['client_platform']
        if 'end_version' in d:
            o.end_version = d['end_version']
        if 'start_version' in d:
            o.start_version = d['start_version']
        return o


