#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PassAccountDTO import PassAccountDTO


class PassportInfoDTO(object):

    def __init__(self):
        self._pass_accounts = None
        self._passport_id = None
        self._register_from = None
        self._register_time = None

    @property
    def pass_accounts(self):
        return self._pass_accounts

    @pass_accounts.setter
    def pass_accounts(self, value):
        if isinstance(value, list):
            self._pass_accounts = list()
            for i in value:
                if isinstance(i, PassAccountDTO):
                    self._pass_accounts.append(i)
                else:
                    self._pass_accounts.append(PassAccountDTO.from_alipay_dict(i))
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def register_from(self):
        return self._register_from

    @register_from.setter
    def register_from(self, value):
        self._register_from = value
    @property
    def register_time(self):
        return self._register_time

    @register_time.setter
    def register_time(self, value):
        self._register_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.pass_accounts:
            if isinstance(self.pass_accounts, list):
                for i in range(0, len(self.pass_accounts)):
                    element = self.pass_accounts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pass_accounts[i] = element.to_alipay_dict()
            if hasattr(self.pass_accounts, 'to_alipay_dict'):
                params['pass_accounts'] = self.pass_accounts.to_alipay_dict()
            else:
                params['pass_accounts'] = self.pass_accounts
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        if self.register_from:
            if hasattr(self.register_from, 'to_alipay_dict'):
                params['register_from'] = self.register_from.to_alipay_dict()
            else:
                params['register_from'] = self.register_from
        if self.register_time:
            if hasattr(self.register_time, 'to_alipay_dict'):
                params['register_time'] = self.register_time.to_alipay_dict()
            else:
                params['register_time'] = self.register_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PassportInfoDTO()
        if 'pass_accounts' in d:
            o.pass_accounts = d['pass_accounts']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        if 'register_from' in d:
            o.register_from = d['register_from']
        if 'register_time' in d:
            o.register_time = d['register_time']
        return o


