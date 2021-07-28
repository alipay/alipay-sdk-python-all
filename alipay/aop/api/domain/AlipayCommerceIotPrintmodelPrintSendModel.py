#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceModelContext import ServiceModelContext
from alipay.aop.api.domain.PrintMessageVO import PrintMessageVO


class AlipayCommerceIotPrintmodelPrintSendModel(object):

    def __init__(self):
        self._context = None
        self._print_message = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        if isinstance(value, ServiceModelContext):
            self._context = value
        else:
            self._context = ServiceModelContext.from_alipay_dict(value)
    @property
    def print_message(self):
        return self._print_message

    @print_message.setter
    def print_message(self, value):
        if isinstance(value, PrintMessageVO):
            self._print_message = value
        else:
            self._print_message = PrintMessageVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.context:
            if hasattr(self.context, 'to_alipay_dict'):
                params['context'] = self.context.to_alipay_dict()
            else:
                params['context'] = self.context
        if self.print_message:
            if hasattr(self.print_message, 'to_alipay_dict'):
                params['print_message'] = self.print_message.to_alipay_dict()
            else:
                params['print_message'] = self.print_message
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotPrintmodelPrintSendModel()
        if 'context' in d:
            o.context = d['context']
        if 'print_message' in d:
            o.print_message = d['print_message']
        return o


