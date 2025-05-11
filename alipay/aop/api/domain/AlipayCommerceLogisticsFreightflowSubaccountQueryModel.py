#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsFreightflowSubaccountQueryModel(object):

    def __init__(self):
        self._logistics_code = None
        self._mode = None
        self._partner_id = None
        self._sub_bank_card_no = None

    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def sub_bank_card_no(self):
        return self._sub_bank_card_no

    @sub_bank_card_no.setter
    def sub_bank_card_no(self, value):
        self._sub_bank_card_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.mode:
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.sub_bank_card_no:
            if hasattr(self.sub_bank_card_no, 'to_alipay_dict'):
                params['sub_bank_card_no'] = self.sub_bank_card_no.to_alipay_dict()
            else:
                params['sub_bank_card_no'] = self.sub_bank_card_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsFreightflowSubaccountQueryModel()
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'mode' in d:
            o.mode = d['mode']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'sub_bank_card_no' in d:
            o.sub_bank_card_no = d['sub_bank_card_no']
        return o


