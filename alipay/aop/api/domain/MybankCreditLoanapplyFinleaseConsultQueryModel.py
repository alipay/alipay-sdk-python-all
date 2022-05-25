#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoanapplyFinleaseConsultQueryModel(object):

    def __init__(self):
        self._corporationname = None
        self._registrationno = None
        self._userid = None

    @property
    def corporationname(self):
        return self._corporationname

    @corporationname.setter
    def corporationname(self, value):
        self._corporationname = value
    @property
    def registrationno(self):
        return self._registrationno

    @registrationno.setter
    def registrationno(self, value):
        self._registrationno = value
    @property
    def userid(self):
        return self._userid

    @userid.setter
    def userid(self, value):
        self._userid = value


    def to_alipay_dict(self):
        params = dict()
        if self.corporationname:
            if hasattr(self.corporationname, 'to_alipay_dict'):
                params['corporationname'] = self.corporationname.to_alipay_dict()
            else:
                params['corporationname'] = self.corporationname
        if self.registrationno:
            if hasattr(self.registrationno, 'to_alipay_dict'):
                params['registrationno'] = self.registrationno.to_alipay_dict()
            else:
                params['registrationno'] = self.registrationno
        if self.userid:
            if hasattr(self.userid, 'to_alipay_dict'):
                params['userid'] = self.userid.to_alipay_dict()
            else:
                params['userid'] = self.userid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoanapplyFinleaseConsultQueryModel()
        if 'corporationname' in d:
            o.corporationname = d['corporationname']
        if 'registrationno' in d:
            o.registrationno = d['registrationno']
        if 'userid' in d:
            o.userid = d['userid']
        return o


