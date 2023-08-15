#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApeItemMaterial(object):

    def __init__(self):
        self._attribute = None
        self._custom = None
        self._goods_detail_pic_list = None
        self._item_id = None
        self._item_name = None
        self._material_pic = None
        self._price_privilege = None

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        self._attribute = value
    @property
    def custom(self):
        return self._custom

    @custom.setter
    def custom(self, value):
        self._custom = value
    @property
    def goods_detail_pic_list(self):
        return self._goods_detail_pic_list

    @goods_detail_pic_list.setter
    def goods_detail_pic_list(self, value):
        if isinstance(value, list):
            self._goods_detail_pic_list = list()
            for i in value:
                self._goods_detail_pic_list.append(i)
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
    def material_pic(self):
        return self._material_pic

    @material_pic.setter
    def material_pic(self, value):
        self._material_pic = value
    @property
    def price_privilege(self):
        return self._price_privilege

    @price_privilege.setter
    def price_privilege(self, value):
        self._price_privilege = value


    def to_alipay_dict(self):
        params = dict()
        if self.attribute:
            if hasattr(self.attribute, 'to_alipay_dict'):
                params['attribute'] = self.attribute.to_alipay_dict()
            else:
                params['attribute'] = self.attribute
        if self.custom:
            if hasattr(self.custom, 'to_alipay_dict'):
                params['custom'] = self.custom.to_alipay_dict()
            else:
                params['custom'] = self.custom
        if self.goods_detail_pic_list:
            if isinstance(self.goods_detail_pic_list, list):
                for i in range(0, len(self.goods_detail_pic_list)):
                    element = self.goods_detail_pic_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_detail_pic_list[i] = element.to_alipay_dict()
            if hasattr(self.goods_detail_pic_list, 'to_alipay_dict'):
                params['goods_detail_pic_list'] = self.goods_detail_pic_list.to_alipay_dict()
            else:
                params['goods_detail_pic_list'] = self.goods_detail_pic_list
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
        if self.material_pic:
            if hasattr(self.material_pic, 'to_alipay_dict'):
                params['material_pic'] = self.material_pic.to_alipay_dict()
            else:
                params['material_pic'] = self.material_pic
        if self.price_privilege:
            if hasattr(self.price_privilege, 'to_alipay_dict'):
                params['price_privilege'] = self.price_privilege.to_alipay_dict()
            else:
                params['price_privilege'] = self.price_privilege
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApeItemMaterial()
        if 'attribute' in d:
            o.attribute = d['attribute']
        if 'custom' in d:
            o.custom = d['custom']
        if 'goods_detail_pic_list' in d:
            o.goods_detail_pic_list = d['goods_detail_pic_list']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'material_pic' in d:
            o.material_pic = d['material_pic']
        if 'price_privilege' in d:
            o.price_privilege = d['price_privilege']
        return o


