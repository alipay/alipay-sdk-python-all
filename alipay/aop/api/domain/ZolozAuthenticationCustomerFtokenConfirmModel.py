#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FtokenInfoQuery import FtokenInfoQuery


class ZolozAuthenticationCustomerFtokenConfirmModel(object):

    def __init__(self):
        self._ftokens = None

    @property
    def ftokens(self):
        return self._ftokens

    @ftokens.setter
    def ftokens(self, value):
        if isinstance(value, list):
            self._ftokens = list()
            for i in value:
                if isinstance(i, FtokenInfoQuery):
                    self._ftokens.append(i)
                else:
                    self._ftokens.append(FtokenInfoQuery.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.ftokens:
            if isinstance(self.ftokens, list):
                for i in range(0, len(self.ftokens)):
                    element = self.ftokens[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ftokens[i] = element.to_alipay_dict()
            if hasattr(self.ftokens, 'to_alipay_dict'):
                params['ftokens'] = self.ftokens.to_alipay_dict()
            else:
                params['ftokens'] = self.ftokens
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozAuthenticationCustomerFtokenConfirmModel()
        if 'ftokens' in d:
            o.ftokens = d['ftokens']
        return o


