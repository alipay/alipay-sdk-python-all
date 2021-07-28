#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayOpenMiniAmpeEnterApplyRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._address = None
        self._contact_email = None
        self._contact_name = None
        self._contact_phone = None
        self._enterprise_name = None
        self._major_products = None
        self._official_website = None
        self._scene_code = None
        self._introduction_file = None
        self._license_pic = None
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
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def major_products(self):
        return self._major_products

    @major_products.setter
    def major_products(self, value):
        self._major_products = value
    @property
    def official_website(self):
        return self._official_website

    @official_website.setter
    def official_website(self, value):
        self._official_website = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value

    @property
    def introduction_file(self):
        return self._introduction_file

    @introduction_file.setter
    def introduction_file(self, value):
        if not isinstance(value, FileItem):
            return
        self._introduction_file = value
    @property
    def license_pic(self):
        return self._license_pic

    @license_pic.setter
    def license_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._license_pic = value

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
        params[P_METHOD] = 'alipay.open.mini.ampe.enter.apply'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = json.dumps(obj=self.address.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['address'] = self.address
        if self.contact_email:
            if hasattr(self.contact_email, 'to_alipay_dict'):
                params['contact_email'] = json.dumps(obj=self.contact_email.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['contact_email'] = self.contact_email
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = json.dumps(obj=self.contact_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['contact_name'] = self.contact_name
        if self.contact_phone:
            if hasattr(self.contact_phone, 'to_alipay_dict'):
                params['contact_phone'] = json.dumps(obj=self.contact_phone.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['contact_phone'] = self.contact_phone
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = json.dumps(obj=self.enterprise_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['enterprise_name'] = self.enterprise_name
        if self.major_products:
            if hasattr(self.major_products, 'to_alipay_dict'):
                params['major_products'] = json.dumps(obj=self.major_products.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['major_products'] = self.major_products
        if self.official_website:
            if hasattr(self.official_website, 'to_alipay_dict'):
                params['official_website'] = json.dumps(obj=self.official_website.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['official_website'] = self.official_website
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = json.dumps(obj=self.scene_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['scene_code'] = self.scene_code
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
        if self.introduction_file:
            multipart_params['introduction_file'] = self.introduction_file
        if self.license_pic:
            multipart_params['license_pic'] = self.license_pic
        return multipart_params
