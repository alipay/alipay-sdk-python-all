#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DecorationLeadsFeedbackContact(object):

    def __init__(self):
        self._contact_result = None
        self._contact_time = None
        self._in_store = None
        self._interest = None

    @property
    def contact_result(self):
        return self._contact_result

    @contact_result.setter
    def contact_result(self, value):
        self._contact_result = value
    @property
    def contact_time(self):
        return self._contact_time

    @contact_time.setter
    def contact_time(self, value):
        self._contact_time = value
    @property
    def in_store(self):
        return self._in_store

    @in_store.setter
    def in_store(self, value):
        self._in_store = value
    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, value):
        self._interest = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_result:
            if hasattr(self.contact_result, 'to_alipay_dict'):
                params['contact_result'] = self.contact_result.to_alipay_dict()
            else:
                params['contact_result'] = self.contact_result
        if self.contact_time:
            if hasattr(self.contact_time, 'to_alipay_dict'):
                params['contact_time'] = self.contact_time.to_alipay_dict()
            else:
                params['contact_time'] = self.contact_time
        if self.in_store:
            if hasattr(self.in_store, 'to_alipay_dict'):
                params['in_store'] = self.in_store.to_alipay_dict()
            else:
                params['in_store'] = self.in_store
        if self.interest:
            if hasattr(self.interest, 'to_alipay_dict'):
                params['interest'] = self.interest.to_alipay_dict()
            else:
                params['interest'] = self.interest
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DecorationLeadsFeedbackContact()
        if 'contact_result' in d:
            o.contact_result = d['contact_result']
        if 'contact_time' in d:
            o.contact_time = d['contact_time']
        if 'in_store' in d:
            o.in_store = d['in_store']
        if 'interest' in d:
            o.interest = d['interest']
        return o


