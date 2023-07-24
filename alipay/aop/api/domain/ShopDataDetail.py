#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopScoreResultInfo import ShopScoreResultInfo


class ShopDataDetail(object):

    def __init__(self):
        self._city_name = None
        self._county_name = None
        self._poi_id = None
        self._province_name = None
        self._shop_address = None
        self._shop_name = None
        self._shop_score_result = None

    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def county_name(self):
        return self._county_name

    @county_name.setter
    def county_name(self, value):
        self._county_name = value
    @property
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def shop_address(self):
        return self._shop_address

    @shop_address.setter
    def shop_address(self, value):
        self._shop_address = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_score_result(self):
        return self._shop_score_result

    @shop_score_result.setter
    def shop_score_result(self, value):
        if isinstance(value, ShopScoreResultInfo):
            self._shop_score_result = value
        else:
            self._shop_score_result = ShopScoreResultInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.county_name:
            if hasattr(self.county_name, 'to_alipay_dict'):
                params['county_name'] = self.county_name.to_alipay_dict()
            else:
                params['county_name'] = self.county_name
        if self.poi_id:
            if hasattr(self.poi_id, 'to_alipay_dict'):
                params['poi_id'] = self.poi_id.to_alipay_dict()
            else:
                params['poi_id'] = self.poi_id
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.shop_address:
            if hasattr(self.shop_address, 'to_alipay_dict'):
                params['shop_address'] = self.shop_address.to_alipay_dict()
            else:
                params['shop_address'] = self.shop_address
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_score_result:
            if hasattr(self.shop_score_result, 'to_alipay_dict'):
                params['shop_score_result'] = self.shop_score_result.to_alipay_dict()
            else:
                params['shop_score_result'] = self.shop_score_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopDataDetail()
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'county_name' in d:
            o.county_name = d['county_name']
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'shop_address' in d:
            o.shop_address = d['shop_address']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_score_result' in d:
            o.shop_score_result = d['shop_score_result']
        return o


