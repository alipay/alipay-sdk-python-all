#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FxiaokeCreateOrUpdateLeadsPredictRecordItemRequest(object):

    def __init__(self):
        self._commodity_cate_code = None
        self._contract_amount = None
        self._software_subscription_years = None

    @property
    def commodity_cate_code(self):
        return self._commodity_cate_code

    @commodity_cate_code.setter
    def commodity_cate_code(self, value):
        self._commodity_cate_code = value
    @property
    def contract_amount(self):
        return self._contract_amount

    @contract_amount.setter
    def contract_amount(self, value):
        self._contract_amount = value
    @property
    def software_subscription_years(self):
        return self._software_subscription_years

    @software_subscription_years.setter
    def software_subscription_years(self, value):
        self._software_subscription_years = value


    def to_alipay_dict(self):
        params = dict()
        if self.commodity_cate_code:
            if hasattr(self.commodity_cate_code, 'to_alipay_dict'):
                params['commodity_cate_code'] = self.commodity_cate_code.to_alipay_dict()
            else:
                params['commodity_cate_code'] = self.commodity_cate_code
        if self.contract_amount:
            if hasattr(self.contract_amount, 'to_alipay_dict'):
                params['contract_amount'] = self.contract_amount.to_alipay_dict()
            else:
                params['contract_amount'] = self.contract_amount
        if self.software_subscription_years:
            if hasattr(self.software_subscription_years, 'to_alipay_dict'):
                params['software_subscription_years'] = self.software_subscription_years.to_alipay_dict()
            else:
                params['software_subscription_years'] = self.software_subscription_years
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FxiaokeCreateOrUpdateLeadsPredictRecordItemRequest()
        if 'commodity_cate_code' in d:
            o.commodity_cate_code = d['commodity_cate_code']
        if 'contract_amount' in d:
            o.contract_amount = d['contract_amount']
        if 'software_subscription_years' in d:
            o.software_subscription_years = d['software_subscription_years']
        return o


