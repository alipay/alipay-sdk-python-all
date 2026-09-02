#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInquiryHospitalSyncModel(object):

    def __init__(self):
        self._campus_type = None
        self._city_code = None
        self._city_name = None
        self._data_version = None
        self._district_code = None
        self._district_name = None
        self._hospital_address = None
        self._hospital_category = None
        self._hospital_id = None
        self._hospital_introduce = None
        self._hospital_level = None
        self._hospital_logo = None
        self._hospital_name = None
        self._hospital_status = None
        self._hospital_telephone = None
        self._hospital_type = None
        self._isv_code = None
        self._latitude = None
        self._longitude = None
        self._org_id = None
        self._platform_code = None
        self._province_code = None
        self._province_name = None
        self._special = None

    @property
    def campus_type(self):
        return self._campus_type

    @campus_type.setter
    def campus_type(self, value):
        self._campus_type = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def data_version(self):
        return self._data_version

    @data_version.setter
    def data_version(self, value):
        self._data_version = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def district_name(self):
        return self._district_name

    @district_name.setter
    def district_name(self, value):
        self._district_name = value
    @property
    def hospital_address(self):
        return self._hospital_address

    @hospital_address.setter
    def hospital_address(self, value):
        self._hospital_address = value
    @property
    def hospital_category(self):
        return self._hospital_category

    @hospital_category.setter
    def hospital_category(self, value):
        self._hospital_category = value
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def hospital_introduce(self):
        return self._hospital_introduce

    @hospital_introduce.setter
    def hospital_introduce(self, value):
        self._hospital_introduce = value
    @property
    def hospital_level(self):
        return self._hospital_level

    @hospital_level.setter
    def hospital_level(self, value):
        self._hospital_level = value
    @property
    def hospital_logo(self):
        return self._hospital_logo

    @hospital_logo.setter
    def hospital_logo(self, value):
        self._hospital_logo = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def hospital_status(self):
        return self._hospital_status

    @hospital_status.setter
    def hospital_status(self, value):
        self._hospital_status = value
    @property
    def hospital_telephone(self):
        return self._hospital_telephone

    @hospital_telephone.setter
    def hospital_telephone(self, value):
        self._hospital_telephone = value
    @property
    def hospital_type(self):
        return self._hospital_type

    @hospital_type.setter
    def hospital_type(self, value):
        self._hospital_type = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def special(self):
        return self._special

    @special.setter
    def special(self, value):
        self._special = value


    def to_alipay_dict(self):
        params = dict()
        if self.campus_type:
            if hasattr(self.campus_type, 'to_alipay_dict'):
                params['campus_type'] = self.campus_type.to_alipay_dict()
            else:
                params['campus_type'] = self.campus_type
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.data_version:
            if hasattr(self.data_version, 'to_alipay_dict'):
                params['data_version'] = self.data_version.to_alipay_dict()
            else:
                params['data_version'] = self.data_version
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.district_name:
            if hasattr(self.district_name, 'to_alipay_dict'):
                params['district_name'] = self.district_name.to_alipay_dict()
            else:
                params['district_name'] = self.district_name
        if self.hospital_address:
            if hasattr(self.hospital_address, 'to_alipay_dict'):
                params['hospital_address'] = self.hospital_address.to_alipay_dict()
            else:
                params['hospital_address'] = self.hospital_address
        if self.hospital_category:
            if hasattr(self.hospital_category, 'to_alipay_dict'):
                params['hospital_category'] = self.hospital_category.to_alipay_dict()
            else:
                params['hospital_category'] = self.hospital_category
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.hospital_introduce:
            if hasattr(self.hospital_introduce, 'to_alipay_dict'):
                params['hospital_introduce'] = self.hospital_introduce.to_alipay_dict()
            else:
                params['hospital_introduce'] = self.hospital_introduce
        if self.hospital_level:
            if hasattr(self.hospital_level, 'to_alipay_dict'):
                params['hospital_level'] = self.hospital_level.to_alipay_dict()
            else:
                params['hospital_level'] = self.hospital_level
        if self.hospital_logo:
            if hasattr(self.hospital_logo, 'to_alipay_dict'):
                params['hospital_logo'] = self.hospital_logo.to_alipay_dict()
            else:
                params['hospital_logo'] = self.hospital_logo
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.hospital_status:
            if hasattr(self.hospital_status, 'to_alipay_dict'):
                params['hospital_status'] = self.hospital_status.to_alipay_dict()
            else:
                params['hospital_status'] = self.hospital_status
        if self.hospital_telephone:
            if hasattr(self.hospital_telephone, 'to_alipay_dict'):
                params['hospital_telephone'] = self.hospital_telephone.to_alipay_dict()
            else:
                params['hospital_telephone'] = self.hospital_telephone
        if self.hospital_type:
            if hasattr(self.hospital_type, 'to_alipay_dict'):
                params['hospital_type'] = self.hospital_type.to_alipay_dict()
            else:
                params['hospital_type'] = self.hospital_type
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.special:
            if hasattr(self.special, 'to_alipay_dict'):
                params['special'] = self.special.to_alipay_dict()
            else:
                params['special'] = self.special
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInquiryHospitalSyncModel()
        if 'campus_type' in d:
            o.campus_type = d['campus_type']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'data_version' in d:
            o.data_version = d['data_version']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'district_name' in d:
            o.district_name = d['district_name']
        if 'hospital_address' in d:
            o.hospital_address = d['hospital_address']
        if 'hospital_category' in d:
            o.hospital_category = d['hospital_category']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'hospital_introduce' in d:
            o.hospital_introduce = d['hospital_introduce']
        if 'hospital_level' in d:
            o.hospital_level = d['hospital_level']
        if 'hospital_logo' in d:
            o.hospital_logo = d['hospital_logo']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'hospital_status' in d:
            o.hospital_status = d['hospital_status']
        if 'hospital_telephone' in d:
            o.hospital_telephone = d['hospital_telephone']
        if 'hospital_type' in d:
            o.hospital_type = d['hospital_type']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'special' in d:
            o.special = d['special']
        return o


