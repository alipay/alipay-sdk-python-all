#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppCommunityTemporaryvisitorstagVerifyModel(object):

    def __init__(self):
        self._open_id = None
        self._tag_type = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def tag_type(self):
        return self._tag_type

    @tag_type.setter
    def tag_type(self, value):
        self._tag_type = value
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
        if self.tag_type:
            if hasattr(self.tag_type, 'to_alipay_dict'):
                params['tag_type'] = self.tag_type.to_alipay_dict()
            else:
                params['tag_type'] = self.tag_type
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
        o = AlipayEbppCommunityTemporaryvisitorstagVerifyModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'tag_type' in d:
            o.tag_type = d['tag_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


