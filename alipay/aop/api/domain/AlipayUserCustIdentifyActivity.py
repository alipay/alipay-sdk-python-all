#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCustIdentifyActivity(object):

    def __init__(self):
        self._activity_info = None
        self._activity_name = None

    @property
    def activity_info(self):
        return self._activity_info

    @activity_info.setter
    def activity_info(self, value):
        self._activity_info = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_info:
            if hasattr(self.activity_info, 'to_alipay_dict'):
                params['activity_info'] = self.activity_info.to_alipay_dict()
            else:
                params['activity_info'] = self.activity_info
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
        o = AlipayUserCustIdentifyActivity()
        if 'activity_info' in d:
            o.activity_info = d['activity_info']
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        return o


