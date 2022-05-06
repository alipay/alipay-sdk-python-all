#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetCallbackInfo import AssetCallbackInfo


class AntMerchantExpandAssetInteractSyncModel(object):

    def __init__(self):
        self._asset_callback_results = None

    @property
    def asset_callback_results(self):
        return self._asset_callback_results

    @asset_callback_results.setter
    def asset_callback_results(self, value):
        if isinstance(value, list):
            self._asset_callback_results = list()
            for i in value:
                if isinstance(i, AssetCallbackInfo):
                    self._asset_callback_results.append(i)
                else:
                    self._asset_callback_results.append(AssetCallbackInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.asset_callback_results:
            if isinstance(self.asset_callback_results, list):
                for i in range(0, len(self.asset_callback_results)):
                    element = self.asset_callback_results[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.asset_callback_results[i] = element.to_alipay_dict()
            if hasattr(self.asset_callback_results, 'to_alipay_dict'):
                params['asset_callback_results'] = self.asset_callback_results.to_alipay_dict()
            else:
                params['asset_callback_results'] = self.asset_callback_results
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandAssetInteractSyncModel()
        if 'asset_callback_results' in d:
            o.asset_callback_results = d['asset_callback_results']
        return o


