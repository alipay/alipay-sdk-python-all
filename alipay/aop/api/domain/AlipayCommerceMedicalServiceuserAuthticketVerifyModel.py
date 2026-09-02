#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalServiceuserAuthticketVerifyModel(object):

    def __init__(self):
        self._auth_ticket = None

    @property
    def auth_ticket(self):
        return self._auth_ticket

    @auth_ticket.setter
    def auth_ticket(self, value):
        self._auth_ticket = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_ticket:
            if hasattr(self.auth_ticket, 'to_alipay_dict'):
                params['auth_ticket'] = self.auth_ticket.to_alipay_dict()
            else:
                params['auth_ticket'] = self.auth_ticket
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalServiceuserAuthticketVerifyModel()
        if 'auth_ticket' in d:
            o.auth_ticket = d['auth_ticket']
        return o


