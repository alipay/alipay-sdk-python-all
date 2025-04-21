#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AttributeBean import AttributeBean
from alipay.aop.api.domain.DiscountSkuBean import DiscountSkuBean
from alipay.aop.api.domain.OriginSkuBean import OriginSkuBean
from alipay.aop.api.domain.SideItemBean import SideItemBean
from alipay.aop.api.domain.SkuBean import SkuBean


class ItemBean(object):

    def __init__(self):
        self._attribute_list = None
        self._description = None
        self._image_url = None
        self._item_discount_sku = None
        self._item_id = None
        self._item_sort = None
        self._menu_id = None
        self._name = None
        self._origin_sku = None
        self._quantity = None
        self._required = None
        self._show_type = None
        self._side_item_list = None
        self._sku_list = None
        self._spec_name = None
        self._thumbnail_url = None

    @property
    def attribute_list(self):
        return self._attribute_list

    @attribute_list.setter
    def attribute_list(self, value):
        if isinstance(value, list):
            self._attribute_list = list()
            for i in value:
                if isinstance(i, AttributeBean):
                    self._attribute_list.append(i)
                else:
                    self._attribute_list.append(AttributeBean.from_alipay_dict(i))
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def item_discount_sku(self):
        return self._item_discount_sku

    @item_discount_sku.setter
    def item_discount_sku(self, value):
        if isinstance(value, DiscountSkuBean):
            self._item_discount_sku = value
        else:
            self._item_discount_sku = DiscountSkuBean.from_alipay_dict(value)
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_sort(self):
        return self._item_sort

    @item_sort.setter
    def item_sort(self, value):
        self._item_sort = value
    @property
    def menu_id(self):
        return self._menu_id

    @menu_id.setter
    def menu_id(self, value):
        self._menu_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def origin_sku(self):
        return self._origin_sku

    @origin_sku.setter
    def origin_sku(self, value):
        if isinstance(value, OriginSkuBean):
            self._origin_sku = value
        else:
            self._origin_sku = OriginSkuBean.from_alipay_dict(value)
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value
    @property
    def show_type(self):
        return self._show_type

    @show_type.setter
    def show_type(self, value):
        self._show_type = value
    @property
    def side_item_list(self):
        return self._side_item_list

    @side_item_list.setter
    def side_item_list(self, value):
        if isinstance(value, list):
            self._side_item_list = list()
            for i in value:
                if isinstance(i, SideItemBean):
                    self._side_item_list.append(i)
                else:
                    self._side_item_list.append(SideItemBean.from_alipay_dict(i))
    @property
    def sku_list(self):
        return self._sku_list

    @sku_list.setter
    def sku_list(self, value):
        if isinstance(value, list):
            self._sku_list = list()
            for i in value:
                if isinstance(i, SkuBean):
                    self._sku_list.append(i)
                else:
                    self._sku_list.append(SkuBean.from_alipay_dict(i))
    @property
    def spec_name(self):
        return self._spec_name

    @spec_name.setter
    def spec_name(self, value):
        self._spec_name = value
    @property
    def thumbnail_url(self):
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, value):
        self._thumbnail_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.attribute_list:
            if isinstance(self.attribute_list, list):
                for i in range(0, len(self.attribute_list)):
                    element = self.attribute_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attribute_list[i] = element.to_alipay_dict()
            if hasattr(self.attribute_list, 'to_alipay_dict'):
                params['attribute_list'] = self.attribute_list.to_alipay_dict()
            else:
                params['attribute_list'] = self.attribute_list
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.item_discount_sku:
            if hasattr(self.item_discount_sku, 'to_alipay_dict'):
                params['item_discount_sku'] = self.item_discount_sku.to_alipay_dict()
            else:
                params['item_discount_sku'] = self.item_discount_sku
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_sort:
            if hasattr(self.item_sort, 'to_alipay_dict'):
                params['item_sort'] = self.item_sort.to_alipay_dict()
            else:
                params['item_sort'] = self.item_sort
        if self.menu_id:
            if hasattr(self.menu_id, 'to_alipay_dict'):
                params['menu_id'] = self.menu_id.to_alipay_dict()
            else:
                params['menu_id'] = self.menu_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.origin_sku:
            if hasattr(self.origin_sku, 'to_alipay_dict'):
                params['origin_sku'] = self.origin_sku.to_alipay_dict()
            else:
                params['origin_sku'] = self.origin_sku
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.required:
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
        if self.show_type:
            if hasattr(self.show_type, 'to_alipay_dict'):
                params['show_type'] = self.show_type.to_alipay_dict()
            else:
                params['show_type'] = self.show_type
        if self.side_item_list:
            if isinstance(self.side_item_list, list):
                for i in range(0, len(self.side_item_list)):
                    element = self.side_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.side_item_list[i] = element.to_alipay_dict()
            if hasattr(self.side_item_list, 'to_alipay_dict'):
                params['side_item_list'] = self.side_item_list.to_alipay_dict()
            else:
                params['side_item_list'] = self.side_item_list
        if self.sku_list:
            if isinstance(self.sku_list, list):
                for i in range(0, len(self.sku_list)):
                    element = self.sku_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_list[i] = element.to_alipay_dict()
            if hasattr(self.sku_list, 'to_alipay_dict'):
                params['sku_list'] = self.sku_list.to_alipay_dict()
            else:
                params['sku_list'] = self.sku_list
        if self.spec_name:
            if hasattr(self.spec_name, 'to_alipay_dict'):
                params['spec_name'] = self.spec_name.to_alipay_dict()
            else:
                params['spec_name'] = self.spec_name
        if self.thumbnail_url:
            if hasattr(self.thumbnail_url, 'to_alipay_dict'):
                params['thumbnail_url'] = self.thumbnail_url.to_alipay_dict()
            else:
                params['thumbnail_url'] = self.thumbnail_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemBean()
        if 'attribute_list' in d:
            o.attribute_list = d['attribute_list']
        if 'description' in d:
            o.description = d['description']
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'item_discount_sku' in d:
            o.item_discount_sku = d['item_discount_sku']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_sort' in d:
            o.item_sort = d['item_sort']
        if 'menu_id' in d:
            o.menu_id = d['menu_id']
        if 'name' in d:
            o.name = d['name']
        if 'origin_sku' in d:
            o.origin_sku = d['origin_sku']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'required' in d:
            o.required = d['required']
        if 'show_type' in d:
            o.show_type = d['show_type']
        if 'side_item_list' in d:
            o.side_item_list = d['side_item_list']
        if 'sku_list' in d:
            o.sku_list = d['sku_list']
        if 'spec_name' in d:
            o.spec_name = d['spec_name']
        if 'thumbnail_url' in d:
            o.thumbnail_url = d['thumbnail_url']
        return o


