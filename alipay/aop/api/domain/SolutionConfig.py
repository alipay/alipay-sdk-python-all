#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SolutionConfig(object):

    def __init__(self):
        self._allow_transfer_param = None

    @property
    def allow_transfer_param(self):
        return self._allow_transfer_param

    @allow_transfer_param.setter
    def allow_transfer_param(self, value):
        self._allow_transfer_param = value


    def to_alipay_dict(self):
        params = dict()
        if self.allow_transfer_param:
            if hasattr(self.allow_transfer_param, 'to_alipay_dict'):
                params['allow_transfer_param'] = self.allow_transfer_param.to_alipay_dict()
            else:
                params['allow_transfer_param'] = self.allow_transfer_param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SolutionConfig()
        if 'allow_transfer_param' in d:
            o.allow_transfer_param = d['allow_transfer_param']
        return o


