#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EffectiveDatesDTO import EffectiveDatesDTO
from alipay.aop.api.domain.RentInfoDTO import RentInfoDTO


class MiniGoodsDetailInfoDTO(object):

    def __init__(self):
        self._body = None
        self._categories_tree = None
        self._effective_dates = None
        self._goods_category = None
        self._goods_id = None
        self._goods_name = None
        self._image_material_id = None
        self._item_cnt = None
        self._item_discount = None
        self._out_item_id = None
        self._out_sku_id = None
        self._platform_item_version_id = None
        self._rent_info = None
        self._sale_price = None
        self._sale_real_price = None
        self._show_url = None

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def categories_tree(self):
        return self._categories_tree

    @categories_tree.setter
    def categories_tree(self, value):
        self._categories_tree = value
    @property
    def effective_dates(self):
        return self._effective_dates

    @effective_dates.setter
    def effective_dates(self, value):
        if isinstance(value, list):
            self._effective_dates = list()
            for i in value:
                if isinstance(i, EffectiveDatesDTO):
                    self._effective_dates.append(i)
                else:
                    self._effective_dates.append(EffectiveDatesDTO.from_alipay_dict(i))
    @property
    def goods_category(self):
        return self._goods_category

    @goods_category.setter
    def goods_category(self, value):
        self._goods_category = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def image_material_id(self):
        return self._image_material_id

    @image_material_id.setter
    def image_material_id(self, value):
        self._image_material_id = value
    @property
    def item_cnt(self):
        return self._item_cnt

    @item_cnt.setter
    def item_cnt(self, value):
        self._item_cnt = value
    @property
    def item_discount(self):
        return self._item_discount

    @item_discount.setter
    def item_discount(self, value):
        self._item_discount = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def platform_item_version_id(self):
        return self._platform_item_version_id

    @platform_item_version_id.setter
    def platform_item_version_id(self, value):
        self._platform_item_version_id = value
    @property
    def rent_info(self):
        return self._rent_info

    @rent_info.setter
    def rent_info(self, value):
        if isinstance(value, RentInfoDTO):
            self._rent_info = value
        else:
            self._rent_info = RentInfoDTO.from_alipay_dict(value)
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def sale_real_price(self):
        return self._sale_real_price

    @sale_real_price.setter
    def sale_real_price(self, value):
        self._sale_real_price = value
    @property
    def show_url(self):
        return self._show_url

    @show_url.setter
    def show_url(self, value):
        self._show_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.categories_tree:
            if hasattr(self.categories_tree, 'to_alipay_dict'):
                params['categories_tree'] = self.categories_tree.to_alipay_dict()
            else:
                params['categories_tree'] = self.categories_tree
        if self.effective_dates:
            if isinstance(self.effective_dates, list):
                for i in range(0, len(self.effective_dates)):
                    element = self.effective_dates[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.effective_dates[i] = element.to_alipay_dict()
            if hasattr(self.effective_dates, 'to_alipay_dict'):
                params['effective_dates'] = self.effective_dates.to_alipay_dict()
            else:
                params['effective_dates'] = self.effective_dates
        if self.goods_category:
            if hasattr(self.goods_category, 'to_alipay_dict'):
                params['goods_category'] = self.goods_category.to_alipay_dict()
            else:
                params['goods_category'] = self.goods_category
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.image_material_id:
            if hasattr(self.image_material_id, 'to_alipay_dict'):
                params['image_material_id'] = self.image_material_id.to_alipay_dict()
            else:
                params['image_material_id'] = self.image_material_id
        if self.item_cnt:
            if hasattr(self.item_cnt, 'to_alipay_dict'):
                params['item_cnt'] = self.item_cnt.to_alipay_dict()
            else:
                params['item_cnt'] = self.item_cnt
        if self.item_discount:
            if hasattr(self.item_discount, 'to_alipay_dict'):
                params['item_discount'] = self.item_discount.to_alipay_dict()
            else:
                params['item_discount'] = self.item_discount
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.platform_item_version_id:
            if hasattr(self.platform_item_version_id, 'to_alipay_dict'):
                params['platform_item_version_id'] = self.platform_item_version_id.to_alipay_dict()
            else:
                params['platform_item_version_id'] = self.platform_item_version_id
        if self.rent_info:
            if hasattr(self.rent_info, 'to_alipay_dict'):
                params['rent_info'] = self.rent_info.to_alipay_dict()
            else:
                params['rent_info'] = self.rent_info
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.sale_real_price:
            if hasattr(self.sale_real_price, 'to_alipay_dict'):
                params['sale_real_price'] = self.sale_real_price.to_alipay_dict()
            else:
                params['sale_real_price'] = self.sale_real_price
        if self.show_url:
            if hasattr(self.show_url, 'to_alipay_dict'):
                params['show_url'] = self.show_url.to_alipay_dict()
            else:
                params['show_url'] = self.show_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniGoodsDetailInfoDTO()
        if 'body' in d:
            o.body = d['body']
        if 'categories_tree' in d:
            o.categories_tree = d['categories_tree']
        if 'effective_dates' in d:
            o.effective_dates = d['effective_dates']
        if 'goods_category' in d:
            o.goods_category = d['goods_category']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'image_material_id' in d:
            o.image_material_id = d['image_material_id']
        if 'item_cnt' in d:
            o.item_cnt = d['item_cnt']
        if 'item_discount' in d:
            o.item_discount = d['item_discount']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'platform_item_version_id' in d:
            o.platform_item_version_id = d['platform_item_version_id']
        if 'rent_info' in d:
            o.rent_info = d['rent_info']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'sale_real_price' in d:
            o.sale_real_price = d['sale_real_price']
        if 'show_url' in d:
            o.show_url = d['show_url']
        return o


