#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTravelGkaCampprizeQueryModel(object):

    def __init__(self):
        self._camp_id = None
        self._login_mobile = None
        self._user_id = None

    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def login_mobile(self):
        return self._login_mobile

    @login_mobile.setter
    def login_mobile(self, value):
        self._login_mobile = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.login_mobile:
            if hasattr(self.login_mobile, 'to_alipay_dict'):
                params['login_mobile'] = self.login_mobile.to_alipay_dict()
            else:
                params['login_mobile'] = self.login_mobile
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
        o = AlipayOverseasTravelGkaCampprizeQueryModel()
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'login_mobile' in d:
            o.login_mobile = d['login_mobile']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


