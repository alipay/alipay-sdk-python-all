#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsUnderwriteClaimReportQueryModel(object):

    def __init__(self):
        self._claim_report_no = None

    @property
    def claim_report_no(self):
        return self._claim_report_no

    @claim_report_no.setter
    def claim_report_no(self, value):
        self._claim_report_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.claim_report_no:
            if hasattr(self.claim_report_no, 'to_alipay_dict'):
                params['claim_report_no'] = self.claim_report_no.to_alipay_dict()
            else:
                params['claim_report_no'] = self.claim_report_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsUnderwriteClaimReportQueryModel()
        if 'claim_report_no' in d:
            o.claim_report_no = d['claim_report_no']
        return o


