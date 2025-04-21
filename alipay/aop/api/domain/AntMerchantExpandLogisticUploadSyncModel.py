#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetPickupLogisticsDetail import AssetPickupLogisticsDetail


class AntMerchantExpandLogisticUploadSyncModel(object):

    def __init__(self):
        self._asset_pickup_logistic_detail = None

    @property
    def asset_pickup_logistic_detail(self):
        return self._asset_pickup_logistic_detail

    @asset_pickup_logistic_detail.setter
    def asset_pickup_logistic_detail(self, value):
        if isinstance(value, AssetPickupLogisticsDetail):
            self._asset_pickup_logistic_detail = value
        else:
            self._asset_pickup_logistic_detail = AssetPickupLogisticsDetail.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.asset_pickup_logistic_detail:
            if hasattr(self.asset_pickup_logistic_detail, 'to_alipay_dict'):
                params['asset_pickup_logistic_detail'] = self.asset_pickup_logistic_detail.to_alipay_dict()
            else:
                params['asset_pickup_logistic_detail'] = self.asset_pickup_logistic_detail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandLogisticUploadSyncModel()
        if 'asset_pickup_logistic_detail' in d:
            o.asset_pickup_logistic_detail = d['asset_pickup_logistic_detail']
        return o


