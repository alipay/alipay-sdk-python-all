#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppJobinterviewTokenGetModel(object):

    def __init__(self):
        self._candidate_id = None
        self._tenant_id = None

    @property
    def candidate_id(self):
        return self._candidate_id

    @candidate_id.setter
    def candidate_id(self, value):
        self._candidate_id = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.candidate_id:
            if hasattr(self.candidate_id, 'to_alipay_dict'):
                params['candidate_id'] = self.candidate_id.to_alipay_dict()
            else:
                params['candidate_id'] = self.candidate_id
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppJobinterviewTokenGetModel()
        if 'candidate_id' in d:
            o.candidate_id = d['candidate_id']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


