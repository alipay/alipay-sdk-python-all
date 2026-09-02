#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BsBillDetail(object):

    def __init__(self):
        self._address = None
        self._biz_time = None
        self._brand_name = None
        self._city_name = None
        self._device_sn = None
        self._digital_poi_name = None
        self._discount_amount = None
        self._district_name = None
        self._goods_id = None
        self._goods_name = None
        self._goods_num = None
        self._merchant_name = None
        self._order_id = None
        self._order_no = None
        self._order_subsidy_amount = None
        self._plan_name = None
        self._province_name = None
        self._status = None
        self._unit_amount = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def digital_poi_name(self):
        return self._digital_poi_name

    @digital_poi_name.setter
    def digital_poi_name(self, value):
        self._digital_poi_name = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def district_name(self):
        return self._district_name

    @district_name.setter
    def district_name(self, value):
        self._district_name = value
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
    def goods_num(self):
        return self._goods_num

    @goods_num.setter
    def goods_num(self, value):
        self._goods_num = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_subsidy_amount(self):
        return self._order_subsidy_amount

    @order_subsidy_amount.setter
    def order_subsidy_amount(self, value):
        self._order_subsidy_amount = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def unit_amount(self):
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, value):
        self._unit_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.digital_poi_name:
            if hasattr(self.digital_poi_name, 'to_alipay_dict'):
                params['digital_poi_name'] = self.digital_poi_name.to_alipay_dict()
            else:
                params['digital_poi_name'] = self.digital_poi_name
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.district_name:
            if hasattr(self.district_name, 'to_alipay_dict'):
                params['district_name'] = self.district_name.to_alipay_dict()
            else:
                params['district_name'] = self.district_name
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
        if self.goods_num:
            if hasattr(self.goods_num, 'to_alipay_dict'):
                params['goods_num'] = self.goods_num.to_alipay_dict()
            else:
                params['goods_num'] = self.goods_num
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_subsidy_amount:
            if hasattr(self.order_subsidy_amount, 'to_alipay_dict'):
                params['order_subsidy_amount'] = self.order_subsidy_amount.to_alipay_dict()
            else:
                params['order_subsidy_amount'] = self.order_subsidy_amount
        if self.plan_name:
            if hasattr(self.plan_name, 'to_alipay_dict'):
                params['plan_name'] = self.plan_name.to_alipay_dict()
            else:
                params['plan_name'] = self.plan_name
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.unit_amount:
            if hasattr(self.unit_amount, 'to_alipay_dict'):
                params['unit_amount'] = self.unit_amount.to_alipay_dict()
            else:
                params['unit_amount'] = self.unit_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BsBillDetail()
        if 'address' in d:
            o.address = d['address']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'digital_poi_name' in d:
            o.digital_poi_name = d['digital_poi_name']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'district_name' in d:
            o.district_name = d['district_name']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'goods_num' in d:
            o.goods_num = d['goods_num']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_subsidy_amount' in d:
            o.order_subsidy_amount = d['order_subsidy_amount']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'status' in d:
            o.status = d['status']
        if 'unit_amount' in d:
            o.unit_amount = d['unit_amount']
        return o


