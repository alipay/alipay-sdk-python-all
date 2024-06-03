#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmMiniappServiceurlQueryModel(object):

    def __init__(self):
        self._biz_tag = None
        self._force_use_bc_chat = None
        self._open_id = None
        self._user_id = None

    @property
    def biz_tag(self):
        return self._biz_tag

    @biz_tag.setter
    def biz_tag(self, value):
        self._biz_tag = value
    @property
    def force_use_bc_chat(self):
        return self._force_use_bc_chat

    @force_use_bc_chat.setter
    def force_use_bc_chat(self, value):
        self._force_use_bc_chat = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tag:
            if hasattr(self.biz_tag, 'to_alipay_dict'):
                params['biz_tag'] = self.biz_tag.to_alipay_dict()
            else:
                params['biz_tag'] = self.biz_tag
        if self.force_use_bc_chat:
            if hasattr(self.force_use_bc_chat, 'to_alipay_dict'):
                params['force_use_bc_chat'] = self.force_use_bc_chat.to_alipay_dict()
            else:
                params['force_use_bc_chat'] = self.force_use_bc_chat
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = AlipayIserviceCcmMiniappServiceurlQueryModel()
        if 'biz_tag' in d:
            o.biz_tag = d['biz_tag']
        if 'force_use_bc_chat' in d:
            o.force_use_bc_chat = d['force_use_bc_chat']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


