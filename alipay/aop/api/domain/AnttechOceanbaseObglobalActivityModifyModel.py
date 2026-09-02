#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalActivityModifyModel(object):

    def __init__(self):
        self._activity_desc = None

    @property
    def activity_desc(self):
        return self._activity_desc

    @activity_desc.setter
    def activity_desc(self, value):
        self._activity_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_desc:
            if hasattr(self.activity_desc, 'to_alipay_dict'):
                params['activity_desc'] = self.activity_desc.to_alipay_dict()
            else:
                params['activity_desc'] = self.activity_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalActivityModifyModel()
        if 'activity_desc' in d:
            o.activity_desc = d['activity_desc']
        return o


