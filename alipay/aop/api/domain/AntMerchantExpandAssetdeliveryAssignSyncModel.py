#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetResult import AssetResult


class AntMerchantExpandAssetdeliveryAssignSyncModel(object):

    def __init__(self):
        self._delivery_results = None

    @property
    def delivery_results(self):
        return self._delivery_results

    @delivery_results.setter
    def delivery_results(self, value):
        if isinstance(value, list):
            self._delivery_results = list()
            for i in value:
                if isinstance(i, AssetResult):
                    self._delivery_results.append(i)
                else:
                    self._delivery_results.append(AssetResult.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_results:
            if isinstance(self.delivery_results, list):
                for i in range(0, len(self.delivery_results)):
                    element = self.delivery_results[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delivery_results[i] = element.to_alipay_dict()
            if hasattr(self.delivery_results, 'to_alipay_dict'):
                params['delivery_results'] = self.delivery_results.to_alipay_dict()
            else:
                params['delivery_results'] = self.delivery_results
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandAssetdeliveryAssignSyncModel()
        if 'delivery_results' in d:
            o.delivery_results = d['delivery_results']
        return o


