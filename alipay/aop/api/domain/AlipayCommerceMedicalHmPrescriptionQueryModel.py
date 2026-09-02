#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHmPrescriptionQueryModel(object):

    def __init__(self):
        self._activity_id = None
        self._channels = None
        self._open_id = None
        self._user_uid = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def channels(self):
        return self._channels

    @channels.setter
    def channels(self, value):
        if isinstance(value, list):
            self._channels = list()
            for i in value:
                self._channels.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_uid(self):
        return self._user_uid

    @user_uid.setter
    def user_uid(self, value):
        self._user_uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.channels:
            if isinstance(self.channels, list):
                for i in range(0, len(self.channels)):
                    element = self.channels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.channels[i] = element.to_alipay_dict()
            if hasattr(self.channels, 'to_alipay_dict'):
                params['channels'] = self.channels.to_alipay_dict()
            else:
                params['channels'] = self.channels
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_uid:
            if hasattr(self.user_uid, 'to_alipay_dict'):
                params['user_uid'] = self.user_uid.to_alipay_dict()
            else:
                params['user_uid'] = self.user_uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHmPrescriptionQueryModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'channels' in d:
            o.channels = d['channels']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_uid' in d:
            o.user_uid = d['user_uid']
        return o


