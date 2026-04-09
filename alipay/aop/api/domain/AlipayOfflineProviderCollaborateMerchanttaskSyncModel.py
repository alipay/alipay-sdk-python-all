#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderCollaborateMerchanttaskSyncModel(object):

    def __init__(self):
        self._leads_change_reason = None
        self._leads_status_change_date = None
        self._merchant_leads_status = None
        self._out_merchant_id = None
        self._task_id = None

    @property
    def leads_change_reason(self):
        return self._leads_change_reason

    @leads_change_reason.setter
    def leads_change_reason(self, value):
        self._leads_change_reason = value
    @property
    def leads_status_change_date(self):
        return self._leads_status_change_date

    @leads_status_change_date.setter
    def leads_status_change_date(self, value):
        self._leads_status_change_date = value
    @property
    def merchant_leads_status(self):
        return self._merchant_leads_status

    @merchant_leads_status.setter
    def merchant_leads_status(self, value):
        self._merchant_leads_status = value
    @property
    def out_merchant_id(self):
        return self._out_merchant_id

    @out_merchant_id.setter
    def out_merchant_id(self, value):
        self._out_merchant_id = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.leads_change_reason:
            if hasattr(self.leads_change_reason, 'to_alipay_dict'):
                params['leads_change_reason'] = self.leads_change_reason.to_alipay_dict()
            else:
                params['leads_change_reason'] = self.leads_change_reason
        if self.leads_status_change_date:
            if hasattr(self.leads_status_change_date, 'to_alipay_dict'):
                params['leads_status_change_date'] = self.leads_status_change_date.to_alipay_dict()
            else:
                params['leads_status_change_date'] = self.leads_status_change_date
        if self.merchant_leads_status:
            if hasattr(self.merchant_leads_status, 'to_alipay_dict'):
                params['merchant_leads_status'] = self.merchant_leads_status.to_alipay_dict()
            else:
                params['merchant_leads_status'] = self.merchant_leads_status
        if self.out_merchant_id:
            if hasattr(self.out_merchant_id, 'to_alipay_dict'):
                params['out_merchant_id'] = self.out_merchant_id.to_alipay_dict()
            else:
                params['out_merchant_id'] = self.out_merchant_id
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderCollaborateMerchanttaskSyncModel()
        if 'leads_change_reason' in d:
            o.leads_change_reason = d['leads_change_reason']
        if 'leads_status_change_date' in d:
            o.leads_status_change_date = d['leads_status_change_date']
        if 'merchant_leads_status' in d:
            o.merchant_leads_status = d['merchant_leads_status']
        if 'out_merchant_id' in d:
            o.out_merchant_id = d['out_merchant_id']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


