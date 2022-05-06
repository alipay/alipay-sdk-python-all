#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ListDetail(object):

    def __init__(self):
        self._extra_data = None
        self._id_card = None
        self._mobile = None
        self._user_name = None

    @property
    def extra_data(self):
        return self._extra_data

    @extra_data.setter
    def extra_data(self, value):
        self._extra_data = value
    @property
    def id_card(self):
        return self._id_card

    @id_card.setter
    def id_card(self, value):
        self._id_card = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.extra_data:
            if hasattr(self.extra_data, 'to_alipay_dict'):
                params['extra_data'] = self.extra_data.to_alipay_dict()
            else:
                params['extra_data'] = self.extra_data
        if self.id_card:
            if hasattr(self.id_card, 'to_alipay_dict'):
                params['id_card'] = self.id_card.to_alipay_dict()
            else:
                params['id_card'] = self.id_card
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
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
        o = ListDetail()
        if 'extra_data' in d:
            o.extra_data = d['extra_data']
        if 'id_card' in d:
            o.id_card = d['id_card']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


