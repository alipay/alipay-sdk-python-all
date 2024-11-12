#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiFqAwardReceiveModel(object):

    def __init__(self):
        self._acquire_mode = None
        self._discount = None
        self._goods_name = None
        self._goods_num = None
        self._goods_type = None
        self._industry = None
        self._open_id = None
        self._pid = None
        self._product_code = None
        self._scene_type = None
        self._smid = None
        self._store_id = None
        self._store_name = None
        self._total_amount = None
        self._trade_place = None
        self._trading = None
        self._user_id = None

    @property
    def acquire_mode(self):
        return self._acquire_mode

    @acquire_mode.setter
    def acquire_mode(self, value):
        self._acquire_mode = value
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def goods_num(self):
        return self._goods_num

    @goods_num.setter
    def goods_num(self, value):
        self._goods_num = value
    @property
    def goods_type(self):
        return self._goods_type

    @goods_type.setter
    def goods_type(self, value):
        self._goods_type = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_place(self):
        return self._trade_place

    @trade_place.setter
    def trade_place(self, value):
        self._trade_place = value
    @property
    def trading(self):
        return self._trading

    @trading.setter
    def trading(self, value):
        self._trading = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.acquire_mode:
            if hasattr(self.acquire_mode, 'to_alipay_dict'):
                params['acquire_mode'] = self.acquire_mode.to_alipay_dict()
            else:
                params['acquire_mode'] = self.acquire_mode
        if self.discount:
            if hasattr(self.discount, 'to_alipay_dict'):
                params['discount'] = self.discount.to_alipay_dict()
            else:
                params['discount'] = self.discount
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.goods_num:
            if hasattr(self.goods_num, 'to_alipay_dict'):
                params['goods_num'] = self.goods_num.to_alipay_dict()
            else:
                params['goods_num'] = self.goods_num
        if self.goods_type:
            if hasattr(self.goods_type, 'to_alipay_dict'):
                params['goods_type'] = self.goods_type.to_alipay_dict()
            else:
                params['goods_type'] = self.goods_type
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.trade_place:
            if hasattr(self.trade_place, 'to_alipay_dict'):
                params['trade_place'] = self.trade_place.to_alipay_dict()
            else:
                params['trade_place'] = self.trade_place
        if self.trading:
            if hasattr(self.trading, 'to_alipay_dict'):
                params['trading'] = self.trading.to_alipay_dict()
            else:
                params['trading'] = self.trading
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
        o = AlipayPcreditHuabeiFqAwardReceiveModel()
        if 'acquire_mode' in d:
            o.acquire_mode = d['acquire_mode']
        if 'discount' in d:
            o.discount = d['discount']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'goods_num' in d:
            o.goods_num = d['goods_num']
        if 'goods_type' in d:
            o.goods_type = d['goods_type']
        if 'industry' in d:
            o.industry = d['industry']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'pid' in d:
            o.pid = d['pid']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'smid' in d:
            o.smid = d['smid']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_place' in d:
            o.trade_place = d['trade_place']
        if 'trading' in d:
            o.trading = d['trading']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


