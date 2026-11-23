#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TransferUserrBeneficiary import TransferUserrBeneficiary
from alipay.aop.api.domain.TransferUserrPayer import TransferUserrPayer
from alipay.aop.api.domain.TransferPaymentBilllq import TransferPaymentBilllq


class AdditionalTransferDetail(object):

    def __init__(self):
        self._beneficiary = None
        self._payer = None
        self._payment_bill = None
        self._transfer_from_region = None
        self._transfer_purpose = None
        self._transfer_reference = None
        self._transfer_to_region = None

    @property
    def beneficiary(self):
        return self._beneficiary

    @beneficiary.setter
    def beneficiary(self, value):
        if isinstance(value, TransferUserrBeneficiary):
            self._beneficiary = value
        else:
            self._beneficiary = TransferUserrBeneficiary.from_alipay_dict(value)
    @property
    def payer(self):
        return self._payer

    @payer.setter
    def payer(self, value):
        if isinstance(value, TransferUserrPayer):
            self._payer = value
        else:
            self._payer = TransferUserrPayer.from_alipay_dict(value)
    @property
    def payment_bill(self):
        return self._payment_bill

    @payment_bill.setter
    def payment_bill(self, value):
        if isinstance(value, TransferPaymentBilllq):
            self._payment_bill = value
        else:
            self._payment_bill = TransferPaymentBilllq.from_alipay_dict(value)
    @property
    def transfer_from_region(self):
        return self._transfer_from_region

    @transfer_from_region.setter
    def transfer_from_region(self, value):
        self._transfer_from_region = value
    @property
    def transfer_purpose(self):
        return self._transfer_purpose

    @transfer_purpose.setter
    def transfer_purpose(self, value):
        self._transfer_purpose = value
    @property
    def transfer_reference(self):
        return self._transfer_reference

    @transfer_reference.setter
    def transfer_reference(self, value):
        self._transfer_reference = value
    @property
    def transfer_to_region(self):
        return self._transfer_to_region

    @transfer_to_region.setter
    def transfer_to_region(self, value):
        self._transfer_to_region = value


    def to_alipay_dict(self):
        params = dict()
        if self.beneficiary:
            if hasattr(self.beneficiary, 'to_alipay_dict'):
                params['beneficiary'] = self.beneficiary.to_alipay_dict()
            else:
                params['beneficiary'] = self.beneficiary
        if self.payer:
            if hasattr(self.payer, 'to_alipay_dict'):
                params['payer'] = self.payer.to_alipay_dict()
            else:
                params['payer'] = self.payer
        if self.payment_bill:
            if hasattr(self.payment_bill, 'to_alipay_dict'):
                params['payment_bill'] = self.payment_bill.to_alipay_dict()
            else:
                params['payment_bill'] = self.payment_bill
        if self.transfer_from_region:
            if hasattr(self.transfer_from_region, 'to_alipay_dict'):
                params['transfer_from_region'] = self.transfer_from_region.to_alipay_dict()
            else:
                params['transfer_from_region'] = self.transfer_from_region
        if self.transfer_purpose:
            if hasattr(self.transfer_purpose, 'to_alipay_dict'):
                params['transfer_purpose'] = self.transfer_purpose.to_alipay_dict()
            else:
                params['transfer_purpose'] = self.transfer_purpose
        if self.transfer_reference:
            if hasattr(self.transfer_reference, 'to_alipay_dict'):
                params['transfer_reference'] = self.transfer_reference.to_alipay_dict()
            else:
                params['transfer_reference'] = self.transfer_reference
        if self.transfer_to_region:
            if hasattr(self.transfer_to_region, 'to_alipay_dict'):
                params['transfer_to_region'] = self.transfer_to_region.to_alipay_dict()
            else:
                params['transfer_to_region'] = self.transfer_to_region
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdditionalTransferDetail()
        if 'beneficiary' in d:
            o.beneficiary = d['beneficiary']
        if 'payer' in d:
            o.payer = d['payer']
        if 'payment_bill' in d:
            o.payment_bill = d['payment_bill']
        if 'transfer_from_region' in d:
            o.transfer_from_region = d['transfer_from_region']
        if 'transfer_purpose' in d:
            o.transfer_purpose = d['transfer_purpose']
        if 'transfer_reference' in d:
            o.transfer_reference = d['transfer_reference']
        if 'transfer_to_region' in d:
            o.transfer_to_region = d['transfer_to_region']
        return o


