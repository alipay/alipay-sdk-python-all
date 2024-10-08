#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditInfoResponse(object):

    def __init__(self):
        self._credit_page_link = None

    @property
    def credit_page_link(self):
        return self._credit_page_link

    @credit_page_link.setter
    def credit_page_link(self, value):
        self._credit_page_link = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_page_link:
            if hasattr(self.credit_page_link, 'to_alipay_dict'):
                params['credit_page_link'] = self.credit_page_link.to_alipay_dict()
            else:
                params['credit_page_link'] = self.credit_page_link
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditInfoResponse()
        if 'credit_page_link' in d:
            o.credit_page_link = d['credit_page_link']
        return o


