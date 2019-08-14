#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetLogisticsRecord import AssetLogisticsRecord


class AntMerchantExpandExpressChangeSyncModel(object):

    def __init__(self):
        self._asset_logistics_record = None

    @property
    def asset_logistics_record(self):
        return self._asset_logistics_record

    @asset_logistics_record.setter
    def asset_logistics_record(self, value):
        if isinstance(value, AssetLogisticsRecord):
            self._asset_logistics_record = value
        else:
            self._asset_logistics_record = AssetLogisticsRecord.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.asset_logistics_record:
            if hasattr(self.asset_logistics_record, 'to_alipay_dict'):
                params['asset_logistics_record'] = self.asset_logistics_record.to_alipay_dict()
            else:
                params['asset_logistics_record'] = self.asset_logistics_record
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandExpressChangeSyncModel()
        if 'asset_logistics_record' in d:
            o.asset_logistics_record = d['asset_logistics_record']
        return o


