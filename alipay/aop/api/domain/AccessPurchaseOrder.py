#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccessPurchaseOrder(object):

    def __init__(self):
        self._apply_date = None
        self._asset_item_id = None
        self._asset_order_id = None
        self._asset_purchase_id = None
        self._city = None
        self._count = None
        self._create_date = None
        self._district = None
        self._is_produce = None
        self._province = None
        self._receiver_address = None
        self._receiver_mobile = None
        self._receiver_name = None
        self._stuff_attr_name = None
        self._stuff_material = None
        self._stuff_size = None
        self._stuff_type = None
        self._template_id = None
        self._template_name = None

    @property
    def apply_date(self):
        return self._apply_date

    @apply_date.setter
    def apply_date(self, value):
        self._apply_date = value
    @property
    def asset_item_id(self):
        return self._asset_item_id

    @asset_item_id.setter
    def asset_item_id(self, value):
        self._asset_item_id = value
    @property
    def asset_order_id(self):
        return self._asset_order_id

    @asset_order_id.setter
    def asset_order_id(self, value):
        self._asset_order_id = value
    @property
    def asset_purchase_id(self):
        return self._asset_purchase_id

    @asset_purchase_id.setter
    def asset_purchase_id(self, value):
        self._asset_purchase_id = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def is_produce(self):
        return self._is_produce

    @is_produce.setter
    def is_produce(self, value):
        self._is_produce = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def receiver_address(self):
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, value):
        self._receiver_address = value
    @property
    def receiver_mobile(self):
        return self._receiver_mobile

    @receiver_mobile.setter
    def receiver_mobile(self, value):
        self._receiver_mobile = value
    @property
    def receiver_name(self):
        return self._receiver_name

    @receiver_name.setter
    def receiver_name(self, value):
        self._receiver_name = value
    @property
    def stuff_attr_name(self):
        return self._stuff_attr_name

    @stuff_attr_name.setter
    def stuff_attr_name(self, value):
        self._stuff_attr_name = value
    @property
    def stuff_material(self):
        return self._stuff_material

    @stuff_material.setter
    def stuff_material(self, value):
        self._stuff_material = value
    @property
    def stuff_size(self):
        return self._stuff_size

    @stuff_size.setter
    def stuff_size(self, value):
        self._stuff_size = value
    @property
    def stuff_type(self):
        return self._stuff_type

    @stuff_type.setter
    def stuff_type(self, value):
        self._stuff_type = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_date:
            if hasattr(self.apply_date, 'to_alipay_dict'):
                params['apply_date'] = self.apply_date.to_alipay_dict()
            else:
                params['apply_date'] = self.apply_date
        if self.asset_item_id:
            if hasattr(self.asset_item_id, 'to_alipay_dict'):
                params['asset_item_id'] = self.asset_item_id.to_alipay_dict()
            else:
                params['asset_item_id'] = self.asset_item_id
        if self.asset_order_id:
            if hasattr(self.asset_order_id, 'to_alipay_dict'):
                params['asset_order_id'] = self.asset_order_id.to_alipay_dict()
            else:
                params['asset_order_id'] = self.asset_order_id
        if self.asset_purchase_id:
            if hasattr(self.asset_purchase_id, 'to_alipay_dict'):
                params['asset_purchase_id'] = self.asset_purchase_id.to_alipay_dict()
            else:
                params['asset_purchase_id'] = self.asset_purchase_id
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.create_date:
            if hasattr(self.create_date, 'to_alipay_dict'):
                params['create_date'] = self.create_date.to_alipay_dict()
            else:
                params['create_date'] = self.create_date
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.is_produce:
            if hasattr(self.is_produce, 'to_alipay_dict'):
                params['is_produce'] = self.is_produce.to_alipay_dict()
            else:
                params['is_produce'] = self.is_produce
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.receiver_address:
            if hasattr(self.receiver_address, 'to_alipay_dict'):
                params['receiver_address'] = self.receiver_address.to_alipay_dict()
            else:
                params['receiver_address'] = self.receiver_address
        if self.receiver_mobile:
            if hasattr(self.receiver_mobile, 'to_alipay_dict'):
                params['receiver_mobile'] = self.receiver_mobile.to_alipay_dict()
            else:
                params['receiver_mobile'] = self.receiver_mobile
        if self.receiver_name:
            if hasattr(self.receiver_name, 'to_alipay_dict'):
                params['receiver_name'] = self.receiver_name.to_alipay_dict()
            else:
                params['receiver_name'] = self.receiver_name
        if self.stuff_attr_name:
            if hasattr(self.stuff_attr_name, 'to_alipay_dict'):
                params['stuff_attr_name'] = self.stuff_attr_name.to_alipay_dict()
            else:
                params['stuff_attr_name'] = self.stuff_attr_name
        if self.stuff_material:
            if hasattr(self.stuff_material, 'to_alipay_dict'):
                params['stuff_material'] = self.stuff_material.to_alipay_dict()
            else:
                params['stuff_material'] = self.stuff_material
        if self.stuff_size:
            if hasattr(self.stuff_size, 'to_alipay_dict'):
                params['stuff_size'] = self.stuff_size.to_alipay_dict()
            else:
                params['stuff_size'] = self.stuff_size
        if self.stuff_type:
            if hasattr(self.stuff_type, 'to_alipay_dict'):
                params['stuff_type'] = self.stuff_type.to_alipay_dict()
            else:
                params['stuff_type'] = self.stuff_type
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccessPurchaseOrder()
        if 'apply_date' in d:
            o.apply_date = d['apply_date']
        if 'asset_item_id' in d:
            o.asset_item_id = d['asset_item_id']
        if 'asset_order_id' in d:
            o.asset_order_id = d['asset_order_id']
        if 'asset_purchase_id' in d:
            o.asset_purchase_id = d['asset_purchase_id']
        if 'city' in d:
            o.city = d['city']
        if 'count' in d:
            o.count = d['count']
        if 'create_date' in d:
            o.create_date = d['create_date']
        if 'district' in d:
            o.district = d['district']
        if 'is_produce' in d:
            o.is_produce = d['is_produce']
        if 'province' in d:
            o.province = d['province']
        if 'receiver_address' in d:
            o.receiver_address = d['receiver_address']
        if 'receiver_mobile' in d:
            o.receiver_mobile = d['receiver_mobile']
        if 'receiver_name' in d:
            o.receiver_name = d['receiver_name']
        if 'stuff_attr_name' in d:
            o.stuff_attr_name = d['stuff_attr_name']
        if 'stuff_material' in d:
            o.stuff_material = d['stuff_material']
        if 'stuff_size' in d:
            o.stuff_size = d['stuff_size']
        if 'stuff_type' in d:
            o.stuff_type = d['stuff_type']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_name' in d:
            o.template_name = d['template_name']
        return o


