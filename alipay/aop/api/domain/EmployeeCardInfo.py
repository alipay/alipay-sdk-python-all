#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ParticipantInfoDTO import ParticipantInfoDTO
from alipay.aop.api.domain.ParticipantInfoDTO import ParticipantInfoDTO


class EmployeeCardInfo(object):

    def __init__(self):
        self._hire_principal = None
        self._invite_principal = None

    @property
    def hire_principal(self):
        return self._hire_principal

    @hire_principal.setter
    def hire_principal(self, value):
        if isinstance(value, ParticipantInfoDTO):
            self._hire_principal = value
        else:
            self._hire_principal = ParticipantInfoDTO.from_alipay_dict(value)
    @property
    def invite_principal(self):
        return self._invite_principal

    @invite_principal.setter
    def invite_principal(self, value):
        if isinstance(value, ParticipantInfoDTO):
            self._invite_principal = value
        else:
            self._invite_principal = ParticipantInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.hire_principal:
            if hasattr(self.hire_principal, 'to_alipay_dict'):
                params['hire_principal'] = self.hire_principal.to_alipay_dict()
            else:
                params['hire_principal'] = self.hire_principal
        if self.invite_principal:
            if hasattr(self.invite_principal, 'to_alipay_dict'):
                params['invite_principal'] = self.invite_principal.to_alipay_dict()
            else:
                params['invite_principal'] = self.invite_principal
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EmployeeCardInfo()
        if 'hire_principal' in d:
            o.hire_principal = d['hire_principal']
        if 'invite_principal' in d:
            o.invite_principal = d['invite_principal']
        return o


