#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasAccountAuditedSyncModel(object):

    def __init__(self):
        self._bank_cards_number = None
        self._biz_token = None
        self._gmt_audited = None

    @property
    def bank_cards_number(self):
        return self._bank_cards_number

    @bank_cards_number.setter
    def bank_cards_number(self, value):
        self._bank_cards_number = value
    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def gmt_audited(self):
        return self._gmt_audited

    @gmt_audited.setter
    def gmt_audited(self, value):
        self._gmt_audited = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_cards_number:
            if hasattr(self.bank_cards_number, 'to_alipay_dict'):
                params['bank_cards_number'] = self.bank_cards_number.to_alipay_dict()
            else:
                params['bank_cards_number'] = self.bank_cards_number
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.gmt_audited:
            if hasattr(self.gmt_audited, 'to_alipay_dict'):
                params['gmt_audited'] = self.gmt_audited.to_alipay_dict()
            else:
                params['gmt_audited'] = self.gmt_audited
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasAccountAuditedSyncModel()
        if 'bank_cards_number' in d:
            o.bank_cards_number = d['bank_cards_number']
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'gmt_audited' in d:
            o.gmt_audited = d['gmt_audited']
        return o


