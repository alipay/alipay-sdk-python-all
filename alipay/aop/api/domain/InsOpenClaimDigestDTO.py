#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsOpenClaimDigestDTO(object):

    def __init__(self):
        self._claim_apply_time = None
        self._claim_assess_time = None
        self._claim_cancel_time = None
        self._claim_fee = None
        self._claim_no = None
        self._claim_record_time = None
        self._claim_report_no = None
        self._claim_status = None
        self._fund_result_code = None
        self._fund_result_desc = None
        self._fund_status = None
        self._out_biz_no = None
        self._policy_no = None
        self._product_code = None
        self._reject_reason = None

    @property
    def claim_apply_time(self):
        return self._claim_apply_time

    @claim_apply_time.setter
    def claim_apply_time(self, value):
        self._claim_apply_time = value
    @property
    def claim_assess_time(self):
        return self._claim_assess_time

    @claim_assess_time.setter
    def claim_assess_time(self, value):
        self._claim_assess_time = value
    @property
    def claim_cancel_time(self):
        return self._claim_cancel_time

    @claim_cancel_time.setter
    def claim_cancel_time(self, value):
        self._claim_cancel_time = value
    @property
    def claim_fee(self):
        return self._claim_fee

    @claim_fee.setter
    def claim_fee(self, value):
        self._claim_fee = value
    @property
    def claim_no(self):
        return self._claim_no

    @claim_no.setter
    def claim_no(self, value):
        self._claim_no = value
    @property
    def claim_record_time(self):
        return self._claim_record_time

    @claim_record_time.setter
    def claim_record_time(self, value):
        self._claim_record_time = value
    @property
    def claim_report_no(self):
        return self._claim_report_no

    @claim_report_no.setter
    def claim_report_no(self, value):
        self._claim_report_no = value
    @property
    def claim_status(self):
        return self._claim_status

    @claim_status.setter
    def claim_status(self, value):
        self._claim_status = value
    @property
    def fund_result_code(self):
        return self._fund_result_code

    @fund_result_code.setter
    def fund_result_code(self, value):
        self._fund_result_code = value
    @property
    def fund_result_desc(self):
        return self._fund_result_desc

    @fund_result_desc.setter
    def fund_result_desc(self, value):
        self._fund_result_desc = value
    @property
    def fund_status(self):
        return self._fund_status

    @fund_status.setter
    def fund_status(self, value):
        self._fund_status = value
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
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.claim_apply_time:
            if hasattr(self.claim_apply_time, 'to_alipay_dict'):
                params['claim_apply_time'] = self.claim_apply_time.to_alipay_dict()
            else:
                params['claim_apply_time'] = self.claim_apply_time
        if self.claim_assess_time:
            if hasattr(self.claim_assess_time, 'to_alipay_dict'):
                params['claim_assess_time'] = self.claim_assess_time.to_alipay_dict()
            else:
                params['claim_assess_time'] = self.claim_assess_time
        if self.claim_cancel_time:
            if hasattr(self.claim_cancel_time, 'to_alipay_dict'):
                params['claim_cancel_time'] = self.claim_cancel_time.to_alipay_dict()
            else:
                params['claim_cancel_time'] = self.claim_cancel_time
        if self.claim_fee:
            if hasattr(self.claim_fee, 'to_alipay_dict'):
                params['claim_fee'] = self.claim_fee.to_alipay_dict()
            else:
                params['claim_fee'] = self.claim_fee
        if self.claim_no:
            if hasattr(self.claim_no, 'to_alipay_dict'):
                params['claim_no'] = self.claim_no.to_alipay_dict()
            else:
                params['claim_no'] = self.claim_no
        if self.claim_record_time:
            if hasattr(self.claim_record_time, 'to_alipay_dict'):
                params['claim_record_time'] = self.claim_record_time.to_alipay_dict()
            else:
                params['claim_record_time'] = self.claim_record_time
        if self.claim_report_no:
            if hasattr(self.claim_report_no, 'to_alipay_dict'):
                params['claim_report_no'] = self.claim_report_no.to_alipay_dict()
            else:
                params['claim_report_no'] = self.claim_report_no
        if self.claim_status:
            if hasattr(self.claim_status, 'to_alipay_dict'):
                params['claim_status'] = self.claim_status.to_alipay_dict()
            else:
                params['claim_status'] = self.claim_status
        if self.fund_result_code:
            if hasattr(self.fund_result_code, 'to_alipay_dict'):
                params['fund_result_code'] = self.fund_result_code.to_alipay_dict()
            else:
                params['fund_result_code'] = self.fund_result_code
        if self.fund_result_desc:
            if hasattr(self.fund_result_desc, 'to_alipay_dict'):
                params['fund_result_desc'] = self.fund_result_desc.to_alipay_dict()
            else:
                params['fund_result_desc'] = self.fund_result_desc
        if self.fund_status:
            if hasattr(self.fund_status, 'to_alipay_dict'):
                params['fund_status'] = self.fund_status.to_alipay_dict()
            else:
                params['fund_status'] = self.fund_status
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
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsOpenClaimDigestDTO()
        if 'claim_apply_time' in d:
            o.claim_apply_time = d['claim_apply_time']
        if 'claim_assess_time' in d:
            o.claim_assess_time = d['claim_assess_time']
        if 'claim_cancel_time' in d:
            o.claim_cancel_time = d['claim_cancel_time']
        if 'claim_fee' in d:
            o.claim_fee = d['claim_fee']
        if 'claim_no' in d:
            o.claim_no = d['claim_no']
        if 'claim_record_time' in d:
            o.claim_record_time = d['claim_record_time']
        if 'claim_report_no' in d:
            o.claim_report_no = d['claim_report_no']
        if 'claim_status' in d:
            o.claim_status = d['claim_status']
        if 'fund_result_code' in d:
            o.fund_result_code = d['fund_result_code']
        if 'fund_result_desc' in d:
            o.fund_result_desc = d['fund_result_desc']
        if 'fund_status' in d:
            o.fund_status = d['fund_status']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        return o


