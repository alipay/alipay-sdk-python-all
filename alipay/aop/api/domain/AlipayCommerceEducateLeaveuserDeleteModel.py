#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateLeaveuserDeleteModel(object):

    def __init__(self):
        self._apply_id = None
        self._inst_id = None
        self._roster_id = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def roster_id(self):
        return self._roster_id

    @roster_id.setter
    def roster_id(self, value):
        self._roster_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.roster_id:
            if hasattr(self.roster_id, 'to_alipay_dict'):
                params['roster_id'] = self.roster_id.to_alipay_dict()
            else:
                params['roster_id'] = self.roster_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateLeaveuserDeleteModel()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'roster_id' in d:
            o.roster_id = d['roster_id']
        return o


