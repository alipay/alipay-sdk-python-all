#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenXlightCrowd(object):

    def __init__(self):
        self._name = None
        self._tag_id = None
        self._user_num = None
        self._valid_date = None

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
    @property
    def valid_date(self):
        return self._valid_date

    @valid_date.setter
    def valid_date(self, value):
        self._valid_date = value


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
        if self.valid_date:
            if hasattr(self.valid_date, 'to_alipay_dict'):
                params['valid_date'] = self.valid_date.to_alipay_dict()
            else:
                params['valid_date'] = self.valid_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenXlightCrowd()
        if 'name' in d:
            o.name = d['name']
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        if 'user_num' in d:
            o.user_num = d['user_num']
        if 'valid_date' in d:
            o.valid_date = d['valid_date']
        return o


