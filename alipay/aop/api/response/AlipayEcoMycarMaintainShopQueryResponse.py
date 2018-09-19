#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarMaintainShopQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarMaintainShopQueryResponse, self).__init__()
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
        self._shop_id = None
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
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarMaintainShopQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'alipay_account' in response:
            self.alipay_account = response['alipay_account']
        if 'brand_ids' in response:
            self.brand_ids = response['brand_ids']
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'close_time' in response:
            self.close_time = response['close_time']
        if 'contact_email' in response:
            self.contact_email = response['contact_email']
        if 'contact_mobile_phone' in response:
            self.contact_mobile_phone = response['contact_mobile_phone']
        if 'contact_name' in response:
            self.contact_name = response['contact_name']
        if 'district_code' in response:
            self.district_code = response['district_code']
        if 'ext_param' in response:
            self.ext_param = response['ext_param']
        if 'industry_app_category_id' in response:
            self.industry_app_category_id = response['industry_app_category_id']
        if 'industry_category_id' in response:
            self.industry_category_id = response['industry_category_id']
        if 'lat' in response:
            self.lat = response['lat']
        if 'lon' in response:
            self.lon = response['lon']
        if 'main_image' in response:
            self.main_image = response['main_image']
        if 'merchant_branch_id' in response:
            self.merchant_branch_id = response['merchant_branch_id']
        if 'open_time' in response:
            self.open_time = response['open_time']
        if 'other_images' in response:
            self.other_images = response['other_images']
        if 'out_shop_id' in response:
            self.out_shop_id = response['out_shop_id']
        if 'province_code' in response:
            self.province_code = response['province_code']
        if 'shop_branch_name' in response:
            self.shop_branch_name = response['shop_branch_name']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'shop_name' in response:
            self.shop_name = response['shop_name']
        if 'shop_tel' in response:
            self.shop_tel = response['shop_tel']
        if 'shop_type' in response:
            self.shop_type = response['shop_type']
        if 'status' in response:
            self.status = response['status']
