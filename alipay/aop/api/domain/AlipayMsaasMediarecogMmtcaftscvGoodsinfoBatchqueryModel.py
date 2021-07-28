#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasMediarecogMmtcaftscvGoodsinfoBatchqueryModel(object):

    def __init__(self):
        self._algorithm_ids = None

    @property
    def algorithm_ids(self):
        return self._algorithm_ids

    @algorithm_ids.setter
    def algorithm_ids(self, value):
        if isinstance(value, list):
            self._algorithm_ids = list()
            for i in value:
                self._algorithm_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.algorithm_ids:
            if isinstance(self.algorithm_ids, list):
                for i in range(0, len(self.algorithm_ids)):
                    element = self.algorithm_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.algorithm_ids[i] = element.to_alipay_dict()
            if hasattr(self.algorithm_ids, 'to_alipay_dict'):
                params['algorithm_ids'] = self.algorithm_ids.to_alipay_dict()
            else:
                params['algorithm_ids'] = self.algorithm_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogMmtcaftscvGoodsinfoBatchqueryModel()
        if 'algorithm_ids' in d:
            o.algorithm_ids = d['algorithm_ids']
        return o


