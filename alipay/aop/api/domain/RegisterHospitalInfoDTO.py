#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RegisterHospitalInfoDTO(object):

    def __init__(self):
        self._address = None
        self._app_code = None
        self._app_name = None
        self._campus_name = None
        self._campus_type = None
        self._depart_feature = None
        self._department = None
        self._detail_url = None
        self._detail_url_type = None
        self._distance = None
        self._feature = None
        self._hospital_id = None
        self._hospital_introduction = None
        self._hospital_level = None
        self._hospital_logo = None
        self._hospital_name = None
        self._hospital_uniq_code = None
        self._institution_code = None
        self._isv_code = None
        self._latitude = None
        self._longitude = None
        self._platform_code = None
        self._register_flag = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def campus_name(self):
        return self._campus_name

    @campus_name.setter
    def campus_name(self, value):
        self._campus_name = value
    @property
    def campus_type(self):
        return self._campus_type

    @campus_type.setter
    def campus_type(self, value):
        self._campus_type = value
    @property
    def depart_feature(self):
        return self._depart_feature

    @depart_feature.setter
    def depart_feature(self, value):
        if isinstance(value, list):
            self._depart_feature = list()
            for i in value:
                self._depart_feature.append(i)
    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        if isinstance(value, list):
            self._department = list()
            for i in value:
                self._department.append(i)
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def detail_url_type(self):
        return self._detail_url_type

    @detail_url_type.setter
    def detail_url_type(self, value):
        self._detail_url_type = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def feature(self):
        return self._feature

    @feature.setter
    def feature(self, value):
        if isinstance(value, list):
            self._feature = list()
            for i in value:
                self._feature.append(i)
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def hospital_introduction(self):
        return self._hospital_introduction

    @hospital_introduction.setter
    def hospital_introduction(self, value):
        self._hospital_introduction = value
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
    def hospital_uniq_code(self):
        return self._hospital_uniq_code

    @hospital_uniq_code.setter
    def hospital_uniq_code(self, value):
        self._hospital_uniq_code = value
    @property
    def institution_code(self):
        return self._institution_code

    @institution_code.setter
    def institution_code(self, value):
        self._institution_code = value
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
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def register_flag(self):
        return self._register_flag

    @register_flag.setter
    def register_flag(self, value):
        self._register_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.campus_name:
            if hasattr(self.campus_name, 'to_alipay_dict'):
                params['campus_name'] = self.campus_name.to_alipay_dict()
            else:
                params['campus_name'] = self.campus_name
        if self.campus_type:
            if hasattr(self.campus_type, 'to_alipay_dict'):
                params['campus_type'] = self.campus_type.to_alipay_dict()
            else:
                params['campus_type'] = self.campus_type
        if self.depart_feature:
            if isinstance(self.depart_feature, list):
                for i in range(0, len(self.depart_feature)):
                    element = self.depart_feature[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.depart_feature[i] = element.to_alipay_dict()
            if hasattr(self.depart_feature, 'to_alipay_dict'):
                params['depart_feature'] = self.depart_feature.to_alipay_dict()
            else:
                params['depart_feature'] = self.depart_feature
        if self.department:
            if isinstance(self.department, list):
                for i in range(0, len(self.department)):
                    element = self.department[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.department[i] = element.to_alipay_dict()
            if hasattr(self.department, 'to_alipay_dict'):
                params['department'] = self.department.to_alipay_dict()
            else:
                params['department'] = self.department
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.detail_url_type:
            if hasattr(self.detail_url_type, 'to_alipay_dict'):
                params['detail_url_type'] = self.detail_url_type.to_alipay_dict()
            else:
                params['detail_url_type'] = self.detail_url_type
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.feature:
            if isinstance(self.feature, list):
                for i in range(0, len(self.feature)):
                    element = self.feature[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.feature[i] = element.to_alipay_dict()
            if hasattr(self.feature, 'to_alipay_dict'):
                params['feature'] = self.feature.to_alipay_dict()
            else:
                params['feature'] = self.feature
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.hospital_introduction:
            if hasattr(self.hospital_introduction, 'to_alipay_dict'):
                params['hospital_introduction'] = self.hospital_introduction.to_alipay_dict()
            else:
                params['hospital_introduction'] = self.hospital_introduction
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
        if self.hospital_uniq_code:
            if hasattr(self.hospital_uniq_code, 'to_alipay_dict'):
                params['hospital_uniq_code'] = self.hospital_uniq_code.to_alipay_dict()
            else:
                params['hospital_uniq_code'] = self.hospital_uniq_code
        if self.institution_code:
            if hasattr(self.institution_code, 'to_alipay_dict'):
                params['institution_code'] = self.institution_code.to_alipay_dict()
            else:
                params['institution_code'] = self.institution_code
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
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.register_flag:
            if hasattr(self.register_flag, 'to_alipay_dict'):
                params['register_flag'] = self.register_flag.to_alipay_dict()
            else:
                params['register_flag'] = self.register_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RegisterHospitalInfoDTO()
        if 'address' in d:
            o.address = d['address']
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'campus_name' in d:
            o.campus_name = d['campus_name']
        if 'campus_type' in d:
            o.campus_type = d['campus_type']
        if 'depart_feature' in d:
            o.depart_feature = d['depart_feature']
        if 'department' in d:
            o.department = d['department']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'detail_url_type' in d:
            o.detail_url_type = d['detail_url_type']
        if 'distance' in d:
            o.distance = d['distance']
        if 'feature' in d:
            o.feature = d['feature']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'hospital_introduction' in d:
            o.hospital_introduction = d['hospital_introduction']
        if 'hospital_level' in d:
            o.hospital_level = d['hospital_level']
        if 'hospital_logo' in d:
            o.hospital_logo = d['hospital_logo']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'hospital_uniq_code' in d:
            o.hospital_uniq_code = d['hospital_uniq_code']
        if 'institution_code' in d:
            o.institution_code = d['institution_code']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'register_flag' in d:
            o.register_flag = d['register_flag']
        return o


