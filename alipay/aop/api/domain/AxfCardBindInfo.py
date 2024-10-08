#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AxfCardBindInfo(object):

    def __init__(self):
        self._bind_card_status = None
        self._bind_user_name = None
        self._bind_user_phone = None

    @property
    def bind_card_status(self):
        return self._bind_card_status

    @bind_card_status.setter
    def bind_card_status(self, value):
        self._bind_card_status = value
    @property
    def bind_user_name(self):
        return self._bind_user_name

    @bind_user_name.setter
    def bind_user_name(self, value):
        self._bind_user_name = value
    @property
    def bind_user_phone(self):
        return self._bind_user_phone

    @bind_user_phone.setter
    def bind_user_phone(self, value):
        self._bind_user_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_card_status:
            if hasattr(self.bind_card_status, 'to_alipay_dict'):
                params['bind_card_status'] = self.bind_card_status.to_alipay_dict()
            else:
                params['bind_card_status'] = self.bind_card_status
        if self.bind_user_name:
            if hasattr(self.bind_user_name, 'to_alipay_dict'):
                params['bind_user_name'] = self.bind_user_name.to_alipay_dict()
            else:
                params['bind_user_name'] = self.bind_user_name
        if self.bind_user_phone:
            if hasattr(self.bind_user_phone, 'to_alipay_dict'):
                params['bind_user_phone'] = self.bind_user_phone.to_alipay_dict()
            else:
                params['bind_user_phone'] = self.bind_user_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AxfCardBindInfo()
        if 'bind_card_status' in d:
            o.bind_card_status = d['bind_card_status']
        if 'bind_user_name' in d:
            o.bind_user_name = d['bind_user_name']
        if 'bind_user_phone' in d:
            o.bind_user_phone = d['bind_user_phone']
        return o


