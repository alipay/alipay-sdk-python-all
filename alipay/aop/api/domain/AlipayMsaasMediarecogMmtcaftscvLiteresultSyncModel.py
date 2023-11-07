#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContrastResult import ContrastResult


class AlipayMsaasMediarecogMmtcaftscvLiteresultSyncModel(object):

    def __init__(self):
        self._contrast_result = None
        self._result_type = None
        self._transaction_id = None

    @property
    def contrast_result(self):
        return self._contrast_result

    @contrast_result.setter
    def contrast_result(self, value):
        if isinstance(value, list):
            self._contrast_result = list()
            for i in value:
                if isinstance(i, ContrastResult):
                    self._contrast_result.append(i)
                else:
                    self._contrast_result.append(ContrastResult.from_alipay_dict(i))
    @property
    def result_type(self):
        return self._result_type

    @result_type.setter
    def result_type(self, value):
        self._result_type = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.contrast_result:
            if isinstance(self.contrast_result, list):
                for i in range(0, len(self.contrast_result)):
                    element = self.contrast_result[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contrast_result[i] = element.to_alipay_dict()
            if hasattr(self.contrast_result, 'to_alipay_dict'):
                params['contrast_result'] = self.contrast_result.to_alipay_dict()
            else:
                params['contrast_result'] = self.contrast_result
        if self.result_type:
            if hasattr(self.result_type, 'to_alipay_dict'):
                params['result_type'] = self.result_type.to_alipay_dict()
            else:
                params['result_type'] = self.result_type
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogMmtcaftscvLiteresultSyncModel()
        if 'contrast_result' in d:
            o.contrast_result = d['contrast_result']
        if 'result_type' in d:
            o.result_type = d['result_type']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        return o


