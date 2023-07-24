#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoApplyItemDetailInfoVO import PromoApplyItemDetailInfoVO


class PromoApplyItemInfoVO(object):

    def __init__(self):
        self._item_id = None
        self._promo_apply_item_detail_infos = None
        self._sku_id = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def promo_apply_item_detail_infos(self):
        return self._promo_apply_item_detail_infos

    @promo_apply_item_detail_infos.setter
    def promo_apply_item_detail_infos(self, value):
        if isinstance(value, list):
            self._promo_apply_item_detail_infos = list()
            for i in value:
                if isinstance(i, PromoApplyItemDetailInfoVO):
                    self._promo_apply_item_detail_infos.append(i)
                else:
                    self._promo_apply_item_detail_infos.append(PromoApplyItemDetailInfoVO.from_alipay_dict(i))
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.promo_apply_item_detail_infos:
            if isinstance(self.promo_apply_item_detail_infos, list):
                for i in range(0, len(self.promo_apply_item_detail_infos)):
                    element = self.promo_apply_item_detail_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promo_apply_item_detail_infos[i] = element.to_alipay_dict()
            if hasattr(self.promo_apply_item_detail_infos, 'to_alipay_dict'):
                params['promo_apply_item_detail_infos'] = self.promo_apply_item_detail_infos.to_alipay_dict()
            else:
                params['promo_apply_item_detail_infos'] = self.promo_apply_item_detail_infos
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoApplyItemInfoVO()
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'promo_apply_item_detail_infos' in d:
            o.promo_apply_item_detail_infos = d['promo_apply_item_detail_infos']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


