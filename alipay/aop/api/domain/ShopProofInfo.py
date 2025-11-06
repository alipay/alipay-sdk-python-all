#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopProofInfo(object):

    def __init__(self):
        self._appeal_letter_url = None
        self._lease_contract_url = None
        self._property_ownership_proof_url = None

    @property
    def appeal_letter_url(self):
        return self._appeal_letter_url

    @appeal_letter_url.setter
    def appeal_letter_url(self, value):
        self._appeal_letter_url = value
    @property
    def lease_contract_url(self):
        return self._lease_contract_url

    @lease_contract_url.setter
    def lease_contract_url(self, value):
        self._lease_contract_url = value
    @property
    def property_ownership_proof_url(self):
        return self._property_ownership_proof_url

    @property_ownership_proof_url.setter
    def property_ownership_proof_url(self, value):
        self._property_ownership_proof_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.appeal_letter_url:
            if hasattr(self.appeal_letter_url, 'to_alipay_dict'):
                params['appeal_letter_url'] = self.appeal_letter_url.to_alipay_dict()
            else:
                params['appeal_letter_url'] = self.appeal_letter_url
        if self.lease_contract_url:
            if hasattr(self.lease_contract_url, 'to_alipay_dict'):
                params['lease_contract_url'] = self.lease_contract_url.to_alipay_dict()
            else:
                params['lease_contract_url'] = self.lease_contract_url
        if self.property_ownership_proof_url:
            if hasattr(self.property_ownership_proof_url, 'to_alipay_dict'):
                params['property_ownership_proof_url'] = self.property_ownership_proof_url.to_alipay_dict()
            else:
                params['property_ownership_proof_url'] = self.property_ownership_proof_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopProofInfo()
        if 'appeal_letter_url' in d:
            o.appeal_letter_url = d['appeal_letter_url']
        if 'lease_contract_url' in d:
            o.lease_contract_url = d['lease_contract_url']
        if 'property_ownership_proof_url' in d:
            o.property_ownership_proof_url = d['property_ownership_proof_url']
        return o


