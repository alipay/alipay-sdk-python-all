#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChargeRelationInfo(object):

    def __init__(self):
        self._primary_id = None
        self._slave_id = None

    @property
    def primary_id(self):
        return self._primary_id

    @primary_id.setter
    def primary_id(self, value):
        self._primary_id = value
    @property
    def slave_id(self):
        return self._slave_id

    @slave_id.setter
    def slave_id(self, value):
        self._slave_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.primary_id:
            if hasattr(self.primary_id, 'to_alipay_dict'):
                params['primary_id'] = self.primary_id.to_alipay_dict()
            else:
                params['primary_id'] = self.primary_id
        if self.slave_id:
            if hasattr(self.slave_id, 'to_alipay_dict'):
                params['slave_id'] = self.slave_id.to_alipay_dict()
            else:
                params['slave_id'] = self.slave_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChargeRelationInfo()
        if 'primary_id' in d:
            o.primary_id = d['primary_id']
        if 'slave_id' in d:
            o.slave_id = d['slave_id']
        return o


