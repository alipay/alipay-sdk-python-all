#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayCommerceOperationShopDeviceCreateRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._category_l_1 = None
        self._category_l_2 = None
        self._city_code = None
        self._city_name = None
        self._company_name = None
        self._device_id = None
        self._device_type = None
        self._district_code = None
        self._district_name = None
        self._eleme_dd_shop_id = None
        self._eleme_dd_shop_name = None
        self._latitude = None
        self._legal_identity_from_date = None
        self._legal_identity_no = None
        self._legal_identity_to_date = None
        self._legal_name = None
        self._license_no = None
        self._longitude = None
        self._merchant_name = None
        self._out_shop_id = None
        self._province_code = None
        self._province_name = None
        self._shop_address = None
        self._shop_name = None
        self._shop_phone = None
        self._shop_type = None
        self._smids = None
        self._valid_to_date = None
        self._legal_identity_back = None
        self._legal_identity_front = None
        self._license_img = None
        self._shop_logo = None
        self._shop_photo = None
        self._version = "1.0"
        self._terminal_type = None
        self._terminal_info = None
        self._prod_code = None
        self._notify_url = None
        self._return_url = None
        self._udf_params = None
        self._need_encrypt = False

    @property
    def biz_model(self):
        return self._biz_model

    @biz_model.setter
    def biz_model(self, value):
        self._biz_model = value

    @property
    def category_l_1(self):
        return self._category_l_1

    @category_l_1.setter
    def category_l_1(self, value):
        self._category_l_1 = value
    @property
    def category_l_2(self):
        return self._category_l_2

    @category_l_2.setter
    def category_l_2(self, value):
        self._category_l_2 = value
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
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
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
    def eleme_dd_shop_id(self):
        return self._eleme_dd_shop_id

    @eleme_dd_shop_id.setter
    def eleme_dd_shop_id(self, value):
        self._eleme_dd_shop_id = value
    @property
    def eleme_dd_shop_name(self):
        return self._eleme_dd_shop_name

    @eleme_dd_shop_name.setter
    def eleme_dd_shop_name(self, value):
        self._eleme_dd_shop_name = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def legal_identity_from_date(self):
        return self._legal_identity_from_date

    @legal_identity_from_date.setter
    def legal_identity_from_date(self, value):
        self._legal_identity_from_date = value
    @property
    def legal_identity_no(self):
        return self._legal_identity_no

    @legal_identity_no.setter
    def legal_identity_no(self, value):
        self._legal_identity_no = value
    @property
    def legal_identity_to_date(self):
        return self._legal_identity_to_date

    @legal_identity_to_date.setter
    def legal_identity_to_date(self, value):
        self._legal_identity_to_date = value
    @property
    def legal_name(self):
        return self._legal_name

    @legal_name.setter
    def legal_name(self, value):
        self._legal_name = value
    @property
    def license_no(self):
        return self._license_no

    @license_no.setter
    def license_no(self, value):
        self._license_no = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
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
    def shop_phone(self):
        return self._shop_phone

    @shop_phone.setter
    def shop_phone(self, value):
        self._shop_phone = value
    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value
    @property
    def smids(self):
        return self._smids

    @smids.setter
    def smids(self, value):
        self._smids = value
    @property
    def valid_to_date(self):
        return self._valid_to_date

    @valid_to_date.setter
    def valid_to_date(self, value):
        self._valid_to_date = value

    @property
    def legal_identity_back(self):
        return self._legal_identity_back

    @legal_identity_back.setter
    def legal_identity_back(self, value):
        if not isinstance(value, FileItem):
            return
        self._legal_identity_back = value
    @property
    def legal_identity_front(self):
        return self._legal_identity_front

    @legal_identity_front.setter
    def legal_identity_front(self, value):
        if not isinstance(value, FileItem):
            return
        self._legal_identity_front = value
    @property
    def license_img(self):
        return self._license_img

    @license_img.setter
    def license_img(self, value):
        if not isinstance(value, FileItem):
            return
        self._license_img = value
    @property
    def shop_logo(self):
        return self._shop_logo

    @shop_logo.setter
    def shop_logo(self, value):
        if not isinstance(value, FileItem):
            return
        self._shop_logo = value
    @property
    def shop_photo(self):
        return self._shop_photo

    @shop_photo.setter
    def shop_photo(self, value):
        if not isinstance(value, FileItem):
            return
        self._shop_photo = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value

    @property
    def terminal_info(self):
        return self._terminal_info

    @terminal_info.setter
    def terminal_info(self, value):
        self._terminal_info = value

    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value

    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, value):
        self._notify_url = value

    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value

    @property
    def udf_params(self):
        return self._udf_params

    @udf_params.setter
    def udf_params(self, value):
        if not isinstance(value, dict):
            return
        self._udf_params = value

    @property
    def need_encrypt(self):
        return self._need_encrypt

    @need_encrypt.setter
    def need_encrypt(self, value):
        self._need_encrypt = value

    def add_other_text_param(self, key, value):
        if not self.udf_params:
            self.udf_params = dict()
        self.udf_params[key] = value

    def get_params(self):
        params = dict()
        params[P_METHOD] = 'alipay.commerce.operation.shop.device.create'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.category_l_1:
            if hasattr(self.category_l_1, 'to_alipay_dict'):
                params['category_l_1'] = json.dumps(obj=self.category_l_1.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['category_l_1'] = self.category_l_1
        if self.category_l_2:
            if hasattr(self.category_l_2, 'to_alipay_dict'):
                params['category_l_2'] = json.dumps(obj=self.category_l_2.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['category_l_2'] = self.category_l_2
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = json.dumps(obj=self.city_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = json.dumps(obj=self.city_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['city_name'] = self.city_name
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = json.dumps(obj=self.company_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['company_name'] = self.company_name
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = json.dumps(obj=self.device_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['device_id'] = self.device_id
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = json.dumps(obj=self.device_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['device_type'] = self.device_type
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = json.dumps(obj=self.district_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['district_code'] = self.district_code
        if self.district_name:
            if hasattr(self.district_name, 'to_alipay_dict'):
                params['district_name'] = json.dumps(obj=self.district_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['district_name'] = self.district_name
        if self.eleme_dd_shop_id:
            if hasattr(self.eleme_dd_shop_id, 'to_alipay_dict'):
                params['eleme_dd_shop_id'] = json.dumps(obj=self.eleme_dd_shop_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['eleme_dd_shop_id'] = self.eleme_dd_shop_id
        if self.eleme_dd_shop_name:
            if hasattr(self.eleme_dd_shop_name, 'to_alipay_dict'):
                params['eleme_dd_shop_name'] = json.dumps(obj=self.eleme_dd_shop_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['eleme_dd_shop_name'] = self.eleme_dd_shop_name
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = json.dumps(obj=self.latitude.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['latitude'] = self.latitude
        if self.legal_identity_from_date:
            if hasattr(self.legal_identity_from_date, 'to_alipay_dict'):
                params['legal_identity_from_date'] = json.dumps(obj=self.legal_identity_from_date.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['legal_identity_from_date'] = self.legal_identity_from_date
        if self.legal_identity_no:
            if hasattr(self.legal_identity_no, 'to_alipay_dict'):
                params['legal_identity_no'] = json.dumps(obj=self.legal_identity_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['legal_identity_no'] = self.legal_identity_no
        if self.legal_identity_to_date:
            if hasattr(self.legal_identity_to_date, 'to_alipay_dict'):
                params['legal_identity_to_date'] = json.dumps(obj=self.legal_identity_to_date.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['legal_identity_to_date'] = self.legal_identity_to_date
        if self.legal_name:
            if hasattr(self.legal_name, 'to_alipay_dict'):
                params['legal_name'] = json.dumps(obj=self.legal_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['legal_name'] = self.legal_name
        if self.license_no:
            if hasattr(self.license_no, 'to_alipay_dict'):
                params['license_no'] = json.dumps(obj=self.license_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['license_no'] = self.license_no
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = json.dumps(obj=self.longitude.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['longitude'] = self.longitude
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = json.dumps(obj=self.merchant_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['merchant_name'] = self.merchant_name
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = json.dumps(obj=self.out_shop_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = json.dumps(obj=self.province_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['province_code'] = self.province_code
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = json.dumps(obj=self.province_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['province_name'] = self.province_name
        if self.shop_address:
            if hasattr(self.shop_address, 'to_alipay_dict'):
                params['shop_address'] = json.dumps(obj=self.shop_address.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['shop_address'] = self.shop_address
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = json.dumps(obj=self.shop_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['shop_name'] = self.shop_name
        if self.shop_phone:
            if hasattr(self.shop_phone, 'to_alipay_dict'):
                params['shop_phone'] = json.dumps(obj=self.shop_phone.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['shop_phone'] = self.shop_phone
        if self.shop_type:
            if hasattr(self.shop_type, 'to_alipay_dict'):
                params['shop_type'] = json.dumps(obj=self.shop_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['shop_type'] = self.shop_type
        if self.smids:
            if hasattr(self.smids, 'to_alipay_dict'):
                params['smids'] = json.dumps(obj=self.smids.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['smids'] = self.smids
        if self.valid_to_date:
            if hasattr(self.valid_to_date, 'to_alipay_dict'):
                params['valid_to_date'] = json.dumps(obj=self.valid_to_date.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['valid_to_date'] = self.valid_to_date
        if self.terminal_type:
            params['terminal_type'] = self.terminal_type
        if self.terminal_info:
            params['terminal_info'] = self.terminal_info
        if self.prod_code:
            params['prod_code'] = self.prod_code
        if self.notify_url:
            params['notify_url'] = self.notify_url
        if self.return_url:
            params['return_url'] = self.return_url
        if self.udf_params:
            params.update(self.udf_params)
        return params

    def get_multipart_params(self):
        multipart_params = dict()
        if self.legal_identity_back:
            multipart_params['legal_identity_back'] = self.legal_identity_back
        if self.legal_identity_front:
            multipart_params['legal_identity_front'] = self.legal_identity_front
        if self.license_img:
            multipart_params['license_img'] = self.license_img
        if self.shop_logo:
            multipart_params['shop_logo'] = self.shop_logo
        if self.shop_photo:
            multipart_params['shop_photo'] = self.shop_photo
        return multipart_params
