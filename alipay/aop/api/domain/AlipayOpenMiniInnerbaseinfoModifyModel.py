#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerbaseinfoModifyModel(object):

    def __init__(self):
        self._app_alias_name = None
        self._app_category_ids = None
        self._app_desc = None
        self._app_english_name = None
        self._app_key = None
        self._app_logo = None
        self._app_name = None
        self._app_slogan = None
        self._inst_code = None
        self._mini_app_id = None
        self._service_email = None
        self._service_phone = None

    @property
    def app_alias_name(self):
        return self._app_alias_name

    @app_alias_name.setter
    def app_alias_name(self, value):
        self._app_alias_name = value
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
    def app_key(self):
        return self._app_key

    @app_key.setter
    def app_key(self, value):
        self._app_key = value
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
    def app_slogan(self):
        return self._app_slogan

    @app_slogan.setter
    def app_slogan(self, value):
        self._app_slogan = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
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
        if self.app_alias_name:
            if hasattr(self.app_alias_name, 'to_alipay_dict'):
                params['app_alias_name'] = self.app_alias_name.to_alipay_dict()
            else:
                params['app_alias_name'] = self.app_alias_name
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
        if self.app_key:
            if hasattr(self.app_key, 'to_alipay_dict'):
                params['app_key'] = self.app_key.to_alipay_dict()
            else:
                params['app_key'] = self.app_key
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
        if self.app_slogan:
            if hasattr(self.app_slogan, 'to_alipay_dict'):
                params['app_slogan'] = self.app_slogan.to_alipay_dict()
            else:
                params['app_slogan'] = self.app_slogan
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
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
        o = AlipayOpenMiniInnerbaseinfoModifyModel()
        if 'app_alias_name' in d:
            o.app_alias_name = d['app_alias_name']
        if 'app_category_ids' in d:
            o.app_category_ids = d['app_category_ids']
        if 'app_desc' in d:
            o.app_desc = d['app_desc']
        if 'app_english_name' in d:
            o.app_english_name = d['app_english_name']
        if 'app_key' in d:
            o.app_key = d['app_key']
        if 'app_logo' in d:
            o.app_logo = d['app_logo']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_slogan' in d:
            o.app_slogan = d['app_slogan']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'service_email' in d:
            o.service_email = d['service_email']
        if 'service_phone' in d:
            o.service_phone = d['service_phone']
        return o


