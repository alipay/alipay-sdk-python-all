#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FulfillmentItemPdfInfo import FulfillmentItemPdfInfo


class ExaminationParam(object):

    def __init__(self):
        self._expected_report_end_time = None
        self._expected_report_start_time = None
        self._item_id_to_pdf = None
        self._verify_code = None

    @property
    def expected_report_end_time(self):
        return self._expected_report_end_time

    @expected_report_end_time.setter
    def expected_report_end_time(self, value):
        self._expected_report_end_time = value
    @property
    def expected_report_start_time(self):
        return self._expected_report_start_time

    @expected_report_start_time.setter
    def expected_report_start_time(self, value):
        self._expected_report_start_time = value
    @property
    def item_id_to_pdf(self):
        return self._item_id_to_pdf

    @item_id_to_pdf.setter
    def item_id_to_pdf(self, value):
        if isinstance(value, list):
            self._item_id_to_pdf = list()
            for i in value:
                if isinstance(i, FulfillmentItemPdfInfo):
                    self._item_id_to_pdf.append(i)
                else:
                    self._item_id_to_pdf.append(FulfillmentItemPdfInfo.from_alipay_dict(i))
    @property
    def verify_code(self):
        return self._verify_code

    @verify_code.setter
    def verify_code(self, value):
        self._verify_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.expected_report_end_time:
            if hasattr(self.expected_report_end_time, 'to_alipay_dict'):
                params['expected_report_end_time'] = self.expected_report_end_time.to_alipay_dict()
            else:
                params['expected_report_end_time'] = self.expected_report_end_time
        if self.expected_report_start_time:
            if hasattr(self.expected_report_start_time, 'to_alipay_dict'):
                params['expected_report_start_time'] = self.expected_report_start_time.to_alipay_dict()
            else:
                params['expected_report_start_time'] = self.expected_report_start_time
        if self.item_id_to_pdf:
            if isinstance(self.item_id_to_pdf, list):
                for i in range(0, len(self.item_id_to_pdf)):
                    element = self.item_id_to_pdf[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_id_to_pdf[i] = element.to_alipay_dict()
            if hasattr(self.item_id_to_pdf, 'to_alipay_dict'):
                params['item_id_to_pdf'] = self.item_id_to_pdf.to_alipay_dict()
            else:
                params['item_id_to_pdf'] = self.item_id_to_pdf
        if self.verify_code:
            if hasattr(self.verify_code, 'to_alipay_dict'):
                params['verify_code'] = self.verify_code.to_alipay_dict()
            else:
                params['verify_code'] = self.verify_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExaminationParam()
        if 'expected_report_end_time' in d:
            o.expected_report_end_time = d['expected_report_end_time']
        if 'expected_report_start_time' in d:
            o.expected_report_start_time = d['expected_report_start_time']
        if 'item_id_to_pdf' in d:
            o.item_id_to_pdf = d['item_id_to_pdf']
        if 'verify_code' in d:
            o.verify_code = d['verify_code']
        return o


