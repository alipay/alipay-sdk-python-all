#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OfferObject import OfferObject


class AlipaySocialBaseContentlibOfferSyncModel(object):

    def __init__(self):
        self._channel_id = None
        self._display_app = None
        self._operate_type = None

    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def display_app(self):
        return self._display_app

    @display_app.setter
    def display_app(self, value):
        if isinstance(value, OfferObject):
            self._display_app = value
        else:
            self._display_app = OfferObject.from_alipay_dict(value)
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.display_app:
            if hasattr(self.display_app, 'to_alipay_dict'):
                params['display_app'] = self.display_app.to_alipay_dict()
            else:
                params['display_app'] = self.display_app
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseContentlibOfferSyncModel()
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'display_app' in d:
            o.display_app = d['display_app']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        return o


