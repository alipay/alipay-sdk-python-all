#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateInstitutionInfoCreateModel(object):

    def __init__(self):
        self._inst_id = None
        self._ref_inst_code = None

    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def ref_inst_code(self):
        return self._ref_inst_code

    @ref_inst_code.setter
    def ref_inst_code(self, value):
        self._ref_inst_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.ref_inst_code:
            if hasattr(self.ref_inst_code, 'to_alipay_dict'):
                params['ref_inst_code'] = self.ref_inst_code.to_alipay_dict()
            else:
                params['ref_inst_code'] = self.ref_inst_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateInstitutionInfoCreateModel()
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'ref_inst_code' in d:
            o.ref_inst_code = d['ref_inst_code']
        return o


