#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNordercateringItemsQueryModel(object):

    def __init__(self):
        self._app_token = None
        self._client_type = None
        self._desk_no = None
        self._exposed_item_list = None
        self._jump_url = None
        self._phone = None
        self._session_id = None
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
    def exposed_item_list(self):
        return self._exposed_item_list

    @exposed_item_list.setter
    def exposed_item_list(self, value):
        self._exposed_item_list = value
    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
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
        if self.exposed_item_list:
            if hasattr(self.exposed_item_list, 'to_alipay_dict'):
                params['exposed_item_list'] = self.exposed_item_list.to_alipay_dict()
            else:
                params['exposed_item_list'] = self.exposed_item_list
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
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
        o = AlipayOpenSpNordercateringItemsQueryModel()
        if 'app_token' in d:
            o.app_token = d['app_token']
        if 'client_type' in d:
            o.client_type = d['client_type']
        if 'desk_no' in d:
            o.desk_no = d['desk_no']
        if 'exposed_item_list' in d:
            o.exposed_item_list = d['exposed_item_list']
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'phone' in d:
            o.phone = d['phone']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_open_id' in d:
            o.user_open_id = d['user_open_id']
        if 'wx_id' in d:
            o.wx_id = d['wx_id']
        return o


