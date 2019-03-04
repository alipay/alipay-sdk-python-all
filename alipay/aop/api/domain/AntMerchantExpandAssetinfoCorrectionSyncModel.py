#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetInfoCorrectionItem import AssetInfoCorrectionItem


class AntMerchantExpandAssetinfoCorrectionSyncModel(object):

    def __init__(self):
        self._asset_correction = None

    @property
    def asset_correction(self):
        return self._asset_correction

    @asset_correction.setter
    def asset_correction(self, value):
        if isinstance(value, AssetInfoCorrectionItem):
            self._asset_correction = value
        else:
            self._asset_correction = AssetInfoCorrectionItem.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.asset_correction:
            if hasattr(self.asset_correction, 'to_alipay_dict'):
                params['asset_correction'] = self.asset_correction.to_alipay_dict()
            else:
                params['asset_correction'] = self.asset_correction
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandAssetinfoCorrectionSyncModel()
        if 'asset_correction' in d:
            o.asset_correction = d['asset_correction']
        return o


