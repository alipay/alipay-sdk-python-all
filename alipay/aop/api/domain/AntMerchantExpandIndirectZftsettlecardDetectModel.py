#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandIndirectZftsettlecardDetectModel(object):

    def __init__(self):
        self._account_holder_name = None
        self._account_no = None
        self._card_alias_no = None
        self._smid = None

    @property
    def account_holder_name(self):
        return self._account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, value):
        self._account_holder_name = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def card_alias_no(self):
        return self._card_alias_no

    @card_alias_no.setter
    def card_alias_no(self, value):
        self._card_alias_no = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_holder_name:
            if hasattr(self.account_holder_name, 'to_alipay_dict'):
                params['account_holder_name'] = self.account_holder_name.to_alipay_dict()
            else:
                params['account_holder_name'] = self.account_holder_name
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.card_alias_no:
            if hasattr(self.card_alias_no, 'to_alipay_dict'):
                params['card_alias_no'] = self.card_alias_no.to_alipay_dict()
            else:
                params['card_alias_no'] = self.card_alias_no
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIndirectZftsettlecardDetectModel()
        if 'account_holder_name' in d:
            o.account_holder_name = d['account_holder_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'card_alias_no' in d:
            o.card_alias_no = d['card_alias_no']
        if 'smid' in d:
            o.smid = d['smid']
        return o


