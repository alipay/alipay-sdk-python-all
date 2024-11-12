#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndrReferralCodeRequestParamDTO(object):

    def __init__(self):
        self._beneficiary_id = None
        self._email = None
        self._link_target = None

    @property
    def beneficiary_id(self):
        return self._beneficiary_id

    @beneficiary_id.setter
    def beneficiary_id(self, value):
        self._beneficiary_id = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def link_target(self):
        return self._link_target

    @link_target.setter
    def link_target(self, value):
        self._link_target = value


    def to_alipay_dict(self):
        params = dict()
        if self.beneficiary_id:
            if hasattr(self.beneficiary_id, 'to_alipay_dict'):
                params['beneficiary_id'] = self.beneficiary_id.to_alipay_dict()
            else:
                params['beneficiary_id'] = self.beneficiary_id
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.link_target:
            if hasattr(self.link_target, 'to_alipay_dict'):
                params['link_target'] = self.link_target.to_alipay_dict()
            else:
                params['link_target'] = self.link_target
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndrReferralCodeRequestParamDTO()
        if 'beneficiary_id' in d:
            o.beneficiary_id = d['beneficiary_id']
        if 'email' in d:
            o.email = d['email']
        if 'link_target' in d:
            o.link_target = d['link_target']
        return o


