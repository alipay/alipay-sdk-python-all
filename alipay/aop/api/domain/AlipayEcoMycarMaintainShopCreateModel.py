#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarMaintainShopCreateModel(object):

    def __init__(self):
        self._address = None
        self._alipay_account = None
        self._brand_ids = None
        self._city_code = None
        self._close_time = None
        self._contact_email = None
        self._contact_mobile_phone = None
        self._contact_name = None
        self._district_code = None
        self._ext_param = None
        self._industry_app_category_id = None
        self._industry_category_id = None
        self._lat = None
        self._lon = None
        self._main_image = None
        self._merchant_branch_id = None
        self._open_time = None
        self._other_images = None
        self._out_shop_id = None
        self._province_code = None
        self._shop_branch_name = None
        self._shop_name = None
        self._shop_tel = None
        self._shop_type = None
        self._status = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def brand_ids(self):
        return self._brand_ids

    @brand_ids.setter
    def brand_ids(self, value):
        if isinstance(value, list):
            self._brand_ids = list()
            for i in value:
                self._brand_ids.append(i)
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def close_time(self):
        return self._close_time

    @close_time.setter
    def close_time(self, value):
        self._close_time = value
    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def contact_mobile_phone(self):
        return self._contact_mobile_phone

    @contact_mobile_phone.setter
    def contact_mobile_phone(self, value):
        self._contact_mobile_phone = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def industry_app_category_id(self):
        return self._industry_app_category_id

    @industry_app_category_id.setter
    def industry_app_category_id(self, value):
        if isinstance(value, list):
            self._industry_app_category_id = list()
            for i in value:
                self._industry_app_category_id.append(i)
    @property
    def industry_category_id(self):
        return self._industry_category_id

    @industry_category_id.setter
    def industry_category_id(self, value):
        if isinstance(value, list):
            self._industry_category_id = list()
            for i in value:
                self._industry_category_id.append(i)
    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, value):
        self._lat = value
    @property
    def lon(self):
        return self._lon

    @lon.setter
    def lon(self, value):
        self._lon = value
    @property
    def main_image(self):
        return self._main_image

    @main_image.setter
    def main_image(self, value):
        self._main_image = value
    @property
    def merchant_branch_id(self):
        return self._merchant_branch_id

    @merchant_branch_id.setter
    def merchant_branch_id(self, value):
        self._merchant_branch_id = value
    @property
    def open_time(self):
        return self._open_time

    @open_time.setter
    def open_time(self, value):
        self._open_time = value
    @property
    def other_images(self):
        return self._other_images

    @other_images.setter
    def other_images(self, value):
        if isinstance(value, list):
            self._other_images = list()
            for i in value:
                self._other_images.append(i)
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def shop_branch_name(self):
        return self._shop_branch_name

    @shop_branch_name.setter
    def shop_branch_name(self, value):
        self._shop_branch_name = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_tel(self):
        return self._shop_tel

    @shop_tel.setter
    def shop_tel(self, value):
        self._shop_tel = value
    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value
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
        if self.alipay_account:
            if hasattr(self.alipay_account, 'to_alipay_dict'):
                params['alipay_account'] = self.alipay_account.to_alipay_dict()
            else:
                params['alipay_account'] = self.alipay_account
        if self.brand_ids:
            if isinstance(self.brand_ids, list):
                for i in range(0, len(self.brand_ids)):
                    element = self.brand_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.brand_ids[i] = element.to_alipay_dict()
            if hasattr(self.brand_ids, 'to_alipay_dict'):
                params['brand_ids'] = self.brand_ids.to_alipay_dict()
            else:
                params['brand_ids'] = self.brand_ids
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.close_time:
            if hasattr(self.close_time, 'to_alipay_dict'):
                params['close_time'] = self.close_time.to_alipay_dict()
            else:
                params['close_time'] = self.close_time
        if self.contact_email:
            if hasattr(self.contact_email, 'to_alipay_dict'):
                params['contact_email'] = self.contact_email.to_alipay_dict()
            else:
                params['contact_email'] = self.contact_email
        if self.contact_mobile_phone:
            if hasattr(self.contact_mobile_phone, 'to_alipay_dict'):
                params['contact_mobile_phone'] = self.contact_mobile_phone.to_alipay_dict()
            else:
                params['contact_mobile_phone'] = self.contact_mobile_phone
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.industry_app_category_id:
            if isinstance(self.industry_app_category_id, list):
                for i in range(0, len(self.industry_app_category_id)):
                    element = self.industry_app_category_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.industry_app_category_id[i] = element.to_alipay_dict()
            if hasattr(self.industry_app_category_id, 'to_alipay_dict'):
                params['industry_app_category_id'] = self.industry_app_category_id.to_alipay_dict()
            else:
                params['industry_app_category_id'] = self.industry_app_category_id
        if self.industry_category_id:
            if isinstance(self.industry_category_id, list):
                for i in range(0, len(self.industry_category_id)):
                    element = self.industry_category_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.industry_category_id[i] = element.to_alipay_dict()
            if hasattr(self.industry_category_id, 'to_alipay_dict'):
                params['industry_category_id'] = self.industry_category_id.to_alipay_dict()
            else:
                params['industry_category_id'] = self.industry_category_id
        if self.lat:
            if hasattr(self.lat, 'to_alipay_dict'):
                params['lat'] = self.lat.to_alipay_dict()
            else:
                params['lat'] = self.lat
        if self.lon:
            if hasattr(self.lon, 'to_alipay_dict'):
                params['lon'] = self.lon.to_alipay_dict()
            else:
                params['lon'] = self.lon
        if self.main_image:
            if hasattr(self.main_image, 'to_alipay_dict'):
                params['main_image'] = self.main_image.to_alipay_dict()
            else:
                params['main_image'] = self.main_image
        if self.merchant_branch_id:
            if hasattr(self.merchant_branch_id, 'to_alipay_dict'):
                params['merchant_branch_id'] = self.merchant_branch_id.to_alipay_dict()
            else:
                params['merchant_branch_id'] = self.merchant_branch_id
        if self.open_time:
            if hasattr(self.open_time, 'to_alipay_dict'):
                params['open_time'] = self.open_time.to_alipay_dict()
            else:
                params['open_time'] = self.open_time
        if self.other_images:
            if isinstance(self.other_images, list):
                for i in range(0, len(self.other_images)):
                    element = self.other_images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_images[i] = element.to_alipay_dict()
            if hasattr(self.other_images, 'to_alipay_dict'):
                params['other_images'] = self.other_images.to_alipay_dict()
            else:
                params['other_images'] = self.other_images
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.shop_branch_name:
            if hasattr(self.shop_branch_name, 'to_alipay_dict'):
                params['shop_branch_name'] = self.shop_branch_name.to_alipay_dict()
            else:
                params['shop_branch_name'] = self.shop_branch_name
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_tel:
            if hasattr(self.shop_tel, 'to_alipay_dict'):
                params['shop_tel'] = self.shop_tel.to_alipay_dict()
            else:
                params['shop_tel'] = self.shop_tel
        if self.shop_type:
            if hasattr(self.shop_type, 'to_alipay_dict'):
                params['shop_type'] = self.shop_type.to_alipay_dict()
            else:
                params['shop_type'] = self.shop_type
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
        o = AlipayEcoMycarMaintainShopCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'alipay_account' in d:
            o.alipay_account = d['alipay_account']
        if 'brand_ids' in d:
            o.brand_ids = d['brand_ids']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'close_time' in d:
            o.close_time = d['close_time']
        if 'contact_email' in d:
            o.contact_email = d['contact_email']
        if 'contact_mobile_phone' in d:
            o.contact_mobile_phone = d['contact_mobile_phone']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'industry_app_category_id' in d:
            o.industry_app_category_id = d['industry_app_category_id']
        if 'industry_category_id' in d:
            o.industry_category_id = d['industry_category_id']
        if 'lat' in d:
            o.lat = d['lat']
        if 'lon' in d:
            o.lon = d['lon']
        if 'main_image' in d:
            o.main_image = d['main_image']
        if 'merchant_branch_id' in d:
            o.merchant_branch_id = d['merchant_branch_id']
        if 'open_time' in d:
            o.open_time = d['open_time']
        if 'other_images' in d:
            o.other_images = d['other_images']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'shop_branch_name' in d:
            o.shop_branch_name = d['shop_branch_name']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_tel' in d:
            o.shop_tel = d['shop_tel']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        if 'status' in d:
            o.status = d['status']
        return o


