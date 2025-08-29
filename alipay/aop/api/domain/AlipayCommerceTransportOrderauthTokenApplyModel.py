#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AuthTokenApplyExtInfo import AuthTokenApplyExtInfo


class AlipayCommerceTransportOrderauthTokenApplyModel(object):

    def __init__(self):
        self._auth_appid = None
        self._auth_industry = None
        self._ext_info = None
        self._id_card_number = None
        self._open_id = None
        self._phone_number = None
        self._user_id = None
        self._user_info_source = None

    @property
    def auth_appid(self):
        return self._auth_appid

    @auth_appid.setter
    def auth_appid(self, value):
        self._auth_appid = value
    @property
    def auth_industry(self):
        return self._auth_industry

    @auth_industry.setter
    def auth_industry(self, value):
        self._auth_industry = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, AuthTokenApplyExtInfo):
            self._ext_info = value
        else:
            self._ext_info = AuthTokenApplyExtInfo.from_alipay_dict(value)
    @property
    def id_card_number(self):
        return self._id_card_number

    @id_card_number.setter
    def id_card_number(self, value):
        self._id_card_number = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_info_source(self):
        return self._user_info_source

    @user_info_source.setter
    def user_info_source(self, value):
        self._user_info_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_appid:
            if hasattr(self.auth_appid, 'to_alipay_dict'):
                params['auth_appid'] = self.auth_appid.to_alipay_dict()
            else:
                params['auth_appid'] = self.auth_appid
        if self.auth_industry:
            if hasattr(self.auth_industry, 'to_alipay_dict'):
                params['auth_industry'] = self.auth_industry.to_alipay_dict()
            else:
                params['auth_industry'] = self.auth_industry
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.id_card_number:
            if hasattr(self.id_card_number, 'to_alipay_dict'):
                params['id_card_number'] = self.id_card_number.to_alipay_dict()
            else:
                params['id_card_number'] = self.id_card_number
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_info_source:
            if hasattr(self.user_info_source, 'to_alipay_dict'):
                params['user_info_source'] = self.user_info_source.to_alipay_dict()
            else:
                params['user_info_source'] = self.user_info_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportOrderauthTokenApplyModel()
        if 'auth_appid' in d:
            o.auth_appid = d['auth_appid']
        if 'auth_industry' in d:
            o.auth_industry = d['auth_industry']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'id_card_number' in d:
            o.id_card_number = d['id_card_number']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_info_source' in d:
            o.user_info_source = d['user_info_source']
        return o


