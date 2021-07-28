#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingRecruitEnrollCloseModel(object):

    def __init__(self):
        self._enroll_id = None

    @property
    def enroll_id(self):
        return self._enroll_id

    @enroll_id.setter
    def enroll_id(self, value):
        self._enroll_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.enroll_id:
            if hasattr(self.enroll_id, 'to_alipay_dict'):
                params['enroll_id'] = self.enroll_id.to_alipay_dict()
            else:
                params['enroll_id'] = self.enroll_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingRecruitEnrollCloseModel()
        if 'enroll_id' in d:
            o.enroll_id = d['enroll_id']
        return o


