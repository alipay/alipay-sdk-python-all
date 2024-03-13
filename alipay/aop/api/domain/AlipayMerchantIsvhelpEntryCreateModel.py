#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantEntryBeneficiaryInfo import MerchantEntryBeneficiaryInfo
from alipay.aop.api.domain.MerchantEntryLegalInfo import MerchantEntryLegalInfo
from alipay.aop.api.domain.MerchantEntryOrgInfo import MerchantEntryOrgInfo


class AlipayMerchantIsvhelpEntryCreateModel(object):

    def __init__(self):
        self._beneficiary_is_legal = None
        self._external_id = None
        self._merchant_entry_beneficiary_info = None
        self._merchant_entry_legal_info = None
        self._merchant_entry_org_info = None

    @property
    def beneficiary_is_legal(self):
        return self._beneficiary_is_legal

    @beneficiary_is_legal.setter
    def beneficiary_is_legal(self, value):
        self._beneficiary_is_legal = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def merchant_entry_beneficiary_info(self):
        return self._merchant_entry_beneficiary_info

    @merchant_entry_beneficiary_info.setter
    def merchant_entry_beneficiary_info(self, value):
        if isinstance(value, MerchantEntryBeneficiaryInfo):
            self._merchant_entry_beneficiary_info = value
        else:
            self._merchant_entry_beneficiary_info = MerchantEntryBeneficiaryInfo.from_alipay_dict(value)
    @property
    def merchant_entry_legal_info(self):
        return self._merchant_entry_legal_info

    @merchant_entry_legal_info.setter
    def merchant_entry_legal_info(self, value):
        if isinstance(value, MerchantEntryLegalInfo):
            self._merchant_entry_legal_info = value
        else:
            self._merchant_entry_legal_info = MerchantEntryLegalInfo.from_alipay_dict(value)
    @property
    def merchant_entry_org_info(self):
        return self._merchant_entry_org_info

    @merchant_entry_org_info.setter
    def merchant_entry_org_info(self, value):
        if isinstance(value, MerchantEntryOrgInfo):
            self._merchant_entry_org_info = value
        else:
            self._merchant_entry_org_info = MerchantEntryOrgInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.beneficiary_is_legal:
            if hasattr(self.beneficiary_is_legal, 'to_alipay_dict'):
                params['beneficiary_is_legal'] = self.beneficiary_is_legal.to_alipay_dict()
            else:
                params['beneficiary_is_legal'] = self.beneficiary_is_legal
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.merchant_entry_beneficiary_info:
            if hasattr(self.merchant_entry_beneficiary_info, 'to_alipay_dict'):
                params['merchant_entry_beneficiary_info'] = self.merchant_entry_beneficiary_info.to_alipay_dict()
            else:
                params['merchant_entry_beneficiary_info'] = self.merchant_entry_beneficiary_info
        if self.merchant_entry_legal_info:
            if hasattr(self.merchant_entry_legal_info, 'to_alipay_dict'):
                params['merchant_entry_legal_info'] = self.merchant_entry_legal_info.to_alipay_dict()
            else:
                params['merchant_entry_legal_info'] = self.merchant_entry_legal_info
        if self.merchant_entry_org_info:
            if hasattr(self.merchant_entry_org_info, 'to_alipay_dict'):
                params['merchant_entry_org_info'] = self.merchant_entry_org_info.to_alipay_dict()
            else:
                params['merchant_entry_org_info'] = self.merchant_entry_org_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantIsvhelpEntryCreateModel()
        if 'beneficiary_is_legal' in d:
            o.beneficiary_is_legal = d['beneficiary_is_legal']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'merchant_entry_beneficiary_info' in d:
            o.merchant_entry_beneficiary_info = d['merchant_entry_beneficiary_info']
        if 'merchant_entry_legal_info' in d:
            o.merchant_entry_legal_info = d['merchant_entry_legal_info']
        if 'merchant_entry_org_info' in d:
            o.merchant_entry_org_info = d['merchant_entry_org_info']
        return o


