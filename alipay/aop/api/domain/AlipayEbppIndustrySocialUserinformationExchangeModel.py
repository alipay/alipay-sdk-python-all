#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustrySocialUserinformationExchangeModel(object):

    def __init__(self):
        self._ins_card_id_encrypt = None
        self._sm_4_iv = None

    @property
    def ins_card_id_encrypt(self):
        return self._ins_card_id_encrypt

    @ins_card_id_encrypt.setter
    def ins_card_id_encrypt(self, value):
        self._ins_card_id_encrypt = value
    @property
    def sm_4_iv(self):
        return self._sm_4_iv

    @sm_4_iv.setter
    def sm_4_iv(self, value):
        self._sm_4_iv = value


    def to_alipay_dict(self):
        params = dict()
        if self.ins_card_id_encrypt:
            if hasattr(self.ins_card_id_encrypt, 'to_alipay_dict'):
                params['ins_card_id_encrypt'] = self.ins_card_id_encrypt.to_alipay_dict()
            else:
                params['ins_card_id_encrypt'] = self.ins_card_id_encrypt
        if self.sm_4_iv:
            if hasattr(self.sm_4_iv, 'to_alipay_dict'):
                params['sm_4_iv'] = self.sm_4_iv.to_alipay_dict()
            else:
                params['sm_4_iv'] = self.sm_4_iv
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustrySocialUserinformationExchangeModel()
        if 'ins_card_id_encrypt' in d:
            o.ins_card_id_encrypt = d['ins_card_id_encrypt']
        if 'sm_4_iv' in d:
            o.sm_4_iv = d['sm_4_iv']
        return o


