#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppItemActivityBaseInfo(object):

    def __init__(self):
        self._activity_name = None

    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppItemActivityBaseInfo()
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        return o


