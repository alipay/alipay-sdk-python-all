#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceItem(object):

    def __init__(self):
        self._advisor_proxy = None
        self._discounted = None
        self._doctor_id = None
        self._free = None
        self._out_sku_id = None
        self._price = None
        self._seller_id = None
        self._service_duration = None
        self._service_duration_unit = None
        self._service_package_item_id = None
        self._sku_id = None
        self._sku_name = None
        self._spu_id = None
        self._store_id = None
        self._sub_package_item_id = None

    @property
    def advisor_proxy(self):
        return self._advisor_proxy

    @advisor_proxy.setter
    def advisor_proxy(self, value):
        self._advisor_proxy = value
    @property
    def discounted(self):
        return self._discounted

    @discounted.setter
    def discounted(self, value):
        self._discounted = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def free(self):
        return self._free

    @free.setter
    def free(self, value):
        self._free = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def service_duration(self):
        return self._service_duration

    @service_duration.setter
    def service_duration(self, value):
        self._service_duration = value
    @property
    def service_duration_unit(self):
        return self._service_duration_unit

    @service_duration_unit.setter
    def service_duration_unit(self, value):
        self._service_duration_unit = value
    @property
    def service_package_item_id(self):
        return self._service_package_item_id

    @service_package_item_id.setter
    def service_package_item_id(self, value):
        self._service_package_item_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sku_name(self):
        return self._sku_name

    @sku_name.setter
    def sku_name(self, value):
        self._sku_name = value
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def sub_package_item_id(self):
        return self._sub_package_item_id

    @sub_package_item_id.setter
    def sub_package_item_id(self, value):
        self._sub_package_item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.advisor_proxy:
            if hasattr(self.advisor_proxy, 'to_alipay_dict'):
                params['advisor_proxy'] = self.advisor_proxy.to_alipay_dict()
            else:
                params['advisor_proxy'] = self.advisor_proxy
        if self.discounted:
            if hasattr(self.discounted, 'to_alipay_dict'):
                params['discounted'] = self.discounted.to_alipay_dict()
            else:
                params['discounted'] = self.discounted
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.free:
            if hasattr(self.free, 'to_alipay_dict'):
                params['free'] = self.free.to_alipay_dict()
            else:
                params['free'] = self.free
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.service_duration:
            if hasattr(self.service_duration, 'to_alipay_dict'):
                params['service_duration'] = self.service_duration.to_alipay_dict()
            else:
                params['service_duration'] = self.service_duration
        if self.service_duration_unit:
            if hasattr(self.service_duration_unit, 'to_alipay_dict'):
                params['service_duration_unit'] = self.service_duration_unit.to_alipay_dict()
            else:
                params['service_duration_unit'] = self.service_duration_unit
        if self.service_package_item_id:
            if hasattr(self.service_package_item_id, 'to_alipay_dict'):
                params['service_package_item_id'] = self.service_package_item_id.to_alipay_dict()
            else:
                params['service_package_item_id'] = self.service_package_item_id
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.sku_name:
            if hasattr(self.sku_name, 'to_alipay_dict'):
                params['sku_name'] = self.sku_name.to_alipay_dict()
            else:
                params['sku_name'] = self.sku_name
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.sub_package_item_id:
            if hasattr(self.sub_package_item_id, 'to_alipay_dict'):
                params['sub_package_item_id'] = self.sub_package_item_id.to_alipay_dict()
            else:
                params['sub_package_item_id'] = self.sub_package_item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceItem()
        if 'advisor_proxy' in d:
            o.advisor_proxy = d['advisor_proxy']
        if 'discounted' in d:
            o.discounted = d['discounted']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'free' in d:
            o.free = d['free']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'price' in d:
            o.price = d['price']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'service_duration' in d:
            o.service_duration = d['service_duration']
        if 'service_duration_unit' in d:
            o.service_duration_unit = d['service_duration_unit']
        if 'service_package_item_id' in d:
            o.service_package_item_id = d['service_package_item_id']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sku_name' in d:
            o.sku_name = d['sku_name']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'sub_package_item_id' in d:
            o.sub_package_item_id = d['sub_package_item_id']
        return o


