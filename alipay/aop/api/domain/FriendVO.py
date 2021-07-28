#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FriendVO(object):

    def __init__(self):
        self._friend_openid = None
        self._head_img = None
        self._relation = None
        self._view_name = None

    @property
    def friend_openid(self):
        return self._friend_openid

    @friend_openid.setter
    def friend_openid(self, value):
        self._friend_openid = value
    @property
    def head_img(self):
        return self._head_img

    @head_img.setter
    def head_img(self, value):
        self._head_img = value
    @property
    def relation(self):
        return self._relation

    @relation.setter
    def relation(self, value):
        self._relation = value
    @property
    def view_name(self):
        return self._view_name

    @view_name.setter
    def view_name(self, value):
        self._view_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.friend_openid:
            if hasattr(self.friend_openid, 'to_alipay_dict'):
                params['friend_openid'] = self.friend_openid.to_alipay_dict()
            else:
                params['friend_openid'] = self.friend_openid
        if self.head_img:
            if hasattr(self.head_img, 'to_alipay_dict'):
                params['head_img'] = self.head_img.to_alipay_dict()
            else:
                params['head_img'] = self.head_img
        if self.relation:
            if hasattr(self.relation, 'to_alipay_dict'):
                params['relation'] = self.relation.to_alipay_dict()
            else:
                params['relation'] = self.relation
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
        o = FriendVO()
        if 'friend_openid' in d:
            o.friend_openid = d['friend_openid']
        if 'head_img' in d:
            o.head_img = d['head_img']
        if 'relation' in d:
            o.relation = d['relation']
        if 'view_name' in d:
            o.view_name = d['view_name']
        return o


