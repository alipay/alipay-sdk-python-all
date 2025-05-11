#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandLeadsCreateModel(object):

    def __init__(self):
        self._address = None
        self._brand_id = None
        self._business_license_key = None
        self._city_code = None
        self._contact_phone = None
        self._customer_id = None
        self._device_num = None
        self._device_type = None
        self._district_code = None
        self._isv_pid = None
        self._latitude = None
        self._leads_from_l_1 = None
        self._leads_from_l_2 = None
        self._leads_name = None
        self._longitude = None
        self._mcc_l_1 = None
        self._mcc_l_2 = None
        self._out_biz_id = None
        self._out_door_pic_oss_key = None
        self._province_code = None
        self._scene_code = None
        self._store_id = None
        self._submit_object = None
        self._work_channel = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def business_license_key(self):
        return self._business_license_key

    @business_license_key.setter
    def business_license_key(self, value):
        self._business_license_key = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def device_num(self):
        return self._device_num

    @device_num.setter
    def device_num(self, value):
        self._device_num = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def leads_from_l_1(self):
        return self._leads_from_l_1

    @leads_from_l_1.setter
    def leads_from_l_1(self, value):
        self._leads_from_l_1 = value
    @property
    def leads_from_l_2(self):
        return self._leads_from_l_2

    @leads_from_l_2.setter
    def leads_from_l_2(self, value):
        self._leads_from_l_2 = value
    @property
    def leads_name(self):
        return self._leads_name

    @leads_name.setter
    def leads_name(self, value):
        self._leads_name = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def mcc_l_1(self):
        return self._mcc_l_1

    @mcc_l_1.setter
    def mcc_l_1(self, value):
        self._mcc_l_1 = value
    @property
    def mcc_l_2(self):
        return self._mcc_l_2

    @mcc_l_2.setter
    def mcc_l_2(self, value):
        self._mcc_l_2 = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def out_door_pic_oss_key(self):
        return self._out_door_pic_oss_key

    @out_door_pic_oss_key.setter
    def out_door_pic_oss_key(self, value):
        self._out_door_pic_oss_key = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def submit_object(self):
        return self._submit_object

    @submit_object.setter
    def submit_object(self, value):
        self._submit_object = value
    @property
    def work_channel(self):
        return self._work_channel

    @work_channel.setter
    def work_channel(self, value):
        self._work_channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.business_license_key:
            if hasattr(self.business_license_key, 'to_alipay_dict'):
                params['business_license_key'] = self.business_license_key.to_alipay_dict()
            else:
                params['business_license_key'] = self.business_license_key
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.contact_phone:
            if hasattr(self.contact_phone, 'to_alipay_dict'):
                params['contact_phone'] = self.contact_phone.to_alipay_dict()
            else:
                params['contact_phone'] = self.contact_phone
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.device_num:
            if hasattr(self.device_num, 'to_alipay_dict'):
                params['device_num'] = self.device_num.to_alipay_dict()
            else:
                params['device_num'] = self.device_num
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.leads_from_l_1:
            if hasattr(self.leads_from_l_1, 'to_alipay_dict'):
                params['leads_from_l_1'] = self.leads_from_l_1.to_alipay_dict()
            else:
                params['leads_from_l_1'] = self.leads_from_l_1
        if self.leads_from_l_2:
            if hasattr(self.leads_from_l_2, 'to_alipay_dict'):
                params['leads_from_l_2'] = self.leads_from_l_2.to_alipay_dict()
            else:
                params['leads_from_l_2'] = self.leads_from_l_2
        if self.leads_name:
            if hasattr(self.leads_name, 'to_alipay_dict'):
                params['leads_name'] = self.leads_name.to_alipay_dict()
            else:
                params['leads_name'] = self.leads_name
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.mcc_l_1:
            if hasattr(self.mcc_l_1, 'to_alipay_dict'):
                params['mcc_l_1'] = self.mcc_l_1.to_alipay_dict()
            else:
                params['mcc_l_1'] = self.mcc_l_1
        if self.mcc_l_2:
            if hasattr(self.mcc_l_2, 'to_alipay_dict'):
                params['mcc_l_2'] = self.mcc_l_2.to_alipay_dict()
            else:
                params['mcc_l_2'] = self.mcc_l_2
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.out_door_pic_oss_key:
            if hasattr(self.out_door_pic_oss_key, 'to_alipay_dict'):
                params['out_door_pic_oss_key'] = self.out_door_pic_oss_key.to_alipay_dict()
            else:
                params['out_door_pic_oss_key'] = self.out_door_pic_oss_key
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.submit_object:
            if hasattr(self.submit_object, 'to_alipay_dict'):
                params['submit_object'] = self.submit_object.to_alipay_dict()
            else:
                params['submit_object'] = self.submit_object
        if self.work_channel:
            if hasattr(self.work_channel, 'to_alipay_dict'):
                params['work_channel'] = self.work_channel.to_alipay_dict()
            else:
                params['work_channel'] = self.work_channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandLeadsCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'business_license_key' in d:
            o.business_license_key = d['business_license_key']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'device_num' in d:
            o.device_num = d['device_num']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'leads_from_l_1' in d:
            o.leads_from_l_1 = d['leads_from_l_1']
        if 'leads_from_l_2' in d:
            o.leads_from_l_2 = d['leads_from_l_2']
        if 'leads_name' in d:
            o.leads_name = d['leads_name']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'mcc_l_1' in d:
            o.mcc_l_1 = d['mcc_l_1']
        if 'mcc_l_2' in d:
            o.mcc_l_2 = d['mcc_l_2']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'out_door_pic_oss_key' in d:
            o.out_door_pic_oss_key = d['out_door_pic_oss_key']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'submit_object' in d:
            o.submit_object = d['submit_object']
        if 'work_channel' in d:
            o.work_channel = d['work_channel']
        return o


