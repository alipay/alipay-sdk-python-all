#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EbikeBindServiceStatisticsDTO(object):

    def __init__(self):
        self._age_flag = None
        self._bind_user_cnt = None
        self._charge_uv = None
        self._exchange_uv = None
        self._green_energy_uv = None
        self._occupation = None
        self._rent_car_uv = None
        self._scene_vst_uv = None
        self._service_uv = None
        self._user_gender = None

    @property
    def age_flag(self):
        return self._age_flag

    @age_flag.setter
    def age_flag(self, value):
        self._age_flag = value
    @property
    def bind_user_cnt(self):
        return self._bind_user_cnt

    @bind_user_cnt.setter
    def bind_user_cnt(self, value):
        self._bind_user_cnt = value
    @property
    def charge_uv(self):
        return self._charge_uv

    @charge_uv.setter
    def charge_uv(self, value):
        self._charge_uv = value
    @property
    def exchange_uv(self):
        return self._exchange_uv

    @exchange_uv.setter
    def exchange_uv(self, value):
        self._exchange_uv = value
    @property
    def green_energy_uv(self):
        return self._green_energy_uv

    @green_energy_uv.setter
    def green_energy_uv(self, value):
        self._green_energy_uv = value
    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, value):
        self._occupation = value
    @property
    def rent_car_uv(self):
        return self._rent_car_uv

    @rent_car_uv.setter
    def rent_car_uv(self, value):
        self._rent_car_uv = value
    @property
    def scene_vst_uv(self):
        return self._scene_vst_uv

    @scene_vst_uv.setter
    def scene_vst_uv(self, value):
        self._scene_vst_uv = value
    @property
    def service_uv(self):
        return self._service_uv

    @service_uv.setter
    def service_uv(self, value):
        self._service_uv = value
    @property
    def user_gender(self):
        return self._user_gender

    @user_gender.setter
    def user_gender(self, value):
        self._user_gender = value


    def to_alipay_dict(self):
        params = dict()
        if self.age_flag:
            if hasattr(self.age_flag, 'to_alipay_dict'):
                params['age_flag'] = self.age_flag.to_alipay_dict()
            else:
                params['age_flag'] = self.age_flag
        if self.bind_user_cnt:
            if hasattr(self.bind_user_cnt, 'to_alipay_dict'):
                params['bind_user_cnt'] = self.bind_user_cnt.to_alipay_dict()
            else:
                params['bind_user_cnt'] = self.bind_user_cnt
        if self.charge_uv:
            if hasattr(self.charge_uv, 'to_alipay_dict'):
                params['charge_uv'] = self.charge_uv.to_alipay_dict()
            else:
                params['charge_uv'] = self.charge_uv
        if self.exchange_uv:
            if hasattr(self.exchange_uv, 'to_alipay_dict'):
                params['exchange_uv'] = self.exchange_uv.to_alipay_dict()
            else:
                params['exchange_uv'] = self.exchange_uv
        if self.green_energy_uv:
            if hasattr(self.green_energy_uv, 'to_alipay_dict'):
                params['green_energy_uv'] = self.green_energy_uv.to_alipay_dict()
            else:
                params['green_energy_uv'] = self.green_energy_uv
        if self.occupation:
            if hasattr(self.occupation, 'to_alipay_dict'):
                params['occupation'] = self.occupation.to_alipay_dict()
            else:
                params['occupation'] = self.occupation
        if self.rent_car_uv:
            if hasattr(self.rent_car_uv, 'to_alipay_dict'):
                params['rent_car_uv'] = self.rent_car_uv.to_alipay_dict()
            else:
                params['rent_car_uv'] = self.rent_car_uv
        if self.scene_vst_uv:
            if hasattr(self.scene_vst_uv, 'to_alipay_dict'):
                params['scene_vst_uv'] = self.scene_vst_uv.to_alipay_dict()
            else:
                params['scene_vst_uv'] = self.scene_vst_uv
        if self.service_uv:
            if hasattr(self.service_uv, 'to_alipay_dict'):
                params['service_uv'] = self.service_uv.to_alipay_dict()
            else:
                params['service_uv'] = self.service_uv
        if self.user_gender:
            if hasattr(self.user_gender, 'to_alipay_dict'):
                params['user_gender'] = self.user_gender.to_alipay_dict()
            else:
                params['user_gender'] = self.user_gender
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EbikeBindServiceStatisticsDTO()
        if 'age_flag' in d:
            o.age_flag = d['age_flag']
        if 'bind_user_cnt' in d:
            o.bind_user_cnt = d['bind_user_cnt']
        if 'charge_uv' in d:
            o.charge_uv = d['charge_uv']
        if 'exchange_uv' in d:
            o.exchange_uv = d['exchange_uv']
        if 'green_energy_uv' in d:
            o.green_energy_uv = d['green_energy_uv']
        if 'occupation' in d:
            o.occupation = d['occupation']
        if 'rent_car_uv' in d:
            o.rent_car_uv = d['rent_car_uv']
        if 'scene_vst_uv' in d:
            o.scene_vst_uv = d['scene_vst_uv']
        if 'service_uv' in d:
            o.service_uv = d['service_uv']
        if 'user_gender' in d:
            o.user_gender = d['user_gender']
        return o


