#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EntryHealthPersonInfo(object):

    def __init__(self):
        self._form_no = None
        self._user_type = None

    @property
    def form_no(self):
        return self._form_no

    @form_no.setter
    def form_no(self, value):
        self._form_no = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.form_no:
            if hasattr(self.form_no, 'to_alipay_dict'):
                params['form_no'] = self.form_no.to_alipay_dict()
            else:
                params['form_no'] = self.form_no
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EntryHealthPersonInfo()
        if 'form_no' in d:
            o.form_no = d['form_no']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


