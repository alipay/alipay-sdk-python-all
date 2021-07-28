#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotSdarttoolMessageQueryModel(object):

    def __init__(self):
        self._message_no = None

    @property
    def message_no(self):
        return self._message_no

    @message_no.setter
    def message_no(self, value):
        self._message_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.message_no:
            if hasattr(self.message_no, 'to_alipay_dict'):
                params['message_no'] = self.message_no.to_alipay_dict()
            else:
                params['message_no'] = self.message_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotSdarttoolMessageQueryModel()
        if 'message_no' in d:
            o.message_no = d['message_no']
        return o


