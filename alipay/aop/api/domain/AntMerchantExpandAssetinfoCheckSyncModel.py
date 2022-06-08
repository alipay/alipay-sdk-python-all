#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CheckDetails import CheckDetails


class AntMerchantExpandAssetinfoCheckSyncModel(object):

    def __init__(self):
        self._batch_no = None
        self._check_details = None
        self._check_phase = None
        self._check_status = None
        self._supplier_id = None
        self._type = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def check_details(self):
        return self._check_details

    @check_details.setter
    def check_details(self, value):
        if isinstance(value, list):
            self._check_details = list()
            for i in value:
                if isinstance(i, CheckDetails):
                    self._check_details.append(i)
                else:
                    self._check_details.append(CheckDetails.from_alipay_dict(i))
    @property
    def check_phase(self):
        return self._check_phase

    @check_phase.setter
    def check_phase(self, value):
        self._check_phase = value
    @property
    def check_status(self):
        return self._check_status

    @check_status.setter
    def check_status(self, value):
        self._check_status = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.check_details:
            if isinstance(self.check_details, list):
                for i in range(0, len(self.check_details)):
                    element = self.check_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.check_details[i] = element.to_alipay_dict()
            if hasattr(self.check_details, 'to_alipay_dict'):
                params['check_details'] = self.check_details.to_alipay_dict()
            else:
                params['check_details'] = self.check_details
        if self.check_phase:
            if hasattr(self.check_phase, 'to_alipay_dict'):
                params['check_phase'] = self.check_phase.to_alipay_dict()
            else:
                params['check_phase'] = self.check_phase
        if self.check_status:
            if hasattr(self.check_status, 'to_alipay_dict'):
                params['check_status'] = self.check_status.to_alipay_dict()
            else:
                params['check_status'] = self.check_status
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandAssetinfoCheckSyncModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'check_details' in d:
            o.check_details = d['check_details']
        if 'check_phase' in d:
            o.check_phase = d['check_phase']
        if 'check_status' in d:
            o.check_status = d['check_status']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'type' in d:
            o.type = d['type']
        return o


