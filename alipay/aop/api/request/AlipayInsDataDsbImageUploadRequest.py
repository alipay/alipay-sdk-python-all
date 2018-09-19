#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayInsDataDsbImageUploadRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._estimate_no = None
        self._frame_no = None
        self._image_format = None
        self._image_name = None
        self._image_path = None
        self._image_properties = None
        self._image_source = None
        self._image_store_type = None
        self._image_type = None
        self._license_no = None
        self._report_no = None
        self._shoot_time = None
        self._image_content = None
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
    def estimate_no(self):
        return self._estimate_no

    @estimate_no.setter
    def estimate_no(self, value):
        self._estimate_no = value
    @property
    def frame_no(self):
        return self._frame_no

    @frame_no.setter
    def frame_no(self, value):
        self._frame_no = value
    @property
    def image_format(self):
        return self._image_format

    @image_format.setter
    def image_format(self, value):
        self._image_format = value
    @property
    def image_name(self):
        return self._image_name

    @image_name.setter
    def image_name(self, value):
        self._image_name = value
    @property
    def image_path(self):
        return self._image_path

    @image_path.setter
    def image_path(self, value):
        self._image_path = value
    @property
    def image_properties(self):
        return self._image_properties

    @image_properties.setter
    def image_properties(self, value):
        self._image_properties = value
    @property
    def image_source(self):
        return self._image_source

    @image_source.setter
    def image_source(self, value):
        self._image_source = value
    @property
    def image_store_type(self):
        return self._image_store_type

    @image_store_type.setter
    def image_store_type(self, value):
        self._image_store_type = value
    @property
    def image_type(self):
        return self._image_type

    @image_type.setter
    def image_type(self, value):
        self._image_type = value
    @property
    def license_no(self):
        return self._license_no

    @license_no.setter
    def license_no(self, value):
        self._license_no = value
    @property
    def report_no(self):
        return self._report_no

    @report_no.setter
    def report_no(self, value):
        self._report_no = value
    @property
    def shoot_time(self):
        return self._shoot_time

    @shoot_time.setter
    def shoot_time(self, value):
        self._shoot_time = value

    @property
    def image_content(self):
        return self._image_content

    @image_content.setter
    def image_content(self, value):
        if not isinstance(value, FileItem):
            return
        self._image_content = value

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
        params[P_METHOD] = 'alipay.ins.data.dsb.image.upload'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.estimate_no:
            if hasattr(self.estimate_no, 'to_alipay_dict'):
                params['estimate_no'] = json.dumps(obj=self.estimate_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['estimate_no'] = self.estimate_no
        if self.frame_no:
            if hasattr(self.frame_no, 'to_alipay_dict'):
                params['frame_no'] = json.dumps(obj=self.frame_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['frame_no'] = self.frame_no
        if self.image_format:
            if hasattr(self.image_format, 'to_alipay_dict'):
                params['image_format'] = json.dumps(obj=self.image_format.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['image_format'] = self.image_format
        if self.image_name:
            if hasattr(self.image_name, 'to_alipay_dict'):
                params['image_name'] = json.dumps(obj=self.image_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['image_name'] = self.image_name
        if self.image_path:
            if hasattr(self.image_path, 'to_alipay_dict'):
                params['image_path'] = json.dumps(obj=self.image_path.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['image_path'] = self.image_path
        if self.image_properties:
            if hasattr(self.image_properties, 'to_alipay_dict'):
                params['image_properties'] = json.dumps(obj=self.image_properties.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['image_properties'] = self.image_properties
        if self.image_source:
            if hasattr(self.image_source, 'to_alipay_dict'):
                params['image_source'] = json.dumps(obj=self.image_source.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['image_source'] = self.image_source
        if self.image_store_type:
            if hasattr(self.image_store_type, 'to_alipay_dict'):
                params['image_store_type'] = json.dumps(obj=self.image_store_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['image_store_type'] = self.image_store_type
        if self.image_type:
            if hasattr(self.image_type, 'to_alipay_dict'):
                params['image_type'] = json.dumps(obj=self.image_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['image_type'] = self.image_type
        if self.license_no:
            if hasattr(self.license_no, 'to_alipay_dict'):
                params['license_no'] = json.dumps(obj=self.license_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['license_no'] = self.license_no
        if self.report_no:
            if hasattr(self.report_no, 'to_alipay_dict'):
                params['report_no'] = json.dumps(obj=self.report_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['report_no'] = self.report_no
        if self.shoot_time:
            if hasattr(self.shoot_time, 'to_alipay_dict'):
                params['shoot_time'] = json.dumps(obj=self.shoot_time.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['shoot_time'] = self.shoot_time
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
        if self.image_content:
            multipart_params['image_content'] = self.image_content
        return multipart_params
