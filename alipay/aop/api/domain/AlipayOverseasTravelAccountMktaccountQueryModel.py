#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CnAccountDTO import CnAccountDTO


class AlipayOverseasTravelAccountMktaccountQueryModel(object):

    def __init__(self):
        self._cn_accounts = None

    @property
    def cn_accounts(self):
        return self._cn_accounts

    @cn_accounts.setter
    def cn_accounts(self, value):
        if isinstance(value, list):
            self._cn_accounts = list()
            for i in value:
                if isinstance(i, CnAccountDTO):
                    self._cn_accounts.append(i)
                else:
                    self._cn_accounts.append(CnAccountDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.cn_accounts:
            if isinstance(self.cn_accounts, list):
                for i in range(0, len(self.cn_accounts)):
                    element = self.cn_accounts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cn_accounts[i] = element.to_alipay_dict()
            if hasattr(self.cn_accounts, 'to_alipay_dict'):
                params['cn_accounts'] = self.cn_accounts.to_alipay_dict()
            else:
                params['cn_accounts'] = self.cn_accounts
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelAccountMktaccountQueryModel()
        if 'cn_accounts' in d:
            o.cn_accounts = d['cn_accounts']
        return o


