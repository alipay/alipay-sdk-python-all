#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExtContext(object):

    def __init__(self):
        self._ebank_form = None
        self._return_message = None

    @property
    def ebank_form(self):
        return self._ebank_form

    @ebank_form.setter
    def ebank_form(self, value):
        self._ebank_form = value
    @property
    def return_message(self):
        return self._return_message

    @return_message.setter
    def return_message(self, value):
        self._return_message = value


    def to_alipay_dict(self):
        params = dict()
        if self.ebank_form:
            if hasattr(self.ebank_form, 'to_alipay_dict'):
                params['ebank_form'] = self.ebank_form.to_alipay_dict()
            else:
                params['ebank_form'] = self.ebank_form
        if self.return_message:
            if hasattr(self.return_message, 'to_alipay_dict'):
                params['return_message'] = self.return_message.to_alipay_dict()
            else:
                params['return_message'] = self.return_message
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExtContext()
        if 'ebank_form' in d:
            o.ebank_form = d['ebank_form']
        if 'return_message' in d:
            o.return_message = d['return_message']
        return o


