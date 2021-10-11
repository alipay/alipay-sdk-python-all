#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReportInfo(object):

    def __init__(self):
        self._case_no = None
        self._case_status = None
        self._case_times = None
        self._end_case_amount = None
        self._end_case_date = None
        self._indemnity_conclusion = None
        self._pay_date = None
        self._policy_no = None
        self._product_name = None
        self._report_date = None
        self._report_no = None

    @property
    def case_no(self):
        return self._case_no

    @case_no.setter
    def case_no(self, value):
        self._case_no = value
    @property
    def case_status(self):
        return self._case_status

    @case_status.setter
    def case_status(self, value):
        self._case_status = value
    @property
    def case_times(self):
        return self._case_times

    @case_times.setter
    def case_times(self, value):
        self._case_times = value
    @property
    def end_case_amount(self):
        return self._end_case_amount

    @end_case_amount.setter
    def end_case_amount(self, value):
        self._end_case_amount = value
    @property
    def end_case_date(self):
        return self._end_case_date

    @end_case_date.setter
    def end_case_date(self, value):
        self._end_case_date = value
    @property
    def indemnity_conclusion(self):
        return self._indemnity_conclusion

    @indemnity_conclusion.setter
    def indemnity_conclusion(self, value):
        self._indemnity_conclusion = value
    @property
    def pay_date(self):
        return self._pay_date

    @pay_date.setter
    def pay_date(self, value):
        self._pay_date = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
    @property
    def report_no(self):
        return self._report_no

    @report_no.setter
    def report_no(self, value):
        self._report_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.case_no:
            if hasattr(self.case_no, 'to_alipay_dict'):
                params['case_no'] = self.case_no.to_alipay_dict()
            else:
                params['case_no'] = self.case_no
        if self.case_status:
            if hasattr(self.case_status, 'to_alipay_dict'):
                params['case_status'] = self.case_status.to_alipay_dict()
            else:
                params['case_status'] = self.case_status
        if self.case_times:
            if hasattr(self.case_times, 'to_alipay_dict'):
                params['case_times'] = self.case_times.to_alipay_dict()
            else:
                params['case_times'] = self.case_times
        if self.end_case_amount:
            if hasattr(self.end_case_amount, 'to_alipay_dict'):
                params['end_case_amount'] = self.end_case_amount.to_alipay_dict()
            else:
                params['end_case_amount'] = self.end_case_amount
        if self.end_case_date:
            if hasattr(self.end_case_date, 'to_alipay_dict'):
                params['end_case_date'] = self.end_case_date.to_alipay_dict()
            else:
                params['end_case_date'] = self.end_case_date
        if self.indemnity_conclusion:
            if hasattr(self.indemnity_conclusion, 'to_alipay_dict'):
                params['indemnity_conclusion'] = self.indemnity_conclusion.to_alipay_dict()
            else:
                params['indemnity_conclusion'] = self.indemnity_conclusion
        if self.pay_date:
            if hasattr(self.pay_date, 'to_alipay_dict'):
                params['pay_date'] = self.pay_date.to_alipay_dict()
            else:
                params['pay_date'] = self.pay_date
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        if self.report_no:
            if hasattr(self.report_no, 'to_alipay_dict'):
                params['report_no'] = self.report_no.to_alipay_dict()
            else:
                params['report_no'] = self.report_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReportInfo()
        if 'case_no' in d:
            o.case_no = d['case_no']
        if 'case_status' in d:
            o.case_status = d['case_status']
        if 'case_times' in d:
            o.case_times = d['case_times']
        if 'end_case_amount' in d:
            o.end_case_amount = d['end_case_amount']
        if 'end_case_date' in d:
            o.end_case_date = d['end_case_date']
        if 'indemnity_conclusion' in d:
            o.indemnity_conclusion = d['indemnity_conclusion']
        if 'pay_date' in d:
            o.pay_date = d['pay_date']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'report_date' in d:
            o.report_date = d['report_date']
        if 'report_no' in d:
            o.report_no = d['report_no']
        return o


