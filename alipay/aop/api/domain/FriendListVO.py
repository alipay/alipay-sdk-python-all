#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FriendListVO(object):

    def __init__(self):
        self._head_img = None
        self._real_friend = None
        self._user_id = None
        self._view_name = None

    @property
    def head_img(self):
        return self._head_img

    @head_img.setter
    def head_img(self, value):
        self._head_img = value
    @property
    def real_friend(self):
        return self._real_friend

    @real_friend.setter
    def real_friend(self, value):
        self._real_friend = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def view_name(self):
        return self._view_name

    @view_name.setter
    def view_name(self, value):
        self._view_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.head_img:
            if hasattr(self.head_img, 'to_alipay_dict'):
                params['head_img'] = self.head_img.to_alipay_dict()
            else:
                params['head_img'] = self.head_img
        if self.real_friend:
            if hasattr(self.real_friend, 'to_alipay_dict'):
                params['real_friend'] = self.real_friend.to_alipay_dict()
            else:
                params['real_friend'] = self.real_friend
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.view_name:
            if hasattr(self.view_name, 'to_alipay_dict'):
                params['view_name'] = self.view_name.to_alipay_dict()
            else:
                params['view_name'] = self.view_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FriendListVO()
        if 'head_img' in d:
            o.head_img = d['head_img']
        if 'real_friend' in d:
            o.real_friend = d['real_friend']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'view_name' in d:
            o.view_name = d['view_name']
        return o


