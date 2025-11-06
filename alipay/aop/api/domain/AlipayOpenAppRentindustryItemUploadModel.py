#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantUploadSpuInfo import MerchantUploadSpuInfo


class AlipayOpenAppRentindustryItemUploadModel(object):

    def __init__(self):
        self._item_sku_infos = None

    @property
    def item_sku_infos(self):
        return self._item_sku_infos

    @item_sku_infos.setter
    def item_sku_infos(self, value):
        if isinstance(value, list):
            self._item_sku_infos = list()
            for i in value:
                if isinstance(i, MerchantUploadSpuInfo):
                    self._item_sku_infos.append(i)
                else:
                    self._item_sku_infos.append(MerchantUploadSpuInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.item_sku_infos:
            if isinstance(self.item_sku_infos, list):
                for i in range(0, len(self.item_sku_infos)):
                    element = self.item_sku_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_sku_infos[i] = element.to_alipay_dict()
            if hasattr(self.item_sku_infos, 'to_alipay_dict'):
                params['item_sku_infos'] = self.item_sku_infos.to_alipay_dict()
            else:
                params['item_sku_infos'] = self.item_sku_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppRentindustryItemUploadModel()
        if 'item_sku_infos' in d:
            o.item_sku_infos = d['item_sku_infos']
        return o


