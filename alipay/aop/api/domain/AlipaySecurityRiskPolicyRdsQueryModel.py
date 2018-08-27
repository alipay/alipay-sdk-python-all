#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskPolicyRdsQueryModel(object):

    def __init__(self):
        self._rds_params = None

    @property
    def rds_params(self):
        return self._rds_params

    @rds_params.setter
    def rds_params(self, value):
        self._rds_params = value


    def to_alipay_dict(self):
        params = dict()
        if self.rds_params:
            if hasattr(self.rds_params, 'to_alipay_dict'):
                params['rds_params'] = self.rds_params.to_alipay_dict()
            else:
                params['rds_params'] = self.rds_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskPolicyRdsQueryModel()
        if 'rds_params' in d:
            o.rds_params = d['rds_params']
        return o


