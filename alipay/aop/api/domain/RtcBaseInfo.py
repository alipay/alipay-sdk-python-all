#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RtcBaseInfo(object):

    def __init__(self):
        self._channel_id = None
        self._rtc_app_id = None
        self._rtc_token = None
        self._rtc_user_id = None
        self._session_id = None

    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def rtc_app_id(self):
        return self._rtc_app_id

    @rtc_app_id.setter
    def rtc_app_id(self, value):
        self._rtc_app_id = value
    @property
    def rtc_token(self):
        return self._rtc_token

    @rtc_token.setter
    def rtc_token(self, value):
        self._rtc_token = value
    @property
    def rtc_user_id(self):
        return self._rtc_user_id

    @rtc_user_id.setter
    def rtc_user_id(self, value):
        self._rtc_user_id = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.rtc_app_id:
            if hasattr(self.rtc_app_id, 'to_alipay_dict'):
                params['rtc_app_id'] = self.rtc_app_id.to_alipay_dict()
            else:
                params['rtc_app_id'] = self.rtc_app_id
        if self.rtc_token:
            if hasattr(self.rtc_token, 'to_alipay_dict'):
                params['rtc_token'] = self.rtc_token.to_alipay_dict()
            else:
                params['rtc_token'] = self.rtc_token
        if self.rtc_user_id:
            if hasattr(self.rtc_user_id, 'to_alipay_dict'):
                params['rtc_user_id'] = self.rtc_user_id.to_alipay_dict()
            else:
                params['rtc_user_id'] = self.rtc_user_id
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RtcBaseInfo()
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'rtc_app_id' in d:
            o.rtc_app_id = d['rtc_app_id']
        if 'rtc_token' in d:
            o.rtc_token = d['rtc_token']
        if 'rtc_user_id' in d:
            o.rtc_user_id = d['rtc_user_id']
        if 'session_id' in d:
            o.session_id = d['session_id']
        return o


