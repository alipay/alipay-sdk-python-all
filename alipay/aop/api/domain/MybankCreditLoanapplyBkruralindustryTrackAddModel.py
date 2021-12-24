#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoanapplyBkruralindustryTrackAddModel(object):

    def __init__(self):
        self._business_no = None
        self._channel = None
        self._identity_type = None
        self._request_id = None
        self._scene = None
        self._track_data = None
        self._uid = None

    @property
    def business_no(self):
        return self._business_no

    @business_no.setter
    def business_no(self, value):
        self._business_no = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def track_data(self):
        return self._track_data

    @track_data.setter
    def track_data(self, value):
        self._track_data = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_no:
            if hasattr(self.business_no, 'to_alipay_dict'):
                params['business_no'] = self.business_no.to_alipay_dict()
            else:
                params['business_no'] = self.business_no
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.track_data:
            if hasattr(self.track_data, 'to_alipay_dict'):
                params['track_data'] = self.track_data.to_alipay_dict()
            else:
                params['track_data'] = self.track_data
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoanapplyBkruralindustryTrackAddModel()
        if 'business_no' in d:
            o.business_no = d['business_no']
        if 'channel' in d:
            o.channel = d['channel']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'scene' in d:
            o.scene = d['scene']
        if 'track_data' in d:
            o.track_data = d['track_data']
        if 'uid' in d:
            o.uid = d['uid']
        return o


