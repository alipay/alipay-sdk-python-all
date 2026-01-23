#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingBeneficiaryGroupSyncModel(object):

    def __init__(self):
        self._action_type = None
        self._bind_contact = None
        self._channel = None
        self._login_type = None
        self._out_biz_no = None
        self._scene_code = None
        self._turing_tag = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def bind_contact(self):
        return self._bind_contact

    @bind_contact.setter
    def bind_contact(self, value):
        self._bind_contact = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def login_type(self):
        return self._login_type

    @login_type.setter
    def login_type(self, value):
        self._login_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def turing_tag(self):
        return self._turing_tag

    @turing_tag.setter
    def turing_tag(self, value):
        self._turing_tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.bind_contact:
            if hasattr(self.bind_contact, 'to_alipay_dict'):
                params['bind_contact'] = self.bind_contact.to_alipay_dict()
            else:
                params['bind_contact'] = self.bind_contact
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.login_type:
            if hasattr(self.login_type, 'to_alipay_dict'):
                params['login_type'] = self.login_type.to_alipay_dict()
            else:
                params['login_type'] = self.login_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.turing_tag:
            if hasattr(self.turing_tag, 'to_alipay_dict'):
                params['turing_tag'] = self.turing_tag.to_alipay_dict()
            else:
                params['turing_tag'] = self.turing_tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingBeneficiaryGroupSyncModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'bind_contact' in d:
            o.bind_contact = d['bind_contact']
        if 'channel' in d:
            o.channel = d['channel']
        if 'login_type' in d:
            o.login_type = d['login_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'turing_tag' in d:
            o.turing_tag = d['turing_tag']
        return o


