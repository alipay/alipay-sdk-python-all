#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetDeliveryDetail import AssetDeliveryDetail


class AntMerchantExpandAssetdeliveryCompleteSyncModel(object):

    def __init__(self):
        self._asset_delivery_details = None

    @property
    def asset_delivery_details(self):
        return self._asset_delivery_details

    @asset_delivery_details.setter
    def asset_delivery_details(self, value):
        if isinstance(value, list):
            self._asset_delivery_details = list()
            for i in value:
                if isinstance(i, AssetDeliveryDetail):
                    self._asset_delivery_details.append(i)
                else:
                    self._asset_delivery_details.append(AssetDeliveryDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.asset_delivery_details:
            if isinstance(self.asset_delivery_details, list):
                for i in range(0, len(self.asset_delivery_details)):
                    element = self.asset_delivery_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.asset_delivery_details[i] = element.to_alipay_dict()
            if hasattr(self.asset_delivery_details, 'to_alipay_dict'):
                params['asset_delivery_details'] = self.asset_delivery_details.to_alipay_dict()
            else:
                params['asset_delivery_details'] = self.asset_delivery_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandAssetdeliveryCompleteSyncModel()
        if 'asset_delivery_details' in d:
            o.asset_delivery_details = d['asset_delivery_details']
        return o


