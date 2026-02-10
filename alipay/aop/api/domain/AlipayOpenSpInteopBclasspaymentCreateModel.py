#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BClassPaymentBankCardInfo import BClassPaymentBankCardInfo
from alipay.aop.api.domain.BClassPaymentContactInfo import BClassPaymentContactInfo


class AlipayOpenSpInteopBclasspaymentCreateModel(object):

    def __init__(self):
        self._bank_card_info = None
        self._contact_info = None
        self._inteop_order_no = None
        self._mcc_code = None
        self._mini_app_id = None

    @property
    def bank_card_info(self):
        return self._bank_card_info

    @bank_card_info.setter
    def bank_card_info(self, value):
        if isinstance(value, BClassPaymentBankCardInfo):
            self._bank_card_info = value
        else:
            self._bank_card_info = BClassPaymentBankCardInfo.from_alipay_dict(value)
    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, BClassPaymentContactInfo):
            self._contact_info = value
        else:
            self._contact_info = BClassPaymentContactInfo.from_alipay_dict(value)
    @property
    def inteop_order_no(self):
        return self._inteop_order_no

    @inteop_order_no.setter
    def inteop_order_no(self, value):
        self._inteop_order_no = value
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_card_info:
            if hasattr(self.bank_card_info, 'to_alipay_dict'):
                params['bank_card_info'] = self.bank_card_info.to_alipay_dict()
            else:
                params['bank_card_info'] = self.bank_card_info
        if self.contact_info:
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.inteop_order_no:
            if hasattr(self.inteop_order_no, 'to_alipay_dict'):
                params['inteop_order_no'] = self.inteop_order_no.to_alipay_dict()
            else:
                params['inteop_order_no'] = self.inteop_order_no
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = self.mcc_code.to_alipay_dict()
            else:
                params['mcc_code'] = self.mcc_code
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpInteopBclasspaymentCreateModel()
        if 'bank_card_info' in d:
            o.bank_card_info = d['bank_card_info']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'inteop_order_no' in d:
            o.inteop_order_no = d['inteop_order_no']
        if 'mcc_code' in d:
            o.mcc_code = d['mcc_code']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        return o


