#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayDiscoveryTaxiOrderConfirmRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._driver_lat = None
        self._driver_license = None
        self._driver_lng = None
        self._driver_name = None
        self._driver_phone = None
        self._is_alipay_support = None
        self._out_biz_no = None
        self._partner_id = None
        self._seller = None
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
    def driver_lat(self):
        return self._driver_lat

    @driver_lat.setter
    def driver_lat(self, value):
        self._driver_lat = value
    @property
    def driver_license(self):
        return self._driver_license

    @driver_license.setter
    def driver_license(self, value):
        self._driver_license = value
    @property
    def driver_lng(self):
        return self._driver_lng

    @driver_lng.setter
    def driver_lng(self, value):
        self._driver_lng = value
    @property
    def driver_name(self):
        return self._driver_name

    @driver_name.setter
    def driver_name(self, value):
        self._driver_name = value
    @property
    def driver_phone(self):
        return self._driver_phone

    @driver_phone.setter
    def driver_phone(self, value):
        self._driver_phone = value
    @property
    def is_alipay_support(self):
        return self._is_alipay_support

    @is_alipay_support.setter
    def is_alipay_support(self, value):
        self._is_alipay_support = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, value):
        self._seller = value


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
        params[P_METHOD] = 'alipay.discovery.taxi.order.confirm'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.driver_lat:
            if hasattr(self.driver_lat, 'to_alipay_dict'):
                params['driver_lat'] = json.dumps(obj=self.driver_lat.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['driver_lat'] = self.driver_lat
        if self.driver_license:
            if hasattr(self.driver_license, 'to_alipay_dict'):
                params['driver_license'] = json.dumps(obj=self.driver_license.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['driver_license'] = self.driver_license
        if self.driver_lng:
            if hasattr(self.driver_lng, 'to_alipay_dict'):
                params['driver_lng'] = json.dumps(obj=self.driver_lng.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['driver_lng'] = self.driver_lng
        if self.driver_name:
            if hasattr(self.driver_name, 'to_alipay_dict'):
                params['driver_name'] = json.dumps(obj=self.driver_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['driver_name'] = self.driver_name
        if self.driver_phone:
            if hasattr(self.driver_phone, 'to_alipay_dict'):
                params['driver_phone'] = json.dumps(obj=self.driver_phone.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['driver_phone'] = self.driver_phone
        if self.is_alipay_support:
            if hasattr(self.is_alipay_support, 'to_alipay_dict'):
                params['is_alipay_support'] = json.dumps(obj=self.is_alipay_support.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['is_alipay_support'] = self.is_alipay_support
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = json.dumps(obj=self.out_biz_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = json.dumps(obj=self.partner_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['partner_id'] = self.partner_id
        if self.seller:
            if hasattr(self.seller, 'to_alipay_dict'):
                params['seller'] = json.dumps(obj=self.seller.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller'] = self.seller
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
        return multipart_params
