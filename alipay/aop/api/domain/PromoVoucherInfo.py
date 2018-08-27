#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromoVoucherInfo(object):

    def __init__(self):
        self._discount = None
        self._is_auto_obtain = None
        self._is_mall_voucher = None
        self._item_brand_name = None
        self._item_gmt_end = None
        self._item_gmt_start = None
        self._item_id = None
        self._item_logo = None
        self._item_name = None
        self._send_item_name = None
        self._shop_id = None
        self._shop_name = None
        self._use_condition_amount = None
        self._value_amount = None
        self._voucher_detail_url = None
        self._voucher_type = None

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value
    @property
    def is_auto_obtain(self):
        return self._is_auto_obtain

    @is_auto_obtain.setter
    def is_auto_obtain(self, value):
        self._is_auto_obtain = value
    @property
    def is_mall_voucher(self):
        return self._is_mall_voucher

    @is_mall_voucher.setter
    def is_mall_voucher(self, value):
        self._is_mall_voucher = value
    @property
    def item_brand_name(self):
        return self._item_brand_name

    @item_brand_name.setter
    def item_brand_name(self, value):
        self._item_brand_name = value
    @property
    def item_gmt_end(self):
        return self._item_gmt_end

    @item_gmt_end.setter
    def item_gmt_end(self, value):
        self._item_gmt_end = value
    @property
    def item_gmt_start(self):
        return self._item_gmt_start

    @item_gmt_start.setter
    def item_gmt_start(self, value):
        self._item_gmt_start = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_logo(self):
        return self._item_logo

    @item_logo.setter
    def item_logo(self, value):
        self._item_logo = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def send_item_name(self):
        return self._send_item_name

    @send_item_name.setter
    def send_item_name(self, value):
        self._send_item_name = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def use_condition_amount(self):
        return self._use_condition_amount

    @use_condition_amount.setter
    def use_condition_amount(self, value):
        self._use_condition_amount = value
    @property
    def value_amount(self):
        return self._value_amount

    @value_amount.setter
    def value_amount(self, value):
        self._value_amount = value
    @property
    def voucher_detail_url(self):
        return self._voucher_detail_url

    @voucher_detail_url.setter
    def voucher_detail_url(self, value):
        self._voucher_detail_url = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount:
            if hasattr(self.discount, 'to_alipay_dict'):
                params['discount'] = self.discount.to_alipay_dict()
            else:
                params['discount'] = self.discount
        if self.is_auto_obtain:
            if hasattr(self.is_auto_obtain, 'to_alipay_dict'):
                params['is_auto_obtain'] = self.is_auto_obtain.to_alipay_dict()
            else:
                params['is_auto_obtain'] = self.is_auto_obtain
        if self.is_mall_voucher:
            if hasattr(self.is_mall_voucher, 'to_alipay_dict'):
                params['is_mall_voucher'] = self.is_mall_voucher.to_alipay_dict()
            else:
                params['is_mall_voucher'] = self.is_mall_voucher
        if self.item_brand_name:
            if hasattr(self.item_brand_name, 'to_alipay_dict'):
                params['item_brand_name'] = self.item_brand_name.to_alipay_dict()
            else:
                params['item_brand_name'] = self.item_brand_name
        if self.item_gmt_end:
            if hasattr(self.item_gmt_end, 'to_alipay_dict'):
                params['item_gmt_end'] = self.item_gmt_end.to_alipay_dict()
            else:
                params['item_gmt_end'] = self.item_gmt_end
        if self.item_gmt_start:
            if hasattr(self.item_gmt_start, 'to_alipay_dict'):
                params['item_gmt_start'] = self.item_gmt_start.to_alipay_dict()
            else:
                params['item_gmt_start'] = self.item_gmt_start
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_logo:
            if hasattr(self.item_logo, 'to_alipay_dict'):
                params['item_logo'] = self.item_logo.to_alipay_dict()
            else:
                params['item_logo'] = self.item_logo
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.send_item_name:
            if hasattr(self.send_item_name, 'to_alipay_dict'):
                params['send_item_name'] = self.send_item_name.to_alipay_dict()
            else:
                params['send_item_name'] = self.send_item_name
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.use_condition_amount:
            if hasattr(self.use_condition_amount, 'to_alipay_dict'):
                params['use_condition_amount'] = self.use_condition_amount.to_alipay_dict()
            else:
                params['use_condition_amount'] = self.use_condition_amount
        if self.value_amount:
            if hasattr(self.value_amount, 'to_alipay_dict'):
                params['value_amount'] = self.value_amount.to_alipay_dict()
            else:
                params['value_amount'] = self.value_amount
        if self.voucher_detail_url:
            if hasattr(self.voucher_detail_url, 'to_alipay_dict'):
                params['voucher_detail_url'] = self.voucher_detail_url.to_alipay_dict()
            else:
                params['voucher_detail_url'] = self.voucher_detail_url
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoVoucherInfo()
        if 'discount' in d:
            o.discount = d['discount']
        if 'is_auto_obtain' in d:
            o.is_auto_obtain = d['is_auto_obtain']
        if 'is_mall_voucher' in d:
            o.is_mall_voucher = d['is_mall_voucher']
        if 'item_brand_name' in d:
            o.item_brand_name = d['item_brand_name']
        if 'item_gmt_end' in d:
            o.item_gmt_end = d['item_gmt_end']
        if 'item_gmt_start' in d:
            o.item_gmt_start = d['item_gmt_start']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_logo' in d:
            o.item_logo = d['item_logo']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'send_item_name' in d:
            o.send_item_name = d['send_item_name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'use_condition_amount' in d:
            o.use_condition_amount = d['use_condition_amount']
        if 'value_amount' in d:
            o.value_amount = d['value_amount']
        if 'voucher_detail_url' in d:
            o.voucher_detail_url = d['voucher_detail_url']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


