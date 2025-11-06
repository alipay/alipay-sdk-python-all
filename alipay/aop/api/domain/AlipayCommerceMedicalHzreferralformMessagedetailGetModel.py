#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHzreferralformMessagedetailGetModel(object):

    def __init__(self):
        self._query = None
        self._referral_from_id = None

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def referral_from_id(self):
        return self._referral_from_id

    @referral_from_id.setter
    def referral_from_id(self, value):
        self._referral_from_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.referral_from_id:
            if hasattr(self.referral_from_id, 'to_alipay_dict'):
                params['referral_from_id'] = self.referral_from_id.to_alipay_dict()
            else:
                params['referral_from_id'] = self.referral_from_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHzreferralformMessagedetailGetModel()
        if 'query' in d:
            o.query = d['query']
        if 'referral_from_id' in d:
            o.referral_from_id = d['referral_from_id']
        return o


