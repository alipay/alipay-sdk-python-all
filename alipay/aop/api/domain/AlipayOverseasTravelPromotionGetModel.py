#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTravelPromotionGetModel(object):

    def __init__(self):
        self._biz_area_codes = None
        self._ch_info = None
        self._city_codes = None
        self._country_codes = None
        self._latitude = None
        self._lbs_reverse_level = None
        self._longitude = None
        self._page_no = None
        self._page_size = None
        self._radius = None
        self._scene_code = None
        self._shop_id = None
        self._top_promotion_ids = None
        self._unique_id = None
        self._user_id = None
        self._user_id_type = None

    @property
    def biz_area_codes(self):
        return self._biz_area_codes

    @biz_area_codes.setter
    def biz_area_codes(self, value):
        if isinstance(value, list):
            self._biz_area_codes = list()
            for i in value:
                self._biz_area_codes.append(i)
    @property
    def ch_info(self):
        return self._ch_info

    @ch_info.setter
    def ch_info(self, value):
        self._ch_info = value
    @property
    def city_codes(self):
        return self._city_codes

    @city_codes.setter
    def city_codes(self, value):
        if isinstance(value, list):
            self._city_codes = list()
            for i in value:
                self._city_codes.append(i)
    @property
    def country_codes(self):
        return self._country_codes

    @country_codes.setter
    def country_codes(self, value):
        if isinstance(value, list):
            self._country_codes = list()
            for i in value:
                self._country_codes.append(i)
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def lbs_reverse_level(self):
        return self._lbs_reverse_level

    @lbs_reverse_level.setter
    def lbs_reverse_level(self, value):
        self._lbs_reverse_level = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def top_promotion_ids(self):
        return self._top_promotion_ids

    @top_promotion_ids.setter
    def top_promotion_ids(self, value):
        if isinstance(value, list):
            self._top_promotion_ids = list()
            for i in value:
                self._top_promotion_ids.append(i)
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_id_type(self):
        return self._user_id_type

    @user_id_type.setter
    def user_id_type(self, value):
        self._user_id_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_area_codes:
            if isinstance(self.biz_area_codes, list):
                for i in range(0, len(self.biz_area_codes)):
                    element = self.biz_area_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_area_codes[i] = element.to_alipay_dict()
            if hasattr(self.biz_area_codes, 'to_alipay_dict'):
                params['biz_area_codes'] = self.biz_area_codes.to_alipay_dict()
            else:
                params['biz_area_codes'] = self.biz_area_codes
        if self.ch_info:
            if hasattr(self.ch_info, 'to_alipay_dict'):
                params['ch_info'] = self.ch_info.to_alipay_dict()
            else:
                params['ch_info'] = self.ch_info
        if self.city_codes:
            if isinstance(self.city_codes, list):
                for i in range(0, len(self.city_codes)):
                    element = self.city_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.city_codes[i] = element.to_alipay_dict()
            if hasattr(self.city_codes, 'to_alipay_dict'):
                params['city_codes'] = self.city_codes.to_alipay_dict()
            else:
                params['city_codes'] = self.city_codes
        if self.country_codes:
            if isinstance(self.country_codes, list):
                for i in range(0, len(self.country_codes)):
                    element = self.country_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.country_codes[i] = element.to_alipay_dict()
            if hasattr(self.country_codes, 'to_alipay_dict'):
                params['country_codes'] = self.country_codes.to_alipay_dict()
            else:
                params['country_codes'] = self.country_codes
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.lbs_reverse_level:
            if hasattr(self.lbs_reverse_level, 'to_alipay_dict'):
                params['lbs_reverse_level'] = self.lbs_reverse_level.to_alipay_dict()
            else:
                params['lbs_reverse_level'] = self.lbs_reverse_level
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.radius:
            if hasattr(self.radius, 'to_alipay_dict'):
                params['radius'] = self.radius.to_alipay_dict()
            else:
                params['radius'] = self.radius
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.top_promotion_ids:
            if isinstance(self.top_promotion_ids, list):
                for i in range(0, len(self.top_promotion_ids)):
                    element = self.top_promotion_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.top_promotion_ids[i] = element.to_alipay_dict()
            if hasattr(self.top_promotion_ids, 'to_alipay_dict'):
                params['top_promotion_ids'] = self.top_promotion_ids.to_alipay_dict()
            else:
                params['top_promotion_ids'] = self.top_promotion_ids
        if self.unique_id:
            if hasattr(self.unique_id, 'to_alipay_dict'):
                params['unique_id'] = self.unique_id.to_alipay_dict()
            else:
                params['unique_id'] = self.unique_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_id_type:
            if hasattr(self.user_id_type, 'to_alipay_dict'):
                params['user_id_type'] = self.user_id_type.to_alipay_dict()
            else:
                params['user_id_type'] = self.user_id_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelPromotionGetModel()
        if 'biz_area_codes' in d:
            o.biz_area_codes = d['biz_area_codes']
        if 'ch_info' in d:
            o.ch_info = d['ch_info']
        if 'city_codes' in d:
            o.city_codes = d['city_codes']
        if 'country_codes' in d:
            o.country_codes = d['country_codes']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'lbs_reverse_level' in d:
            o.lbs_reverse_level = d['lbs_reverse_level']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'radius' in d:
            o.radius = d['radius']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'top_promotion_ids' in d:
            o.top_promotion_ids = d['top_promotion_ids']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_id_type' in d:
            o.user_id_type = d['user_id_type']
        return o


