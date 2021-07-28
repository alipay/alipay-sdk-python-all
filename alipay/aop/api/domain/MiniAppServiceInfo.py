#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniAppServiceInfo(object):

    def __init__(self):
        self._biz_status = None
        self._is_inner = None
        self._is_order = None
        self._isv_app_id = None
        self._mini_app_id = None
        self._mini_app_name = None
        self._seller_id = None
        self._seller_name = None
        self._service_code = None
        self._service_logo = None
        self._service_name = None
        self._service_slogan = None
        self._show_type = None

    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def is_inner(self):
        return self._is_inner

    @is_inner.setter
    def is_inner(self, value):
        self._is_inner = value
    @property
    def is_order(self):
        return self._is_order

    @is_order.setter
    def is_order(self, value):
        self._is_order = value
    @property
    def isv_app_id(self):
        return self._isv_app_id

    @isv_app_id.setter
    def isv_app_id(self, value):
        self._isv_app_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def mini_app_name(self):
        return self._mini_app_name

    @mini_app_name.setter
    def mini_app_name(self, value):
        self._mini_app_name = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def seller_name(self):
        return self._seller_name

    @seller_name.setter
    def seller_name(self, value):
        self._seller_name = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_logo(self):
        return self._service_logo

    @service_logo.setter
    def service_logo(self, value):
        self._service_logo = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_slogan(self):
        return self._service_slogan

    @service_slogan.setter
    def service_slogan(self, value):
        self._service_slogan = value
    @property
    def show_type(self):
        return self._show_type

    @show_type.setter
    def show_type(self, value):
        self._show_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_status:
            if hasattr(self.biz_status, 'to_alipay_dict'):
                params['biz_status'] = self.biz_status.to_alipay_dict()
            else:
                params['biz_status'] = self.biz_status
        if self.is_inner:
            if hasattr(self.is_inner, 'to_alipay_dict'):
                params['is_inner'] = self.is_inner.to_alipay_dict()
            else:
                params['is_inner'] = self.is_inner
        if self.is_order:
            if hasattr(self.is_order, 'to_alipay_dict'):
                params['is_order'] = self.is_order.to_alipay_dict()
            else:
                params['is_order'] = self.is_order
        if self.isv_app_id:
            if hasattr(self.isv_app_id, 'to_alipay_dict'):
                params['isv_app_id'] = self.isv_app_id.to_alipay_dict()
            else:
                params['isv_app_id'] = self.isv_app_id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.mini_app_name:
            if hasattr(self.mini_app_name, 'to_alipay_dict'):
                params['mini_app_name'] = self.mini_app_name.to_alipay_dict()
            else:
                params['mini_app_name'] = self.mini_app_name
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.seller_name:
            if hasattr(self.seller_name, 'to_alipay_dict'):
                params['seller_name'] = self.seller_name.to_alipay_dict()
            else:
                params['seller_name'] = self.seller_name
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_logo:
            if hasattr(self.service_logo, 'to_alipay_dict'):
                params['service_logo'] = self.service_logo.to_alipay_dict()
            else:
                params['service_logo'] = self.service_logo
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.service_slogan:
            if hasattr(self.service_slogan, 'to_alipay_dict'):
                params['service_slogan'] = self.service_slogan.to_alipay_dict()
            else:
                params['service_slogan'] = self.service_slogan
        if self.show_type:
            if hasattr(self.show_type, 'to_alipay_dict'):
                params['show_type'] = self.show_type.to_alipay_dict()
            else:
                params['show_type'] = self.show_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppServiceInfo()
        if 'biz_status' in d:
            o.biz_status = d['biz_status']
        if 'is_inner' in d:
            o.is_inner = d['is_inner']
        if 'is_order' in d:
            o.is_order = d['is_order']
        if 'isv_app_id' in d:
            o.isv_app_id = d['isv_app_id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'mini_app_name' in d:
            o.mini_app_name = d['mini_app_name']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'seller_name' in d:
            o.seller_name = d['seller_name']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_logo' in d:
            o.service_logo = d['service_logo']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_slogan' in d:
            o.service_slogan = d['service_slogan']
        if 'show_type' in d:
            o.show_type = d['show_type']
        return o


