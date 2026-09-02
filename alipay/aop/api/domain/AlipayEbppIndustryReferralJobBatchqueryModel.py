#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryReferralJobBatchqueryModel(object):

    def __init__(self):
        self._city_code = None
        self._distance_range = None
        self._latitude = None
        self._longitude = None
        self._page_num = None
        self._page_size = None
        self._recommender_id = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def distance_range(self):
        return self._distance_range

    @distance_range.setter
    def distance_range(self, value):
        self._distance_range = value
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
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def recommender_id(self):
        return self._recommender_id

    @recommender_id.setter
    def recommender_id(self, value):
        self._recommender_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.distance_range:
            if hasattr(self.distance_range, 'to_alipay_dict'):
                params['distance_range'] = self.distance_range.to_alipay_dict()
            else:
                params['distance_range'] = self.distance_range
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
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.recommender_id:
            if hasattr(self.recommender_id, 'to_alipay_dict'):
                params['recommender_id'] = self.recommender_id.to_alipay_dict()
            else:
                params['recommender_id'] = self.recommender_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryReferralJobBatchqueryModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'distance_range' in d:
            o.distance_range = d['distance_range']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'recommender_id' in d:
            o.recommender_id = d['recommender_id']
        return o


