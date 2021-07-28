#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsPerson import InsPerson
from alipay.aop.api.domain.InsOrderInfo import InsOrderInfo
from alipay.aop.api.domain.InsPerson import InsPerson


class AlipayInsSceneClaimNewreportCreateModel(object):

    def __init__(self):
        self._apply_reason = None
        self._apply_result = None
        self._beneficiary = None
        self._biz_data = None
        self._claim_fee = None
        self._claim_report_reason = None
        self._order_info = None
        self._out_biz_no = None
        self._policy_no = None
        self._prod_code = None
        self._reporter = None

    @property
    def apply_reason(self):
        return self._apply_reason

    @apply_reason.setter
    def apply_reason(self, value):
        self._apply_reason = value
    @property
    def apply_result(self):
        return self._apply_result

    @apply_result.setter
    def apply_result(self, value):
        self._apply_result = value
    @property
    def beneficiary(self):
        return self._beneficiary

    @beneficiary.setter
    def beneficiary(self, value):
        if isinstance(value, InsPerson):
            self._beneficiary = value
        else:
            self._beneficiary = InsPerson.from_alipay_dict(value)
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def claim_fee(self):
        return self._claim_fee

    @claim_fee.setter
    def claim_fee(self, value):
        self._claim_fee = value
    @property
    def claim_report_reason(self):
        return self._claim_report_reason

    @claim_report_reason.setter
    def claim_report_reason(self, value):
        self._claim_report_reason = value
    @property
    def order_info(self):
        return self._order_info

    @order_info.setter
    def order_info(self, value):
        if isinstance(value, InsOrderInfo):
            self._order_info = value
        else:
            self._order_info = InsOrderInfo.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def reporter(self):
        return self._reporter

    @reporter.setter
    def reporter(self, value):
        if isinstance(value, InsPerson):
            self._reporter = value
        else:
            self._reporter = InsPerson.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.apply_reason:
            if hasattr(self.apply_reason, 'to_alipay_dict'):
                params['apply_reason'] = self.apply_reason.to_alipay_dict()
            else:
                params['apply_reason'] = self.apply_reason
        if self.apply_result:
            if hasattr(self.apply_result, 'to_alipay_dict'):
                params['apply_result'] = self.apply_result.to_alipay_dict()
            else:
                params['apply_result'] = self.apply_result
        if self.beneficiary:
            if hasattr(self.beneficiary, 'to_alipay_dict'):
                params['beneficiary'] = self.beneficiary.to_alipay_dict()
            else:
                params['beneficiary'] = self.beneficiary
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.claim_fee:
            if hasattr(self.claim_fee, 'to_alipay_dict'):
                params['claim_fee'] = self.claim_fee.to_alipay_dict()
            else:
                params['claim_fee'] = self.claim_fee
        if self.claim_report_reason:
            if hasattr(self.claim_report_reason, 'to_alipay_dict'):
                params['claim_report_reason'] = self.claim_report_reason.to_alipay_dict()
            else:
                params['claim_report_reason'] = self.claim_report_reason
        if self.order_info:
            if hasattr(self.order_info, 'to_alipay_dict'):
                params['order_info'] = self.order_info.to_alipay_dict()
            else:
                params['order_info'] = self.order_info
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.reporter:
            if hasattr(self.reporter, 'to_alipay_dict'):
                params['reporter'] = self.reporter.to_alipay_dict()
            else:
                params['reporter'] = self.reporter
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneClaimNewreportCreateModel()
        if 'apply_reason' in d:
            o.apply_reason = d['apply_reason']
        if 'apply_result' in d:
            o.apply_result = d['apply_result']
        if 'beneficiary' in d:
            o.beneficiary = d['beneficiary']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'claim_fee' in d:
            o.claim_fee = d['claim_fee']
        if 'claim_report_reason' in d:
            o.claim_report_reason = d['claim_report_reason']
        if 'order_info' in d:
            o.order_info = d['order_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'reporter' in d:
            o.reporter = d['reporter']
        return o


