#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiGoodsOrderSyncModel(object):

    def __init__(self):
        self._alipay_order_id = None
        self._alipay_user_id = None
        self._biz_item_id = None
        self._biz_item_name = None
        self._biz_src = None
        self._biz_timestamp = None
        self._city_code = None
        self._gmt_active = None
        self._gmt_expired = None
        self._img_url = None
        self._number = None
        self._out_order_id = None
        self._refund_amount = None
        self._refund_number = None
        self._trade_amount = None
        self._trade_dt = None
        self._use_number = None

    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def biz_item_id(self):
        return self._biz_item_id

    @biz_item_id.setter
    def biz_item_id(self, value):
        self._biz_item_id = value
    @property
    def biz_item_name(self):
        return self._biz_item_name

    @biz_item_name.setter
    def biz_item_name(self, value):
        self._biz_item_name = value
    @property
    def biz_src(self):
        return self._biz_src

    @biz_src.setter
    def biz_src(self, value):
        self._biz_src = value
    @property
    def biz_timestamp(self):
        return self._biz_timestamp

    @biz_timestamp.setter
    def biz_timestamp(self, value):
        self._biz_timestamp = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def gmt_active(self):
        return self._gmt_active

    @gmt_active.setter
    def gmt_active(self, value):
        self._gmt_active = value
    @property
    def gmt_expired(self):
        return self._gmt_expired

    @gmt_expired.setter
    def gmt_expired(self, value):
        self._gmt_expired = value
    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_number(self):
        return self._refund_number

    @refund_number.setter
    def refund_number(self, value):
        self._refund_number = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def trade_dt(self):
        return self._trade_dt

    @trade_dt.setter
    def trade_dt(self, value):
        self._trade_dt = value
    @property
    def use_number(self):
        return self._use_number

    @use_number.setter
    def use_number(self, value):
        self._use_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_id:
            if hasattr(self.alipay_order_id, 'to_alipay_dict'):
                params['alipay_order_id'] = self.alipay_order_id.to_alipay_dict()
            else:
                params['alipay_order_id'] = self.alipay_order_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.biz_item_id:
            if hasattr(self.biz_item_id, 'to_alipay_dict'):
                params['biz_item_id'] = self.biz_item_id.to_alipay_dict()
            else:
                params['biz_item_id'] = self.biz_item_id
        if self.biz_item_name:
            if hasattr(self.biz_item_name, 'to_alipay_dict'):
                params['biz_item_name'] = self.biz_item_name.to_alipay_dict()
            else:
                params['biz_item_name'] = self.biz_item_name
        if self.biz_src:
            if hasattr(self.biz_src, 'to_alipay_dict'):
                params['biz_src'] = self.biz_src.to_alipay_dict()
            else:
                params['biz_src'] = self.biz_src
        if self.biz_timestamp:
            if hasattr(self.biz_timestamp, 'to_alipay_dict'):
                params['biz_timestamp'] = self.biz_timestamp.to_alipay_dict()
            else:
                params['biz_timestamp'] = self.biz_timestamp
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.gmt_active:
            if hasattr(self.gmt_active, 'to_alipay_dict'):
                params['gmt_active'] = self.gmt_active.to_alipay_dict()
            else:
                params['gmt_active'] = self.gmt_active
        if self.gmt_expired:
            if hasattr(self.gmt_expired, 'to_alipay_dict'):
                params['gmt_expired'] = self.gmt_expired.to_alipay_dict()
            else:
                params['gmt_expired'] = self.gmt_expired
        if self.img_url:
            if hasattr(self.img_url, 'to_alipay_dict'):
                params['img_url'] = self.img_url.to_alipay_dict()
            else:
                params['img_url'] = self.img_url
        if self.number:
            if hasattr(self.number, 'to_alipay_dict'):
                params['number'] = self.number.to_alipay_dict()
            else:
                params['number'] = self.number
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_number:
            if hasattr(self.refund_number, 'to_alipay_dict'):
                params['refund_number'] = self.refund_number.to_alipay_dict()
            else:
                params['refund_number'] = self.refund_number
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        if self.trade_dt:
            if hasattr(self.trade_dt, 'to_alipay_dict'):
                params['trade_dt'] = self.trade_dt.to_alipay_dict()
            else:
                params['trade_dt'] = self.trade_dt
        if self.use_number:
            if hasattr(self.use_number, 'to_alipay_dict'):
                params['use_number'] = self.use_number.to_alipay_dict()
            else:
                params['use_number'] = self.use_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiGoodsOrderSyncModel()
        if 'alipay_order_id' in d:
            o.alipay_order_id = d['alipay_order_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_item_id' in d:
            o.biz_item_id = d['biz_item_id']
        if 'biz_item_name' in d:
            o.biz_item_name = d['biz_item_name']
        if 'biz_src' in d:
            o.biz_src = d['biz_src']
        if 'biz_timestamp' in d:
            o.biz_timestamp = d['biz_timestamp']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'gmt_active' in d:
            o.gmt_active = d['gmt_active']
        if 'gmt_expired' in d:
            o.gmt_expired = d['gmt_expired']
        if 'img_url' in d:
            o.img_url = d['img_url']
        if 'number' in d:
            o.number = d['number']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_number' in d:
            o.refund_number = d['refund_number']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        if 'trade_dt' in d:
            o.trade_dt = d['trade_dt']
        if 'use_number' in d:
            o.use_number = d['use_number']
        return o


