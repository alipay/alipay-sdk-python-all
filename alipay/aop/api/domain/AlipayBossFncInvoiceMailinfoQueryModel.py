#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncInvoiceMailinfoQueryModel(object):

    def __init__(self):
        self._mail_id = None

    @property
    def mail_id(self):
        return self._mail_id

    @mail_id.setter
    def mail_id(self, value):
        self._mail_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.mail_id:
            if hasattr(self.mail_id, 'to_alipay_dict'):
                params['mail_id'] = self.mail_id.to_alipay_dict()
            else:
                params['mail_id'] = self.mail_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncInvoiceMailinfoQueryModel()
        if 'mail_id' in d:
            o.mail_id = d['mail_id']
        return o


