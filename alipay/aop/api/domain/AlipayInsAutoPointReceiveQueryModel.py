#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsAutoPointReceiveQueryModel(object):

    def __init__(self):
        self._auto_campaign_type = None
        self._open_id = None
        self._scene_type = None
        self._user_id = None

    @property
    def auto_campaign_type(self):
        return self._auto_campaign_type

    @auto_campaign_type.setter
    def auto_campaign_type(self, value):
        self._auto_campaign_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auto_campaign_type:
            if hasattr(self.auto_campaign_type, 'to_alipay_dict'):
                params['auto_campaign_type'] = self.auto_campaign_type.to_alipay_dict()
            else:
                params['auto_campaign_type'] = self.auto_campaign_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
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
        o = AlipayInsAutoPointReceiveQueryModel()
        if 'auto_campaign_type' in d:
            o.auto_campaign_type = d['auto_campaign_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


