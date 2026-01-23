#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalAqUsersimpleQueryModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._aq_user_id = None
        self._open_id = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def aq_user_id(self):
        return self._aq_user_id

    @aq_user_id.setter
    def aq_user_id(self, value):
        self._aq_user_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.aq_user_id:
            if hasattr(self.aq_user_id, 'to_alipay_dict'):
                params['aq_user_id'] = self.aq_user_id.to_alipay_dict()
            else:
                params['aq_user_id'] = self.aq_user_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalAqUsersimpleQueryModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'aq_user_id' in d:
            o.aq_user_id = d['aq_user_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        return o


