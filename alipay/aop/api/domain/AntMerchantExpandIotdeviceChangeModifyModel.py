#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandIotdeviceChangeModifyModel(object):

    def __init__(self):
        self._device_sn = None
        self._gmt_created = None
        self._order_id = None
        self._policy_type = None
        self._settled_alipay_id = None
        self._shop_address = None
        self._shop_city = None
        self._shop_district = None
        self._shop_industry = None
        self._shop_latitude = None
        self._shop_linkman_mobile = None
        self._shop_linkman_name = None
        self._shop_longitude = None
        self._shop_name = None
        self._shop_open_time = None
        self._shop_province = None
        self._signed_alipay_id = None
        self._supplier_sn = None

    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def gmt_created(self):
        return self._gmt_created

    @gmt_created.setter
    def gmt_created(self, value):
        self._gmt_created = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def policy_type(self):
        return self._policy_type

    @policy_type.setter
    def policy_type(self, value):
        self._policy_type = value
    @property
    def settled_alipay_id(self):
        return self._settled_alipay_id

    @settled_alipay_id.setter
    def settled_alipay_id(self, value):
        self._settled_alipay_id = value
    @property
    def shop_address(self):
        return self._shop_address

    @shop_address.setter
    def shop_address(self, value):
        self._shop_address = value
    @property
    def shop_city(self):
        return self._shop_city

    @shop_city.setter
    def shop_city(self, value):
        self._shop_city = value
    @property
    def shop_district(self):
        return self._shop_district

    @shop_district.setter
    def shop_district(self, value):
        self._shop_district = value
    @property
    def shop_industry(self):
        return self._shop_industry

    @shop_industry.setter
    def shop_industry(self, value):
        self._shop_industry = value
    @property
    def shop_latitude(self):
        return self._shop_latitude

    @shop_latitude.setter
    def shop_latitude(self, value):
        self._shop_latitude = value
    @property
    def shop_linkman_mobile(self):
        return self._shop_linkman_mobile

    @shop_linkman_mobile.setter
    def shop_linkman_mobile(self, value):
        self._shop_linkman_mobile = value
    @property
    def shop_linkman_name(self):
        return self._shop_linkman_name

    @shop_linkman_name.setter
    def shop_linkman_name(self, value):
        self._shop_linkman_name = value
    @property
    def shop_longitude(self):
        return self._shop_longitude

    @shop_longitude.setter
    def shop_longitude(self, value):
        self._shop_longitude = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_open_time(self):
        return self._shop_open_time

    @shop_open_time.setter
    def shop_open_time(self, value):
        self._shop_open_time = value
    @property
    def shop_province(self):
        return self._shop_province

    @shop_province.setter
    def shop_province(self, value):
        self._shop_province = value
    @property
    def signed_alipay_id(self):
        return self._signed_alipay_id

    @signed_alipay_id.setter
    def signed_alipay_id(self, value):
        self._signed_alipay_id = value
    @property
    def supplier_sn(self):
        return self._supplier_sn

    @supplier_sn.setter
    def supplier_sn(self, value):
        self._supplier_sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.gmt_created:
            if hasattr(self.gmt_created, 'to_alipay_dict'):
                params['gmt_created'] = self.gmt_created.to_alipay_dict()
            else:
                params['gmt_created'] = self.gmt_created
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.policy_type:
            if hasattr(self.policy_type, 'to_alipay_dict'):
                params['policy_type'] = self.policy_type.to_alipay_dict()
            else:
                params['policy_type'] = self.policy_type
        if self.settled_alipay_id:
            if hasattr(self.settled_alipay_id, 'to_alipay_dict'):
                params['settled_alipay_id'] = self.settled_alipay_id.to_alipay_dict()
            else:
                params['settled_alipay_id'] = self.settled_alipay_id
        if self.shop_address:
            if hasattr(self.shop_address, 'to_alipay_dict'):
                params['shop_address'] = self.shop_address.to_alipay_dict()
            else:
                params['shop_address'] = self.shop_address
        if self.shop_city:
            if hasattr(self.shop_city, 'to_alipay_dict'):
                params['shop_city'] = self.shop_city.to_alipay_dict()
            else:
                params['shop_city'] = self.shop_city
        if self.shop_district:
            if hasattr(self.shop_district, 'to_alipay_dict'):
                params['shop_district'] = self.shop_district.to_alipay_dict()
            else:
                params['shop_district'] = self.shop_district
        if self.shop_industry:
            if hasattr(self.shop_industry, 'to_alipay_dict'):
                params['shop_industry'] = self.shop_industry.to_alipay_dict()
            else:
                params['shop_industry'] = self.shop_industry
        if self.shop_latitude:
            if hasattr(self.shop_latitude, 'to_alipay_dict'):
                params['shop_latitude'] = self.shop_latitude.to_alipay_dict()
            else:
                params['shop_latitude'] = self.shop_latitude
        if self.shop_linkman_mobile:
            if hasattr(self.shop_linkman_mobile, 'to_alipay_dict'):
                params['shop_linkman_mobile'] = self.shop_linkman_mobile.to_alipay_dict()
            else:
                params['shop_linkman_mobile'] = self.shop_linkman_mobile
        if self.shop_linkman_name:
            if hasattr(self.shop_linkman_name, 'to_alipay_dict'):
                params['shop_linkman_name'] = self.shop_linkman_name.to_alipay_dict()
            else:
                params['shop_linkman_name'] = self.shop_linkman_name
        if self.shop_longitude:
            if hasattr(self.shop_longitude, 'to_alipay_dict'):
                params['shop_longitude'] = self.shop_longitude.to_alipay_dict()
            else:
                params['shop_longitude'] = self.shop_longitude
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_open_time:
            if hasattr(self.shop_open_time, 'to_alipay_dict'):
                params['shop_open_time'] = self.shop_open_time.to_alipay_dict()
            else:
                params['shop_open_time'] = self.shop_open_time
        if self.shop_province:
            if hasattr(self.shop_province, 'to_alipay_dict'):
                params['shop_province'] = self.shop_province.to_alipay_dict()
            else:
                params['shop_province'] = self.shop_province
        if self.signed_alipay_id:
            if hasattr(self.signed_alipay_id, 'to_alipay_dict'):
                params['signed_alipay_id'] = self.signed_alipay_id.to_alipay_dict()
            else:
                params['signed_alipay_id'] = self.signed_alipay_id
        if self.supplier_sn:
            if hasattr(self.supplier_sn, 'to_alipay_dict'):
                params['supplier_sn'] = self.supplier_sn.to_alipay_dict()
            else:
                params['supplier_sn'] = self.supplier_sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIotdeviceChangeModifyModel()
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'gmt_created' in d:
            o.gmt_created = d['gmt_created']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'policy_type' in d:
            o.policy_type = d['policy_type']
        if 'settled_alipay_id' in d:
            o.settled_alipay_id = d['settled_alipay_id']
        if 'shop_address' in d:
            o.shop_address = d['shop_address']
        if 'shop_city' in d:
            o.shop_city = d['shop_city']
        if 'shop_district' in d:
            o.shop_district = d['shop_district']
        if 'shop_industry' in d:
            o.shop_industry = d['shop_industry']
        if 'shop_latitude' in d:
            o.shop_latitude = d['shop_latitude']
        if 'shop_linkman_mobile' in d:
            o.shop_linkman_mobile = d['shop_linkman_mobile']
        if 'shop_linkman_name' in d:
            o.shop_linkman_name = d['shop_linkman_name']
        if 'shop_longitude' in d:
            o.shop_longitude = d['shop_longitude']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_open_time' in d:
            o.shop_open_time = d['shop_open_time']
        if 'shop_province' in d:
            o.shop_province = d['shop_province']
        if 'signed_alipay_id' in d:
            o.signed_alipay_id = d['signed_alipay_id']
        if 'supplier_sn' in d:
            o.supplier_sn = d['supplier_sn']
        return o


