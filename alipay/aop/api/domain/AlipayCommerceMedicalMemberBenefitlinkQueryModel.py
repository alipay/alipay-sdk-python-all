#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalMemberBenefitlinkQueryModel(object):

    def __init__(self):
        self._benefit_code = None
        self._open_id = None

    @property
    def benefit_code(self):
        return self._benefit_code

    @benefit_code.setter
    def benefit_code(self, value):
        self._benefit_code = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_code:
            if hasattr(self.benefit_code, 'to_alipay_dict'):
                params['benefit_code'] = self.benefit_code.to_alipay_dict()
            else:
                params['benefit_code'] = self.benefit_code
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMemberBenefitlinkQueryModel()
        if 'benefit_code' in d:
            o.benefit_code = d['benefit_code']
        if 'open_id' in d:
            o.open_id = d['open_id']
        return o


