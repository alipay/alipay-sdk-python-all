#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHealthArchiveSaveModel(object):

    def __init__(self):
        self._chat_id = None
        self._data = None
        self._data_id = None
        self._data_name = None
        self._data_source = None
        self._data_sub_type = None
        self._data_type = None
        self._open_id = None
        self._pic_type = None
        self._pic_url = None
        self._session_id = None
        self._user_card_no = None
        self._user_cert_type = None
        self._user_id = None

    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def data_name(self):
        return self._data_name

    @data_name.setter
    def data_name(self, value):
        self._data_name = value
    @property
    def data_source(self):
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        self._data_source = value
    @property
    def data_sub_type(self):
        return self._data_sub_type

    @data_sub_type.setter
    def data_sub_type(self, value):
        self._data_sub_type = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pic_type(self):
        return self._pic_type

    @pic_type.setter
    def pic_type(self, value):
        self._pic_type = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def user_card_no(self):
        return self._user_card_no

    @user_card_no.setter
    def user_card_no(self, value):
        self._user_card_no = value
    @property
    def user_cert_type(self):
        return self._user_cert_type

    @user_cert_type.setter
    def user_cert_type(self, value):
        self._user_cert_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.data_name:
            if hasattr(self.data_name, 'to_alipay_dict'):
                params['data_name'] = self.data_name.to_alipay_dict()
            else:
                params['data_name'] = self.data_name
        if self.data_source:
            if hasattr(self.data_source, 'to_alipay_dict'):
                params['data_source'] = self.data_source.to_alipay_dict()
            else:
                params['data_source'] = self.data_source
        if self.data_sub_type:
            if hasattr(self.data_sub_type, 'to_alipay_dict'):
                params['data_sub_type'] = self.data_sub_type.to_alipay_dict()
            else:
                params['data_sub_type'] = self.data_sub_type
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.pic_type:
            if hasattr(self.pic_type, 'to_alipay_dict'):
                params['pic_type'] = self.pic_type.to_alipay_dict()
            else:
                params['pic_type'] = self.pic_type
        if self.pic_url:
            if hasattr(self.pic_url, 'to_alipay_dict'):
                params['pic_url'] = self.pic_url.to_alipay_dict()
            else:
                params['pic_url'] = self.pic_url
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.user_card_no:
            if hasattr(self.user_card_no, 'to_alipay_dict'):
                params['user_card_no'] = self.user_card_no.to_alipay_dict()
            else:
                params['user_card_no'] = self.user_card_no
        if self.user_cert_type:
            if hasattr(self.user_cert_type, 'to_alipay_dict'):
                params['user_cert_type'] = self.user_cert_type.to_alipay_dict()
            else:
                params['user_cert_type'] = self.user_cert_type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHealthArchiveSaveModel()
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'data' in d:
            o.data = d['data']
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'data_name' in d:
            o.data_name = d['data_name']
        if 'data_source' in d:
            o.data_source = d['data_source']
        if 'data_sub_type' in d:
            o.data_sub_type = d['data_sub_type']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'pic_type' in d:
            o.pic_type = d['pic_type']
        if 'pic_url' in d:
            o.pic_url = d['pic_url']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'user_card_no' in d:
            o.user_card_no = d['user_card_no']
        if 'user_cert_type' in d:
            o.user_cert_type = d['user_cert_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


