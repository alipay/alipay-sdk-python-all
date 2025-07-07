#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleOutAssessInfo(object):

    def __init__(self):
        self._estimate_result_id = None

    @property
    def estimate_result_id(self):
        return self._estimate_result_id

    @estimate_result_id.setter
    def estimate_result_id(self, value):
        self._estimate_result_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.estimate_result_id:
            if hasattr(self.estimate_result_id, 'to_alipay_dict'):
                params['estimate_result_id'] = self.estimate_result_id.to_alipay_dict()
            else:
                params['estimate_result_id'] = self.estimate_result_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleOutAssessInfo()
        if 'estimate_result_id' in d:
            o.estimate_result_id = d['estimate_result_id']
        return o


