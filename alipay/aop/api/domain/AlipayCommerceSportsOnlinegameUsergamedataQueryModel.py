#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsOnlinegameUsergamedataQueryModel(object):

    def __init__(self):
        self._open_id = None
        self._out_user_game_no = None
        self._page_index = None
        self._page_size = None
        self._user_game_id = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_user_game_no(self):
        return self._out_user_game_no

    @out_user_game_no.setter
    def out_user_game_no(self, value):
        self._out_user_game_no = value
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def user_game_id(self):
        return self._user_game_id

    @user_game_id.setter
    def user_game_id(self, value):
        self._user_game_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_user_game_no:
            if hasattr(self.out_user_game_no, 'to_alipay_dict'):
                params['out_user_game_no'] = self.out_user_game_no.to_alipay_dict()
            else:
                params['out_user_game_no'] = self.out_user_game_no
        if self.page_index:
            if hasattr(self.page_index, 'to_alipay_dict'):
                params['page_index'] = self.page_index.to_alipay_dict()
            else:
                params['page_index'] = self.page_index
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.user_game_id:
            if hasattr(self.user_game_id, 'to_alipay_dict'):
                params['user_game_id'] = self.user_game_id.to_alipay_dict()
            else:
                params['user_game_id'] = self.user_game_id
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
        o = AlipayCommerceSportsOnlinegameUsergamedataQueryModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_user_game_no' in d:
            o.out_user_game_no = d['out_user_game_no']
        if 'page_index' in d:
            o.page_index = d['page_index']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'user_game_id' in d:
            o.user_game_id = d['user_game_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


