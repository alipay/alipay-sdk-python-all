#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankEcnyWelfarewalletBalanceQueryModel(object):

    def __init__(self):
        self._partner_abbr_name = None
        self._partner_id = None
        self._wallet_id = None

    @property
    def partner_abbr_name(self):
        return self._partner_abbr_name

    @partner_abbr_name.setter
    def partner_abbr_name(self, value):
        self._partner_abbr_name = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def wallet_id(self):
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, value):
        self._wallet_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.partner_abbr_name:
            if hasattr(self.partner_abbr_name, 'to_alipay_dict'):
                params['partner_abbr_name'] = self.partner_abbr_name.to_alipay_dict()
            else:
                params['partner_abbr_name'] = self.partner_abbr_name
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.wallet_id:
            if hasattr(self.wallet_id, 'to_alipay_dict'):
                params['wallet_id'] = self.wallet_id.to_alipay_dict()
            else:
                params['wallet_id'] = self.wallet_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankEcnyWelfarewalletBalanceQueryModel()
        if 'partner_abbr_name' in d:
            o.partner_abbr_name = d['partner_abbr_name']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'wallet_id' in d:
            o.wallet_id = d['wallet_id']
        return o


