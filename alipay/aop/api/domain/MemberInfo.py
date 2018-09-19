#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MemberInfo(object):

    def __init__(self):
        self._gender = None
        self._group_nick_name = None
        self._inviter_uid = None
        self._member_img = None
        self._nick_name = None
        self._uid = None

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def group_nick_name(self):
        return self._group_nick_name

    @group_nick_name.setter
    def group_nick_name(self, value):
        self._group_nick_name = value
    @property
    def inviter_uid(self):
        return self._inviter_uid

    @inviter_uid.setter
    def inviter_uid(self, value):
        self._inviter_uid = value
    @property
    def member_img(self):
        return self._member_img

    @member_img.setter
    def member_img(self, value):
        self._member_img = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.group_nick_name:
            if hasattr(self.group_nick_name, 'to_alipay_dict'):
                params['group_nick_name'] = self.group_nick_name.to_alipay_dict()
            else:
                params['group_nick_name'] = self.group_nick_name
        if self.inviter_uid:
            if hasattr(self.inviter_uid, 'to_alipay_dict'):
                params['inviter_uid'] = self.inviter_uid.to_alipay_dict()
            else:
                params['inviter_uid'] = self.inviter_uid
        if self.member_img:
            if hasattr(self.member_img, 'to_alipay_dict'):
                params['member_img'] = self.member_img.to_alipay_dict()
            else:
                params['member_img'] = self.member_img
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberInfo()
        if 'gender' in d:
            o.gender = d['gender']
        if 'group_nick_name' in d:
            o.group_nick_name = d['group_nick_name']
        if 'inviter_uid' in d:
            o.inviter_uid = d['inviter_uid']
        if 'member_img' in d:
            o.member_img = d['member_img']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'uid' in d:
            o.uid = d['uid']
        return o


