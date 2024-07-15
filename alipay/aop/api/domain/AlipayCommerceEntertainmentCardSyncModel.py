#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEntertainmentCardSyncModel(object):

    def __init__(self):
        self._active_date = None
        self._biz_date = None
        self._expire_date = None
        self._level = None
        self._message_flag = None
        self._open_id = None
        self._serial_number = None
        self._template_code = None
        self._user_id = None

    @property
    def active_date(self):
        return self._active_date

    @active_date.setter
    def active_date(self, value):
        self._active_date = value
    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def message_flag(self):
        return self._message_flag

    @message_flag.setter
    def message_flag(self, value):
        self._message_flag = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        self._serial_number = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_date:
            if hasattr(self.active_date, 'to_alipay_dict'):
                params['active_date'] = self.active_date.to_alipay_dict()
            else:
                params['active_date'] = self.active_date
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.message_flag:
            if hasattr(self.message_flag, 'to_alipay_dict'):
                params['message_flag'] = self.message_flag.to_alipay_dict()
            else:
                params['message_flag'] = self.message_flag
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.serial_number:
            if hasattr(self.serial_number, 'to_alipay_dict'):
                params['serial_number'] = self.serial_number.to_alipay_dict()
            else:
                params['serial_number'] = self.serial_number
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
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
        o = AlipayCommerceEntertainmentCardSyncModel()
        if 'active_date' in d:
            o.active_date = d['active_date']
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'level' in d:
            o.level = d['level']
        if 'message_flag' in d:
            o.message_flag = d['message_flag']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'serial_number' in d:
            o.serial_number = d['serial_number']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


