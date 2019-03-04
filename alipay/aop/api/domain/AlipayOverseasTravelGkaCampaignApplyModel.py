#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTravelGkaCampaignApplyModel(object):

    def __init__(self):
        self._camp_id = None
        self._client_ip = None
        self._device_info = None
        self._extend_info = None
        self._json_ua = None
        self._login_mobile = None
        self._user_id = None

    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def client_ip(self):
        return self._client_ip

    @client_ip.setter
    def client_ip(self, value):
        self._client_ip = value
    @property
    def device_info(self):
        return self._device_info

    @device_info.setter
    def device_info(self, value):
        self._device_info = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def json_ua(self):
        return self._json_ua

    @json_ua.setter
    def json_ua(self, value):
        self._json_ua = value
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
        if self.client_ip:
            if hasattr(self.client_ip, 'to_alipay_dict'):
                params['client_ip'] = self.client_ip.to_alipay_dict()
            else:
                params['client_ip'] = self.client_ip
        if self.device_info:
            if hasattr(self.device_info, 'to_alipay_dict'):
                params['device_info'] = self.device_info.to_alipay_dict()
            else:
                params['device_info'] = self.device_info
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.json_ua:
            if hasattr(self.json_ua, 'to_alipay_dict'):
                params['json_ua'] = self.json_ua.to_alipay_dict()
            else:
                params['json_ua'] = self.json_ua
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
        o = AlipayOverseasTravelGkaCampaignApplyModel()
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'client_ip' in d:
            o.client_ip = d['client_ip']
        if 'device_info' in d:
            o.device_info = d['device_info']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'json_ua' in d:
            o.json_ua = d['json_ua']
        if 'login_mobile' in d:
            o.login_mobile = d['login_mobile']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


