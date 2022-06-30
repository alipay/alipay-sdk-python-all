#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenViolationViolationdetailQueryModel(object):

    def __init__(self):
        self._violation_record_id = None

    @property
    def violation_record_id(self):
        return self._violation_record_id

    @violation_record_id.setter
    def violation_record_id(self, value):
        self._violation_record_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.violation_record_id:
            if hasattr(self.violation_record_id, 'to_alipay_dict'):
                params['violation_record_id'] = self.violation_record_id.to_alipay_dict()
            else:
                params['violation_record_id'] = self.violation_record_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenViolationViolationdetailQueryModel()
        if 'violation_record_id' in d:
            o.violation_record_id = d['violation_record_id']
        return o


