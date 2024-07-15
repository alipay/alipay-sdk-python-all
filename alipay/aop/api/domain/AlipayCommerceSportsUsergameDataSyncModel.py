#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsUsergameDataSyncModel(object):

    def __init__(self):
        self._game_id = None
        self._open_id = None
        self._out_user_game_no = None
        self._source_id = None
        self._status = None
        self._user_game_data_id_list = None
        self._user_game_id = None
        self._user_id = None

    @property
    def game_id(self):
        return self._game_id

    @game_id.setter
    def game_id(self, value):
        self._game_id = value
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
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_game_data_id_list(self):
        return self._user_game_data_id_list

    @user_game_data_id_list.setter
    def user_game_data_id_list(self, value):
        if isinstance(value, list):
            self._user_game_data_id_list = list()
            for i in value:
                self._user_game_data_id_list.append(i)
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
        if self.game_id:
            if hasattr(self.game_id, 'to_alipay_dict'):
                params['game_id'] = self.game_id.to_alipay_dict()
            else:
                params['game_id'] = self.game_id
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
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.user_game_data_id_list:
            if isinstance(self.user_game_data_id_list, list):
                for i in range(0, len(self.user_game_data_id_list)):
                    element = self.user_game_data_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_game_data_id_list[i] = element.to_alipay_dict()
            if hasattr(self.user_game_data_id_list, 'to_alipay_dict'):
                params['user_game_data_id_list'] = self.user_game_data_id_list.to_alipay_dict()
            else:
                params['user_game_data_id_list'] = self.user_game_data_id_list
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
        o = AlipayCommerceSportsUsergameDataSyncModel()
        if 'game_id' in d:
            o.game_id = d['game_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_user_game_no' in d:
            o.out_user_game_no = d['out_user_game_no']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'status' in d:
            o.status = d['status']
        if 'user_game_data_id_list' in d:
            o.user_game_data_id_list = d['user_game_data_id_list']
        if 'user_game_id' in d:
            o.user_game_id = d['user_game_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


