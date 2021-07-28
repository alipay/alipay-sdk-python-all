#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerappCreateModel(object):

    def __init__(self):
        self._app_category_ids = None
        self._app_desc = None
        self._app_english_name = None
        self._app_logo = None
        self._app_name = None
        self._app_origin = None
        self._app_slogan = None
        self._app_sub_type = None
        self._app_type = None
        self._isv_app_id = None
        self._mini_app_id = None
        self._mini_category_ids = None
        self._pid = None
        self._service_email = None
        self._service_phone = None

    @property
    def app_category_ids(self):
        return self._app_category_ids

    @app_category_ids.setter
    def app_category_ids(self, value):
        self._app_category_ids = value
    @property
    def app_desc(self):
        return self._app_desc

    @app_desc.setter
    def app_desc(self, value):
        self._app_desc = value
    @property
    def app_english_name(self):
        return self._app_english_name

    @app_english_name.setter
    def app_english_name(self, value):
        self._app_english_name = value
    @property
    def app_logo(self):
        return self._app_logo

    @app_logo.setter
    def app_logo(self, value):
        self._app_logo = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_origin(self):
        return self._app_origin

    @app_origin.setter
    def app_origin(self, value):
        self._app_origin = value
    @property
    def app_slogan(self):
        return self._app_slogan

    @app_slogan.setter
    def app_slogan(self, value):
        self._app_slogan = value
    @property
    def app_sub_type(self):
        return self._app_sub_type

    @app_sub_type.setter
    def app_sub_type(self, value):
        self._app_sub_type = value
    @property
    def app_type(self):
        return self._app_type

    @app_type.setter
    def app_type(self, value):
        self._app_type = value
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
    def mini_category_ids(self):
        return self._mini_category_ids

    @mini_category_ids.setter
    def mini_category_ids(self, value):
        self._mini_category_ids = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def service_email(self):
        return self._service_email

    @service_email.setter
    def service_email(self, value):
        self._service_email = value
    @property
    def service_phone(self):
        return self._service_phone

    @service_phone.setter
    def service_phone(self, value):
        self._service_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_category_ids:
            if hasattr(self.app_category_ids, 'to_alipay_dict'):
                params['app_category_ids'] = self.app_category_ids.to_alipay_dict()
            else:
                params['app_category_ids'] = self.app_category_ids
        if self.app_desc:
            if hasattr(self.app_desc, 'to_alipay_dict'):
                params['app_desc'] = self.app_desc.to_alipay_dict()
            else:
                params['app_desc'] = self.app_desc
        if self.app_english_name:
            if hasattr(self.app_english_name, 'to_alipay_dict'):
                params['app_english_name'] = self.app_english_name.to_alipay_dict()
            else:
                params['app_english_name'] = self.app_english_name
        if self.app_logo:
            if hasattr(self.app_logo, 'to_alipay_dict'):
                params['app_logo'] = self.app_logo.to_alipay_dict()
            else:
                params['app_logo'] = self.app_logo
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_origin:
            if hasattr(self.app_origin, 'to_alipay_dict'):
                params['app_origin'] = self.app_origin.to_alipay_dict()
            else:
                params['app_origin'] = self.app_origin
        if self.app_slogan:
            if hasattr(self.app_slogan, 'to_alipay_dict'):
                params['app_slogan'] = self.app_slogan.to_alipay_dict()
            else:
                params['app_slogan'] = self.app_slogan
        if self.app_sub_type:
            if hasattr(self.app_sub_type, 'to_alipay_dict'):
                params['app_sub_type'] = self.app_sub_type.to_alipay_dict()
            else:
                params['app_sub_type'] = self.app_sub_type
        if self.app_type:
            if hasattr(self.app_type, 'to_alipay_dict'):
                params['app_type'] = self.app_type.to_alipay_dict()
            else:
                params['app_type'] = self.app_type
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
        if self.mini_category_ids:
            if hasattr(self.mini_category_ids, 'to_alipay_dict'):
                params['mini_category_ids'] = self.mini_category_ids.to_alipay_dict()
            else:
                params['mini_category_ids'] = self.mini_category_ids
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.service_email:
            if hasattr(self.service_email, 'to_alipay_dict'):
                params['service_email'] = self.service_email.to_alipay_dict()
            else:
                params['service_email'] = self.service_email
        if self.service_phone:
            if hasattr(self.service_phone, 'to_alipay_dict'):
                params['service_phone'] = self.service_phone.to_alipay_dict()
            else:
                params['service_phone'] = self.service_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerappCreateModel()
        if 'app_category_ids' in d:
            o.app_category_ids = d['app_category_ids']
        if 'app_desc' in d:
            o.app_desc = d['app_desc']
        if 'app_english_name' in d:
            o.app_english_name = d['app_english_name']
        if 'app_logo' in d:
            o.app_logo = d['app_logo']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_origin' in d:
            o.app_origin = d['app_origin']
        if 'app_slogan' in d:
            o.app_slogan = d['app_slogan']
        if 'app_sub_type' in d:
            o.app_sub_type = d['app_sub_type']
        if 'app_type' in d:
            o.app_type = d['app_type']
        if 'isv_app_id' in d:
            o.isv_app_id = d['isv_app_id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'mini_category_ids' in d:
            o.mini_category_ids = d['mini_category_ids']
        if 'pid' in d:
            o.pid = d['pid']
        if 'service_email' in d:
            o.service_email = d['service_email']
        if 'service_phone' in d:
            o.service_phone = d['service_phone']
        return o


