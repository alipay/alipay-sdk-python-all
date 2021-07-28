#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstAccountDTO import InstAccountDTO


class AlipayAccountInstfundAccountSyncModel(object):

    def __init__(self):
        self._inst_account = None

    @property
    def inst_account(self):
        return self._inst_account

    @inst_account.setter
    def inst_account(self, value):
        if isinstance(value, InstAccountDTO):
            self._inst_account = value
        else:
            self._inst_account = InstAccountDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.inst_account:
            if hasattr(self.inst_account, 'to_alipay_dict'):
                params['inst_account'] = self.inst_account.to_alipay_dict()
            else:
                params['inst_account'] = self.inst_account
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountInstfundAccountSyncModel()
        if 'inst_account' in d:
            o.inst_account = d['inst_account']
        return o


