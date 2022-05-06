#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoanapplyFinleaseConsultQueryModel(object):

    def __init__(self):
        self._userid = None

    @property
    def userid(self):
        return self._userid

    @userid.setter
    def userid(self, value):
        self._userid = value


    def to_alipay_dict(self):
        params = dict()
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
        if 'userid' in d:
            o.userid = d['userid']
        return o


