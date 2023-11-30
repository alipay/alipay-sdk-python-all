#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcomItemExtendDetailDTO import EcomItemExtendDetailDTO


class EcomItemDTO(object):

    def __init__(self):
        self._alipay_item_id = None
        self._buyout_money = None
        self._cat_order_count = None
        self._cat_order_refund_exchange_rate = None
        self._item_condition = None
        self._item_detail = None
        self._item_id = None
        self._item_model = None
        self._item_pict_url = None
        self._item_price = None
        self._item_title = None
        self._item_value = None
        self._leaf_cat_id = None
        self._leaf_cat_name = None
        self._root_cat_id = None
        self._root_cat_name = None
        self._sku_amount = None
        self._sku_max_price = None
        self._sku_min_price = None

    @property
    def alipay_item_id(self):
        return self._alipay_item_id

    @alipay_item_id.setter
    def alipay_item_id(self, value):
        self._alipay_item_id = value
    @property
    def buyout_money(self):
        return self._buyout_money

    @buyout_money.setter
    def buyout_money(self, value):
        self._buyout_money = value
    @property
    def cat_order_count(self):
        return self._cat_order_count

    @cat_order_count.setter
    def cat_order_count(self, value):
        self._cat_order_count = value
    @property
    def cat_order_refund_exchange_rate(self):
        return self._cat_order_refund_exchange_rate

    @cat_order_refund_exchange_rate.setter
    def cat_order_refund_exchange_rate(self, value):
        self._cat_order_refund_exchange_rate = value
    @property
    def item_condition(self):
        return self._item_condition

    @item_condition.setter
    def item_condition(self, value):
        self._item_condition = value
    @property
    def item_detail(self):
        return self._item_detail

    @item_detail.setter
    def item_detail(self, value):
        if isinstance(value, EcomItemExtendDetailDTO):
            self._item_detail = value
        else:
            self._item_detail = EcomItemExtendDetailDTO.from_alipay_dict(value)
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_model(self):
        return self._item_model

    @item_model.setter
    def item_model(self, value):
        self._item_model = value
    @property
    def item_pict_url(self):
        return self._item_pict_url

    @item_pict_url.setter
    def item_pict_url(self, value):
        self._item_pict_url = value
    @property
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, value):
        self._item_price = value
    @property
    def item_title(self):
        return self._item_title

    @item_title.setter
    def item_title(self, value):
        self._item_title = value
    @property
    def item_value(self):
        return self._item_value

    @item_value.setter
    def item_value(self, value):
        self._item_value = value
    @property
    def leaf_cat_id(self):
        return self._leaf_cat_id

    @leaf_cat_id.setter
    def leaf_cat_id(self, value):
        self._leaf_cat_id = value
    @property
    def leaf_cat_name(self):
        return self._leaf_cat_name

    @leaf_cat_name.setter
    def leaf_cat_name(self, value):
        self._leaf_cat_name = value
    @property
    def root_cat_id(self):
        return self._root_cat_id

    @root_cat_id.setter
    def root_cat_id(self, value):
        self._root_cat_id = value
    @property
    def root_cat_name(self):
        return self._root_cat_name

    @root_cat_name.setter
    def root_cat_name(self, value):
        self._root_cat_name = value
    @property
    def sku_amount(self):
        return self._sku_amount

    @sku_amount.setter
    def sku_amount(self, value):
        self._sku_amount = value
    @property
    def sku_max_price(self):
        return self._sku_max_price

    @sku_max_price.setter
    def sku_max_price(self, value):
        self._sku_max_price = value
    @property
    def sku_min_price(self):
        return self._sku_min_price

    @sku_min_price.setter
    def sku_min_price(self, value):
        self._sku_min_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_item_id:
            if hasattr(self.alipay_item_id, 'to_alipay_dict'):
                params['alipay_item_id'] = self.alipay_item_id.to_alipay_dict()
            else:
                params['alipay_item_id'] = self.alipay_item_id
        if self.buyout_money:
            if hasattr(self.buyout_money, 'to_alipay_dict'):
                params['buyout_money'] = self.buyout_money.to_alipay_dict()
            else:
                params['buyout_money'] = self.buyout_money
        if self.cat_order_count:
            if hasattr(self.cat_order_count, 'to_alipay_dict'):
                params['cat_order_count'] = self.cat_order_count.to_alipay_dict()
            else:
                params['cat_order_count'] = self.cat_order_count
        if self.cat_order_refund_exchange_rate:
            if hasattr(self.cat_order_refund_exchange_rate, 'to_alipay_dict'):
                params['cat_order_refund_exchange_rate'] = self.cat_order_refund_exchange_rate.to_alipay_dict()
            else:
                params['cat_order_refund_exchange_rate'] = self.cat_order_refund_exchange_rate
        if self.item_condition:
            if hasattr(self.item_condition, 'to_alipay_dict'):
                params['item_condition'] = self.item_condition.to_alipay_dict()
            else:
                params['item_condition'] = self.item_condition
        if self.item_detail:
            if hasattr(self.item_detail, 'to_alipay_dict'):
                params['item_detail'] = self.item_detail.to_alipay_dict()
            else:
                params['item_detail'] = self.item_detail
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_model:
            if hasattr(self.item_model, 'to_alipay_dict'):
                params['item_model'] = self.item_model.to_alipay_dict()
            else:
                params['item_model'] = self.item_model
        if self.item_pict_url:
            if hasattr(self.item_pict_url, 'to_alipay_dict'):
                params['item_pict_url'] = self.item_pict_url.to_alipay_dict()
            else:
                params['item_pict_url'] = self.item_pict_url
        if self.item_price:
            if hasattr(self.item_price, 'to_alipay_dict'):
                params['item_price'] = self.item_price.to_alipay_dict()
            else:
                params['item_price'] = self.item_price
        if self.item_title:
            if hasattr(self.item_title, 'to_alipay_dict'):
                params['item_title'] = self.item_title.to_alipay_dict()
            else:
                params['item_title'] = self.item_title
        if self.item_value:
            if hasattr(self.item_value, 'to_alipay_dict'):
                params['item_value'] = self.item_value.to_alipay_dict()
            else:
                params['item_value'] = self.item_value
        if self.leaf_cat_id:
            if hasattr(self.leaf_cat_id, 'to_alipay_dict'):
                params['leaf_cat_id'] = self.leaf_cat_id.to_alipay_dict()
            else:
                params['leaf_cat_id'] = self.leaf_cat_id
        if self.leaf_cat_name:
            if hasattr(self.leaf_cat_name, 'to_alipay_dict'):
                params['leaf_cat_name'] = self.leaf_cat_name.to_alipay_dict()
            else:
                params['leaf_cat_name'] = self.leaf_cat_name
        if self.root_cat_id:
            if hasattr(self.root_cat_id, 'to_alipay_dict'):
                params['root_cat_id'] = self.root_cat_id.to_alipay_dict()
            else:
                params['root_cat_id'] = self.root_cat_id
        if self.root_cat_name:
            if hasattr(self.root_cat_name, 'to_alipay_dict'):
                params['root_cat_name'] = self.root_cat_name.to_alipay_dict()
            else:
                params['root_cat_name'] = self.root_cat_name
        if self.sku_amount:
            if hasattr(self.sku_amount, 'to_alipay_dict'):
                params['sku_amount'] = self.sku_amount.to_alipay_dict()
            else:
                params['sku_amount'] = self.sku_amount
        if self.sku_max_price:
            if hasattr(self.sku_max_price, 'to_alipay_dict'):
                params['sku_max_price'] = self.sku_max_price.to_alipay_dict()
            else:
                params['sku_max_price'] = self.sku_max_price
        if self.sku_min_price:
            if hasattr(self.sku_min_price, 'to_alipay_dict'):
                params['sku_min_price'] = self.sku_min_price.to_alipay_dict()
            else:
                params['sku_min_price'] = self.sku_min_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcomItemDTO()
        if 'alipay_item_id' in d:
            o.alipay_item_id = d['alipay_item_id']
        if 'buyout_money' in d:
            o.buyout_money = d['buyout_money']
        if 'cat_order_count' in d:
            o.cat_order_count = d['cat_order_count']
        if 'cat_order_refund_exchange_rate' in d:
            o.cat_order_refund_exchange_rate = d['cat_order_refund_exchange_rate']
        if 'item_condition' in d:
            o.item_condition = d['item_condition']
        if 'item_detail' in d:
            o.item_detail = d['item_detail']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_model' in d:
            o.item_model = d['item_model']
        if 'item_pict_url' in d:
            o.item_pict_url = d['item_pict_url']
        if 'item_price' in d:
            o.item_price = d['item_price']
        if 'item_title' in d:
            o.item_title = d['item_title']
        if 'item_value' in d:
            o.item_value = d['item_value']
        if 'leaf_cat_id' in d:
            o.leaf_cat_id = d['leaf_cat_id']
        if 'leaf_cat_name' in d:
            o.leaf_cat_name = d['leaf_cat_name']
        if 'root_cat_id' in d:
            o.root_cat_id = d['root_cat_id']
        if 'root_cat_name' in d:
            o.root_cat_name = d['root_cat_name']
        if 'sku_amount' in d:
            o.sku_amount = d['sku_amount']
        if 'sku_max_price' in d:
            o.sku_max_price = d['sku_max_price']
        if 'sku_min_price' in d:
            o.sku_min_price = d['sku_min_price']
        return o


