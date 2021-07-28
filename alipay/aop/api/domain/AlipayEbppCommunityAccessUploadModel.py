#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppCommunityAccessUploadModel(object):

    def __init__(self):
        self._community_short_name = None
        self._dev_id = None
        self._enter_error_message = None
        self._enter_record_id = None
        self._enter_success = None
        self._enter_time = None
        self._user_id_encrypt = None

    @property
    def community_short_name(self):
        return self._community_short_name

    @community_short_name.setter
    def community_short_name(self, value):
        self._community_short_name = value
    @property
    def dev_id(self):
        return self._dev_id

    @dev_id.setter
    def dev_id(self, value):
        self._dev_id = value
    @property
    def enter_error_message(self):
        return self._enter_error_message

    @enter_error_message.setter
    def enter_error_message(self, value):
        self._enter_error_message = value
    @property
    def enter_record_id(self):
        return self._enter_record_id

    @enter_record_id.setter
    def enter_record_id(self, value):
        self._enter_record_id = value
    @property
    def enter_success(self):
        return self._enter_success

    @enter_success.setter
    def enter_success(self, value):
        self._enter_success = value
    @property
    def enter_time(self):
        return self._enter_time

    @enter_time.setter
    def enter_time(self, value):
        self._enter_time = value
    @property
    def user_id_encrypt(self):
        return self._user_id_encrypt

    @user_id_encrypt.setter
    def user_id_encrypt(self, value):
        self._user_id_encrypt = value


    def to_alipay_dict(self):
        params = dict()
        if self.community_short_name:
            if hasattr(self.community_short_name, 'to_alipay_dict'):
                params['community_short_name'] = self.community_short_name.to_alipay_dict()
            else:
                params['community_short_name'] = self.community_short_name
        if self.dev_id:
            if hasattr(self.dev_id, 'to_alipay_dict'):
                params['dev_id'] = self.dev_id.to_alipay_dict()
            else:
                params['dev_id'] = self.dev_id
        if self.enter_error_message:
            if hasattr(self.enter_error_message, 'to_alipay_dict'):
                params['enter_error_message'] = self.enter_error_message.to_alipay_dict()
            else:
                params['enter_error_message'] = self.enter_error_message
        if self.enter_record_id:
            if hasattr(self.enter_record_id, 'to_alipay_dict'):
                params['enter_record_id'] = self.enter_record_id.to_alipay_dict()
            else:
                params['enter_record_id'] = self.enter_record_id
        if self.enter_success:
            if hasattr(self.enter_success, 'to_alipay_dict'):
                params['enter_success'] = self.enter_success.to_alipay_dict()
            else:
                params['enter_success'] = self.enter_success
        if self.enter_time:
            if hasattr(self.enter_time, 'to_alipay_dict'):
                params['enter_time'] = self.enter_time.to_alipay_dict()
            else:
                params['enter_time'] = self.enter_time
        if self.user_id_encrypt:
            if hasattr(self.user_id_encrypt, 'to_alipay_dict'):
                params['user_id_encrypt'] = self.user_id_encrypt.to_alipay_dict()
            else:
                params['user_id_encrypt'] = self.user_id_encrypt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppCommunityAccessUploadModel()
        if 'community_short_name' in d:
            o.community_short_name = d['community_short_name']
        if 'dev_id' in d:
            o.dev_id = d['dev_id']
        if 'enter_error_message' in d:
            o.enter_error_message = d['enter_error_message']
        if 'enter_record_id' in d:
            o.enter_record_id = d['enter_record_id']
        if 'enter_success' in d:
            o.enter_success = d['enter_success']
        if 'enter_time' in d:
            o.enter_time = d['enter_time']
        if 'user_id_encrypt' in d:
            o.user_id_encrypt = d['user_id_encrypt']
        return o


