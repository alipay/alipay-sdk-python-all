#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiRetailTopinstanceQueryModel(object):

    def __init__(self):
        self._instance_type = None

    @property
    def instance_type(self):
        return self._instance_type

    @instance_type.setter
    def instance_type(self, value):
        self._instance_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.instance_type:
            if hasattr(self.instance_type, 'to_alipay_dict'):
                params['instance_type'] = self.instance_type.to_alipay_dict()
            else:
                params['instance_type'] = self.instance_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailTopinstanceQueryModel()
        if 'instance_type' in d:
            o.instance_type = d['instance_type']
        return o


