#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopServiceItem import ShopServiceItem
from alipay.aop.api.domain.ServiceTimeInfo import ServiceTimeInfo
from alipay.aop.api.domain.ShopStaffInfo import ShopStaffInfo


class AntMerchantExpandStoreShopserviceModifyModel(object):

    def __init__(self):
        self._is_valid = None
        self._name = None
        self._notify_phone = None
        self._out_biz_no = None
        self._service_desc = None
        self._service_items = None
        self._service_time = None
        self._shop_id = None
        self._shop_service_id = None
        self._shop_staffs = None
        self._sku_id = None
        self._store_open_id = None

    @property
    def is_valid(self):
        return self._is_valid

    @is_valid.setter
    def is_valid(self, value):
        self._is_valid = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def notify_phone(self):
        return self._notify_phone

    @notify_phone.setter
    def notify_phone(self, value):
        self._notify_phone = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def service_desc(self):
        return self._service_desc

    @service_desc.setter
    def service_desc(self, value):
        self._service_desc = value
    @property
    def service_items(self):
        return self._service_items

    @service_items.setter
    def service_items(self, value):
        if isinstance(value, list):
            self._service_items = list()
            for i in value:
                if isinstance(i, ShopServiceItem):
                    self._service_items.append(i)
                else:
                    self._service_items.append(ShopServiceItem.from_alipay_dict(i))
    @property
    def service_time(self):
        return self._service_time

    @service_time.setter
    def service_time(self, value):
        if isinstance(value, ServiceTimeInfo):
            self._service_time = value
        else:
            self._service_time = ServiceTimeInfo.from_alipay_dict(value)
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_service_id(self):
        return self._shop_service_id

    @shop_service_id.setter
    def shop_service_id(self, value):
        self._shop_service_id = value
    @property
    def shop_staffs(self):
        return self._shop_staffs

    @shop_staffs.setter
    def shop_staffs(self, value):
        if isinstance(value, list):
            self._shop_staffs = list()
            for i in value:
                if isinstance(i, ShopStaffInfo):
                    self._shop_staffs.append(i)
                else:
                    self._shop_staffs.append(ShopStaffInfo.from_alipay_dict(i))
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def store_open_id(self):
        return self._store_open_id

    @store_open_id.setter
    def store_open_id(self, value):
        self._store_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_valid:
            if hasattr(self.is_valid, 'to_alipay_dict'):
                params['is_valid'] = self.is_valid.to_alipay_dict()
            else:
                params['is_valid'] = self.is_valid
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.notify_phone:
            if hasattr(self.notify_phone, 'to_alipay_dict'):
                params['notify_phone'] = self.notify_phone.to_alipay_dict()
            else:
                params['notify_phone'] = self.notify_phone
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.service_desc:
            if hasattr(self.service_desc, 'to_alipay_dict'):
                params['service_desc'] = self.service_desc.to_alipay_dict()
            else:
                params['service_desc'] = self.service_desc
        if self.service_items:
            if isinstance(self.service_items, list):
                for i in range(0, len(self.service_items)):
                    element = self.service_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_items[i] = element.to_alipay_dict()
            if hasattr(self.service_items, 'to_alipay_dict'):
                params['service_items'] = self.service_items.to_alipay_dict()
            else:
                params['service_items'] = self.service_items
        if self.service_time:
            if hasattr(self.service_time, 'to_alipay_dict'):
                params['service_time'] = self.service_time.to_alipay_dict()
            else:
                params['service_time'] = self.service_time
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_service_id:
            if hasattr(self.shop_service_id, 'to_alipay_dict'):
                params['shop_service_id'] = self.shop_service_id.to_alipay_dict()
            else:
                params['shop_service_id'] = self.shop_service_id
        if self.shop_staffs:
            if isinstance(self.shop_staffs, list):
                for i in range(0, len(self.shop_staffs)):
                    element = self.shop_staffs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_staffs[i] = element.to_alipay_dict()
            if hasattr(self.shop_staffs, 'to_alipay_dict'):
                params['shop_staffs'] = self.shop_staffs.to_alipay_dict()
            else:
                params['shop_staffs'] = self.shop_staffs
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.store_open_id:
            if hasattr(self.store_open_id, 'to_alipay_dict'):
                params['store_open_id'] = self.store_open_id.to_alipay_dict()
            else:
                params['store_open_id'] = self.store_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandStoreShopserviceModifyModel()
        if 'is_valid' in d:
            o.is_valid = d['is_valid']
        if 'name' in d:
            o.name = d['name']
        if 'notify_phone' in d:
            o.notify_phone = d['notify_phone']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'service_desc' in d:
            o.service_desc = d['service_desc']
        if 'service_items' in d:
            o.service_items = d['service_items']
        if 'service_time' in d:
            o.service_time = d['service_time']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_service_id' in d:
            o.shop_service_id = d['shop_service_id']
        if 'shop_staffs' in d:
            o.shop_staffs = d['shop_staffs']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'store_open_id' in d:
            o.store_open_id = d['store_open_id']
        return o


