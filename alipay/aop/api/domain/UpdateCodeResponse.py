#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UpdateCodeResult import UpdateCodeResult


class UpdateCodeResponse(object):

    def __init__(self):
        self._update_code_result = None

    @property
    def update_code_result(self):
        return self._update_code_result

    @update_code_result.setter
    def update_code_result(self, value):
        if isinstance(value, list):
            self._update_code_result = list()
            for i in value:
                if isinstance(i, UpdateCodeResult):
                    self._update_code_result.append(i)
                else:
                    self._update_code_result.append(UpdateCodeResult.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.update_code_result:
            if isinstance(self.update_code_result, list):
                for i in range(0, len(self.update_code_result)):
                    element = self.update_code_result[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.update_code_result[i] = element.to_alipay_dict()
            if hasattr(self.update_code_result, 'to_alipay_dict'):
                params['update_code_result'] = self.update_code_result.to_alipay_dict()
            else:
                params['update_code_result'] = self.update_code_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UpdateCodeResponse()
        if 'update_code_result' in d:
            o.update_code_result = d['update_code_result']
        return o


