#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsuClaimAttachmentVo(object):

    def __init__(self):
        self._anamnesis = None
        self._ids = None
        self._invoice = None

    @property
    def anamnesis(self):
        return self._anamnesis

    @anamnesis.setter
    def anamnesis(self, value):
        if isinstance(value, list):
            self._anamnesis = list()
            for i in value:
                self._anamnesis.append(i)
    @property
    def ids(self):
        return self._ids

    @ids.setter
    def ids(self, value):
        if isinstance(value, list):
            self._ids = list()
            for i in value:
                self._ids.append(i)
    @property
    def invoice(self):
        return self._invoice

    @invoice.setter
    def invoice(self, value):
        if isinstance(value, list):
            self._invoice = list()
            for i in value:
                self._invoice.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.anamnesis:
            if isinstance(self.anamnesis, list):
                for i in range(0, len(self.anamnesis)):
                    element = self.anamnesis[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.anamnesis[i] = element.to_alipay_dict()
            if hasattr(self.anamnesis, 'to_alipay_dict'):
                params['anamnesis'] = self.anamnesis.to_alipay_dict()
            else:
                params['anamnesis'] = self.anamnesis
        if self.ids:
            if isinstance(self.ids, list):
                for i in range(0, len(self.ids)):
                    element = self.ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ids[i] = element.to_alipay_dict()
            if hasattr(self.ids, 'to_alipay_dict'):
                params['ids'] = self.ids.to_alipay_dict()
            else:
                params['ids'] = self.ids
        if self.invoice:
            if isinstance(self.invoice, list):
                for i in range(0, len(self.invoice)):
                    element = self.invoice[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice[i] = element.to_alipay_dict()
            if hasattr(self.invoice, 'to_alipay_dict'):
                params['invoice'] = self.invoice.to_alipay_dict()
            else:
                params['invoice'] = self.invoice
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsuClaimAttachmentVo()
        if 'anamnesis' in d:
            o.anamnesis = d['anamnesis']
        if 'ids' in d:
            o.ids = d['ids']
        if 'invoice' in d:
            o.invoice = d['invoice']
        return o


