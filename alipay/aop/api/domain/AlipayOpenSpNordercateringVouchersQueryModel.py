#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNordercateringVouchersQueryModel(object):

    def __init__(self):
        self._app_token = None
        self._client_type = None
        self._desk_no = None
        self._phone = None
        self._shop_id = None
        self._user_id = None
        self._user_open_id = None
        self._wx_id = None

    @property
    def app_token(self):
        return self._app_token

    @app_token.setter
    def app_token(self, value):
        self._app_token = value
    @property
    def client_type(self):
        return self._client_type

    @client_type.setter
    def client_type(self, value):
        self._client_type = value
    @property
    def desk_no(self):
        return self._desk_no

    @desk_no.setter
    def desk_no(self, value):
        self._desk_no = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_open_id(self):
        return self._user_open_id

    @user_open_id.setter
    def user_open_id(self, value):
        self._user_open_id = value
    @property
    def wx_id(self):
        return self._wx_id

    @wx_id.setter
    def wx_id(self, value):
        self._wx_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_token:
            if hasattr(self.app_token, 'to_alipay_dict'):
                params['app_token'] = self.app_token.to_alipay_dict()
            else:
                params['app_token'] = self.app_token
        if self.client_type:
            if hasattr(self.client_type, 'to_alipay_dict'):
                params['client_type'] = self.client_type.to_alipay_dict()
            else:
                params['client_type'] = self.client_type
        if self.desk_no:
            if hasattr(self.desk_no, 'to_alipay_dict'):
                params['desk_no'] = self.desk_no.to_alipay_dict()
            else:
                params['desk_no'] = self.desk_no
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_open_id:
            if hasattr(self.user_open_id, 'to_alipay_dict'):
                params['user_open_id'] = self.user_open_id.to_alipay_dict()
            else:
                params['user_open_id'] = self.user_open_id
        if self.wx_id:
            if hasattr(self.wx_id, 'to_alipay_dict'):
                params['wx_id'] = self.wx_id.to_alipay_dict()
            else:
                params['wx_id'] = self.wx_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNordercateringVouchersQueryModel()
        if 'app_token' in d:
            o.app_token = d['app_token']
        if 'client_type' in d:
            o.client_type = d['client_type']
        if 'desk_no' in d:
            o.desk_no = d['desk_no']
        if 'phone' in d:
            o.phone = d['phone']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_open_id' in d:
            o.user_open_id = d['user_open_id']
        if 'wx_id' in d:
            o.wx_id = d['wx_id']
        return o


