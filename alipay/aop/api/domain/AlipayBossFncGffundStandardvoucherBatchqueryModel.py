#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StandardVoucherMultipleConditionQueryRequest import StandardVoucherMultipleConditionQueryRequest


class AlipayBossFncGffundStandardvoucherBatchqueryModel(object):

    def __init__(self):
        self._standard_voucher_multiple_condition_query_request = None

    @property
    def standard_voucher_multiple_condition_query_request(self):
        return self._standard_voucher_multiple_condition_query_request

    @standard_voucher_multiple_condition_query_request.setter
    def standard_voucher_multiple_condition_query_request(self, value):
        if isinstance(value, StandardVoucherMultipleConditionQueryRequest):
            self._standard_voucher_multiple_condition_query_request = value
        else:
            self._standard_voucher_multiple_condition_query_request = StandardVoucherMultipleConditionQueryRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.standard_voucher_multiple_condition_query_request:
            if hasattr(self.standard_voucher_multiple_condition_query_request, 'to_alipay_dict'):
                params['standard_voucher_multiple_condition_query_request'] = self.standard_voucher_multiple_condition_query_request.to_alipay_dict()
            else:
                params['standard_voucher_multiple_condition_query_request'] = self.standard_voucher_multiple_condition_query_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGffundStandardvoucherBatchqueryModel()
        if 'standard_voucher_multiple_condition_query_request' in d:
            o.standard_voucher_multiple_condition_query_request = d['standard_voucher_multiple_condition_query_request']
        return o


