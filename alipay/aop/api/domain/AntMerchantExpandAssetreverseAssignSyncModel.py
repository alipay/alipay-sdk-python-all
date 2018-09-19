#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetResult import AssetResult


class AntMerchantExpandAssetreverseAssignSyncModel(object):

    def __init__(self):
        self._reverse_results = None

    @property
    def reverse_results(self):
        return self._reverse_results

    @reverse_results.setter
    def reverse_results(self, value):
        if isinstance(value, list):
            self._reverse_results = list()
            for i in value:
                if isinstance(i, AssetResult):
                    self._reverse_results.append(i)
                else:
                    self._reverse_results.append(AssetResult.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.reverse_results:
            if isinstance(self.reverse_results, list):
                for i in range(0, len(self.reverse_results)):
                    element = self.reverse_results[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.reverse_results[i] = element.to_alipay_dict()
            if hasattr(self.reverse_results, 'to_alipay_dict'):
                params['reverse_results'] = self.reverse_results.to_alipay_dict()
            else:
                params['reverse_results'] = self.reverse_results
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandAssetreverseAssignSyncModel()
        if 'reverse_results' in d:
            o.reverse_results = d['reverse_results']
        return o


