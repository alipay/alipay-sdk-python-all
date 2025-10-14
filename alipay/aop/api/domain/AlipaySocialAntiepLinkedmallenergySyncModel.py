#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialAntiepLinkedmallenergySyncModel(object):

    def __init__(self):
        self._amount = None
        self._biz_context = None
        self._item_id = None
        self._lm_order_id = None
        self._modified_time = None
        self._open_id = None
        self._order_status = None
        self._pre_order_status = None
        self._scene_code = None
        self._sku_id = None
        self._user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_context(self):
        return self._biz_context

    @biz_context.setter
    def biz_context(self, value):
        self._biz_context = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def lm_order_id(self):
        return self._lm_order_id

    @lm_order_id.setter
    def lm_order_id(self, value):
        self._lm_order_id = value
    @property
    def modified_time(self):
        return self._modified_time

    @modified_time.setter
    def modified_time(self, value):
        self._modified_time = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def pre_order_status(self):
        return self._pre_order_status

    @pre_order_status.setter
    def pre_order_status(self, value):
        self._pre_order_status = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_context:
            if hasattr(self.biz_context, 'to_alipay_dict'):
                params['biz_context'] = self.biz_context.to_alipay_dict()
            else:
                params['biz_context'] = self.biz_context
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.lm_order_id:
            if hasattr(self.lm_order_id, 'to_alipay_dict'):
                params['lm_order_id'] = self.lm_order_id.to_alipay_dict()
            else:
                params['lm_order_id'] = self.lm_order_id
        if self.modified_time:
            if hasattr(self.modified_time, 'to_alipay_dict'):
                params['modified_time'] = self.modified_time.to_alipay_dict()
            else:
                params['modified_time'] = self.modified_time
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.pre_order_status:
            if hasattr(self.pre_order_status, 'to_alipay_dict'):
                params['pre_order_status'] = self.pre_order_status.to_alipay_dict()
            else:
                params['pre_order_status'] = self.pre_order_status
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
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
        o = AlipaySocialAntiepLinkedmallenergySyncModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_context' in d:
            o.biz_context = d['biz_context']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'lm_order_id' in d:
            o.lm_order_id = d['lm_order_id']
        if 'modified_time' in d:
            o.modified_time = d['modified_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'pre_order_status' in d:
            o.pre_order_status = d['pre_order_status']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


