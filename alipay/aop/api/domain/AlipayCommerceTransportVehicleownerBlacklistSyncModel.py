#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportVehicleownerBlacklistSyncModel(object):

    def __init__(self):
        self._agreement_no = None
        self._plate_color = None
        self._plate_no = None
        self._source = None
        self._status_opt = None
        self._status_opt_time = None
        self._status_reason = None
        self._status_reason_code = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def status_opt(self):
        return self._status_opt

    @status_opt.setter
    def status_opt(self, value):
        self._status_opt = value
    @property
    def status_opt_time(self):
        return self._status_opt_time

    @status_opt_time.setter
    def status_opt_time(self, value):
        self._status_opt_time = value
    @property
    def status_reason(self):
        return self._status_reason

    @status_reason.setter
    def status_reason(self, value):
        self._status_reason = value
    @property
    def status_reason_code(self):
        return self._status_reason_code

    @status_reason_code.setter
    def status_reason_code(self, value):
        self._status_reason_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.plate_color:
            if hasattr(self.plate_color, 'to_alipay_dict'):
                params['plate_color'] = self.plate_color.to_alipay_dict()
            else:
                params['plate_color'] = self.plate_color
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.status_opt:
            if hasattr(self.status_opt, 'to_alipay_dict'):
                params['status_opt'] = self.status_opt.to_alipay_dict()
            else:
                params['status_opt'] = self.status_opt
        if self.status_opt_time:
            if hasattr(self.status_opt_time, 'to_alipay_dict'):
                params['status_opt_time'] = self.status_opt_time.to_alipay_dict()
            else:
                params['status_opt_time'] = self.status_opt_time
        if self.status_reason:
            if hasattr(self.status_reason, 'to_alipay_dict'):
                params['status_reason'] = self.status_reason.to_alipay_dict()
            else:
                params['status_reason'] = self.status_reason
        if self.status_reason_code:
            if hasattr(self.status_reason_code, 'to_alipay_dict'):
                params['status_reason_code'] = self.status_reason_code.to_alipay_dict()
            else:
                params['status_reason_code'] = self.status_reason_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportVehicleownerBlacklistSyncModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'source' in d:
            o.source = d['source']
        if 'status_opt' in d:
            o.status_opt = d['status_opt']
        if 'status_opt_time' in d:
            o.status_opt_time = d['status_opt_time']
        if 'status_reason' in d:
            o.status_reason = d['status_reason']
        if 'status_reason_code' in d:
            o.status_reason_code = d['status_reason_code']
        return o


