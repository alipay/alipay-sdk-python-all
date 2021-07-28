#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApplyCodeResult import ApplyCodeResult


class ApplyCodeResponse(object):

    def __init__(self):
        self._apply_code_result = None

    @property
    def apply_code_result(self):
        return self._apply_code_result

    @apply_code_result.setter
    def apply_code_result(self, value):
        if isinstance(value, list):
            self._apply_code_result = list()
            for i in value:
                if isinstance(i, ApplyCodeResult):
                    self._apply_code_result.append(i)
                else:
                    self._apply_code_result.append(ApplyCodeResult.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.apply_code_result:
            if isinstance(self.apply_code_result, list):
                for i in range(0, len(self.apply_code_result)):
                    element = self.apply_code_result[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apply_code_result[i] = element.to_alipay_dict()
            if hasattr(self.apply_code_result, 'to_alipay_dict'):
                params['apply_code_result'] = self.apply_code_result.to_alipay_dict()
            else:
                params['apply_code_result'] = self.apply_code_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApplyCodeResponse()
        if 'apply_code_result' in d:
            o.apply_code_result = d['apply_code_result']
        return o


