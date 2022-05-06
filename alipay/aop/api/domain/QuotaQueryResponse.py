#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AccountQuotaDetail import AccountQuotaDetail


class QuotaQueryResponse(object):

    def __init__(self):
        self._agreement_no = None
        self._error_code = None
        self._fail_reason = None
        self._quota_details = None
        self._success = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def quota_details(self):
        return self._quota_details

    @quota_details.setter
    def quota_details(self, value):
        if isinstance(value, AccountQuotaDetail):
            self._quota_details = value
        else:
            self._quota_details = AccountQuotaDetail.from_alipay_dict(value)
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.quota_details:
            if hasattr(self.quota_details, 'to_alipay_dict'):
                params['quota_details'] = self.quota_details.to_alipay_dict()
            else:
                params['quota_details'] = self.quota_details
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QuotaQueryResponse()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'quota_details' in d:
            o.quota_details = d['quota_details']
        if 'success' in d:
            o.success = d['success']
        return o


