#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcomItemExtendDetailDTO(object):

    def __init__(self):
        self._ext_info = None
        self._game_account = None
        self._game_account_client = None
        self._game_account_client_id = None
        self._game_id = None
        self._game_name = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def game_account(self):
        return self._game_account

    @game_account.setter
    def game_account(self, value):
        self._game_account = value
    @property
    def game_account_client(self):
        return self._game_account_client

    @game_account_client.setter
    def game_account_client(self, value):
        self._game_account_client = value
    @property
    def game_account_client_id(self):
        return self._game_account_client_id

    @game_account_client_id.setter
    def game_account_client_id(self, value):
        self._game_account_client_id = value
    @property
    def game_id(self):
        return self._game_id

    @game_id.setter
    def game_id(self, value):
        self._game_id = value
    @property
    def game_name(self):
        return self._game_name

    @game_name.setter
    def game_name(self, value):
        self._game_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.game_account:
            if hasattr(self.game_account, 'to_alipay_dict'):
                params['game_account'] = self.game_account.to_alipay_dict()
            else:
                params['game_account'] = self.game_account
        if self.game_account_client:
            if hasattr(self.game_account_client, 'to_alipay_dict'):
                params['game_account_client'] = self.game_account_client.to_alipay_dict()
            else:
                params['game_account_client'] = self.game_account_client
        if self.game_account_client_id:
            if hasattr(self.game_account_client_id, 'to_alipay_dict'):
                params['game_account_client_id'] = self.game_account_client_id.to_alipay_dict()
            else:
                params['game_account_client_id'] = self.game_account_client_id
        if self.game_id:
            if hasattr(self.game_id, 'to_alipay_dict'):
                params['game_id'] = self.game_id.to_alipay_dict()
            else:
                params['game_id'] = self.game_id
        if self.game_name:
            if hasattr(self.game_name, 'to_alipay_dict'):
                params['game_name'] = self.game_name.to_alipay_dict()
            else:
                params['game_name'] = self.game_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcomItemExtendDetailDTO()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'game_account' in d:
            o.game_account = d['game_account']
        if 'game_account_client' in d:
            o.game_account_client = d['game_account_client']
        if 'game_account_client_id' in d:
            o.game_account_client_id = d['game_account_client_id']
        if 'game_id' in d:
            o.game_id = d['game_id']
        if 'game_name' in d:
            o.game_name = d['game_name']
        return o


