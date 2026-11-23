#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreateOrderExtInfo(object):

    def __init__(self):
        self._afu_app_id = None

    @property
    def afu_app_id(self):
        return self._afu_app_id

    @afu_app_id.setter
    def afu_app_id(self, value):
        self._afu_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.afu_app_id:
            if hasattr(self.afu_app_id, 'to_alipay_dict'):
                params['afu_app_id'] = self.afu_app_id.to_alipay_dict()
            else:
                params['afu_app_id'] = self.afu_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreateOrderExtInfo()
        if 'afu_app_id' in d:
            o.afu_app_id = d['afu_app_id']
        return o


