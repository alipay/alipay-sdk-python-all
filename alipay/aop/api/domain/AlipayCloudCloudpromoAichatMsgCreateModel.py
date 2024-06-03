#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoAichatMsgCreateModel(object):

    def __init__(self):
        self._biz_trans_data = None
        self._chat_query = None
        self._open_id = None
        self._out_biz_no = None
        self._robot_id = None
        self._scene = None
        self._user_id = None

    @property
    def biz_trans_data(self):
        return self._biz_trans_data

    @biz_trans_data.setter
    def biz_trans_data(self, value):
        self._biz_trans_data = value
    @property
    def chat_query(self):
        return self._chat_query

    @chat_query.setter
    def chat_query(self, value):
        self._chat_query = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def robot_id(self):
        return self._robot_id

    @robot_id.setter
    def robot_id(self, value):
        self._robot_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_trans_data:
            if hasattr(self.biz_trans_data, 'to_alipay_dict'):
                params['biz_trans_data'] = self.biz_trans_data.to_alipay_dict()
            else:
                params['biz_trans_data'] = self.biz_trans_data
        if self.chat_query:
            if hasattr(self.chat_query, 'to_alipay_dict'):
                params['chat_query'] = self.chat_query.to_alipay_dict()
            else:
                params['chat_query'] = self.chat_query
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.robot_id:
            if hasattr(self.robot_id, 'to_alipay_dict'):
                params['robot_id'] = self.robot_id.to_alipay_dict()
            else:
                params['robot_id'] = self.robot_id
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
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
        o = AlipayCloudCloudpromoAichatMsgCreateModel()
        if 'biz_trans_data' in d:
            o.biz_trans_data = d['biz_trans_data']
        if 'chat_query' in d:
            o.chat_query = d['chat_query']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'robot_id' in d:
            o.robot_id = d['robot_id']
        if 'scene' in d:
            o.scene = d['scene']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


