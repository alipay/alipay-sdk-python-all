#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentPlanCancelInfo(object):

    def __init__(self):
        self._cancel_start_installment_no = None
        self._reason_code = None
        self._reason_desc = None

    @property
    def cancel_start_installment_no(self):
        return self._cancel_start_installment_no

    @cancel_start_installment_no.setter
    def cancel_start_installment_no(self, value):
        self._cancel_start_installment_no = value
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value
    @property
    def reason_desc(self):
        return self._reason_desc

    @reason_desc.setter
    def reason_desc(self, value):
        self._reason_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_start_installment_no:
            if hasattr(self.cancel_start_installment_no, 'to_alipay_dict'):
                params['cancel_start_installment_no'] = self.cancel_start_installment_no.to_alipay_dict()
            else:
                params['cancel_start_installment_no'] = self.cancel_start_installment_no
        if self.reason_code:
            if hasattr(self.reason_code, 'to_alipay_dict'):
                params['reason_code'] = self.reason_code.to_alipay_dict()
            else:
                params['reason_code'] = self.reason_code
        if self.reason_desc:
            if hasattr(self.reason_desc, 'to_alipay_dict'):
                params['reason_desc'] = self.reason_desc.to_alipay_dict()
            else:
                params['reason_desc'] = self.reason_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentPlanCancelInfo()
        if 'cancel_start_installment_no' in d:
            o.cancel_start_installment_no = d['cancel_start_installment_no']
        if 'reason_code' in d:
            o.reason_code = d['reason_code']
        if 'reason_desc' in d:
            o.reason_desc = d['reason_desc']
        return o


