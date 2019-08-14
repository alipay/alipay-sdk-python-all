#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportNfccardSendModel(object):

    def __init__(self):
        self._card_no = None
        self._card_status = None
        self._issue_org_no = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_status(self):
        return self._card_status

    @card_status.setter
    def card_status(self, value):
        self._card_status = value
    @property
    def issue_org_no(self):
        return self._issue_org_no

    @issue_org_no.setter
    def issue_org_no(self, value):
        self._issue_org_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_status:
            if hasattr(self.card_status, 'to_alipay_dict'):
                params['card_status'] = self.card_status.to_alipay_dict()
            else:
                params['card_status'] = self.card_status
        if self.issue_org_no:
            if hasattr(self.issue_org_no, 'to_alipay_dict'):
                params['issue_org_no'] = self.issue_org_no.to_alipay_dict()
            else:
                params['issue_org_no'] = self.issue_org_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportNfccardSendModel()
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_status' in d:
            o.card_status = d['card_status']
        if 'issue_org_no' in d:
            o.issue_org_no = d['issue_org_no']
        return o


