#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TuitionISVPayerInfoDTO(object):

    def __init__(self):
        self._alipay_logon_id = None
        self._payer_identity_card_number = None
        self._payer_phone_number = None

    @property
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
    @property
    def payer_identity_card_number(self):
        return self._payer_identity_card_number

    @payer_identity_card_number.setter
    def payer_identity_card_number(self, value):
        self._payer_identity_card_number = value
    @property
    def payer_phone_number(self):
        return self._payer_phone_number

    @payer_phone_number.setter
    def payer_phone_number(self, value):
        self._payer_phone_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_logon_id:
            if hasattr(self.alipay_logon_id, 'to_alipay_dict'):
                params['alipay_logon_id'] = self.alipay_logon_id.to_alipay_dict()
            else:
                params['alipay_logon_id'] = self.alipay_logon_id
        if self.payer_identity_card_number:
            if hasattr(self.payer_identity_card_number, 'to_alipay_dict'):
                params['payer_identity_card_number'] = self.payer_identity_card_number.to_alipay_dict()
            else:
                params['payer_identity_card_number'] = self.payer_identity_card_number
        if self.payer_phone_number:
            if hasattr(self.payer_phone_number, 'to_alipay_dict'):
                params['payer_phone_number'] = self.payer_phone_number.to_alipay_dict()
            else:
                params['payer_phone_number'] = self.payer_phone_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TuitionISVPayerInfoDTO()
        if 'alipay_logon_id' in d:
            o.alipay_logon_id = d['alipay_logon_id']
        if 'payer_identity_card_number' in d:
            o.payer_identity_card_number = d['payer_identity_card_number']
        if 'payer_phone_number' in d:
            o.payer_phone_number = d['payer_phone_number']
        return o


