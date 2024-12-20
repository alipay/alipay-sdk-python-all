#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceEnergyaggrSubinviteQueryModel(object):

    def __init__(self):
        self._product_agreement_code = None
        self._sub_invite_id = None

    @property
    def product_agreement_code(self):
        return self._product_agreement_code

    @product_agreement_code.setter
    def product_agreement_code(self, value):
        self._product_agreement_code = value
    @property
    def sub_invite_id(self):
        return self._sub_invite_id

    @sub_invite_id.setter
    def sub_invite_id(self, value):
        self._sub_invite_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.product_agreement_code:
            if hasattr(self.product_agreement_code, 'to_alipay_dict'):
                params['product_agreement_code'] = self.product_agreement_code.to_alipay_dict()
            else:
                params['product_agreement_code'] = self.product_agreement_code
        if self.sub_invite_id:
            if hasattr(self.sub_invite_id, 'to_alipay_dict'):
                params['sub_invite_id'] = self.sub_invite_id.to_alipay_dict()
            else:
                params['sub_invite_id'] = self.sub_invite_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceEnergyaggrSubinviteQueryModel()
        if 'product_agreement_code' in d:
            o.product_agreement_code = d['product_agreement_code']
        if 'sub_invite_id' in d:
            o.sub_invite_id = d['sub_invite_id']
        return o


