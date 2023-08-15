#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IotPaymentCustomInfo(object):

    def __init__(self):
        self._amount_show = None
        self._title = None

    @property
    def amount_show(self):
        return self._amount_show

    @amount_show.setter
    def amount_show(self, value):
        self._amount_show = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_show:
            if hasattr(self.amount_show, 'to_alipay_dict'):
                params['amount_show'] = self.amount_show.to_alipay_dict()
            else:
                params['amount_show'] = self.amount_show
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotPaymentCustomInfo()
        if 'amount_show' in d:
            o.amount_show = d['amount_show']
        if 'title' in d:
            o.title = d['title']
        return o


