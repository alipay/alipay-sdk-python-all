#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndexDetail(object):

    def __init__(self):
        self._area_code = None
        self._area_name = None
        self._city_ranking = None
        self._county_ranking = None
        self._id = None
        self._index_val = None
        self._period = None

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def area_name(self):
        return self._area_name

    @area_name.setter
    def area_name(self, value):
        self._area_name = value
    @property
    def city_ranking(self):
        return self._city_ranking

    @city_ranking.setter
    def city_ranking(self, value):
        self._city_ranking = value
    @property
    def county_ranking(self):
        return self._county_ranking

    @county_ranking.setter
    def county_ranking(self, value):
        self._county_ranking = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def index_val(self):
        return self._index_val

    @index_val.setter
    def index_val(self, value):
        self._index_val = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.area_name:
            if hasattr(self.area_name, 'to_alipay_dict'):
                params['area_name'] = self.area_name.to_alipay_dict()
            else:
                params['area_name'] = self.area_name
        if self.city_ranking:
            if hasattr(self.city_ranking, 'to_alipay_dict'):
                params['city_ranking'] = self.city_ranking.to_alipay_dict()
            else:
                params['city_ranking'] = self.city_ranking
        if self.county_ranking:
            if hasattr(self.county_ranking, 'to_alipay_dict'):
                params['county_ranking'] = self.county_ranking.to_alipay_dict()
            else:
                params['county_ranking'] = self.county_ranking
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.index_val:
            if hasattr(self.index_val, 'to_alipay_dict'):
                params['index_val'] = self.index_val.to_alipay_dict()
            else:
                params['index_val'] = self.index_val
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndexDetail()
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'area_name' in d:
            o.area_name = d['area_name']
        if 'city_ranking' in d:
            o.city_ranking = d['city_ranking']
        if 'county_ranking' in d:
            o.county_ranking = d['county_ranking']
        if 'id' in d:
            o.id = d['id']
        if 'index_val' in d:
            o.index_val = d['index_val']
        if 'period' in d:
            o.period = d['period']
        return o


