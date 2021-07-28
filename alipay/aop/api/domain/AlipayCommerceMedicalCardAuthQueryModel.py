#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalCardAuthQueryModel(object):

    def __init__(self):
        self._ins_code = None
        self._relation_type = None

    @property
    def ins_code(self):
        return self._ins_code

    @ins_code.setter
    def ins_code(self, value):
        self._ins_code = value
    @property
    def relation_type(self):
        return self._relation_type

    @relation_type.setter
    def relation_type(self, value):
        self._relation_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.ins_code:
            if hasattr(self.ins_code, 'to_alipay_dict'):
                params['ins_code'] = self.ins_code.to_alipay_dict()
            else:
                params['ins_code'] = self.ins_code
        if self.relation_type:
            if hasattr(self.relation_type, 'to_alipay_dict'):
                params['relation_type'] = self.relation_type.to_alipay_dict()
            else:
                params['relation_type'] = self.relation_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalCardAuthQueryModel()
        if 'ins_code' in d:
            o.ins_code = d['ins_code']
        if 'relation_type' in d:
            o.relation_type = d['relation_type']
        return o


