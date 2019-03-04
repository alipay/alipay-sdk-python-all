#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneProductAgreementSignModel(object):

    def __init__(self):
        self._agreement_sign_type = None
        self._alipay_user_id = None
        self._channel = None
        self._effect_end_time = None
        self._effect_start_time = None
        self._item_id = None
        self._sign_user_id = None
        self._sign_user_type = None

    @property
    def agreement_sign_type(self):
        return self._agreement_sign_type

    @agreement_sign_type.setter
    def agreement_sign_type(self, value):
        self._agreement_sign_type = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def effect_end_time(self):
        return self._effect_end_time

    @effect_end_time.setter
    def effect_end_time(self, value):
        self._effect_end_time = value
    @property
    def effect_start_time(self):
        return self._effect_start_time

    @effect_start_time.setter
    def effect_start_time(self, value):
        self._effect_start_time = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def sign_user_id(self):
        return self._sign_user_id

    @sign_user_id.setter
    def sign_user_id(self, value):
        self._sign_user_id = value
    @property
    def sign_user_type(self):
        return self._sign_user_type

    @sign_user_type.setter
    def sign_user_type(self, value):
        self._sign_user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_sign_type:
            if hasattr(self.agreement_sign_type, 'to_alipay_dict'):
                params['agreement_sign_type'] = self.agreement_sign_type.to_alipay_dict()
            else:
                params['agreement_sign_type'] = self.agreement_sign_type
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.effect_end_time:
            if hasattr(self.effect_end_time, 'to_alipay_dict'):
                params['effect_end_time'] = self.effect_end_time.to_alipay_dict()
            else:
                params['effect_end_time'] = self.effect_end_time
        if self.effect_start_time:
            if hasattr(self.effect_start_time, 'to_alipay_dict'):
                params['effect_start_time'] = self.effect_start_time.to_alipay_dict()
            else:
                params['effect_start_time'] = self.effect_start_time
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.sign_user_id:
            if hasattr(self.sign_user_id, 'to_alipay_dict'):
                params['sign_user_id'] = self.sign_user_id.to_alipay_dict()
            else:
                params['sign_user_id'] = self.sign_user_id
        if self.sign_user_type:
            if hasattr(self.sign_user_type, 'to_alipay_dict'):
                params['sign_user_type'] = self.sign_user_type.to_alipay_dict()
            else:
                params['sign_user_type'] = self.sign_user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneProductAgreementSignModel()
        if 'agreement_sign_type' in d:
            o.agreement_sign_type = d['agreement_sign_type']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'effect_end_time' in d:
            o.effect_end_time = d['effect_end_time']
        if 'effect_start_time' in d:
            o.effect_start_time = d['effect_start_time']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'sign_user_id' in d:
            o.sign_user_id = d['sign_user_id']
        if 'sign_user_type' in d:
            o.sign_user_type = d['sign_user_type']
        return o


