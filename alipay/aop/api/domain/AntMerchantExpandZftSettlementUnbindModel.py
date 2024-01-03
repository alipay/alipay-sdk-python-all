#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandZftSettlementUnbindModel(object):

    def __init__(self):
        self._alipay_logon_id = None
        self._card_alias_no = None
        self._smid = None

    @property
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
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
        if self.alipay_logon_id:
            if hasattr(self.alipay_logon_id, 'to_alipay_dict'):
                params['alipay_logon_id'] = self.alipay_logon_id.to_alipay_dict()
            else:
                params['alipay_logon_id'] = self.alipay_logon_id
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
        o = AntMerchantExpandZftSettlementUnbindModel()
        if 'alipay_logon_id' in d:
            o.alipay_logon_id = d['alipay_logon_id']
        if 'card_alias_no' in d:
            o.card_alias_no = d['card_alias_no']
        if 'smid' in d:
            o.smid = d['smid']
        return o


