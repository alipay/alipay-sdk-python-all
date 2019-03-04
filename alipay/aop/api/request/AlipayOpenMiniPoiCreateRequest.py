#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayOpenMiniPoiCreateRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._certificate = None
        self._poi_address = None
        self._related_name = None
        self._fifth_related_material = None
        self._first_related_material = None
        self._fourth_related_material = None
        self._second_related_material = None
        self._third_related_material = None
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
    def certificate(self):
        return self._certificate

    @certificate.setter
    def certificate(self, value):
        self._certificate = value
    @property
    def poi_address(self):
        return self._poi_address

    @poi_address.setter
    def poi_address(self, value):
        self._poi_address = value
    @property
    def related_name(self):
        return self._related_name

    @related_name.setter
    def related_name(self, value):
        self._related_name = value

    @property
    def fifth_related_material(self):
        return self._fifth_related_material

    @fifth_related_material.setter
    def fifth_related_material(self, value):
        if not isinstance(value, FileItem):
            return
        self._fifth_related_material = value
    @property
    def first_related_material(self):
        return self._first_related_material

    @first_related_material.setter
    def first_related_material(self, value):
        if not isinstance(value, FileItem):
            return
        self._first_related_material = value
    @property
    def fourth_related_material(self):
        return self._fourth_related_material

    @fourth_related_material.setter
    def fourth_related_material(self, value):
        if not isinstance(value, FileItem):
            return
        self._fourth_related_material = value
    @property
    def second_related_material(self):
        return self._second_related_material

    @second_related_material.setter
    def second_related_material(self, value):
        if not isinstance(value, FileItem):
            return
        self._second_related_material = value
    @property
    def third_related_material(self):
        return self._third_related_material

    @third_related_material.setter
    def third_related_material(self, value):
        if not isinstance(value, FileItem):
            return
        self._third_related_material = value

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
        params[P_METHOD] = 'alipay.open.mini.poi.create'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.certificate:
            if hasattr(self.certificate, 'to_alipay_dict'):
                params['certificate'] = json.dumps(obj=self.certificate.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['certificate'] = self.certificate
        if self.poi_address:
            if hasattr(self.poi_address, 'to_alipay_dict'):
                params['poi_address'] = json.dumps(obj=self.poi_address.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['poi_address'] = self.poi_address
        if self.related_name:
            if hasattr(self.related_name, 'to_alipay_dict'):
                params['related_name'] = json.dumps(obj=self.related_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['related_name'] = self.related_name
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
        if self.fifth_related_material:
            multipart_params['fifth_related_material'] = self.fifth_related_material
        if self.first_related_material:
            multipart_params['first_related_material'] = self.first_related_material
        if self.fourth_related_material:
            multipart_params['fourth_related_material'] = self.fourth_related_material
        if self.second_related_material:
            multipart_params['second_related_material'] = self.second_related_material
        if self.third_related_material:
            multipart_params['third_related_material'] = self.third_related_material
        return multipart_params
