#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserSportshealthAccountDepositModel(object):

    def __init__(self):
        self._apdid_token = None
        self._award_amount = None
        self._client_ip = None
        self._is_award_directly = None
        self._open_id = None
        self._out_biz_channel = None
        self._out_biz_no = None
        self._sub_scene = None
        self._user_id = None

    @property
    def apdid_token(self):
        return self._apdid_token

    @apdid_token.setter
    def apdid_token(self, value):
        self._apdid_token = value
    @property
    def award_amount(self):
        return self._award_amount

    @award_amount.setter
    def award_amount(self, value):
        self._award_amount = value
    @property
    def client_ip(self):
        return self._client_ip

    @client_ip.setter
    def client_ip(self, value):
        self._client_ip = value
    @property
    def is_award_directly(self):
        return self._is_award_directly

    @is_award_directly.setter
    def is_award_directly(self, value):
        self._is_award_directly = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_channel(self):
        return self._out_biz_channel

    @out_biz_channel.setter
    def out_biz_channel(self, value):
        self._out_biz_channel = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def sub_scene(self):
        return self._sub_scene

    @sub_scene.setter
    def sub_scene(self, value):
        self._sub_scene = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apdid_token:
            if hasattr(self.apdid_token, 'to_alipay_dict'):
                params['apdid_token'] = self.apdid_token.to_alipay_dict()
            else:
                params['apdid_token'] = self.apdid_token
        if self.award_amount:
            if hasattr(self.award_amount, 'to_alipay_dict'):
                params['award_amount'] = self.award_amount.to_alipay_dict()
            else:
                params['award_amount'] = self.award_amount
        if self.client_ip:
            if hasattr(self.client_ip, 'to_alipay_dict'):
                params['client_ip'] = self.client_ip.to_alipay_dict()
            else:
                params['client_ip'] = self.client_ip
        if self.is_award_directly:
            if hasattr(self.is_award_directly, 'to_alipay_dict'):
                params['is_award_directly'] = self.is_award_directly.to_alipay_dict()
            else:
                params['is_award_directly'] = self.is_award_directly
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_channel:
            if hasattr(self.out_biz_channel, 'to_alipay_dict'):
                params['out_biz_channel'] = self.out_biz_channel.to_alipay_dict()
            else:
                params['out_biz_channel'] = self.out_biz_channel
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.sub_scene:
            if hasattr(self.sub_scene, 'to_alipay_dict'):
                params['sub_scene'] = self.sub_scene.to_alipay_dict()
            else:
                params['sub_scene'] = self.sub_scene
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
        o = AlipayUserSportshealthAccountDepositModel()
        if 'apdid_token' in d:
            o.apdid_token = d['apdid_token']
        if 'award_amount' in d:
            o.award_amount = d['award_amount']
        if 'client_ip' in d:
            o.client_ip = d['client_ip']
        if 'is_award_directly' in d:
            o.is_award_directly = d['is_award_directly']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_channel' in d:
            o.out_biz_channel = d['out_biz_channel']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'sub_scene' in d:
            o.sub_scene = d['sub_scene']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


