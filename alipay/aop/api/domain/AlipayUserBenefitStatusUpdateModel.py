#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserBenefitStatusUpdateModel(object):

    def __init__(self):
        self._benefit_id = None
        self._benefit_new_flag = None
        self._benefit_status = None

    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def benefit_new_flag(self):
        return self._benefit_new_flag

    @benefit_new_flag.setter
    def benefit_new_flag(self, value):
        self._benefit_new_flag = value
    @property
    def benefit_status(self):
        return self._benefit_status

    @benefit_status.setter
    def benefit_status(self, value):
        self._benefit_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.benefit_new_flag:
            if hasattr(self.benefit_new_flag, 'to_alipay_dict'):
                params['benefit_new_flag'] = self.benefit_new_flag.to_alipay_dict()
            else:
                params['benefit_new_flag'] = self.benefit_new_flag
        if self.benefit_status:
            if hasattr(self.benefit_status, 'to_alipay_dict'):
                params['benefit_status'] = self.benefit_status.to_alipay_dict()
            else:
                params['benefit_status'] = self.benefit_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserBenefitStatusUpdateModel()
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'benefit_new_flag' in d:
            o.benefit_new_flag = d['benefit_new_flag']
        if 'benefit_status' in d:
            o.benefit_status = d['benefit_status']
        return o


