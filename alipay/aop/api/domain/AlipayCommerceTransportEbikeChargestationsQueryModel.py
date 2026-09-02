#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LocationParam import LocationParam
from alipay.aop.api.domain.LocationParam import LocationParam


class AlipayCommerceTransportEbikeChargestationsQueryModel(object):

    def __init__(self):
        self._city_code = None
        self._page_no = None
        self._page_size = None
        self._partner_code = None
        self._search_location = None
        self._search_radius = None
        self._user_location = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
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
    def partner_code(self):
        return self._partner_code

    @partner_code.setter
    def partner_code(self, value):
        self._partner_code = value
    @property
    def search_location(self):
        return self._search_location

    @search_location.setter
    def search_location(self, value):
        if isinstance(value, LocationParam):
            self._search_location = value
        else:
            self._search_location = LocationParam.from_alipay_dict(value)
    @property
    def search_radius(self):
        return self._search_radius

    @search_radius.setter
    def search_radius(self, value):
        self._search_radius = value
    @property
    def user_location(self):
        return self._user_location

    @user_location.setter
    def user_location(self, value):
        if isinstance(value, LocationParam):
            self._user_location = value
        else:
            self._user_location = LocationParam.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
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
        if self.partner_code:
            if hasattr(self.partner_code, 'to_alipay_dict'):
                params['partner_code'] = self.partner_code.to_alipay_dict()
            else:
                params['partner_code'] = self.partner_code
        if self.search_location:
            if hasattr(self.search_location, 'to_alipay_dict'):
                params['search_location'] = self.search_location.to_alipay_dict()
            else:
                params['search_location'] = self.search_location
        if self.search_radius:
            if hasattr(self.search_radius, 'to_alipay_dict'):
                params['search_radius'] = self.search_radius.to_alipay_dict()
            else:
                params['search_radius'] = self.search_radius
        if self.user_location:
            if hasattr(self.user_location, 'to_alipay_dict'):
                params['user_location'] = self.user_location.to_alipay_dict()
            else:
                params['user_location'] = self.user_location
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEbikeChargestationsQueryModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'partner_code' in d:
            o.partner_code = d['partner_code']
        if 'search_location' in d:
            o.search_location = d['search_location']
        if 'search_radius' in d:
            o.search_radius = d['search_radius']
        if 'user_location' in d:
            o.user_location = d['user_location']
        return o


