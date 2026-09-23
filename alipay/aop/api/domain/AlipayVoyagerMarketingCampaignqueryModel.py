#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoyagerEnvInfo import VoyagerEnvInfo


class AlipayVoyagerMarketingCampaignqueryModel(object):

    def __init__(self):
        self._area_code = None
        self._city_code = None
        self._country_code = None
        self._env_info = None
        self._ext_info = None
        self._latitude = None
        self._locale = None
        self._longitude = None
        self._open_id = None
        self._polymer_block_code = None
        self._user_id = None

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def country_code(self):
        return self._country_code

    @country_code.setter
    def country_code(self, value):
        self._country_code = value
    @property
    def env_info(self):
        return self._env_info

    @env_info.setter
    def env_info(self, value):
        if isinstance(value, VoyagerEnvInfo):
            self._env_info = value
        else:
            self._env_info = VoyagerEnvInfo.from_alipay_dict(value)
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, value):
        self._locale = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def polymer_block_code(self):
        return self._polymer_block_code

    @polymer_block_code.setter
    def polymer_block_code(self, value):
        self._polymer_block_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.country_code:
            if hasattr(self.country_code, 'to_alipay_dict'):
                params['country_code'] = self.country_code.to_alipay_dict()
            else:
                params['country_code'] = self.country_code
        if self.env_info:
            if hasattr(self.env_info, 'to_alipay_dict'):
                params['env_info'] = self.env_info.to_alipay_dict()
            else:
                params['env_info'] = self.env_info
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.locale:
            if hasattr(self.locale, 'to_alipay_dict'):
                params['locale'] = self.locale.to_alipay_dict()
            else:
                params['locale'] = self.locale
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.polymer_block_code:
            if hasattr(self.polymer_block_code, 'to_alipay_dict'):
                params['polymer_block_code'] = self.polymer_block_code.to_alipay_dict()
            else:
                params['polymer_block_code'] = self.polymer_block_code
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
        o = AlipayVoyagerMarketingCampaignqueryModel()
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'country_code' in d:
            o.country_code = d['country_code']
        if 'env_info' in d:
            o.env_info = d['env_info']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'locale' in d:
            o.locale = d['locale']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'polymer_block_code' in d:
            o.polymer_block_code = d['polymer_block_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


