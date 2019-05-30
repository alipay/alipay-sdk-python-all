#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMessageEntity(object):

    def __init__(self):
        self._alipay_user_id = None
        self._app_code = None
        self._certificate_number = None
        self._certificate_type = None
        self._certificate_username = None
        self._city_code = None
        self._ext_info = None
        self._industry_type = None
        self._msg_type = None
        self._target_url = None
        self._uuid = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def certificate_number(self):
        return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, value):
        self._certificate_number = value
    @property
    def certificate_type(self):
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, value):
        self._certificate_type = value
    @property
    def certificate_username(self):
        return self._certificate_username

    @certificate_username.setter
    def certificate_username(self, value):
        self._certificate_username = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def industry_type(self):
        return self._industry_type

    @industry_type.setter
    def industry_type(self, value):
        self._industry_type = value
    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value
    @property
    def target_url(self):
        return self._target_url

    @target_url.setter
    def target_url(self, value):
        self._target_url = value
    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.certificate_number:
            if hasattr(self.certificate_number, 'to_alipay_dict'):
                params['certificate_number'] = self.certificate_number.to_alipay_dict()
            else:
                params['certificate_number'] = self.certificate_number
        if self.certificate_type:
            if hasattr(self.certificate_type, 'to_alipay_dict'):
                params['certificate_type'] = self.certificate_type.to_alipay_dict()
            else:
                params['certificate_type'] = self.certificate_type
        if self.certificate_username:
            if hasattr(self.certificate_username, 'to_alipay_dict'):
                params['certificate_username'] = self.certificate_username.to_alipay_dict()
            else:
                params['certificate_username'] = self.certificate_username
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.industry_type:
            if hasattr(self.industry_type, 'to_alipay_dict'):
                params['industry_type'] = self.industry_type.to_alipay_dict()
            else:
                params['industry_type'] = self.industry_type
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = self.msg_type.to_alipay_dict()
            else:
                params['msg_type'] = self.msg_type
        if self.target_url:
            if hasattr(self.target_url, 'to_alipay_dict'):
                params['target_url'] = self.target_url.to_alipay_dict()
            else:
                params['target_url'] = self.target_url
        if self.uuid:
            if hasattr(self.uuid, 'to_alipay_dict'):
                params['uuid'] = self.uuid.to_alipay_dict()
            else:
                params['uuid'] = self.uuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMessageEntity()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'certificate_number' in d:
            o.certificate_number = d['certificate_number']
        if 'certificate_type' in d:
            o.certificate_type = d['certificate_type']
        if 'certificate_username' in d:
            o.certificate_username = d['certificate_username']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'industry_type' in d:
            o.industry_type = d['industry_type']
        if 'msg_type' in d:
            o.msg_type = d['msg_type']
        if 'target_url' in d:
            o.target_url = d['target_url']
        if 'uuid' in d:
            o.uuid = d['uuid']
        return o


