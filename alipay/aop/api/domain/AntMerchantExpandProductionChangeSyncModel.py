#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandProductionChangeSyncModel(object):

    def __init__(self):
        self._batch_no = None
        self._complete_date = None
        self._production_phase = None
        self._project_no = None
        self._success_amount = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def complete_date(self):
        return self._complete_date

    @complete_date.setter
    def complete_date(self, value):
        self._complete_date = value
    @property
    def production_phase(self):
        return self._production_phase

    @production_phase.setter
    def production_phase(self, value):
        self._production_phase = value
    @property
    def project_no(self):
        return self._project_no

    @project_no.setter
    def project_no(self, value):
        self._project_no = value
    @property
    def success_amount(self):
        return self._success_amount

    @success_amount.setter
    def success_amount(self, value):
        self._success_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.complete_date:
            if hasattr(self.complete_date, 'to_alipay_dict'):
                params['complete_date'] = self.complete_date.to_alipay_dict()
            else:
                params['complete_date'] = self.complete_date
        if self.production_phase:
            if hasattr(self.production_phase, 'to_alipay_dict'):
                params['production_phase'] = self.production_phase.to_alipay_dict()
            else:
                params['production_phase'] = self.production_phase
        if self.project_no:
            if hasattr(self.project_no, 'to_alipay_dict'):
                params['project_no'] = self.project_no.to_alipay_dict()
            else:
                params['project_no'] = self.project_no
        if self.success_amount:
            if hasattr(self.success_amount, 'to_alipay_dict'):
                params['success_amount'] = self.success_amount.to_alipay_dict()
            else:
                params['success_amount'] = self.success_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandProductionChangeSyncModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'complete_date' in d:
            o.complete_date = d['complete_date']
        if 'production_phase' in d:
            o.production_phase = d['production_phase']
        if 'project_no' in d:
            o.project_no = d['project_no']
        if 'success_amount' in d:
            o.success_amount = d['success_amount']
        return o


