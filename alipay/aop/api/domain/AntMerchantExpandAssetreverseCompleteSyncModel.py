#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetReverseDetail import AssetReverseDetail


class AntMerchantExpandAssetreverseCompleteSyncModel(object):

    def __init__(self):
        self._asset_reverse_details = None

    @property
    def asset_reverse_details(self):
        return self._asset_reverse_details

    @asset_reverse_details.setter
    def asset_reverse_details(self, value):
        if isinstance(value, list):
            self._asset_reverse_details = list()
            for i in value:
                if isinstance(i, AssetReverseDetail):
                    self._asset_reverse_details.append(i)
                else:
                    self._asset_reverse_details.append(AssetReverseDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.asset_reverse_details:
            if isinstance(self.asset_reverse_details, list):
                for i in range(0, len(self.asset_reverse_details)):
                    element = self.asset_reverse_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.asset_reverse_details[i] = element.to_alipay_dict()
            if hasattr(self.asset_reverse_details, 'to_alipay_dict'):
                params['asset_reverse_details'] = self.asset_reverse_details.to_alipay_dict()
            else:
                params['asset_reverse_details'] = self.asset_reverse_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandAssetreverseCompleteSyncModel()
        if 'asset_reverse_details' in d:
            o.asset_reverse_details = d['asset_reverse_details']
        return o


