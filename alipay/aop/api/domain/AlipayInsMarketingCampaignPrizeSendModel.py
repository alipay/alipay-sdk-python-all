#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsMktFactorDTO import InsMktFactorDTO


class AlipayInsMarketingCampaignPrizeSendModel(object):

    def __init__(self):
        self._account_id = None
        self._account_type = None
        self._campaign_id = None
        self._factors = None
        self._out_biz_no = None
        self._request_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        self._campaign_id = value
    @property
    def factors(self):
        return self._factors

    @factors.setter
    def factors(self, value):
        if isinstance(value, list):
            self._factors = list()
            for i in value:
                if isinstance(i, InsMktFactorDTO):
                    self._factors.append(i)
                else:
                    self._factors.append(InsMktFactorDTO.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.campaign_id:
            if hasattr(self.campaign_id, 'to_alipay_dict'):
                params['campaign_id'] = self.campaign_id.to_alipay_dict()
            else:
                params['campaign_id'] = self.campaign_id
        if self.factors:
            if isinstance(self.factors, list):
                for i in range(0, len(self.factors)):
                    element = self.factors[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.factors[i] = element.to_alipay_dict()
            if hasattr(self.factors, 'to_alipay_dict'):
                params['factors'] = self.factors.to_alipay_dict()
            else:
                params['factors'] = self.factors
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsMarketingCampaignPrizeSendModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'campaign_id' in d:
            o.campaign_id = d['campaign_id']
        if 'factors' in d:
            o.factors = d['factors']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


