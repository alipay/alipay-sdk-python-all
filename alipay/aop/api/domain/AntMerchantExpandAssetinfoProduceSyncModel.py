#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetInfoItem import AssetInfoItem


class AntMerchantExpandAssetinfoProduceSyncModel(object):

    def __init__(self):
        self._asset_infos = None

    @property
    def asset_infos(self):
        return self._asset_infos

    @asset_infos.setter
    def asset_infos(self, value):
        if isinstance(value, list):
            self._asset_infos = list()
            for i in value:
                if isinstance(i, AssetInfoItem):
                    self._asset_infos.append(i)
                else:
                    self._asset_infos.append(AssetInfoItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.asset_infos:
            if isinstance(self.asset_infos, list):
                for i in range(0, len(self.asset_infos)):
                    element = self.asset_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.asset_infos[i] = element.to_alipay_dict()
            if hasattr(self.asset_infos, 'to_alipay_dict'):
                params['asset_infos'] = self.asset_infos.to_alipay_dict()
            else:
                params['asset_infos'] = self.asset_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandAssetinfoProduceSyncModel()
        if 'asset_infos' in d:
            o.asset_infos = d['asset_infos']
        return o


