#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CoverageLiability(object):

    def __init__(self):
        self._compensation_times = None
        self._deductible = None
        self._liability_desc = None
        self._liability_name = None
        self._liability_no = None
        self._sum_insured = None
        self._wait_period_end = None

    @property
    def compensation_times(self):
        return self._compensation_times

    @compensation_times.setter
    def compensation_times(self, value):
        self._compensation_times = value
    @property
    def deductible(self):
        return self._deductible

    @deductible.setter
    def deductible(self, value):
        self._deductible = value
    @property
    def liability_desc(self):
        return self._liability_desc

    @liability_desc.setter
    def liability_desc(self, value):
        self._liability_desc = value
    @property
    def liability_name(self):
        return self._liability_name

    @liability_name.setter
    def liability_name(self, value):
        self._liability_name = value
    @property
    def liability_no(self):
        return self._liability_no

    @liability_no.setter
    def liability_no(self, value):
        self._liability_no = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value
    @property
    def wait_period_end(self):
        return self._wait_period_end

    @wait_period_end.setter
    def wait_period_end(self, value):
        self._wait_period_end = value


    def to_alipay_dict(self):
        params = dict()
        if self.compensation_times:
            if hasattr(self.compensation_times, 'to_alipay_dict'):
                params['compensation_times'] = self.compensation_times.to_alipay_dict()
            else:
                params['compensation_times'] = self.compensation_times
        if self.deductible:
            if hasattr(self.deductible, 'to_alipay_dict'):
                params['deductible'] = self.deductible.to_alipay_dict()
            else:
                params['deductible'] = self.deductible
        if self.liability_desc:
            if hasattr(self.liability_desc, 'to_alipay_dict'):
                params['liability_desc'] = self.liability_desc.to_alipay_dict()
            else:
                params['liability_desc'] = self.liability_desc
        if self.liability_name:
            if hasattr(self.liability_name, 'to_alipay_dict'):
                params['liability_name'] = self.liability_name.to_alipay_dict()
            else:
                params['liability_name'] = self.liability_name
        if self.liability_no:
            if hasattr(self.liability_no, 'to_alipay_dict'):
                params['liability_no'] = self.liability_no.to_alipay_dict()
            else:
                params['liability_no'] = self.liability_no
        if self.sum_insured:
            if hasattr(self.sum_insured, 'to_alipay_dict'):
                params['sum_insured'] = self.sum_insured.to_alipay_dict()
            else:
                params['sum_insured'] = self.sum_insured
        if self.wait_period_end:
            if hasattr(self.wait_period_end, 'to_alipay_dict'):
                params['wait_period_end'] = self.wait_period_end.to_alipay_dict()
            else:
                params['wait_period_end'] = self.wait_period_end
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CoverageLiability()
        if 'compensation_times' in d:
            o.compensation_times = d['compensation_times']
        if 'deductible' in d:
            o.deductible = d['deductible']
        if 'liability_desc' in d:
            o.liability_desc = d['liability_desc']
        if 'liability_name' in d:
            o.liability_name = d['liability_name']
        if 'liability_no' in d:
            o.liability_no = d['liability_no']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        if 'wait_period_end' in d:
            o.wait_period_end = d['wait_period_end']
        return o


