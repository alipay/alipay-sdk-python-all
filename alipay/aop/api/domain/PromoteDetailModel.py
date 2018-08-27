#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoteItemModel import PromoteItemModel
from alipay.aop.api.domain.PromoteDataModel import PromoteDataModel


class PromoteDetailModel(object):

    def __init__(self):
        self._adv_id = None
        self._biz_id = None
        self._biz_type = None
        self._item_info = None
        self._promote_data = None

    @property
    def adv_id(self):
        return self._adv_id

    @adv_id.setter
    def adv_id(self, value):
        self._adv_id = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def item_info(self):
        return self._item_info

    @item_info.setter
    def item_info(self, value):
        if isinstance(value, PromoteItemModel):
            self._item_info = value
        else:
            self._item_info = PromoteItemModel.from_alipay_dict(value)
    @property
    def promote_data(self):
        return self._promote_data

    @promote_data.setter
    def promote_data(self, value):
        if isinstance(value, PromoteDataModel):
            self._promote_data = value
        else:
            self._promote_data = PromoteDataModel.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.adv_id:
            if hasattr(self.adv_id, 'to_alipay_dict'):
                params['adv_id'] = self.adv_id.to_alipay_dict()
            else:
                params['adv_id'] = self.adv_id
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.item_info:
            if hasattr(self.item_info, 'to_alipay_dict'):
                params['item_info'] = self.item_info.to_alipay_dict()
            else:
                params['item_info'] = self.item_info
        if self.promote_data:
            if hasattr(self.promote_data, 'to_alipay_dict'):
                params['promote_data'] = self.promote_data.to_alipay_dict()
            else:
                params['promote_data'] = self.promote_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoteDetailModel()
        if 'adv_id' in d:
            o.adv_id = d['adv_id']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'item_info' in d:
            o.item_info = d['item_info']
        if 'promote_data' in d:
            o.promote_data = d['promote_data']
        return o


