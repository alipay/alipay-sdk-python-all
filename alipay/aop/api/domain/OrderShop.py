#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderShop(object):

    def __init__(self):
        self._legal_person_identity_card = None
        self._shop_address = None
        self._shop_city = None
        self._shop_district = None
        self._shop_industry = None
        self._shop_latitude = None
        self._shop_licence_photo = None
        self._shop_linkman_mobile = None
        self._shop_linkman_name = None
        self._shop_longitude = None
        self._shop_name = None
        self._shop_open_time = None
        self._shop_province = None

    @property
    def legal_person_identity_card(self):
        return self._legal_person_identity_card

    @legal_person_identity_card.setter
    def legal_person_identity_card(self, value):
        self._legal_person_identity_card = value
    @property
    def shop_address(self):
        return self._shop_address

    @shop_address.setter
    def shop_address(self, value):
        self._shop_address = value
    @property
    def shop_city(self):
        return self._shop_city

    @shop_city.setter
    def shop_city(self, value):
        self._shop_city = value
    @property
    def shop_district(self):
        return self._shop_district

    @shop_district.setter
    def shop_district(self, value):
        self._shop_district = value
    @property
    def shop_industry(self):
        return self._shop_industry

    @shop_industry.setter
    def shop_industry(self, value):
        self._shop_industry = value
    @property
    def shop_latitude(self):
        return self._shop_latitude

    @shop_latitude.setter
    def shop_latitude(self, value):
        self._shop_latitude = value
    @property
    def shop_licence_photo(self):
        return self._shop_licence_photo

    @shop_licence_photo.setter
    def shop_licence_photo(self, value):
        self._shop_licence_photo = value
    @property
    def shop_linkman_mobile(self):
        return self._shop_linkman_mobile

    @shop_linkman_mobile.setter
    def shop_linkman_mobile(self, value):
        self._shop_linkman_mobile = value
    @property
    def shop_linkman_name(self):
        return self._shop_linkman_name

    @shop_linkman_name.setter
    def shop_linkman_name(self, value):
        self._shop_linkman_name = value
    @property
    def shop_longitude(self):
        return self._shop_longitude

    @shop_longitude.setter
    def shop_longitude(self, value):
        self._shop_longitude = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_open_time(self):
        return self._shop_open_time

    @shop_open_time.setter
    def shop_open_time(self, value):
        self._shop_open_time = value
    @property
    def shop_province(self):
        return self._shop_province

    @shop_province.setter
    def shop_province(self, value):
        self._shop_province = value


    def to_alipay_dict(self):
        params = dict()
        if self.legal_person_identity_card:
            if hasattr(self.legal_person_identity_card, 'to_alipay_dict'):
                params['legal_person_identity_card'] = self.legal_person_identity_card.to_alipay_dict()
            else:
                params['legal_person_identity_card'] = self.legal_person_identity_card
        if self.shop_address:
            if hasattr(self.shop_address, 'to_alipay_dict'):
                params['shop_address'] = self.shop_address.to_alipay_dict()
            else:
                params['shop_address'] = self.shop_address
        if self.shop_city:
            if hasattr(self.shop_city, 'to_alipay_dict'):
                params['shop_city'] = self.shop_city.to_alipay_dict()
            else:
                params['shop_city'] = self.shop_city
        if self.shop_district:
            if hasattr(self.shop_district, 'to_alipay_dict'):
                params['shop_district'] = self.shop_district.to_alipay_dict()
            else:
                params['shop_district'] = self.shop_district
        if self.shop_industry:
            if hasattr(self.shop_industry, 'to_alipay_dict'):
                params['shop_industry'] = self.shop_industry.to_alipay_dict()
            else:
                params['shop_industry'] = self.shop_industry
        if self.shop_latitude:
            if hasattr(self.shop_latitude, 'to_alipay_dict'):
                params['shop_latitude'] = self.shop_latitude.to_alipay_dict()
            else:
                params['shop_latitude'] = self.shop_latitude
        if self.shop_licence_photo:
            if hasattr(self.shop_licence_photo, 'to_alipay_dict'):
                params['shop_licence_photo'] = self.shop_licence_photo.to_alipay_dict()
            else:
                params['shop_licence_photo'] = self.shop_licence_photo
        if self.shop_linkman_mobile:
            if hasattr(self.shop_linkman_mobile, 'to_alipay_dict'):
                params['shop_linkman_mobile'] = self.shop_linkman_mobile.to_alipay_dict()
            else:
                params['shop_linkman_mobile'] = self.shop_linkman_mobile
        if self.shop_linkman_name:
            if hasattr(self.shop_linkman_name, 'to_alipay_dict'):
                params['shop_linkman_name'] = self.shop_linkman_name.to_alipay_dict()
            else:
                params['shop_linkman_name'] = self.shop_linkman_name
        if self.shop_longitude:
            if hasattr(self.shop_longitude, 'to_alipay_dict'):
                params['shop_longitude'] = self.shop_longitude.to_alipay_dict()
            else:
                params['shop_longitude'] = self.shop_longitude
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_open_time:
            if hasattr(self.shop_open_time, 'to_alipay_dict'):
                params['shop_open_time'] = self.shop_open_time.to_alipay_dict()
            else:
                params['shop_open_time'] = self.shop_open_time
        if self.shop_province:
            if hasattr(self.shop_province, 'to_alipay_dict'):
                params['shop_province'] = self.shop_province.to_alipay_dict()
            else:
                params['shop_province'] = self.shop_province
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderShop()
        if 'legal_person_identity_card' in d:
            o.legal_person_identity_card = d['legal_person_identity_card']
        if 'shop_address' in d:
            o.shop_address = d['shop_address']
        if 'shop_city' in d:
            o.shop_city = d['shop_city']
        if 'shop_district' in d:
            o.shop_district = d['shop_district']
        if 'shop_industry' in d:
            o.shop_industry = d['shop_industry']
        if 'shop_latitude' in d:
            o.shop_latitude = d['shop_latitude']
        if 'shop_licence_photo' in d:
            o.shop_licence_photo = d['shop_licence_photo']
        if 'shop_linkman_mobile' in d:
            o.shop_linkman_mobile = d['shop_linkman_mobile']
        if 'shop_linkman_name' in d:
            o.shop_linkman_name = d['shop_linkman_name']
        if 'shop_longitude' in d:
            o.shop_longitude = d['shop_longitude']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_open_time' in d:
            o.shop_open_time = d['shop_open_time']
        if 'shop_province' in d:
            o.shop_province = d['shop_province']
        return o


