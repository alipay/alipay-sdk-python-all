#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAccountInvitedConvertSyncModel(object):

    def __init__(self):
        self._convert_tag = None
        self._user_id = None

    @property
    def convert_tag(self):
        return self._convert_tag

    @convert_tag.setter
    def convert_tag(self, value):
        self._convert_tag = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.convert_tag:
            if hasattr(self.convert_tag, 'to_alipay_dict'):
                params['convert_tag'] = self.convert_tag.to_alipay_dict()
            else:
                params['convert_tag'] = self.convert_tag
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
        o = AlipayUserAccountInvitedConvertSyncModel()
        if 'convert_tag' in d:
            o.convert_tag = d['convert_tag']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


