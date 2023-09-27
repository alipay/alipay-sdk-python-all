#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncGfsmartpayInvoicebillserviceBatchqueryModel(object):

    def __init__(self):
        self._biz_code = None
        self._biz_document_nos = None
        self._related_document_nos = None
        self._test_mode = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_document_nos(self):
        return self._biz_document_nos

    @biz_document_nos.setter
    def biz_document_nos(self, value):
        if isinstance(value, list):
            self._biz_document_nos = list()
            for i in value:
                self._biz_document_nos.append(i)
    @property
    def related_document_nos(self):
        return self._related_document_nos

    @related_document_nos.setter
    def related_document_nos(self, value):
        if isinstance(value, list):
            self._related_document_nos = list()
            for i in value:
                self._related_document_nos.append(i)
    @property
    def test_mode(self):
        return self._test_mode

    @test_mode.setter
    def test_mode(self, value):
        self._test_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_document_nos:
            if isinstance(self.biz_document_nos, list):
                for i in range(0, len(self.biz_document_nos)):
                    element = self.biz_document_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_document_nos[i] = element.to_alipay_dict()
            if hasattr(self.biz_document_nos, 'to_alipay_dict'):
                params['biz_document_nos'] = self.biz_document_nos.to_alipay_dict()
            else:
                params['biz_document_nos'] = self.biz_document_nos
        if self.related_document_nos:
            if isinstance(self.related_document_nos, list):
                for i in range(0, len(self.related_document_nos)):
                    element = self.related_document_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_document_nos[i] = element.to_alipay_dict()
            if hasattr(self.related_document_nos, 'to_alipay_dict'):
                params['related_document_nos'] = self.related_document_nos.to_alipay_dict()
            else:
                params['related_document_nos'] = self.related_document_nos
        if self.test_mode:
            if hasattr(self.test_mode, 'to_alipay_dict'):
                params['test_mode'] = self.test_mode.to_alipay_dict()
            else:
                params['test_mode'] = self.test_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsmartpayInvoicebillserviceBatchqueryModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_document_nos' in d:
            o.biz_document_nos = d['biz_document_nos']
        if 'related_document_nos' in d:
            o.related_document_nos = d['related_document_nos']
        if 'test_mode' in d:
            o.test_mode = d['test_mode']
        return o


