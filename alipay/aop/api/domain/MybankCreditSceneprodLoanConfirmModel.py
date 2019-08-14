#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSceneprodLoanConfirmModel(object):

    def __init__(self):
        self._apply_no = None
        self._approve_result = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._fin_order_no = None
        self._refuse_code = None
        self._refuse_reason = None
        self._remark = None
        self._request_id = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def approve_result(self):
        return self._approve_result

    @approve_result.setter
    def approve_result(self, value):
        self._approve_result = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def fin_order_no(self):
        return self._fin_order_no

    @fin_order_no.setter
    def fin_order_no(self, value):
        self._fin_order_no = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def refuse_reason(self):
        return self._refuse_reason

    @refuse_reason.setter
    def refuse_reason(self, value):
        self._refuse_reason = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.approve_result:
            if hasattr(self.approve_result, 'to_alipay_dict'):
                params['approve_result'] = self.approve_result.to_alipay_dict()
            else:
                params['approve_result'] = self.approve_result
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.fin_order_no:
            if hasattr(self.fin_order_no, 'to_alipay_dict'):
                params['fin_order_no'] = self.fin_order_no.to_alipay_dict()
            else:
                params['fin_order_no'] = self.fin_order_no
        if self.refuse_code:
            if hasattr(self.refuse_code, 'to_alipay_dict'):
                params['refuse_code'] = self.refuse_code.to_alipay_dict()
            else:
                params['refuse_code'] = self.refuse_code
        if self.refuse_reason:
            if hasattr(self.refuse_reason, 'to_alipay_dict'):
                params['refuse_reason'] = self.refuse_reason.to_alipay_dict()
            else:
                params['refuse_reason'] = self.refuse_reason
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
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
        o = MybankCreditSceneprodLoanConfirmModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'approve_result' in d:
            o.approve_result = d['approve_result']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'fin_order_no' in d:
            o.fin_order_no = d['fin_order_no']
        if 'refuse_code' in d:
            o.refuse_code = d['refuse_code']
        if 'refuse_reason' in d:
            o.refuse_reason = d['refuse_reason']
        if 'remark' in d:
            o.remark = d['remark']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


