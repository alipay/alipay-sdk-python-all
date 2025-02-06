#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZmepAnnualReportInvestInfo(object):

    def __init__(self):
        self._ep_cert_no = None
        self._invest_ep_name = None

    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def invest_ep_name(self):
        return self._invest_ep_name

    @invest_ep_name.setter
    def invest_ep_name(self, value):
        self._invest_ep_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.invest_ep_name:
            if hasattr(self.invest_ep_name, 'to_alipay_dict'):
                params['invest_ep_name'] = self.invest_ep_name.to_alipay_dict()
            else:
                params['invest_ep_name'] = self.invest_ep_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmepAnnualReportInvestInfo()
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'invest_ep_name' in d:
            o.invest_ep_name = d['invest_ep_name']
        return o


