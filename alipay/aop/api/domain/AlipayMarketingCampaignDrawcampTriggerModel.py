#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignDrawcampTriggerModel(object):

    def __init__(self):
        self._bind_mobile = None
        self._camp_id = None
        self._camp_source = None
        self._channel_info = None
        self._client_ip = None
        self._json_ua = None
        self._login_id = None
        self._out_biz_no = None
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
    def camp_source(self):
        return self._camp_source

    @camp_source.setter
    def camp_source(self, value):
        self._camp_source = value
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
    def json_ua(self):
        return self._json_ua

    @json_ua.setter
    def json_ua(self, value):
        self._json_ua = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
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
        if self.camp_source:
            if hasattr(self.camp_source, 'to_alipay_dict'):
                params['camp_source'] = self.camp_source.to_alipay_dict()
            else:
                params['camp_source'] = self.camp_source
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
        if self.json_ua:
            if hasattr(self.json_ua, 'to_alipay_dict'):
                params['json_ua'] = self.json_ua.to_alipay_dict()
            else:
                params['json_ua'] = self.json_ua
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        o = AlipayMarketingCampaignDrawcampTriggerModel()
        if 'bind_mobile' in d:
            o.bind_mobile = d['bind_mobile']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'camp_source' in d:
            o.camp_source = d['camp_source']
        if 'channel_info' in d:
            o.channel_info = d['channel_info']
        if 'client_ip' in d:
            o.client_ip = d['client_ip']
        if 'json_ua' in d:
            o.json_ua = d['json_ua']
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


