#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SecuUserList(object):

    def __init__(self):
        self._agreement_no = None
        self._avatar_url = None
        self._gender = None
        self._motto = None
        self._nick_name = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def avatar_url(self):
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, value):
        self._avatar_url = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def motto(self):
        return self._motto

    @motto.setter
    def motto(self, value):
        self._motto = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.avatar_url:
            if hasattr(self.avatar_url, 'to_alipay_dict'):
                params['avatar_url'] = self.avatar_url.to_alipay_dict()
            else:
                params['avatar_url'] = self.avatar_url
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.motto:
            if hasattr(self.motto, 'to_alipay_dict'):
                params['motto'] = self.motto.to_alipay_dict()
            else:
                params['motto'] = self.motto
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SecuUserList()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'avatar_url' in d:
            o.avatar_url = d['avatar_url']
        if 'gender' in d:
            o.gender = d['gender']
        if 'motto' in d:
            o.motto = d['motto']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        return o


