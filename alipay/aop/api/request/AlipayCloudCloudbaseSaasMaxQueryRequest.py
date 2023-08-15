#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayCloudCloudbaseSaasMaxQueryRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._biz_app_id = None
        self._image_type = None
        self._image_value = None
        self._model_version = None
        self._route = None
        self._service_code = None
        self._side = None
        self._uri = None
        self._use_iot = None
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
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def image_type(self):
        return self._image_type

    @image_type.setter
    def image_type(self, value):
        self._image_type = value
    @property
    def image_value(self):
        return self._image_value

    @image_value.setter
    def image_value(self, value):
        self._image_value = value
    @property
    def model_version(self):
        return self._model_version

    @model_version.setter
    def model_version(self, value):
        self._model_version = value
    @property
    def route(self):
        return self._route

    @route.setter
    def route(self, value):
        self._route = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value
    @property
    def uri(self):
        return self._uri

    @uri.setter
    def uri(self, value):
        self._uri = value
    @property
    def use_iot(self):
        return self._use_iot

    @use_iot.setter
    def use_iot(self, value):
        self._use_iot = value


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
        params[P_METHOD] = 'alipay.cloud.cloudbase.saas.max.query'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = json.dumps(obj=self.biz_app_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.image_type:
            if hasattr(self.image_type, 'to_alipay_dict'):
                params['image_type'] = json.dumps(obj=self.image_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['image_type'] = self.image_type
        if self.image_value:
            if hasattr(self.image_value, 'to_alipay_dict'):
                params['image_value'] = json.dumps(obj=self.image_value.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['image_value'] = self.image_value
        if self.model_version:
            if hasattr(self.model_version, 'to_alipay_dict'):
                params['model_version'] = json.dumps(obj=self.model_version.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['model_version'] = self.model_version
        if self.route:
            if hasattr(self.route, 'to_alipay_dict'):
                params['route'] = json.dumps(obj=self.route.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['route'] = self.route
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = json.dumps(obj=self.service_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['service_code'] = self.service_code
        if self.side:
            if hasattr(self.side, 'to_alipay_dict'):
                params['side'] = json.dumps(obj=self.side.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['side'] = self.side
        if self.uri:
            if hasattr(self.uri, 'to_alipay_dict'):
                params['uri'] = json.dumps(obj=self.uri.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['uri'] = self.uri
        if self.use_iot:
            if hasattr(self.use_iot, 'to_alipay_dict'):
                params['use_iot'] = json.dumps(obj=self.use_iot.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['use_iot'] = self.use_iot
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
