#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MrchCrmUserTagInfo import MrchCrmUserTagInfo


class MrchCrmUserInfo(object):

    def __init__(self):
        self._encrypt_email = None
        self._encrypt_mobile = None
        self._tag_list = None

    @property
    def encrypt_email(self):
        return self._encrypt_email

    @encrypt_email.setter
    def encrypt_email(self, value):
        self._encrypt_email = value
    @property
    def encrypt_mobile(self):
        return self._encrypt_mobile

    @encrypt_mobile.setter
    def encrypt_mobile(self, value):
        self._encrypt_mobile = value
    @property
    def tag_list(self):
        return self._tag_list

    @tag_list.setter
    def tag_list(self, value):
        if isinstance(value, list):
            self._tag_list = list()
            for i in value:
                if isinstance(i, MrchCrmUserTagInfo):
                    self._tag_list.append(i)
                else:
                    self._tag_list.append(MrchCrmUserTagInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.encrypt_email:
            if hasattr(self.encrypt_email, 'to_alipay_dict'):
                params['encrypt_email'] = self.encrypt_email.to_alipay_dict()
            else:
                params['encrypt_email'] = self.encrypt_email
        if self.encrypt_mobile:
            if hasattr(self.encrypt_mobile, 'to_alipay_dict'):
                params['encrypt_mobile'] = self.encrypt_mobile.to_alipay_dict()
            else:
                params['encrypt_mobile'] = self.encrypt_mobile
        if self.tag_list:
            if isinstance(self.tag_list, list):
                for i in range(0, len(self.tag_list)):
                    element = self.tag_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_list[i] = element.to_alipay_dict()
            if hasattr(self.tag_list, 'to_alipay_dict'):
                params['tag_list'] = self.tag_list.to_alipay_dict()
            else:
                params['tag_list'] = self.tag_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MrchCrmUserInfo()
        if 'encrypt_email' in d:
            o.encrypt_email = d['encrypt_email']
        if 'encrypt_mobile' in d:
            o.encrypt_mobile = d['encrypt_mobile']
        if 'tag_list' in d:
            o.tag_list = d['tag_list']
        return o


