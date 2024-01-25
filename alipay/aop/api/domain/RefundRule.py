#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RefundRuleDetail import RefundRuleDetail


class RefundRule(object):

    def __init__(self):
        self._end_date = None
        self._refund_rule_details = None
        self._refund_rule_id = None
        self._refund_rule_type = None
        self._start_date = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def refund_rule_details(self):
        return self._refund_rule_details

    @refund_rule_details.setter
    def refund_rule_details(self, value):
        if isinstance(value, list):
            self._refund_rule_details = list()
            for i in value:
                if isinstance(i, RefundRuleDetail):
                    self._refund_rule_details.append(i)
                else:
                    self._refund_rule_details.append(RefundRuleDetail.from_alipay_dict(i))
    @property
    def refund_rule_id(self):
        return self._refund_rule_id

    @refund_rule_id.setter
    def refund_rule_id(self, value):
        self._refund_rule_id = value
    @property
    def refund_rule_type(self):
        return self._refund_rule_type

    @refund_rule_type.setter
    def refund_rule_type(self, value):
        self._refund_rule_type = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.refund_rule_details:
            if isinstance(self.refund_rule_details, list):
                for i in range(0, len(self.refund_rule_details)):
                    element = self.refund_rule_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_rule_details[i] = element.to_alipay_dict()
            if hasattr(self.refund_rule_details, 'to_alipay_dict'):
                params['refund_rule_details'] = self.refund_rule_details.to_alipay_dict()
            else:
                params['refund_rule_details'] = self.refund_rule_details
        if self.refund_rule_id:
            if hasattr(self.refund_rule_id, 'to_alipay_dict'):
                params['refund_rule_id'] = self.refund_rule_id.to_alipay_dict()
            else:
                params['refund_rule_id'] = self.refund_rule_id
        if self.refund_rule_type:
            if hasattr(self.refund_rule_type, 'to_alipay_dict'):
                params['refund_rule_type'] = self.refund_rule_type.to_alipay_dict()
            else:
                params['refund_rule_type'] = self.refund_rule_type
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundRule()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'refund_rule_details' in d:
            o.refund_rule_details = d['refund_rule_details']
        if 'refund_rule_id' in d:
            o.refund_rule_id = d['refund_rule_id']
        if 'refund_rule_type' in d:
            o.refund_rule_type = d['refund_rule_type']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


