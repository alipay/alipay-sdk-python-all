#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExemptApprovalProcessDetail(object):

    def __init__(self):
        self._exempt_approval_process_state = None
        self._exempt_approval_process_url = None

    @property
    def exempt_approval_process_state(self):
        return self._exempt_approval_process_state

    @exempt_approval_process_state.setter
    def exempt_approval_process_state(self, value):
        self._exempt_approval_process_state = value
    @property
    def exempt_approval_process_url(self):
        return self._exempt_approval_process_url

    @exempt_approval_process_url.setter
    def exempt_approval_process_url(self, value):
        self._exempt_approval_process_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.exempt_approval_process_state:
            if hasattr(self.exempt_approval_process_state, 'to_alipay_dict'):
                params['exempt_approval_process_state'] = self.exempt_approval_process_state.to_alipay_dict()
            else:
                params['exempt_approval_process_state'] = self.exempt_approval_process_state
        if self.exempt_approval_process_url:
            if hasattr(self.exempt_approval_process_url, 'to_alipay_dict'):
                params['exempt_approval_process_url'] = self.exempt_approval_process_url.to_alipay_dict()
            else:
                params['exempt_approval_process_url'] = self.exempt_approval_process_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExemptApprovalProcessDetail()
        if 'exempt_approval_process_state' in d:
            o.exempt_approval_process_state = d['exempt_approval_process_state']
        if 'exempt_approval_process_url' in d:
            o.exempt_approval_process_url = d['exempt_approval_process_url']
        return o


