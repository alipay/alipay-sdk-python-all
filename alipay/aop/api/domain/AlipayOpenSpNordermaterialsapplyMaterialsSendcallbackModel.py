#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CallBackMaterialsInfo import CallBackMaterialsInfo


class AlipayOpenSpNordermaterialsapplyMaterialsSendcallbackModel(object):

    def __init__(self):
        self._apply_id = None
        self._area = None
        self._city = None
        self._detail_address = None
        self._materials_info = None
        self._merchant_name = None
        self._order_app_id = None
        self._province = None
        self._rebate_pid = None
        self._shop_id = None
        self._shop_name = None
        self._shop_order_no = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def detail_address(self):
        return self._detail_address

    @detail_address.setter
    def detail_address(self, value):
        self._detail_address = value
    @property
    def materials_info(self):
        return self._materials_info

    @materials_info.setter
    def materials_info(self, value):
        if isinstance(value, list):
            self._materials_info = list()
            for i in value:
                if isinstance(i, CallBackMaterialsInfo):
                    self._materials_info.append(i)
                else:
                    self._materials_info.append(CallBackMaterialsInfo.from_alipay_dict(i))
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def order_app_id(self):
        return self._order_app_id

    @order_app_id.setter
    def order_app_id(self, value):
        self._order_app_id = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def rebate_pid(self):
        return self._rebate_pid

    @rebate_pid.setter
    def rebate_pid(self, value):
        self._rebate_pid = value
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
    def shop_order_no(self):
        return self._shop_order_no

    @shop_order_no.setter
    def shop_order_no(self, value):
        self._shop_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.area:
            if hasattr(self.area, 'to_alipay_dict'):
                params['area'] = self.area.to_alipay_dict()
            else:
                params['area'] = self.area
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.detail_address:
            if hasattr(self.detail_address, 'to_alipay_dict'):
                params['detail_address'] = self.detail_address.to_alipay_dict()
            else:
                params['detail_address'] = self.detail_address
        if self.materials_info:
            if isinstance(self.materials_info, list):
                for i in range(0, len(self.materials_info)):
                    element = self.materials_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.materials_info[i] = element.to_alipay_dict()
            if hasattr(self.materials_info, 'to_alipay_dict'):
                params['materials_info'] = self.materials_info.to_alipay_dict()
            else:
                params['materials_info'] = self.materials_info
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.order_app_id:
            if hasattr(self.order_app_id, 'to_alipay_dict'):
                params['order_app_id'] = self.order_app_id.to_alipay_dict()
            else:
                params['order_app_id'] = self.order_app_id
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.rebate_pid:
            if hasattr(self.rebate_pid, 'to_alipay_dict'):
                params['rebate_pid'] = self.rebate_pid.to_alipay_dict()
            else:
                params['rebate_pid'] = self.rebate_pid
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
        if self.shop_order_no:
            if hasattr(self.shop_order_no, 'to_alipay_dict'):
                params['shop_order_no'] = self.shop_order_no.to_alipay_dict()
            else:
                params['shop_order_no'] = self.shop_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNordermaterialsapplyMaterialsSendcallbackModel()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'area' in d:
            o.area = d['area']
        if 'city' in d:
            o.city = d['city']
        if 'detail_address' in d:
            o.detail_address = d['detail_address']
        if 'materials_info' in d:
            o.materials_info = d['materials_info']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'order_app_id' in d:
            o.order_app_id = d['order_app_id']
        if 'province' in d:
            o.province = d['province']
        if 'rebate_pid' in d:
            o.rebate_pid = d['rebate_pid']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_order_no' in d:
            o.shop_order_no = d['shop_order_no']
        return o


