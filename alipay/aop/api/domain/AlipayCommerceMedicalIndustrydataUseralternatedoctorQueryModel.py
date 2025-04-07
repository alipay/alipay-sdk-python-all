#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalIndustrydataUseralternatedoctorQueryModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._user_id_open_id = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def user_id_open_id(self):
        return self._user_id_open_id

    @user_id_open_id.setter
    def user_id_open_id(self, value):
        self._user_id_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.user_id_open_id:
            if hasattr(self.user_id_open_id, 'to_alipay_dict'):
                params['user_id_open_id'] = self.user_id_open_id.to_alipay_dict()
            else:
                params['user_id_open_id'] = self.user_id_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataUseralternatedoctorQueryModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'user_id_open_id' in d:
            o.user_id_open_id = d['user_id_open_id']
        return o


