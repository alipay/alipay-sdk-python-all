#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AddVolunteerReq import AddVolunteerReq


class AlipayDigitalmgmtWelfarefoundationUpdatevolunteersCreateModel(object):

    def __init__(self):
        self._tenant = None
        self._volunteers = None

    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value
    @property
    def volunteers(self):
        return self._volunteers

    @volunteers.setter
    def volunteers(self, value):
        if isinstance(value, list):
            self._volunteers = list()
            for i in value:
                if isinstance(i, AddVolunteerReq):
                    self._volunteers.append(i)
                else:
                    self._volunteers.append(AddVolunteerReq.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        if self.volunteers:
            if isinstance(self.volunteers, list):
                for i in range(0, len(self.volunteers)):
                    element = self.volunteers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.volunteers[i] = element.to_alipay_dict()
            if hasattr(self.volunteers, 'to_alipay_dict'):
                params['volunteers'] = self.volunteers.to_alipay_dict()
            else:
                params['volunteers'] = self.volunteers
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtWelfarefoundationUpdatevolunteersCreateModel()
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'volunteers' in d:
            o.volunteers = d['volunteers']
        return o


