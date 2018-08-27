#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicPartnerMenuOperateModel(object):

    def __init__(self):
        self._action_param = None
        self._action_type = None
        self._agreement_id = None
        self._public_id = None
        self._third_account_id = None
        self._user_id = None

    @property
    def action_param(self):
        return self._action_param

    @action_param.setter
    def action_param(self, value):
        self._action_param = value
    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value
    @property
    def third_account_id(self):
        return self._third_account_id

    @third_account_id.setter
    def third_account_id(self, value):
        self._third_account_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_param:
            if hasattr(self.action_param, 'to_alipay_dict'):
                params['action_param'] = self.action_param.to_alipay_dict()
            else:
                params['action_param'] = self.action_param
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.agreement_id:
            if hasattr(self.agreement_id, 'to_alipay_dict'):
                params['agreement_id'] = self.agreement_id.to_alipay_dict()
            else:
                params['agreement_id'] = self.agreement_id
        if self.public_id:
            if hasattr(self.public_id, 'to_alipay_dict'):
                params['public_id'] = self.public_id.to_alipay_dict()
            else:
                params['public_id'] = self.public_id
        if self.third_account_id:
            if hasattr(self.third_account_id, 'to_alipay_dict'):
                params['third_account_id'] = self.third_account_id.to_alipay_dict()
            else:
                params['third_account_id'] = self.third_account_id
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
        o = AlipayOpenPublicPartnerMenuOperateModel()
        if 'action_param' in d:
            o.action_param = d['action_param']
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'agreement_id' in d:
            o.agreement_id = d['agreement_id']
        if 'public_id' in d:
            o.public_id = d['public_id']
        if 'third_account_id' in d:
            o.third_account_id = d['third_account_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


