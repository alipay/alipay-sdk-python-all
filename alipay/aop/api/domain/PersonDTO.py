#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PersonDTO(object):

    def __init__(self):
        self._resign = None
        self._user_name = None
        self._work_no = None

    @property
    def resign(self):
        return self._resign

    @resign.setter
    def resign(self, value):
        self._resign = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def work_no(self):
        return self._work_no

    @work_no.setter
    def work_no(self, value):
        self._work_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.resign:
            if hasattr(self.resign, 'to_alipay_dict'):
                params['resign'] = self.resign.to_alipay_dict()
            else:
                params['resign'] = self.resign
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.work_no:
            if hasattr(self.work_no, 'to_alipay_dict'):
                params['work_no'] = self.work_no.to_alipay_dict()
            else:
                params['work_no'] = self.work_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PersonDTO()
        if 'resign' in d:
            o.resign = d['resign']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'work_no' in d:
            o.work_no = d['work_no']
        return o


