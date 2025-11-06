#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZmEpAePrepayExtParam(object):

    def __init__(self):
        self._gmt_audit = None
        self._pay_time = None
        self._ship_time = None
        self._tenant_site = None

    @property
    def gmt_audit(self):
        return self._gmt_audit

    @gmt_audit.setter
    def gmt_audit(self, value):
        self._gmt_audit = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def ship_time(self):
        return self._ship_time

    @ship_time.setter
    def ship_time(self, value):
        self._ship_time = value
    @property
    def tenant_site(self):
        return self._tenant_site

    @tenant_site.setter
    def tenant_site(self, value):
        self._tenant_site = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_audit:
            if hasattr(self.gmt_audit, 'to_alipay_dict'):
                params['gmt_audit'] = self.gmt_audit.to_alipay_dict()
            else:
                params['gmt_audit'] = self.gmt_audit
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.ship_time:
            if hasattr(self.ship_time, 'to_alipay_dict'):
                params['ship_time'] = self.ship_time.to_alipay_dict()
            else:
                params['ship_time'] = self.ship_time
        if self.tenant_site:
            if hasattr(self.tenant_site, 'to_alipay_dict'):
                params['tenant_site'] = self.tenant_site.to_alipay_dict()
            else:
                params['tenant_site'] = self.tenant_site
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmEpAePrepayExtParam()
        if 'gmt_audit' in d:
            o.gmt_audit = d['gmt_audit']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'ship_time' in d:
            o.ship_time = d['ship_time']
        if 'tenant_site' in d:
            o.tenant_site = d['tenant_site']
        return o


