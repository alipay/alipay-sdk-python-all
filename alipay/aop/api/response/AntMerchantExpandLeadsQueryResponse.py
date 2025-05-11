#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandLeadsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandLeadsQueryResponse, self).__init__()
        self._address = None
        self._brand_id = None
        self._business_license_key = None
        self._city_code = None
        self._contact_phone = None
        self._customer_id = None
        self._device_num = None
        self._device_sn_list = None
        self._device_type = None
        self._district_code = None
        self._isv_pid = None
        self._latitude = None
        self._leads_from_l_1 = None
        self._leads_from_l_2 = None
        self._leads_id = None
        self._leads_name = None
        self._leads_status = None
        self._longitude = None
        self._mcc_l_1 = None
        self._mcc_l_2 = None
        self._out_door_pic_oss_key = None
        self._province_code = None
        self._scene_code = None
        self._store_id = None
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
    def device_sn_list(self):
        return self._device_sn_list

    @device_sn_list.setter
    def device_sn_list(self, value):
        if isinstance(value, list):
            self._device_sn_list = list()
            for i in value:
                self._device_sn_list.append(i)
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
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
    @property
    def leads_name(self):
        return self._leads_name

    @leads_name.setter
    def leads_name(self, value):
        self._leads_name = value
    @property
    def leads_status(self):
        return self._leads_status

    @leads_status.setter
    def leads_status(self, value):
        self._leads_status = value
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
    def work_channel(self):
        return self._work_channel

    @work_channel.setter
    def work_channel(self, value):
        self._work_channel = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandLeadsQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'brand_id' in response:
            self.brand_id = response['brand_id']
        if 'business_license_key' in response:
            self.business_license_key = response['business_license_key']
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'contact_phone' in response:
            self.contact_phone = response['contact_phone']
        if 'customer_id' in response:
            self.customer_id = response['customer_id']
        if 'device_num' in response:
            self.device_num = response['device_num']
        if 'device_sn_list' in response:
            self.device_sn_list = response['device_sn_list']
        if 'device_type' in response:
            self.device_type = response['device_type']
        if 'district_code' in response:
            self.district_code = response['district_code']
        if 'isv_pid' in response:
            self.isv_pid = response['isv_pid']
        if 'latitude' in response:
            self.latitude = response['latitude']
        if 'leads_from_l_1' in response:
            self.leads_from_l_1 = response['leads_from_l_1']
        if 'leads_from_l_2' in response:
            self.leads_from_l_2 = response['leads_from_l_2']
        if 'leads_id' in response:
            self.leads_id = response['leads_id']
        if 'leads_name' in response:
            self.leads_name = response['leads_name']
        if 'leads_status' in response:
            self.leads_status = response['leads_status']
        if 'longitude' in response:
            self.longitude = response['longitude']
        if 'mcc_l_1' in response:
            self.mcc_l_1 = response['mcc_l_1']
        if 'mcc_l_2' in response:
            self.mcc_l_2 = response['mcc_l_2']
        if 'out_door_pic_oss_key' in response:
            self.out_door_pic_oss_key = response['out_door_pic_oss_key']
        if 'province_code' in response:
            self.province_code = response['province_code']
        if 'scene_code' in response:
            self.scene_code = response['scene_code']
        if 'store_id' in response:
            self.store_id = response['store_id']
        if 'work_channel' in response:
            self.work_channel = response['work_channel']
