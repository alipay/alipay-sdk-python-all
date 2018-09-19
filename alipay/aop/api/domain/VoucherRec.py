#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherRec(object):

    def __init__(self):
        self._all_keep_count = None
        self._code = None
        self._cover = None
        self._crowds = None
        self._discount = None
        self._ext_info = None
        self._has_crowd = None
        self._is_auto_obtain = None
        self._is_mall_voucher = None
        self._item_brand_name = None
        self._item_gmt_end = None
        self._item_gmt_start = None
        self._item_id = None
        self._item_name = None
        self._item_quantity = None
        self._item_sales_mode = None
        self._item_sold_quantity = None
        self._original_amount = None
        self._per_value_amount = None
        self._picture_details = None
        self._price_mode = None
        self._purchase_mode = None
        self._send_item_name = None
        self._shop_id = None
        self._shop_name = None
        self._threshold_amount = None
        self._use_condition_amount = None
        self._valid_times = None
        self._value_amount = None
        self._voucher_detail_url = None
        self._voucher_logo_url = None
        self._voucher_type = None

    @property
    def all_keep_count(self):
        return self._all_keep_count

    @all_keep_count.setter
    def all_keep_count(self, value):
        self._all_keep_count = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def cover(self):
        return self._cover

    @cover.setter
    def cover(self, value):
        self._cover = value
    @property
    def crowds(self):
        return self._crowds

    @crowds.setter
    def crowds(self, value):
        self._crowds = value
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def has_crowd(self):
        return self._has_crowd

    @has_crowd.setter
    def has_crowd(self, value):
        self._has_crowd = value
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
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_quantity(self):
        return self._item_quantity

    @item_quantity.setter
    def item_quantity(self, value):
        self._item_quantity = value
    @property
    def item_sales_mode(self):
        return self._item_sales_mode

    @item_sales_mode.setter
    def item_sales_mode(self, value):
        self._item_sales_mode = value
    @property
    def item_sold_quantity(self):
        return self._item_sold_quantity

    @item_sold_quantity.setter
    def item_sold_quantity(self, value):
        self._item_sold_quantity = value
    @property
    def original_amount(self):
        return self._original_amount

    @original_amount.setter
    def original_amount(self, value):
        self._original_amount = value
    @property
    def per_value_amount(self):
        return self._per_value_amount

    @per_value_amount.setter
    def per_value_amount(self, value):
        self._per_value_amount = value
    @property
    def picture_details(self):
        return self._picture_details

    @picture_details.setter
    def picture_details(self, value):
        self._picture_details = value
    @property
    def price_mode(self):
        return self._price_mode

    @price_mode.setter
    def price_mode(self, value):
        self._price_mode = value
    @property
    def purchase_mode(self):
        return self._purchase_mode

    @purchase_mode.setter
    def purchase_mode(self, value):
        self._purchase_mode = value
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
    def threshold_amount(self):
        return self._threshold_amount

    @threshold_amount.setter
    def threshold_amount(self, value):
        self._threshold_amount = value
    @property
    def use_condition_amount(self):
        return self._use_condition_amount

    @use_condition_amount.setter
    def use_condition_amount(self, value):
        self._use_condition_amount = value
    @property
    def valid_times(self):
        return self._valid_times

    @valid_times.setter
    def valid_times(self, value):
        self._valid_times = value
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
    def voucher_logo_url(self):
        return self._voucher_logo_url

    @voucher_logo_url.setter
    def voucher_logo_url(self, value):
        self._voucher_logo_url = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.all_keep_count:
            if hasattr(self.all_keep_count, 'to_alipay_dict'):
                params['all_keep_count'] = self.all_keep_count.to_alipay_dict()
            else:
                params['all_keep_count'] = self.all_keep_count
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.cover:
            if hasattr(self.cover, 'to_alipay_dict'):
                params['cover'] = self.cover.to_alipay_dict()
            else:
                params['cover'] = self.cover
        if self.crowds:
            if hasattr(self.crowds, 'to_alipay_dict'):
                params['crowds'] = self.crowds.to_alipay_dict()
            else:
                params['crowds'] = self.crowds
        if self.discount:
            if hasattr(self.discount, 'to_alipay_dict'):
                params['discount'] = self.discount.to_alipay_dict()
            else:
                params['discount'] = self.discount
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.has_crowd:
            if hasattr(self.has_crowd, 'to_alipay_dict'):
                params['has_crowd'] = self.has_crowd.to_alipay_dict()
            else:
                params['has_crowd'] = self.has_crowd
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
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_quantity:
            if hasattr(self.item_quantity, 'to_alipay_dict'):
                params['item_quantity'] = self.item_quantity.to_alipay_dict()
            else:
                params['item_quantity'] = self.item_quantity
        if self.item_sales_mode:
            if hasattr(self.item_sales_mode, 'to_alipay_dict'):
                params['item_sales_mode'] = self.item_sales_mode.to_alipay_dict()
            else:
                params['item_sales_mode'] = self.item_sales_mode
        if self.item_sold_quantity:
            if hasattr(self.item_sold_quantity, 'to_alipay_dict'):
                params['item_sold_quantity'] = self.item_sold_quantity.to_alipay_dict()
            else:
                params['item_sold_quantity'] = self.item_sold_quantity
        if self.original_amount:
            if hasattr(self.original_amount, 'to_alipay_dict'):
                params['original_amount'] = self.original_amount.to_alipay_dict()
            else:
                params['original_amount'] = self.original_amount
        if self.per_value_amount:
            if hasattr(self.per_value_amount, 'to_alipay_dict'):
                params['per_value_amount'] = self.per_value_amount.to_alipay_dict()
            else:
                params['per_value_amount'] = self.per_value_amount
        if self.picture_details:
            if hasattr(self.picture_details, 'to_alipay_dict'):
                params['picture_details'] = self.picture_details.to_alipay_dict()
            else:
                params['picture_details'] = self.picture_details
        if self.price_mode:
            if hasattr(self.price_mode, 'to_alipay_dict'):
                params['price_mode'] = self.price_mode.to_alipay_dict()
            else:
                params['price_mode'] = self.price_mode
        if self.purchase_mode:
            if hasattr(self.purchase_mode, 'to_alipay_dict'):
                params['purchase_mode'] = self.purchase_mode.to_alipay_dict()
            else:
                params['purchase_mode'] = self.purchase_mode
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
        if self.threshold_amount:
            if hasattr(self.threshold_amount, 'to_alipay_dict'):
                params['threshold_amount'] = self.threshold_amount.to_alipay_dict()
            else:
                params['threshold_amount'] = self.threshold_amount
        if self.use_condition_amount:
            if hasattr(self.use_condition_amount, 'to_alipay_dict'):
                params['use_condition_amount'] = self.use_condition_amount.to_alipay_dict()
            else:
                params['use_condition_amount'] = self.use_condition_amount
        if self.valid_times:
            if hasattr(self.valid_times, 'to_alipay_dict'):
                params['valid_times'] = self.valid_times.to_alipay_dict()
            else:
                params['valid_times'] = self.valid_times
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
        if self.voucher_logo_url:
            if hasattr(self.voucher_logo_url, 'to_alipay_dict'):
                params['voucher_logo_url'] = self.voucher_logo_url.to_alipay_dict()
            else:
                params['voucher_logo_url'] = self.voucher_logo_url
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
        o = VoucherRec()
        if 'all_keep_count' in d:
            o.all_keep_count = d['all_keep_count']
        if 'code' in d:
            o.code = d['code']
        if 'cover' in d:
            o.cover = d['cover']
        if 'crowds' in d:
            o.crowds = d['crowds']
        if 'discount' in d:
            o.discount = d['discount']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'has_crowd' in d:
            o.has_crowd = d['has_crowd']
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
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_quantity' in d:
            o.item_quantity = d['item_quantity']
        if 'item_sales_mode' in d:
            o.item_sales_mode = d['item_sales_mode']
        if 'item_sold_quantity' in d:
            o.item_sold_quantity = d['item_sold_quantity']
        if 'original_amount' in d:
            o.original_amount = d['original_amount']
        if 'per_value_amount' in d:
            o.per_value_amount = d['per_value_amount']
        if 'picture_details' in d:
            o.picture_details = d['picture_details']
        if 'price_mode' in d:
            o.price_mode = d['price_mode']
        if 'purchase_mode' in d:
            o.purchase_mode = d['purchase_mode']
        if 'send_item_name' in d:
            o.send_item_name = d['send_item_name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'threshold_amount' in d:
            o.threshold_amount = d['threshold_amount']
        if 'use_condition_amount' in d:
            o.use_condition_amount = d['use_condition_amount']
        if 'valid_times' in d:
            o.valid_times = d['valid_times']
        if 'value_amount' in d:
            o.value_amount = d['value_amount']
        if 'voucher_detail_url' in d:
            o.voucher_detail_url = d['voucher_detail_url']
        if 'voucher_logo_url' in d:
            o.voucher_logo_url = d['voucher_logo_url']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


