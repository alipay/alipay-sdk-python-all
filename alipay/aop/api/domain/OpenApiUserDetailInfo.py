#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiUserDetailInfo(object):

    def __init__(self):
        self._award_invitee = None
        self._award_inviter = None
        self._icon = None
        self._index = None
        self._name = None
        self._uid = None

    @property
    def award_invitee(self):
        return self._award_invitee

    @award_invitee.setter
    def award_invitee(self, value):
        self._award_invitee = value
    @property
    def award_inviter(self):
        return self._award_inviter

    @award_inviter.setter
    def award_inviter(self, value):
        self._award_inviter = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.award_invitee:
            if hasattr(self.award_invitee, 'to_alipay_dict'):
                params['award_invitee'] = self.award_invitee.to_alipay_dict()
            else:
                params['award_invitee'] = self.award_invitee
        if self.award_inviter:
            if hasattr(self.award_inviter, 'to_alipay_dict'):
                params['award_inviter'] = self.award_inviter.to_alipay_dict()
            else:
                params['award_inviter'] = self.award_inviter
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.index:
            if hasattr(self.index, 'to_alipay_dict'):
                params['index'] = self.index.to_alipay_dict()
            else:
                params['index'] = self.index
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
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
        o = OpenApiUserDetailInfo()
        if 'award_invitee' in d:
            o.award_invitee = d['award_invitee']
        if 'award_inviter' in d:
            o.award_inviter = d['award_inviter']
        if 'icon' in d:
            o.icon = d['icon']
        if 'index' in d:
            o.index = d['index']
        if 'name' in d:
            o.name = d['name']
        if 'uid' in d:
            o.uid = d['uid']
        return o


