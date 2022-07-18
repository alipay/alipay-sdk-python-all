#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MrchCrmUserTagInfo import MrchCrmUserTagInfo


class MrchCrmUser(object):

    def __init__(self):
        self._encrypt_identity_id = None
        self._encrypt_identity_type = None
        self._tag_list = None

    @property
    def encrypt_identity_id(self):
        return self._encrypt_identity_id

    @encrypt_identity_id.setter
    def encrypt_identity_id(self, value):
        self._encrypt_identity_id = value
    @property
    def encrypt_identity_type(self):
        return self._encrypt_identity_type

    @encrypt_identity_type.setter
    def encrypt_identity_type(self, value):
        self._encrypt_identity_type = value
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
        if self.encrypt_identity_id:
            if hasattr(self.encrypt_identity_id, 'to_alipay_dict'):
                params['encrypt_identity_id'] = self.encrypt_identity_id.to_alipay_dict()
            else:
                params['encrypt_identity_id'] = self.encrypt_identity_id
        if self.encrypt_identity_type:
            if hasattr(self.encrypt_identity_type, 'to_alipay_dict'):
                params['encrypt_identity_type'] = self.encrypt_identity_type.to_alipay_dict()
            else:
                params['encrypt_identity_type'] = self.encrypt_identity_type
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
        o = MrchCrmUser()
        if 'encrypt_identity_id' in d:
            o.encrypt_identity_id = d['encrypt_identity_id']
        if 'encrypt_identity_type' in d:
            o.encrypt_identity_type = d['encrypt_identity_type']
        if 'tag_list' in d:
            o.tag_list = d['tag_list']
        return o


