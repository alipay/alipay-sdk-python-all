#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FulfillmentItemPdfInfo import FulfillmentItemPdfInfo


class ExaminationCheckInfo(object):

    def __init__(self):
        self._check_no = None
        self._report_info_list = None

    @property
    def check_no(self):
        return self._check_no

    @check_no.setter
    def check_no(self, value):
        self._check_no = value
    @property
    def report_info_list(self):
        return self._report_info_list

    @report_info_list.setter
    def report_info_list(self, value):
        if isinstance(value, list):
            self._report_info_list = list()
            for i in value:
                if isinstance(i, FulfillmentItemPdfInfo):
                    self._report_info_list.append(i)
                else:
                    self._report_info_list.append(FulfillmentItemPdfInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.check_no:
            if hasattr(self.check_no, 'to_alipay_dict'):
                params['check_no'] = self.check_no.to_alipay_dict()
            else:
                params['check_no'] = self.check_no
        if self.report_info_list:
            if isinstance(self.report_info_list, list):
                for i in range(0, len(self.report_info_list)):
                    element = self.report_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.report_info_list[i] = element.to_alipay_dict()
            if hasattr(self.report_info_list, 'to_alipay_dict'):
                params['report_info_list'] = self.report_info_list.to_alipay_dict()
            else:
                params['report_info_list'] = self.report_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExaminationCheckInfo()
        if 'check_no' in d:
            o.check_no = d['check_no']
        if 'report_info_list' in d:
            o.report_info_list = d['report_info_list']
        return o


