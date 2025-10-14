#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentGoodsDetailInfoDTO(object):

    def __init__(self):
        self._body = None
        self._goods_picture_ids = None
        self._image_material_id = None
        self._imei = None
        self._item_brand = None
        self._item_category = None
        self._item_cnt = None
        self._item_description = None
        self._item_fineness = None
        self._item_fineness_grade = None
        self._item_name = None
        self._item_value = None
        self._out_item_id = None
        self._out_sku_id = None
        self._rent_model = None
        self._sale_price = None
        self._supervised = None

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def goods_picture_ids(self):
        return self._goods_picture_ids

    @goods_picture_ids.setter
    def goods_picture_ids(self, value):
        if isinstance(value, list):
            self._goods_picture_ids = list()
            for i in value:
                self._goods_picture_ids.append(i)
    @property
    def image_material_id(self):
        return self._image_material_id

    @image_material_id.setter
    def image_material_id(self, value):
        self._image_material_id = value
    @property
    def imei(self):
        return self._imei

    @imei.setter
    def imei(self, value):
        self._imei = value
    @property
    def item_brand(self):
        return self._item_brand

    @item_brand.setter
    def item_brand(self, value):
        self._item_brand = value
    @property
    def item_category(self):
        return self._item_category

    @item_category.setter
    def item_category(self, value):
        self._item_category = value
    @property
    def item_cnt(self):
        return self._item_cnt

    @item_cnt.setter
    def item_cnt(self, value):
        self._item_cnt = value
    @property
    def item_description(self):
        return self._item_description

    @item_description.setter
    def item_description(self, value):
        self._item_description = value
    @property
    def item_fineness(self):
        return self._item_fineness

    @item_fineness.setter
    def item_fineness(self, value):
        self._item_fineness = value
    @property
    def item_fineness_grade(self):
        return self._item_fineness_grade

    @item_fineness_grade.setter
    def item_fineness_grade(self, value):
        self._item_fineness_grade = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_value(self):
        return self._item_value

    @item_value.setter
    def item_value(self, value):
        self._item_value = value
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
    def rent_model(self):
        return self._rent_model

    @rent_model.setter
    def rent_model(self, value):
        self._rent_model = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def supervised(self):
        return self._supervised

    @supervised.setter
    def supervised(self, value):
        self._supervised = value


    def to_alipay_dict(self):
        params = dict()
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.goods_picture_ids:
            if isinstance(self.goods_picture_ids, list):
                for i in range(0, len(self.goods_picture_ids)):
                    element = self.goods_picture_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_picture_ids[i] = element.to_alipay_dict()
            if hasattr(self.goods_picture_ids, 'to_alipay_dict'):
                params['goods_picture_ids'] = self.goods_picture_ids.to_alipay_dict()
            else:
                params['goods_picture_ids'] = self.goods_picture_ids
        if self.image_material_id:
            if hasattr(self.image_material_id, 'to_alipay_dict'):
                params['image_material_id'] = self.image_material_id.to_alipay_dict()
            else:
                params['image_material_id'] = self.image_material_id
        if self.imei:
            if hasattr(self.imei, 'to_alipay_dict'):
                params['imei'] = self.imei.to_alipay_dict()
            else:
                params['imei'] = self.imei
        if self.item_brand:
            if hasattr(self.item_brand, 'to_alipay_dict'):
                params['item_brand'] = self.item_brand.to_alipay_dict()
            else:
                params['item_brand'] = self.item_brand
        if self.item_category:
            if hasattr(self.item_category, 'to_alipay_dict'):
                params['item_category'] = self.item_category.to_alipay_dict()
            else:
                params['item_category'] = self.item_category
        if self.item_cnt:
            if hasattr(self.item_cnt, 'to_alipay_dict'):
                params['item_cnt'] = self.item_cnt.to_alipay_dict()
            else:
                params['item_cnt'] = self.item_cnt
        if self.item_description:
            if hasattr(self.item_description, 'to_alipay_dict'):
                params['item_description'] = self.item_description.to_alipay_dict()
            else:
                params['item_description'] = self.item_description
        if self.item_fineness:
            if hasattr(self.item_fineness, 'to_alipay_dict'):
                params['item_fineness'] = self.item_fineness.to_alipay_dict()
            else:
                params['item_fineness'] = self.item_fineness
        if self.item_fineness_grade:
            if hasattr(self.item_fineness_grade, 'to_alipay_dict'):
                params['item_fineness_grade'] = self.item_fineness_grade.to_alipay_dict()
            else:
                params['item_fineness_grade'] = self.item_fineness_grade
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_value:
            if hasattr(self.item_value, 'to_alipay_dict'):
                params['item_value'] = self.item_value.to_alipay_dict()
            else:
                params['item_value'] = self.item_value
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
        if self.rent_model:
            if hasattr(self.rent_model, 'to_alipay_dict'):
                params['rent_model'] = self.rent_model.to_alipay_dict()
            else:
                params['rent_model'] = self.rent_model
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.supervised:
            if hasattr(self.supervised, 'to_alipay_dict'):
                params['supervised'] = self.supervised.to_alipay_dict()
            else:
                params['supervised'] = self.supervised
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentGoodsDetailInfoDTO()
        if 'body' in d:
            o.body = d['body']
        if 'goods_picture_ids' in d:
            o.goods_picture_ids = d['goods_picture_ids']
        if 'image_material_id' in d:
            o.image_material_id = d['image_material_id']
        if 'imei' in d:
            o.imei = d['imei']
        if 'item_brand' in d:
            o.item_brand = d['item_brand']
        if 'item_category' in d:
            o.item_category = d['item_category']
        if 'item_cnt' in d:
            o.item_cnt = d['item_cnt']
        if 'item_description' in d:
            o.item_description = d['item_description']
        if 'item_fineness' in d:
            o.item_fineness = d['item_fineness']
        if 'item_fineness_grade' in d:
            o.item_fineness_grade = d['item_fineness_grade']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_value' in d:
            o.item_value = d['item_value']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'rent_model' in d:
            o.rent_model = d['rent_model']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'supervised' in d:
            o.supervised = d['supervised']
        return o


