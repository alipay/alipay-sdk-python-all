#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniResourceDeleteModel(object):

    def __init__(self):
        self._resource_id = None

    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.resource_id:
            if hasattr(self.resource_id, 'to_alipay_dict'):
                params['resource_id'] = self.resource_id.to_alipay_dict()
            else:
                params['resource_id'] = self.resource_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniResourceDeleteModel()
        if 'resource_id' in d:
            o.resource_id = d['resource_id']
        return o


