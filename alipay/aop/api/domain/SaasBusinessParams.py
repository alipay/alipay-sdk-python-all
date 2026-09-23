#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SaasBusinessParams(object):

    def __init__(self):
        self._campus_card = None
        self._saas_ebank_bank_code = None
        self._saas_ebank_inst_id = None

    @property
    def campus_card(self):
        return self._campus_card

    @campus_card.setter
    def campus_card(self, value):
        self._campus_card = value
    @property
    def saas_ebank_bank_code(self):
        return self._saas_ebank_bank_code

    @saas_ebank_bank_code.setter
    def saas_ebank_bank_code(self, value):
        self._saas_ebank_bank_code = value
    @property
    def saas_ebank_inst_id(self):
        return self._saas_ebank_inst_id

    @saas_ebank_inst_id.setter
    def saas_ebank_inst_id(self, value):
        self._saas_ebank_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.campus_card:
            if hasattr(self.campus_card, 'to_alipay_dict'):
                params['campus_card'] = self.campus_card.to_alipay_dict()
            else:
                params['campus_card'] = self.campus_card
        if self.saas_ebank_bank_code:
            if hasattr(self.saas_ebank_bank_code, 'to_alipay_dict'):
                params['saas_ebank_bank_code'] = self.saas_ebank_bank_code.to_alipay_dict()
            else:
                params['saas_ebank_bank_code'] = self.saas_ebank_bank_code
        if self.saas_ebank_inst_id:
            if hasattr(self.saas_ebank_inst_id, 'to_alipay_dict'):
                params['saas_ebank_inst_id'] = self.saas_ebank_inst_id.to_alipay_dict()
            else:
                params['saas_ebank_inst_id'] = self.saas_ebank_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SaasBusinessParams()
        if 'campus_card' in d:
            o.campus_card = d['campus_card']
        if 'saas_ebank_bank_code' in d:
            o.saas_ebank_bank_code = d['saas_ebank_bank_code']
        if 'saas_ebank_inst_id' in d:
            o.saas_ebank_inst_id = d['saas_ebank_inst_id']
        return o


