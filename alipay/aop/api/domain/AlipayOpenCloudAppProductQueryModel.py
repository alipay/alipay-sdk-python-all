#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenCloudAppProductQueryModel(object):

    def __init__(self):
        self._invoke_app_id = None

    @property
    def invoke_app_id(self):
        return self._invoke_app_id

    @invoke_app_id.setter
    def invoke_app_id(self, value):
        self._invoke_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.invoke_app_id:
            if hasattr(self.invoke_app_id, 'to_alipay_dict'):
                params['invoke_app_id'] = self.invoke_app_id.to_alipay_dict()
            else:
                params['invoke_app_id'] = self.invoke_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenCloudAppProductQueryModel()
        if 'invoke_app_id' in d:
            o.invoke_app_id = d['invoke_app_id']
        return o


