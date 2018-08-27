#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayQueryCardModelResult(object):

    def __init__(self):
        self._balance = None
        self._card_data = None
        self._card_no = None
        self._card_status = None
        self._card_type = None
        self._ext_info = None
        self._last_update_time = None
        self._status_code = None
        self._status_msg = None
        self._user_auth_info = None
        self._user_id = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def card_data(self):
        return self._card_data

    @card_data.setter
    def card_data(self, value):
        self._card_data = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_status(self):
        return self._card_status

    @card_status.setter
    def card_status(self, value):
        self._card_status = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def last_update_time(self):
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, value):
        self._last_update_time = value
    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value
    @property
    def status_msg(self):
        return self._status_msg

    @status_msg.setter
    def status_msg(self, value):
        self._status_msg = value
    @property
    def user_auth_info(self):
        return self._user_auth_info

    @user_auth_info.setter
    def user_auth_info(self, value):
        self._user_auth_info = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.card_data:
            if hasattr(self.card_data, 'to_alipay_dict'):
                params['card_data'] = self.card_data.to_alipay_dict()
            else:
                params['card_data'] = self.card_data
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_status:
            if hasattr(self.card_status, 'to_alipay_dict'):
                params['card_status'] = self.card_status.to_alipay_dict()
            else:
                params['card_status'] = self.card_status
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.last_update_time:
            if hasattr(self.last_update_time, 'to_alipay_dict'):
                params['last_update_time'] = self.last_update_time.to_alipay_dict()
            else:
                params['last_update_time'] = self.last_update_time
        if self.status_code:
            if hasattr(self.status_code, 'to_alipay_dict'):
                params['status_code'] = self.status_code.to_alipay_dict()
            else:
                params['status_code'] = self.status_code
        if self.status_msg:
            if hasattr(self.status_msg, 'to_alipay_dict'):
                params['status_msg'] = self.status_msg.to_alipay_dict()
            else:
                params['status_msg'] = self.status_msg
        if self.user_auth_info:
            if hasattr(self.user_auth_info, 'to_alipay_dict'):
                params['user_auth_info'] = self.user_auth_info.to_alipay_dict()
            else:
                params['user_auth_info'] = self.user_auth_info
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
        o = AlipayQueryCardModelResult()
        if 'balance' in d:
            o.balance = d['balance']
        if 'card_data' in d:
            o.card_data = d['card_data']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_status' in d:
            o.card_status = d['card_status']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'last_update_time' in d:
            o.last_update_time = d['last_update_time']
        if 'status_code' in d:
            o.status_code = d['status_code']
        if 'status_msg' in d:
            o.status_msg = d['status_msg']
        if 'user_auth_info' in d:
            o.user_auth_info = d['user_auth_info']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


