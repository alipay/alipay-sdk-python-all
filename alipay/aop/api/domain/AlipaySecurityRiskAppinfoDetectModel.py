#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskAppinfoDetectModel(object):

    def __init__(self):
        self._app_info_list = None
        self._extend_params = None
        self._source = None

    @property
    def app_info_list(self):
        return self._app_info_list

    @app_info_list.setter
    def app_info_list(self, value):
        self._app_info_list = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_info_list:
            if hasattr(self.app_info_list, 'to_alipay_dict'):
                params['app_info_list'] = self.app_info_list.to_alipay_dict()
            else:
                params['app_info_list'] = self.app_info_list
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskAppinfoDetectModel()
        if 'app_info_list' in d:
            o.app_info_list = d['app_info_list']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'source' in d:
            o.source = d['source']
        return o


