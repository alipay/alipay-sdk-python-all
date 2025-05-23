#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenXlightCrowdChildLevelThree(object):

    def __init__(self):
        self._name = None
        self._tag_id = None
        self._user_num = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value
    @property
    def user_num(self):
        return self._user_num

    @user_num.setter
    def user_num(self, value):
        self._user_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.tag_id:
            if hasattr(self.tag_id, 'to_alipay_dict'):
                params['tag_id'] = self.tag_id.to_alipay_dict()
            else:
                params['tag_id'] = self.tag_id
        if self.user_num:
            if hasattr(self.user_num, 'to_alipay_dict'):
                params['user_num'] = self.user_num.to_alipay_dict()
            else:
                params['user_num'] = self.user_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenXlightCrowdChildLevelThree()
        if 'name' in d:
            o.name = d['name']
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        if 'user_num' in d:
            o.user_num = d['user_num']
        return o


