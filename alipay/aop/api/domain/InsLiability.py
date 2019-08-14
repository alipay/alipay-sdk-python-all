#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsOption import InsOption
from alipay.aop.api.domain.InsSumInsured import InsSumInsured


class InsLiability(object):

    def __init__(self):
        self._coverage = None
        self._disabled = None
        self._iop = None
        self._iop_premium = None
        self._liability_desc = None
        self._liability_name = None
        self._liability_no = None
        self._liability_premium = None
        self._liability_rates = None
        self._options = None
        self._premium = None
        self._sum_insured = None

    @property
    def coverage(self):
        return self._coverage

    @coverage.setter
    def coverage(self, value):
        self._coverage = value
    @property
    def disabled(self):
        return self._disabled

    @disabled.setter
    def disabled(self, value):
        self._disabled = value
    @property
    def iop(self):
        return self._iop

    @iop.setter
    def iop(self, value):
        self._iop = value
    @property
    def iop_premium(self):
        return self._iop_premium

    @iop_premium.setter
    def iop_premium(self, value):
        self._iop_premium = value
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
    def liability_premium(self):
        return self._liability_premium

    @liability_premium.setter
    def liability_premium(self, value):
        self._liability_premium = value
    @property
    def liability_rates(self):
        return self._liability_rates

    @liability_rates.setter
    def liability_rates(self, value):
        self._liability_rates = value
    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        if isinstance(value, list):
            self._options = list()
            for i in value:
                if isinstance(i, InsOption):
                    self._options.append(i)
                else:
                    self._options.append(InsOption.from_alipay_dict(i))
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        if isinstance(value, InsSumInsured):
            self._sum_insured = value
        else:
            self._sum_insured = InsSumInsured.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.coverage:
            if hasattr(self.coverage, 'to_alipay_dict'):
                params['coverage'] = self.coverage.to_alipay_dict()
            else:
                params['coverage'] = self.coverage
        if self.disabled:
            if hasattr(self.disabled, 'to_alipay_dict'):
                params['disabled'] = self.disabled.to_alipay_dict()
            else:
                params['disabled'] = self.disabled
        if self.iop:
            if hasattr(self.iop, 'to_alipay_dict'):
                params['iop'] = self.iop.to_alipay_dict()
            else:
                params['iop'] = self.iop
        if self.iop_premium:
            if hasattr(self.iop_premium, 'to_alipay_dict'):
                params['iop_premium'] = self.iop_premium.to_alipay_dict()
            else:
                params['iop_premium'] = self.iop_premium
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
        if self.liability_premium:
            if hasattr(self.liability_premium, 'to_alipay_dict'):
                params['liability_premium'] = self.liability_premium.to_alipay_dict()
            else:
                params['liability_premium'] = self.liability_premium
        if self.liability_rates:
            if hasattr(self.liability_rates, 'to_alipay_dict'):
                params['liability_rates'] = self.liability_rates.to_alipay_dict()
            else:
                params['liability_rates'] = self.liability_rates
        if self.options:
            if isinstance(self.options, list):
                for i in range(0, len(self.options)):
                    element = self.options[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.options[i] = element.to_alipay_dict()
            if hasattr(self.options, 'to_alipay_dict'):
                params['options'] = self.options.to_alipay_dict()
            else:
                params['options'] = self.options
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
        if self.sum_insured:
            if hasattr(self.sum_insured, 'to_alipay_dict'):
                params['sum_insured'] = self.sum_insured.to_alipay_dict()
            else:
                params['sum_insured'] = self.sum_insured
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsLiability()
        if 'coverage' in d:
            o.coverage = d['coverage']
        if 'disabled' in d:
            o.disabled = d['disabled']
        if 'iop' in d:
            o.iop = d['iop']
        if 'iop_premium' in d:
            o.iop_premium = d['iop_premium']
        if 'liability_desc' in d:
            o.liability_desc = d['liability_desc']
        if 'liability_name' in d:
            o.liability_name = d['liability_name']
        if 'liability_no' in d:
            o.liability_no = d['liability_no']
        if 'liability_premium' in d:
            o.liability_premium = d['liability_premium']
        if 'liability_rates' in d:
            o.liability_rates = d['liability_rates']
        if 'options' in d:
            o.options = d['options']
        if 'premium' in d:
            o.premium = d['premium']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        return o


