#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FollowupExecutionResultParams(object):

    def __init__(self):
        self._params_data = None

    @property
    def params_data(self):
        return self._params_data

    @params_data.setter
    def params_data(self, value):
        self._params_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.params_data:
            if hasattr(self.params_data, 'to_alipay_dict'):
                params['params_data'] = self.params_data.to_alipay_dict()
            else:
                params['params_data'] = self.params_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FollowupExecutionResultParams()
        if 'params_data' in d:
            o.params_data = d['params_data']
        return o


