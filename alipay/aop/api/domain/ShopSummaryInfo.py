#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopCategoryInfo import ShopCategoryInfo


class ShopSummaryInfo(object):

    def __init__(self):
        self._address = None
        self._branch_shop_name = None
        self._brand_name = None
        self._business_time = None
        self._category_infos = None
        self._city_code = None
        self._city_name = None
        self._display_status = None
        self._district_code = None
        self._district_name = None
        self._landline_no = None
        self._latitude = None
        self._logo = None
        self._logo_url = None
        self._longitude = None
        self._main_image = None
        self._main_image_url = None
        self._main_shop_name = None
        self._mobile_no = None
        self._per_pay = None
        self._principal_id = None
        self._province_code = None
        self._province_name = None
        self._shop_id = None
        self._status = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def branch_shop_name(self):
        return self._branch_shop_name

    @branch_shop_name.setter
    def branch_shop_name(self, value):
        self._branch_shop_name = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        self._business_time = value
    @property
    def category_infos(self):
        return self._category_infos

    @category_infos.setter
    def category_infos(self, value):
        if isinstance(value, list):
            self._category_infos = list()
            for i in value:
                if isinstance(i, ShopCategoryInfo):
                    self._category_infos.append(i)
                else:
                    self._category_infos.append(ShopCategoryInfo.from_alipay_dict(i))
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def display_status(self):
        return self._display_status

    @display_status.setter
    def display_status(self, value):
        self._display_status = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def district_name(self):
        return self._district_name

    @district_name.setter
    def district_name(self, value):
        self._district_name = value
    @property
    def landline_no(self):
        return self._landline_no

    @landline_no.setter
    def landline_no(self, value):
        self._landline_no = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def main_image(self):
        return self._main_image

    @main_image.setter
    def main_image(self, value):
        self._main_image = value
    @property
    def main_image_url(self):
        return self._main_image_url

    @main_image_url.setter
    def main_image_url(self, value):
        self._main_image_url = value
    @property
    def main_shop_name(self):
        return self._main_shop_name

    @main_shop_name.setter
    def main_shop_name(self, value):
        self._main_shop_name = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def per_pay(self):
        return self._per_pay

    @per_pay.setter
    def per_pay(self, value):
        self._per_pay = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.branch_shop_name:
            if hasattr(self.branch_shop_name, 'to_alipay_dict'):
                params['branch_shop_name'] = self.branch_shop_name.to_alipay_dict()
            else:
                params['branch_shop_name'] = self.branch_shop_name
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.business_time:
            if hasattr(self.business_time, 'to_alipay_dict'):
                params['business_time'] = self.business_time.to_alipay_dict()
            else:
                params['business_time'] = self.business_time
        if self.category_infos:
            if isinstance(self.category_infos, list):
                for i in range(0, len(self.category_infos)):
                    element = self.category_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_infos[i] = element.to_alipay_dict()
            if hasattr(self.category_infos, 'to_alipay_dict'):
                params['category_infos'] = self.category_infos.to_alipay_dict()
            else:
                params['category_infos'] = self.category_infos
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.display_status:
            if hasattr(self.display_status, 'to_alipay_dict'):
                params['display_status'] = self.display_status.to_alipay_dict()
            else:
                params['display_status'] = self.display_status
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.district_name:
            if hasattr(self.district_name, 'to_alipay_dict'):
                params['district_name'] = self.district_name.to_alipay_dict()
            else:
                params['district_name'] = self.district_name
        if self.landline_no:
            if hasattr(self.landline_no, 'to_alipay_dict'):
                params['landline_no'] = self.landline_no.to_alipay_dict()
            else:
                params['landline_no'] = self.landline_no
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.main_image:
            if hasattr(self.main_image, 'to_alipay_dict'):
                params['main_image'] = self.main_image.to_alipay_dict()
            else:
                params['main_image'] = self.main_image
        if self.main_image_url:
            if hasattr(self.main_image_url, 'to_alipay_dict'):
                params['main_image_url'] = self.main_image_url.to_alipay_dict()
            else:
                params['main_image_url'] = self.main_image_url
        if self.main_shop_name:
            if hasattr(self.main_shop_name, 'to_alipay_dict'):
                params['main_shop_name'] = self.main_shop_name.to_alipay_dict()
            else:
                params['main_shop_name'] = self.main_shop_name
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.per_pay:
            if hasattr(self.per_pay, 'to_alipay_dict'):
                params['per_pay'] = self.per_pay.to_alipay_dict()
            else:
                params['per_pay'] = self.per_pay
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopSummaryInfo()
        if 'address' in d:
            o.address = d['address']
        if 'branch_shop_name' in d:
            o.branch_shop_name = d['branch_shop_name']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'business_time' in d:
            o.business_time = d['business_time']
        if 'category_infos' in d:
            o.category_infos = d['category_infos']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'display_status' in d:
            o.display_status = d['display_status']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'district_name' in d:
            o.district_name = d['district_name']
        if 'landline_no' in d:
            o.landline_no = d['landline_no']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'logo' in d:
            o.logo = d['logo']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'main_image' in d:
            o.main_image = d['main_image']
        if 'main_image_url' in d:
            o.main_image_url = d['main_image_url']
        if 'main_shop_name' in d:
            o.main_shop_name = d['main_shop_name']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'per_pay' in d:
            o.per_pay = d['per_pay']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'status' in d:
            o.status = d['status']
        return o


