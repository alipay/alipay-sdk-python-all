#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialGamecenterGamerightsConsultModel(object):

    def __init__(self):
        self._consult_right_num = None
        self._consult_right_type = None
        self._open_id = None
        self._user_id = None

    @property
    def consult_right_num(self):
        return self._consult_right_num

    @consult_right_num.setter
    def consult_right_num(self, value):
        self._consult_right_num = value
    @property
    def consult_right_type(self):
        return self._consult_right_type

    @consult_right_type.setter
    def consult_right_type(self, value):
        self._consult_right_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.consult_right_num:
            if hasattr(self.consult_right_num, 'to_alipay_dict'):
                params['consult_right_num'] = self.consult_right_num.to_alipay_dict()
            else:
                params['consult_right_num'] = self.consult_right_num
        if self.consult_right_type:
            if hasattr(self.consult_right_type, 'to_alipay_dict'):
                params['consult_right_type'] = self.consult_right_type.to_alipay_dict()
            else:
                params['consult_right_type'] = self.consult_right_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialGamecenterGamerightsConsultModel()
        if 'consult_right_num' in d:
            o.consult_right_num = d['consult_right_num']
        if 'consult_right_type' in d:
            o.consult_right_type = d['consult_right_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


