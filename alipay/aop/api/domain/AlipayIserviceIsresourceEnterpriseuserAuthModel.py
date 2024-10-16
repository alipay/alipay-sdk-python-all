#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsresourceEnterpriseuserAuthModel(object):

    def __init__(self):
        self._auth_account = None
        self._auth_channel = None
        self._tnt_inst_id = None

    @property
    def auth_account(self):
        return self._auth_account

    @auth_account.setter
    def auth_account(self, value):
        self._auth_account = value
    @property
    def auth_channel(self):
        return self._auth_channel

    @auth_channel.setter
    def auth_channel(self, value):
        self._auth_channel = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_account:
            if hasattr(self.auth_account, 'to_alipay_dict'):
                params['auth_account'] = self.auth_account.to_alipay_dict()
            else:
                params['auth_account'] = self.auth_account
        if self.auth_channel:
            if hasattr(self.auth_channel, 'to_alipay_dict'):
                params['auth_channel'] = self.auth_channel.to_alipay_dict()
            else:
                params['auth_channel'] = self.auth_channel
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIsresourceEnterpriseuserAuthModel()
        if 'auth_account' in d:
            o.auth_account = d['auth_account']
        if 'auth_channel' in d:
            o.auth_channel = d['auth_channel']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


