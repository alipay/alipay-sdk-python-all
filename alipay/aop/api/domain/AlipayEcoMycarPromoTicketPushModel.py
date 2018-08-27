#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarPromoTicketPushModel(object):

    def __init__(self):
        self._apply_no = None
        self._apply_status = None
        self._code_no = None
        self._ticket_id = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def code_no(self):
        return self._code_no

    @code_no.setter
    def code_no(self, value):
        self._code_no = value
    @property
    def ticket_id(self):
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, value):
        self._ticket_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.code_no:
            if hasattr(self.code_no, 'to_alipay_dict'):
                params['code_no'] = self.code_no.to_alipay_dict()
            else:
                params['code_no'] = self.code_no
        if self.ticket_id:
            if hasattr(self.ticket_id, 'to_alipay_dict'):
                params['ticket_id'] = self.ticket_id.to_alipay_dict()
            else:
                params['ticket_id'] = self.ticket_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarPromoTicketPushModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'code_no' in d:
            o.code_no = d['code_no']
        if 'ticket_id' in d:
            o.ticket_id = d['ticket_id']
        return o


