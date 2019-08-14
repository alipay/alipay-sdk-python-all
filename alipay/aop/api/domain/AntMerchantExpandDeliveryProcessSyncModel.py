#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetDeliveryProcessInfo import AssetDeliveryProcessInfo


class AntMerchantExpandDeliveryProcessSyncModel(object):

    def __init__(self):
        self._asset_delivery_process_info = None

    @property
    def asset_delivery_process_info(self):
        return self._asset_delivery_process_info

    @asset_delivery_process_info.setter
    def asset_delivery_process_info(self, value):
        if isinstance(value, AssetDeliveryProcessInfo):
            self._asset_delivery_process_info = value
        else:
            self._asset_delivery_process_info = AssetDeliveryProcessInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.asset_delivery_process_info:
            if hasattr(self.asset_delivery_process_info, 'to_alipay_dict'):
                params['asset_delivery_process_info'] = self.asset_delivery_process_info.to_alipay_dict()
            else:
                params['asset_delivery_process_info'] = self.asset_delivery_process_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandDeliveryProcessSyncModel()
        if 'asset_delivery_process_info' in d:
            o.asset_delivery_process_info = d['asset_delivery_process_info']
        return o


