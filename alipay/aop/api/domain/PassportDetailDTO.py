#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MemberDTO import MemberDTO
from alipay.aop.api.domain.PassAccountDTO import PassAccountDTO


class PassportDetailDTO(object):

    def __init__(self):
        self._id = None
        self._member = None
        self._pass_accounts = None
        self._status = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def member(self):
        return self._member

    @member.setter
    def member(self, value):
        if isinstance(value, MemberDTO):
            self._member = value
        else:
            self._member = MemberDTO.from_alipay_dict(value)
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.member:
            if hasattr(self.member, 'to_alipay_dict'):
                params['member'] = self.member.to_alipay_dict()
            else:
                params['member'] = self.member
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PassportDetailDTO()
        if 'id' in d:
            o.id = d['id']
        if 'member' in d:
            o.member = d['member']
        if 'pass_accounts' in d:
            o.pass_accounts = d['pass_accounts']
        if 'status' in d:
            o.status = d['status']
        return o


