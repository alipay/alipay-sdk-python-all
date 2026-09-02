#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ResaleDeliveryInfoVO(object):

    def __init__(self):
        self._address = None
        self._city_code = None
        self._delivery_status = None
        self._delivery_type = None
        self._district_code = None
        self._logistics_bill_no = None
        self._logistics_platform = None
        self._mobile = None
        self._name = None
        self._province_code = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def delivery_status(self):
        return self._delivery_status

    @delivery_status.setter
    def delivery_status(self, value):
        self._delivery_status = value
    @property
    def delivery_type(self):
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, value):
        self._delivery_type = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def logistics_bill_no(self):
        return self._logistics_bill_no

    @logistics_bill_no.setter
    def logistics_bill_no(self, value):
        self._logistics_bill_no = value
    @property
    def logistics_platform(self):
        return self._logistics_platform

    @logistics_platform.setter
    def logistics_platform(self, value):
        self._logistics_platform = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.delivery_status:
            if hasattr(self.delivery_status, 'to_alipay_dict'):
                params['delivery_status'] = self.delivery_status.to_alipay_dict()
            else:
                params['delivery_status'] = self.delivery_status
        if self.delivery_type:
            if hasattr(self.delivery_type, 'to_alipay_dict'):
                params['delivery_type'] = self.delivery_type.to_alipay_dict()
            else:
                params['delivery_type'] = self.delivery_type
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.logistics_bill_no:
            if hasattr(self.logistics_bill_no, 'to_alipay_dict'):
                params['logistics_bill_no'] = self.logistics_bill_no.to_alipay_dict()
            else:
                params['logistics_bill_no'] = self.logistics_bill_no
        if self.logistics_platform:
            if hasattr(self.logistics_platform, 'to_alipay_dict'):
                params['logistics_platform'] = self.logistics_platform.to_alipay_dict()
            else:
                params['logistics_platform'] = self.logistics_platform
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ResaleDeliveryInfoVO()
        if 'address' in d:
            o.address = d['address']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'delivery_status' in d:
            o.delivery_status = d['delivery_status']
        if 'delivery_type' in d:
            o.delivery_type = d['delivery_type']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'logistics_bill_no' in d:
            o.logistics_bill_no = d['logistics_bill_no']
        if 'logistics_platform' in d:
            o.logistics_platform = d['logistics_platform']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        if 'province_code' in d:
            o.province_code = d['province_code']
        return o


