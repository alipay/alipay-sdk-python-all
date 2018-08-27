#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetResult import AssetResult


class AntMerchantExpandAssetproduceAssignSyncModel(object):

    def __init__(self):
        self._asset_results = None

    @property
    def asset_results(self):
        return self._asset_results

    @asset_results.setter
    def asset_results(self, value):
        if isinstance(value, list):
            self._asset_results = list()
            for i in value:
                if isinstance(i, AssetResult):
                    self._asset_results.append(i)
                else:
                    self._asset_results.append(AssetResult.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.asset_results:
            if isinstance(self.asset_results, list):
                for i in range(0, len(self.asset_results)):
                    element = self.asset_results[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.asset_results[i] = element.to_alipay_dict()
            if hasattr(self.asset_results, 'to_alipay_dict'):
                params['asset_results'] = self.asset_results.to_alipay_dict()
            else:
                params['asset_results'] = self.asset_results
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandAssetproduceAssignSyncModel()
        if 'asset_results' in d:
            o.asset_results = d['asset_results']
        return o


