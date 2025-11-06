#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HDFConditiondesc(object):

    def __init__(self):
        self._condition_desc = None

    @property
    def condition_desc(self):
        return self._condition_desc

    @condition_desc.setter
    def condition_desc(self, value):
        self._condition_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.condition_desc:
            if hasattr(self.condition_desc, 'to_alipay_dict'):
                params['condition_desc'] = self.condition_desc.to_alipay_dict()
            else:
                params['condition_desc'] = self.condition_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HDFConditiondesc()
        if 'condition_desc' in d:
            o.condition_desc = d['condition_desc']
        return o


