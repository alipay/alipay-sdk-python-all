#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContentErrorDetai import ContentErrorDetai


class ContentErrorInfo(object):

    def __init__(self):
        self._error_amount = None
        self._error_details = None

    @property
    def error_amount(self):
        return self._error_amount

    @error_amount.setter
    def error_amount(self, value):
        self._error_amount = value
    @property
    def error_details(self):
        return self._error_details

    @error_details.setter
    def error_details(self, value):
        if isinstance(value, list):
            self._error_details = list()
            for i in value:
                if isinstance(i, ContentErrorDetai):
                    self._error_details.append(i)
                else:
                    self._error_details.append(ContentErrorDetai.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.error_amount:
            if hasattr(self.error_amount, 'to_alipay_dict'):
                params['error_amount'] = self.error_amount.to_alipay_dict()
            else:
                params['error_amount'] = self.error_amount
        if self.error_details:
            if isinstance(self.error_details, list):
                for i in range(0, len(self.error_details)):
                    element = self.error_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.error_details[i] = element.to_alipay_dict()
            if hasattr(self.error_details, 'to_alipay_dict'):
                params['error_details'] = self.error_details.to_alipay_dict()
            else:
                params['error_details'] = self.error_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentErrorInfo()
        if 'error_amount' in d:
            o.error_amount = d['error_amount']
        if 'error_details' in d:
            o.error_details = d['error_details']
        return o


