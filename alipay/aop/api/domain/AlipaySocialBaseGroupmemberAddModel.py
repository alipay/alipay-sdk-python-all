#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseGroupmemberAddModel(object):

    def __init__(self):
        self._friend_validate = None
        self._group_id = None
        self._user_ids = None

    @property
    def friend_validate(self):
        return self._friend_validate

    @friend_validate.setter
    def friend_validate(self, value):
        self._friend_validate = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def user_ids(self):
        return self._user_ids

    @user_ids.setter
    def user_ids(self, value):
        if isinstance(value, list):
            self._user_ids = list()
            for i in value:
                self._user_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.friend_validate:
            if hasattr(self.friend_validate, 'to_alipay_dict'):
                params['friend_validate'] = self.friend_validate.to_alipay_dict()
            else:
                params['friend_validate'] = self.friend_validate
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.user_ids:
            if isinstance(self.user_ids, list):
                for i in range(0, len(self.user_ids)):
                    element = self.user_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_ids[i] = element.to_alipay_dict()
            if hasattr(self.user_ids, 'to_alipay_dict'):
                params['user_ids'] = self.user_ids.to_alipay_dict()
            else:
                params['user_ids'] = self.user_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseGroupmemberAddModel()
        if 'friend_validate' in d:
            o.friend_validate = d['friend_validate']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'user_ids' in d:
            o.user_ids = d['user_ids']
        return o


