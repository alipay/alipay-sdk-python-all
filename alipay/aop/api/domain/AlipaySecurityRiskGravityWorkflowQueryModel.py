#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskGravityWorkflowQueryModel(object):

    def __init__(self):
        self._pu_id = None

    @property
    def pu_id(self):
        return self._pu_id

    @pu_id.setter
    def pu_id(self, value):
        self._pu_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.pu_id:
            if hasattr(self.pu_id, 'to_alipay_dict'):
                params['pu_id'] = self.pu_id.to_alipay_dict()
            else:
                params['pu_id'] = self.pu_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskGravityWorkflowQueryModel()
        if 'pu_id' in d:
            o.pu_id = d['pu_id']
        return o


