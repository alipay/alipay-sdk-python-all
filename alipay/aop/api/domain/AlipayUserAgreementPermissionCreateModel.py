#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessParamsMap import BusinessParamsMap


class AlipayUserAgreementPermissionCreateModel(object):

    def __init__(self):
        self._agreement_no = None
        self._business_params = None
        self._notice_template = None
        self._out_request_no = None
        self._total_amount = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        if isinstance(value, BusinessParamsMap):
            self._business_params = value
        else:
            self._business_params = BusinessParamsMap.from_alipay_dict(value)
    @property
    def notice_template(self):
        return self._notice_template

    @notice_template.setter
    def notice_template(self, value):
        self._notice_template = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.business_params:
            if hasattr(self.business_params, 'to_alipay_dict'):
                params['business_params'] = self.business_params.to_alipay_dict()
            else:
                params['business_params'] = self.business_params
        if self.notice_template:
            if hasattr(self.notice_template, 'to_alipay_dict'):
                params['notice_template'] = self.notice_template.to_alipay_dict()
            else:
                params['notice_template'] = self.notice_template
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAgreementPermissionCreateModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'notice_template' in d:
            o.notice_template = d['notice_template']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


