#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LocalSettleBillItem(object):

    def __init__(self):
        self._alipay_discount_amount = None
        self._category_name = None
        self._certificate_id = None
        self._certificate_serial_no = None
        self._certificate_status = None
        self._direction_type_en = None
        self._gmt_create = None
        self._item_id = None
        self._item_name = None
        self._mini_app_id = None
        self._mvirtual_amount = None
        self._order_id = None
        self._original_price = None
        self._out_shop_id = None
        self._out_shop_name = None
        self._settle_account_loginid_bank = None
        self._settle_account_type = None
        self._settle_amount = None
        self._settle_batch_no = None
        self._settle_gmt = None
        self._settle_shop_id = None
        self._settle_shop_name = None
        self._total_cash = None
        self._trade_no = None
        self._trade_order_scene_desc = None
        self._use_order_no = None
        self._use_time = None
        self._use_trade_no = None

    @property
    def alipay_discount_amount(self):
        return self._alipay_discount_amount

    @alipay_discount_amount.setter
    def alipay_discount_amount(self, value):
        self._alipay_discount_amount = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def certificate_serial_no(self):
        return self._certificate_serial_no

    @certificate_serial_no.setter
    def certificate_serial_no(self, value):
        self._certificate_serial_no = value
    @property
    def certificate_status(self):
        return self._certificate_status

    @certificate_status.setter
    def certificate_status(self, value):
        self._certificate_status = value
    @property
    def direction_type_en(self):
        return self._direction_type_en

    @direction_type_en.setter
    def direction_type_en(self, value):
        self._direction_type_en = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def mvirtual_amount(self):
        return self._mvirtual_amount

    @mvirtual_amount.setter
    def mvirtual_amount(self, value):
        self._mvirtual_amount = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def out_shop_name(self):
        return self._out_shop_name

    @out_shop_name.setter
    def out_shop_name(self, value):
        self._out_shop_name = value
    @property
    def settle_account_loginid_bank(self):
        return self._settle_account_loginid_bank

    @settle_account_loginid_bank.setter
    def settle_account_loginid_bank(self, value):
        self._settle_account_loginid_bank = value
    @property
    def settle_account_type(self):
        return self._settle_account_type

    @settle_account_type.setter
    def settle_account_type(self, value):
        self._settle_account_type = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        self._settle_amount = value
    @property
    def settle_batch_no(self):
        return self._settle_batch_no

    @settle_batch_no.setter
    def settle_batch_no(self, value):
        self._settle_batch_no = value
    @property
    def settle_gmt(self):
        return self._settle_gmt

    @settle_gmt.setter
    def settle_gmt(self, value):
        self._settle_gmt = value
    @property
    def settle_shop_id(self):
        return self._settle_shop_id

    @settle_shop_id.setter
    def settle_shop_id(self, value):
        self._settle_shop_id = value
    @property
    def settle_shop_name(self):
        return self._settle_shop_name

    @settle_shop_name.setter
    def settle_shop_name(self, value):
        self._settle_shop_name = value
    @property
    def total_cash(self):
        return self._total_cash

    @total_cash.setter
    def total_cash(self, value):
        self._total_cash = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_order_scene_desc(self):
        return self._trade_order_scene_desc

    @trade_order_scene_desc.setter
    def trade_order_scene_desc(self, value):
        self._trade_order_scene_desc = value
    @property
    def use_order_no(self):
        return self._use_order_no

    @use_order_no.setter
    def use_order_no(self, value):
        self._use_order_no = value
    @property
    def use_time(self):
        return self._use_time

    @use_time.setter
    def use_time(self, value):
        self._use_time = value
    @property
    def use_trade_no(self):
        return self._use_trade_no

    @use_trade_no.setter
    def use_trade_no(self, value):
        self._use_trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_discount_amount:
            if hasattr(self.alipay_discount_amount, 'to_alipay_dict'):
                params['alipay_discount_amount'] = self.alipay_discount_amount.to_alipay_dict()
            else:
                params['alipay_discount_amount'] = self.alipay_discount_amount
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.certificate_serial_no:
            if hasattr(self.certificate_serial_no, 'to_alipay_dict'):
                params['certificate_serial_no'] = self.certificate_serial_no.to_alipay_dict()
            else:
                params['certificate_serial_no'] = self.certificate_serial_no
        if self.certificate_status:
            if hasattr(self.certificate_status, 'to_alipay_dict'):
                params['certificate_status'] = self.certificate_status.to_alipay_dict()
            else:
                params['certificate_status'] = self.certificate_status
        if self.direction_type_en:
            if hasattr(self.direction_type_en, 'to_alipay_dict'):
                params['direction_type_en'] = self.direction_type_en.to_alipay_dict()
            else:
                params['direction_type_en'] = self.direction_type_en
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.mvirtual_amount:
            if hasattr(self.mvirtual_amount, 'to_alipay_dict'):
                params['mvirtual_amount'] = self.mvirtual_amount.to_alipay_dict()
            else:
                params['mvirtual_amount'] = self.mvirtual_amount
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.out_shop_name:
            if hasattr(self.out_shop_name, 'to_alipay_dict'):
                params['out_shop_name'] = self.out_shop_name.to_alipay_dict()
            else:
                params['out_shop_name'] = self.out_shop_name
        if self.settle_account_loginid_bank:
            if hasattr(self.settle_account_loginid_bank, 'to_alipay_dict'):
                params['settle_account_loginid_bank'] = self.settle_account_loginid_bank.to_alipay_dict()
            else:
                params['settle_account_loginid_bank'] = self.settle_account_loginid_bank
        if self.settle_account_type:
            if hasattr(self.settle_account_type, 'to_alipay_dict'):
                params['settle_account_type'] = self.settle_account_type.to_alipay_dict()
            else:
                params['settle_account_type'] = self.settle_account_type
        if self.settle_amount:
            if hasattr(self.settle_amount, 'to_alipay_dict'):
                params['settle_amount'] = self.settle_amount.to_alipay_dict()
            else:
                params['settle_amount'] = self.settle_amount
        if self.settle_batch_no:
            if hasattr(self.settle_batch_no, 'to_alipay_dict'):
                params['settle_batch_no'] = self.settle_batch_no.to_alipay_dict()
            else:
                params['settle_batch_no'] = self.settle_batch_no
        if self.settle_gmt:
            if hasattr(self.settle_gmt, 'to_alipay_dict'):
                params['settle_gmt'] = self.settle_gmt.to_alipay_dict()
            else:
                params['settle_gmt'] = self.settle_gmt
        if self.settle_shop_id:
            if hasattr(self.settle_shop_id, 'to_alipay_dict'):
                params['settle_shop_id'] = self.settle_shop_id.to_alipay_dict()
            else:
                params['settle_shop_id'] = self.settle_shop_id
        if self.settle_shop_name:
            if hasattr(self.settle_shop_name, 'to_alipay_dict'):
                params['settle_shop_name'] = self.settle_shop_name.to_alipay_dict()
            else:
                params['settle_shop_name'] = self.settle_shop_name
        if self.total_cash:
            if hasattr(self.total_cash, 'to_alipay_dict'):
                params['total_cash'] = self.total_cash.to_alipay_dict()
            else:
                params['total_cash'] = self.total_cash
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_order_scene_desc:
            if hasattr(self.trade_order_scene_desc, 'to_alipay_dict'):
                params['trade_order_scene_desc'] = self.trade_order_scene_desc.to_alipay_dict()
            else:
                params['trade_order_scene_desc'] = self.trade_order_scene_desc
        if self.use_order_no:
            if hasattr(self.use_order_no, 'to_alipay_dict'):
                params['use_order_no'] = self.use_order_no.to_alipay_dict()
            else:
                params['use_order_no'] = self.use_order_no
        if self.use_time:
            if hasattr(self.use_time, 'to_alipay_dict'):
                params['use_time'] = self.use_time.to_alipay_dict()
            else:
                params['use_time'] = self.use_time
        if self.use_trade_no:
            if hasattr(self.use_trade_no, 'to_alipay_dict'):
                params['use_trade_no'] = self.use_trade_no.to_alipay_dict()
            else:
                params['use_trade_no'] = self.use_trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LocalSettleBillItem()
        if 'alipay_discount_amount' in d:
            o.alipay_discount_amount = d['alipay_discount_amount']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'certificate_serial_no' in d:
            o.certificate_serial_no = d['certificate_serial_no']
        if 'certificate_status' in d:
            o.certificate_status = d['certificate_status']
        if 'direction_type_en' in d:
            o.direction_type_en = d['direction_type_en']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'mvirtual_amount' in d:
            o.mvirtual_amount = d['mvirtual_amount']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'out_shop_name' in d:
            o.out_shop_name = d['out_shop_name']
        if 'settle_account_loginid_bank' in d:
            o.settle_account_loginid_bank = d['settle_account_loginid_bank']
        if 'settle_account_type' in d:
            o.settle_account_type = d['settle_account_type']
        if 'settle_amount' in d:
            o.settle_amount = d['settle_amount']
        if 'settle_batch_no' in d:
            o.settle_batch_no = d['settle_batch_no']
        if 'settle_gmt' in d:
            o.settle_gmt = d['settle_gmt']
        if 'settle_shop_id' in d:
            o.settle_shop_id = d['settle_shop_id']
        if 'settle_shop_name' in d:
            o.settle_shop_name = d['settle_shop_name']
        if 'total_cash' in d:
            o.total_cash = d['total_cash']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_order_scene_desc' in d:
            o.trade_order_scene_desc = d['trade_order_scene_desc']
        if 'use_order_no' in d:
            o.use_order_no = d['use_order_no']
        if 'use_time' in d:
            o.use_time = d['use_time']
        if 'use_trade_no' in d:
            o.use_trade_no = d['use_trade_no']
        return o


