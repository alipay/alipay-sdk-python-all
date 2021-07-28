#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Member import Member


class MybankCreditSupplychainCreditpaySyncnameCreateModel(object):

    def __init__(self):
        self._apply_time = None
        self._channel_tag = None
        self._handle_type = None
        self._promo_end_time = None
        self._promo_start_time = None
        self._promo_type = None
        self._promo_value = None
        self._request_id = None
        self._scene_user_id = None
        self._seller = None

    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def channel_tag(self):
        return self._channel_tag

    @channel_tag.setter
    def channel_tag(self, value):
        self._channel_tag = value
    @property
    def handle_type(self):
        return self._handle_type

    @handle_type.setter
    def handle_type(self, value):
        self._handle_type = value
    @property
    def promo_end_time(self):
        return self._promo_end_time

    @promo_end_time.setter
    def promo_end_time(self, value):
        self._promo_end_time = value
    @property
    def promo_start_time(self):
        return self._promo_start_time

    @promo_start_time.setter
    def promo_start_time(self, value):
        self._promo_start_time = value
    @property
    def promo_type(self):
        return self._promo_type

    @promo_type.setter
    def promo_type(self, value):
        self._promo_type = value
    @property
    def promo_value(self):
        return self._promo_value

    @promo_value.setter
    def promo_value(self, value):
        self._promo_value = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def scene_user_id(self):
        return self._scene_user_id

    @scene_user_id.setter
    def scene_user_id(self, value):
        self._scene_user_id = value
    @property
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, value):
        if isinstance(value, Member):
            self._seller = value
        else:
            self._seller = Member.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.channel_tag:
            if hasattr(self.channel_tag, 'to_alipay_dict'):
                params['channel_tag'] = self.channel_tag.to_alipay_dict()
            else:
                params['channel_tag'] = self.channel_tag
        if self.handle_type:
            if hasattr(self.handle_type, 'to_alipay_dict'):
                params['handle_type'] = self.handle_type.to_alipay_dict()
            else:
                params['handle_type'] = self.handle_type
        if self.promo_end_time:
            if hasattr(self.promo_end_time, 'to_alipay_dict'):
                params['promo_end_time'] = self.promo_end_time.to_alipay_dict()
            else:
                params['promo_end_time'] = self.promo_end_time
        if self.promo_start_time:
            if hasattr(self.promo_start_time, 'to_alipay_dict'):
                params['promo_start_time'] = self.promo_start_time.to_alipay_dict()
            else:
                params['promo_start_time'] = self.promo_start_time
        if self.promo_type:
            if hasattr(self.promo_type, 'to_alipay_dict'):
                params['promo_type'] = self.promo_type.to_alipay_dict()
            else:
                params['promo_type'] = self.promo_type
        if self.promo_value:
            if hasattr(self.promo_value, 'to_alipay_dict'):
                params['promo_value'] = self.promo_value.to_alipay_dict()
            else:
                params['promo_value'] = self.promo_value
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.scene_user_id:
            if hasattr(self.scene_user_id, 'to_alipay_dict'):
                params['scene_user_id'] = self.scene_user_id.to_alipay_dict()
            else:
                params['scene_user_id'] = self.scene_user_id
        if self.seller:
            if hasattr(self.seller, 'to_alipay_dict'):
                params['seller'] = self.seller.to_alipay_dict()
            else:
                params['seller'] = self.seller
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainCreditpaySyncnameCreateModel()
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'channel_tag' in d:
            o.channel_tag = d['channel_tag']
        if 'handle_type' in d:
            o.handle_type = d['handle_type']
        if 'promo_end_time' in d:
            o.promo_end_time = d['promo_end_time']
        if 'promo_start_time' in d:
            o.promo_start_time = d['promo_start_time']
        if 'promo_type' in d:
            o.promo_type = d['promo_type']
        if 'promo_value' in d:
            o.promo_value = d['promo_value']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'scene_user_id' in d:
            o.scene_user_id = d['scene_user_id']
        if 'seller' in d:
            o.seller = d['seller']
        return o


