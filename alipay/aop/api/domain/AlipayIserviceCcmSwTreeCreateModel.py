#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmSwTreeCreateModel(object):

    def __init__(self):
        self._ccs_instance_id = None
        self._name = None

    @property
    def ccs_instance_id(self):
        return self._ccs_instance_id

    @ccs_instance_id.setter
    def ccs_instance_id(self, value):
        self._ccs_instance_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ccs_instance_id:
            if hasattr(self.ccs_instance_id, 'to_alipay_dict'):
                params['ccs_instance_id'] = self.ccs_instance_id.to_alipay_dict()
            else:
                params['ccs_instance_id'] = self.ccs_instance_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmSwTreeCreateModel()
        if 'ccs_instance_id' in d:
            o.ccs_instance_id = d['ccs_instance_id']
        if 'name' in d:
            o.name = d['name']
        return o


