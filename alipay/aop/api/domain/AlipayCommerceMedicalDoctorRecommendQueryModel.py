#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalDoctorRecommendQueryModel(object):

    def __init__(self):
        self._channel_code = None
        self._city_code = None
        self._district_code = None
        self._exclude_doctor_id = None
        self._experiment_name = None
        self._hdf_department_name = None
        self._hdf_disease_name = None
        self._hdf_tag_code = None
        self._limit = None
        self._open_id = None
        self._price = None
        self._province_code = None
        self._scene_code = None
        self._title = None
        self._user_id = None

    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def exclude_doctor_id(self):
        return self._exclude_doctor_id

    @exclude_doctor_id.setter
    def exclude_doctor_id(self, value):
        if isinstance(value, list):
            self._exclude_doctor_id = list()
            for i in value:
                self._exclude_doctor_id.append(i)
    @property
    def experiment_name(self):
        return self._experiment_name

    @experiment_name.setter
    def experiment_name(self, value):
        self._experiment_name = value
    @property
    def hdf_department_name(self):
        return self._hdf_department_name

    @hdf_department_name.setter
    def hdf_department_name(self, value):
        self._hdf_department_name = value
    @property
    def hdf_disease_name(self):
        return self._hdf_disease_name

    @hdf_disease_name.setter
    def hdf_disease_name(self, value):
        self._hdf_disease_name = value
    @property
    def hdf_tag_code(self):
        return self._hdf_tag_code

    @hdf_tag_code.setter
    def hdf_tag_code(self, value):
        if isinstance(value, list):
            self._hdf_tag_code = list()
            for i in value:
                self._hdf_tag_code.append(i)
    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
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
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, list):
            self._title = list()
            for i in value:
                self._title.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.exclude_doctor_id:
            if isinstance(self.exclude_doctor_id, list):
                for i in range(0, len(self.exclude_doctor_id)):
                    element = self.exclude_doctor_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.exclude_doctor_id[i] = element.to_alipay_dict()
            if hasattr(self.exclude_doctor_id, 'to_alipay_dict'):
                params['exclude_doctor_id'] = self.exclude_doctor_id.to_alipay_dict()
            else:
                params['exclude_doctor_id'] = self.exclude_doctor_id
        if self.experiment_name:
            if hasattr(self.experiment_name, 'to_alipay_dict'):
                params['experiment_name'] = self.experiment_name.to_alipay_dict()
            else:
                params['experiment_name'] = self.experiment_name
        if self.hdf_department_name:
            if hasattr(self.hdf_department_name, 'to_alipay_dict'):
                params['hdf_department_name'] = self.hdf_department_name.to_alipay_dict()
            else:
                params['hdf_department_name'] = self.hdf_department_name
        if self.hdf_disease_name:
            if hasattr(self.hdf_disease_name, 'to_alipay_dict'):
                params['hdf_disease_name'] = self.hdf_disease_name.to_alipay_dict()
            else:
                params['hdf_disease_name'] = self.hdf_disease_name
        if self.hdf_tag_code:
            if isinstance(self.hdf_tag_code, list):
                for i in range(0, len(self.hdf_tag_code)):
                    element = self.hdf_tag_code[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hdf_tag_code[i] = element.to_alipay_dict()
            if hasattr(self.hdf_tag_code, 'to_alipay_dict'):
                params['hdf_tag_code'] = self.hdf_tag_code.to_alipay_dict()
            else:
                params['hdf_tag_code'] = self.hdf_tag_code
        if self.limit:
            if hasattr(self.limit, 'to_alipay_dict'):
                params['limit'] = self.limit.to_alipay_dict()
            else:
                params['limit'] = self.limit
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
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
        if self.title:
            if isinstance(self.title, list):
                for i in range(0, len(self.title)):
                    element = self.title[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.title[i] = element.to_alipay_dict()
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalDoctorRecommendQueryModel()
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'exclude_doctor_id' in d:
            o.exclude_doctor_id = d['exclude_doctor_id']
        if 'experiment_name' in d:
            o.experiment_name = d['experiment_name']
        if 'hdf_department_name' in d:
            o.hdf_department_name = d['hdf_department_name']
        if 'hdf_disease_name' in d:
            o.hdf_disease_name = d['hdf_disease_name']
        if 'hdf_tag_code' in d:
            o.hdf_tag_code = d['hdf_tag_code']
        if 'limit' in d:
            o.limit = d['limit']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'price' in d:
            o.price = d['price']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'title' in d:
            o.title = d['title']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


