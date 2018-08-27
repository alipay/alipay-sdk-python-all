#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Matcher(object):

    def __init__(self):
        self._identity_card = None
        self._mobile_no = None
        self._user_id = None

    @property
    def identity_card(self):
        return self._identity_card

    @identity_card.setter
    def identity_card(self, value):
        self._identity_card = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.identity_card:
            if hasattr(self.identity_card, 'to_alipay_dict'):
                params['identity_card'] = self.identity_card.to_alipay_dict()
            else:
                params['identity_card'] = self.identity_card
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
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
        o = Matcher()
        if 'identity_card' in d:
            o.identity_card = d['identity_card']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


