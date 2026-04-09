#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandChannelpoiurlModifyModel(object):

    def __init__(self):
        self._app_status = None
        self._service_id = None
        self._service_name = None
        self._service_type = None
        self._shop_app_id = None
        self._shop_id = None
        self._url = None

    @property
    def app_status(self):
        return self._app_status

    @app_status.setter
    def app_status(self, value):
        self._app_status = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def shop_app_id(self):
        return self._shop_app_id

    @shop_app_id.setter
    def shop_app_id(self, value):
        self._shop_app_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_status:
            if hasattr(self.app_status, 'to_alipay_dict'):
                params['app_status'] = self.app_status.to_alipay_dict()
            else:
                params['app_status'] = self.app_status
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.shop_app_id:
            if hasattr(self.shop_app_id, 'to_alipay_dict'):
                params['shop_app_id'] = self.shop_app_id.to_alipay_dict()
            else:
                params['shop_app_id'] = self.shop_app_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandChannelpoiurlModifyModel()
        if 'app_status' in d:
            o.app_status = d['app_status']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'shop_app_id' in d:
            o.shop_app_id = d['shop_app_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'url' in d:
            o.url = d['url']
        return o


