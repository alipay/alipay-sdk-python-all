#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignUnitedopencouponConfigQueryModel(object):

    def __init__(self):
        self._bind_mobile = None
        self._camp_id = None
        self._channel_info = None
        self._client_ip = None
        self._login_id = None
        self._open_id = None
        self._term_id = None
        self._user_id = None

    @property
    def bind_mobile(self):
        return self._bind_mobile

    @bind_mobile.setter
    def bind_mobile(self, value):
        self._bind_mobile = value
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def channel_info(self):
        return self._channel_info

    @channel_info.setter
    def channel_info(self, value):
        self._channel_info = value
    @property
    def client_ip(self):
        return self._client_ip

    @client_ip.setter
    def client_ip(self, value):
        self._client_ip = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def term_id(self):
        return self._term_id

    @term_id.setter
    def term_id(self, value):
        self._term_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_mobile:
            if hasattr(self.bind_mobile, 'to_alipay_dict'):
                params['bind_mobile'] = self.bind_mobile.to_alipay_dict()
            else:
                params['bind_mobile'] = self.bind_mobile
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.channel_info:
            if hasattr(self.channel_info, 'to_alipay_dict'):
                params['channel_info'] = self.channel_info.to_alipay_dict()
            else:
                params['channel_info'] = self.channel_info
        if self.client_ip:
            if hasattr(self.client_ip, 'to_alipay_dict'):
                params['client_ip'] = self.client_ip.to_alipay_dict()
            else:
                params['client_ip'] = self.client_ip
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.term_id:
            if hasattr(self.term_id, 'to_alipay_dict'):
                params['term_id'] = self.term_id.to_alipay_dict()
            else:
                params['term_id'] = self.term_id
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
        o = AlipayMarketingCampaignUnitedopencouponConfigQueryModel()
        if 'bind_mobile' in d:
            o.bind_mobile = d['bind_mobile']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'channel_info' in d:
            o.channel_info = d['channel_info']
        if 'client_ip' in d:
            o.client_ip = d['client_ip']
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'term_id' in d:
            o.term_id = d['term_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


