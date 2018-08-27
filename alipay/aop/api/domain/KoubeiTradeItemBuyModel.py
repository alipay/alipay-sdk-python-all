#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiTradeItemBuyModel(object):

    def __init__(self):
        self._buyer_phone_number = None
        self._buyer_user_name = None
        self._craftsman_id = None
        self._current_price = None
        self._ext_info = None
        self._item_id = None
        self._original_price = None
        self._out_biz_no = None
        self._partner_id = None
        self._quantity = None
        self._reserve_end_time = None
        self._reserve_start_time = None
        self._shop_id = None

    @property
    def buyer_phone_number(self):
        return self._buyer_phone_number

    @buyer_phone_number.setter
    def buyer_phone_number(self, value):
        self._buyer_phone_number = value
    @property
    def buyer_user_name(self):
        return self._buyer_user_name

    @buyer_user_name.setter
    def buyer_user_name(self, value):
        self._buyer_user_name = value
    @property
    def craftsman_id(self):
        return self._craftsman_id

    @craftsman_id.setter
    def craftsman_id(self, value):
        self._craftsman_id = value
    @property
    def current_price(self):
        return self._current_price

    @current_price.setter
    def current_price(self, value):
        self._current_price = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def reserve_end_time(self):
        return self._reserve_end_time

    @reserve_end_time.setter
    def reserve_end_time(self, value):
        self._reserve_end_time = value
    @property
    def reserve_start_time(self):
        return self._reserve_start_time

    @reserve_start_time.setter
    def reserve_start_time(self, value):
        self._reserve_start_time = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_phone_number:
            if hasattr(self.buyer_phone_number, 'to_alipay_dict'):
                params['buyer_phone_number'] = self.buyer_phone_number.to_alipay_dict()
            else:
                params['buyer_phone_number'] = self.buyer_phone_number
        if self.buyer_user_name:
            if hasattr(self.buyer_user_name, 'to_alipay_dict'):
                params['buyer_user_name'] = self.buyer_user_name.to_alipay_dict()
            else:
                params['buyer_user_name'] = self.buyer_user_name
        if self.craftsman_id:
            if hasattr(self.craftsman_id, 'to_alipay_dict'):
                params['craftsman_id'] = self.craftsman_id.to_alipay_dict()
            else:
                params['craftsman_id'] = self.craftsman_id
        if self.current_price:
            if hasattr(self.current_price, 'to_alipay_dict'):
                params['current_price'] = self.current_price.to_alipay_dict()
            else:
                params['current_price'] = self.current_price
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.reserve_end_time:
            if hasattr(self.reserve_end_time, 'to_alipay_dict'):
                params['reserve_end_time'] = self.reserve_end_time.to_alipay_dict()
            else:
                params['reserve_end_time'] = self.reserve_end_time
        if self.reserve_start_time:
            if hasattr(self.reserve_start_time, 'to_alipay_dict'):
                params['reserve_start_time'] = self.reserve_start_time.to_alipay_dict()
            else:
                params['reserve_start_time'] = self.reserve_start_time
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiTradeItemBuyModel()
        if 'buyer_phone_number' in d:
            o.buyer_phone_number = d['buyer_phone_number']
        if 'buyer_user_name' in d:
            o.buyer_user_name = d['buyer_user_name']
        if 'craftsman_id' in d:
            o.craftsman_id = d['craftsman_id']
        if 'current_price' in d:
            o.current_price = d['current_price']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'reserve_end_time' in d:
            o.reserve_end_time = d['reserve_end_time']
        if 'reserve_start_time' in d:
            o.reserve_start_time = d['reserve_start_time']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


