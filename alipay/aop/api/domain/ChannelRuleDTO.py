#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChannelRuleDTO(object):

    def __init__(self):
        self._marketing_types = None

    @property
    def marketing_types(self):
        return self._marketing_types

    @marketing_types.setter
    def marketing_types(self, value):
        self._marketing_types = value


    def to_alipay_dict(self):
        params = dict()
        if self.marketing_types:
            if hasattr(self.marketing_types, 'to_alipay_dict'):
                params['marketing_types'] = self.marketing_types.to_alipay_dict()
            else:
                params['marketing_types'] = self.marketing_types
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChannelRuleDTO()
        if 'marketing_types' in d:
            o.marketing_types = d['marketing_types']
        return o


