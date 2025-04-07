#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InquiryBizContent(object):

    def __init__(self):
        self._has_record = None

    @property
    def has_record(self):
        return self._has_record

    @has_record.setter
    def has_record(self, value):
        self._has_record = value


    def to_alipay_dict(self):
        params = dict()
        if self.has_record:
            if hasattr(self.has_record, 'to_alipay_dict'):
                params['has_record'] = self.has_record.to_alipay_dict()
            else:
                params['has_record'] = self.has_record
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InquiryBizContent()
        if 'has_record' in d:
            o.has_record = d['has_record']
        return o


