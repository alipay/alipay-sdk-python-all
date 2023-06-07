#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RefundedInfo(object):

    def __init__(self):
        self._application_no = None
        self._evoa_fee_amount = None
        self._process_by = None
        self._process_date_time = None
        self._remark = None
        self._service_fee_amount = None
        self._status = None
        self._voa_no = None

    @property
    def application_no(self):
        return self._application_no

    @application_no.setter
    def application_no(self, value):
        self._application_no = value
    @property
    def evoa_fee_amount(self):
        return self._evoa_fee_amount

    @evoa_fee_amount.setter
    def evoa_fee_amount(self, value):
        self._evoa_fee_amount = value
    @property
    def process_by(self):
        return self._process_by

    @process_by.setter
    def process_by(self, value):
        self._process_by = value
    @property
    def process_date_time(self):
        return self._process_date_time

    @process_date_time.setter
    def process_date_time(self, value):
        self._process_date_time = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def service_fee_amount(self):
        return self._service_fee_amount

    @service_fee_amount.setter
    def service_fee_amount(self, value):
        self._service_fee_amount = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def voa_no(self):
        return self._voa_no

    @voa_no.setter
    def voa_no(self, value):
        self._voa_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.application_no:
            if hasattr(self.application_no, 'to_alipay_dict'):
                params['application_no'] = self.application_no.to_alipay_dict()
            else:
                params['application_no'] = self.application_no
        if self.evoa_fee_amount:
            if hasattr(self.evoa_fee_amount, 'to_alipay_dict'):
                params['evoa_fee_amount'] = self.evoa_fee_amount.to_alipay_dict()
            else:
                params['evoa_fee_amount'] = self.evoa_fee_amount
        if self.process_by:
            if hasattr(self.process_by, 'to_alipay_dict'):
                params['process_by'] = self.process_by.to_alipay_dict()
            else:
                params['process_by'] = self.process_by
        if self.process_date_time:
            if hasattr(self.process_date_time, 'to_alipay_dict'):
                params['process_date_time'] = self.process_date_time.to_alipay_dict()
            else:
                params['process_date_time'] = self.process_date_time
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.service_fee_amount:
            if hasattr(self.service_fee_amount, 'to_alipay_dict'):
                params['service_fee_amount'] = self.service_fee_amount.to_alipay_dict()
            else:
                params['service_fee_amount'] = self.service_fee_amount
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.voa_no:
            if hasattr(self.voa_no, 'to_alipay_dict'):
                params['voa_no'] = self.voa_no.to_alipay_dict()
            else:
                params['voa_no'] = self.voa_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundedInfo()
        if 'application_no' in d:
            o.application_no = d['application_no']
        if 'evoa_fee_amount' in d:
            o.evoa_fee_amount = d['evoa_fee_amount']
        if 'process_by' in d:
            o.process_by = d['process_by']
        if 'process_date_time' in d:
            o.process_date_time = d['process_date_time']
        if 'remark' in d:
            o.remark = d['remark']
        if 'service_fee_amount' in d:
            o.service_fee_amount = d['service_fee_amount']
        if 'status' in d:
            o.status = d['status']
        if 'voa_no' in d:
            o.voa_no = d['voa_no']
        return o


