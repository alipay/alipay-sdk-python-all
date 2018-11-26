#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdCtidVerifyModel(object):

    def __init__(self):
        self._id_number = None
        self._identify_model = None
        self._picture = None
        self._user_name = None

    @property
    def id_number(self):
        return self._id_number

    @id_number.setter
    def id_number(self, value):
        self._id_number = value
    @property
    def identify_model(self):
        return self._identify_model

    @identify_model.setter
    def identify_model(self, value):
        self._identify_model = value
    @property
    def picture(self):
        return self._picture

    @picture.setter
    def picture(self, value):
        self._picture = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.id_number:
            if hasattr(self.id_number, 'to_alipay_dict'):
                params['id_number'] = self.id_number.to_alipay_dict()
            else:
                params['id_number'] = self.id_number
        if self.identify_model:
            if hasattr(self.identify_model, 'to_alipay_dict'):
                params['identify_model'] = self.identify_model.to_alipay_dict()
            else:
                params['identify_model'] = self.identify_model
        if self.picture:
            if hasattr(self.picture, 'to_alipay_dict'):
                params['picture'] = self.picture.to_alipay_dict()
            else:
                params['picture'] = self.picture
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdCtidVerifyModel()
        if 'id_number' in d:
            o.id_number = d['id_number']
        if 'identify_model' in d:
            o.identify_model = d['identify_model']
        if 'picture' in d:
            o.picture = d['picture']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


