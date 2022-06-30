#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskGoodConfig(object):

    def __init__(self):
        self._good_id = None
        self._good_name = None

    @property
    def good_id(self):
        return self._good_id

    @good_id.setter
    def good_id(self, value):
        self._good_id = value
    @property
    def good_name(self):
        return self._good_name

    @good_name.setter
    def good_name(self, value):
        self._good_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.good_id:
            if hasattr(self.good_id, 'to_alipay_dict'):
                params['good_id'] = self.good_id.to_alipay_dict()
            else:
                params['good_id'] = self.good_id
        if self.good_name:
            if hasattr(self.good_name, 'to_alipay_dict'):
                params['good_name'] = self.good_name.to_alipay_dict()
            else:
                params['good_name'] = self.good_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskGoodConfig()
        if 'good_id' in d:
            o.good_id = d['good_id']
        if 'good_name' in d:
            o.good_name = d['good_name']
        return o


