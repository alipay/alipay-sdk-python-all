#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetChannelInfo import AssetChannelInfo


class VoucherDetailModel(object):

    def __init__(self):
        self._can_use_asset_channel_infos = None

    @property
    def can_use_asset_channel_infos(self):
        return self._can_use_asset_channel_infos

    @can_use_asset_channel_infos.setter
    def can_use_asset_channel_infos(self, value):
        if isinstance(value, list):
            self._can_use_asset_channel_infos = list()
            for i in value:
                if isinstance(i, AssetChannelInfo):
                    self._can_use_asset_channel_infos.append(i)
                else:
                    self._can_use_asset_channel_infos.append(AssetChannelInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.can_use_asset_channel_infos:
            if isinstance(self.can_use_asset_channel_infos, list):
                for i in range(0, len(self.can_use_asset_channel_infos)):
                    element = self.can_use_asset_channel_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.can_use_asset_channel_infos[i] = element.to_alipay_dict()
            if hasattr(self.can_use_asset_channel_infos, 'to_alipay_dict'):
                params['can_use_asset_channel_infos'] = self.can_use_asset_channel_infos.to_alipay_dict()
            else:
                params['can_use_asset_channel_infos'] = self.can_use_asset_channel_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherDetailModel()
        if 'can_use_asset_channel_infos' in d:
            o.can_use_asset_channel_infos = d['can_use_asset_channel_infos']
        return o


