#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemDeliveryDetail import ItemDeliveryDetail


class AntMerchantExpandAssetproduceCompleteSyncModel(object):

    def __init__(self):
        self._asset_produce_details = None

    @property
    def asset_produce_details(self):
        return self._asset_produce_details

    @asset_produce_details.setter
    def asset_produce_details(self, value):
        if isinstance(value, list):
            self._asset_produce_details = list()
            for i in value:
                if isinstance(i, ItemDeliveryDetail):
                    self._asset_produce_details.append(i)
                else:
                    self._asset_produce_details.append(ItemDeliveryDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.asset_produce_details:
            if isinstance(self.asset_produce_details, list):
                for i in range(0, len(self.asset_produce_details)):
                    element = self.asset_produce_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.asset_produce_details[i] = element.to_alipay_dict()
            if hasattr(self.asset_produce_details, 'to_alipay_dict'):
                params['asset_produce_details'] = self.asset_produce_details.to_alipay_dict()
            else:
                params['asset_produce_details'] = self.asset_produce_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandAssetproduceCompleteSyncModel()
        if 'asset_produce_details' in d:
            o.asset_produce_details = d['asset_produce_details']
        return o


