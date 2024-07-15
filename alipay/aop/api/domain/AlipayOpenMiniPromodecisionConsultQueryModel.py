#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemDetailInfo import ItemDetailInfo
from alipay.aop.api.domain.OutPromoInfo import OutPromoInfo


class AlipayOpenMiniPromodecisionConsultQueryModel(object):

    def __init__(self):
        self._item_detail_info = None
        self._open_id = None
        self._out_promo_info = None
        self._user_id = None

    @property
    def item_detail_info(self):
        return self._item_detail_info

    @item_detail_info.setter
    def item_detail_info(self, value):
        if isinstance(value, ItemDetailInfo):
            self._item_detail_info = value
        else:
            self._item_detail_info = ItemDetailInfo.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_promo_info(self):
        return self._out_promo_info

    @out_promo_info.setter
    def out_promo_info(self, value):
        if isinstance(value, OutPromoInfo):
            self._out_promo_info = value
        else:
            self._out_promo_info = OutPromoInfo.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_detail_info:
            if hasattr(self.item_detail_info, 'to_alipay_dict'):
                params['item_detail_info'] = self.item_detail_info.to_alipay_dict()
            else:
                params['item_detail_info'] = self.item_detail_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_promo_info:
            if hasattr(self.out_promo_info, 'to_alipay_dict'):
                params['out_promo_info'] = self.out_promo_info.to_alipay_dict()
            else:
                params['out_promo_info'] = self.out_promo_info
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniPromodecisionConsultQueryModel()
        if 'item_detail_info' in d:
            o.item_detail_info = d['item_detail_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_promo_info' in d:
            o.out_promo_info = d['out_promo_info']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


