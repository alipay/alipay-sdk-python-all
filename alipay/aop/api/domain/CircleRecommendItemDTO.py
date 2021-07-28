#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AoiInfoDTO import AoiInfoDTO
from alipay.aop.api.domain.ItemStoreDTO import ItemStoreDTO


class CircleRecommendItemDTO(object):

    def __init__(self):
        self._aoi_info = None
        self._discount = None
        self._item_cover = None
        self._item_detail_url = None
        self._item_id = None
        self._item_label = None
        self._item_name = None
        self._item_store = None
        self._original_price = None
        self._sales_info = None
        self._saved_money = None
        self._saved_money_info = None
        self._sell_price = None
        self._sold_quantity = None
        self._store_id = None

    @property
    def aoi_info(self):
        return self._aoi_info

    @aoi_info.setter
    def aoi_info(self, value):
        if isinstance(value, AoiInfoDTO):
            self._aoi_info = value
        else:
            self._aoi_info = AoiInfoDTO.from_alipay_dict(value)
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value
    @property
    def item_cover(self):
        return self._item_cover

    @item_cover.setter
    def item_cover(self, value):
        self._item_cover = value
    @property
    def item_detail_url(self):
        return self._item_detail_url

    @item_detail_url.setter
    def item_detail_url(self, value):
        self._item_detail_url = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_label(self):
        return self._item_label

    @item_label.setter
    def item_label(self, value):
        self._item_label = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_store(self):
        return self._item_store

    @item_store.setter
    def item_store(self, value):
        if isinstance(value, ItemStoreDTO):
            self._item_store = value
        else:
            self._item_store = ItemStoreDTO.from_alipay_dict(value)
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def sales_info(self):
        return self._sales_info

    @sales_info.setter
    def sales_info(self, value):
        self._sales_info = value
    @property
    def saved_money(self):
        return self._saved_money

    @saved_money.setter
    def saved_money(self, value):
        self._saved_money = value
    @property
    def saved_money_info(self):
        return self._saved_money_info

    @saved_money_info.setter
    def saved_money_info(self, value):
        self._saved_money_info = value
    @property
    def sell_price(self):
        return self._sell_price

    @sell_price.setter
    def sell_price(self, value):
        self._sell_price = value
    @property
    def sold_quantity(self):
        return self._sold_quantity

    @sold_quantity.setter
    def sold_quantity(self, value):
        self._sold_quantity = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.aoi_info:
            if hasattr(self.aoi_info, 'to_alipay_dict'):
                params['aoi_info'] = self.aoi_info.to_alipay_dict()
            else:
                params['aoi_info'] = self.aoi_info
        if self.discount:
            if hasattr(self.discount, 'to_alipay_dict'):
                params['discount'] = self.discount.to_alipay_dict()
            else:
                params['discount'] = self.discount
        if self.item_cover:
            if hasattr(self.item_cover, 'to_alipay_dict'):
                params['item_cover'] = self.item_cover.to_alipay_dict()
            else:
                params['item_cover'] = self.item_cover
        if self.item_detail_url:
            if hasattr(self.item_detail_url, 'to_alipay_dict'):
                params['item_detail_url'] = self.item_detail_url.to_alipay_dict()
            else:
                params['item_detail_url'] = self.item_detail_url
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_label:
            if hasattr(self.item_label, 'to_alipay_dict'):
                params['item_label'] = self.item_label.to_alipay_dict()
            else:
                params['item_label'] = self.item_label
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_store:
            if hasattr(self.item_store, 'to_alipay_dict'):
                params['item_store'] = self.item_store.to_alipay_dict()
            else:
                params['item_store'] = self.item_store
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.sales_info:
            if hasattr(self.sales_info, 'to_alipay_dict'):
                params['sales_info'] = self.sales_info.to_alipay_dict()
            else:
                params['sales_info'] = self.sales_info
        if self.saved_money:
            if hasattr(self.saved_money, 'to_alipay_dict'):
                params['saved_money'] = self.saved_money.to_alipay_dict()
            else:
                params['saved_money'] = self.saved_money
        if self.saved_money_info:
            if hasattr(self.saved_money_info, 'to_alipay_dict'):
                params['saved_money_info'] = self.saved_money_info.to_alipay_dict()
            else:
                params['saved_money_info'] = self.saved_money_info
        if self.sell_price:
            if hasattr(self.sell_price, 'to_alipay_dict'):
                params['sell_price'] = self.sell_price.to_alipay_dict()
            else:
                params['sell_price'] = self.sell_price
        if self.sold_quantity:
            if hasattr(self.sold_quantity, 'to_alipay_dict'):
                params['sold_quantity'] = self.sold_quantity.to_alipay_dict()
            else:
                params['sold_quantity'] = self.sold_quantity
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CircleRecommendItemDTO()
        if 'aoi_info' in d:
            o.aoi_info = d['aoi_info']
        if 'discount' in d:
            o.discount = d['discount']
        if 'item_cover' in d:
            o.item_cover = d['item_cover']
        if 'item_detail_url' in d:
            o.item_detail_url = d['item_detail_url']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_label' in d:
            o.item_label = d['item_label']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_store' in d:
            o.item_store = d['item_store']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'sales_info' in d:
            o.sales_info = d['sales_info']
        if 'saved_money' in d:
            o.saved_money = d['saved_money']
        if 'saved_money_info' in d:
            o.saved_money_info = d['saved_money_info']
        if 'sell_price' in d:
            o.sell_price = d['sell_price']
        if 'sold_quantity' in d:
            o.sold_quantity = d['sold_quantity']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


