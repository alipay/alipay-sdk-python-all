#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReportBasicInfo(object):

    def __init__(self):
        self._accident_date = None
        self._apply_trade_no = None
        self._estimate_amount = None
        self._policy_no = None
        self._related_order_no = None
        self._report_date = None
        self._report_unique_key = None
        self._reporter_contact_info = None
        self._reporter_name = None
        self._ticket_no = None

    @property
    def accident_date(self):
        return self._accident_date

    @accident_date.setter
    def accident_date(self, value):
        self._accident_date = value
    @property
    def apply_trade_no(self):
        return self._apply_trade_no

    @apply_trade_no.setter
    def apply_trade_no(self, value):
        self._apply_trade_no = value
    @property
    def estimate_amount(self):
        return self._estimate_amount

    @estimate_amount.setter
    def estimate_amount(self, value):
        self._estimate_amount = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def related_order_no(self):
        return self._related_order_no

    @related_order_no.setter
    def related_order_no(self, value):
        self._related_order_no = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
    @property
    def report_unique_key(self):
        return self._report_unique_key

    @report_unique_key.setter
    def report_unique_key(self, value):
        self._report_unique_key = value
    @property
    def reporter_contact_info(self):
        return self._reporter_contact_info

    @reporter_contact_info.setter
    def reporter_contact_info(self, value):
        self._reporter_contact_info = value
    @property
    def reporter_name(self):
        return self._reporter_name

    @reporter_name.setter
    def reporter_name(self, value):
        self._reporter_name = value
    @property
    def ticket_no(self):
        return self._ticket_no

    @ticket_no.setter
    def ticket_no(self, value):
        self._ticket_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.accident_date:
            if hasattr(self.accident_date, 'to_alipay_dict'):
                params['accident_date'] = self.accident_date.to_alipay_dict()
            else:
                params['accident_date'] = self.accident_date
        if self.apply_trade_no:
            if hasattr(self.apply_trade_no, 'to_alipay_dict'):
                params['apply_trade_no'] = self.apply_trade_no.to_alipay_dict()
            else:
                params['apply_trade_no'] = self.apply_trade_no
        if self.estimate_amount:
            if hasattr(self.estimate_amount, 'to_alipay_dict'):
                params['estimate_amount'] = self.estimate_amount.to_alipay_dict()
            else:
                params['estimate_amount'] = self.estimate_amount
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.related_order_no:
            if hasattr(self.related_order_no, 'to_alipay_dict'):
                params['related_order_no'] = self.related_order_no.to_alipay_dict()
            else:
                params['related_order_no'] = self.related_order_no
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        if self.report_unique_key:
            if hasattr(self.report_unique_key, 'to_alipay_dict'):
                params['report_unique_key'] = self.report_unique_key.to_alipay_dict()
            else:
                params['report_unique_key'] = self.report_unique_key
        if self.reporter_contact_info:
            if hasattr(self.reporter_contact_info, 'to_alipay_dict'):
                params['reporter_contact_info'] = self.reporter_contact_info.to_alipay_dict()
            else:
                params['reporter_contact_info'] = self.reporter_contact_info
        if self.reporter_name:
            if hasattr(self.reporter_name, 'to_alipay_dict'):
                params['reporter_name'] = self.reporter_name.to_alipay_dict()
            else:
                params['reporter_name'] = self.reporter_name
        if self.ticket_no:
            if hasattr(self.ticket_no, 'to_alipay_dict'):
                params['ticket_no'] = self.ticket_no.to_alipay_dict()
            else:
                params['ticket_no'] = self.ticket_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReportBasicInfo()
        if 'accident_date' in d:
            o.accident_date = d['accident_date']
        if 'apply_trade_no' in d:
            o.apply_trade_no = d['apply_trade_no']
        if 'estimate_amount' in d:
            o.estimate_amount = d['estimate_amount']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'related_order_no' in d:
            o.related_order_no = d['related_order_no']
        if 'report_date' in d:
            o.report_date = d['report_date']
        if 'report_unique_key' in d:
            o.report_unique_key = d['report_unique_key']
        if 'reporter_contact_info' in d:
            o.reporter_contact_info = d['reporter_contact_info']
        if 'reporter_name' in d:
            o.reporter_name = d['reporter_name']
        if 'ticket_no' in d:
            o.ticket_no = d['ticket_no']
        return o


