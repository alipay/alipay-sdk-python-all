#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandTerminateConsultresultSyncModel(object):

    def __init__(self):
        self._batch_no = None
        self._biz_no = None
        self._consult_type = None
        self._status = None
        self._supplier_id = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def consult_type(self):
        return self._consult_type

    @consult_type.setter
    def consult_type(self, value):
        self._consult_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.consult_type:
            if hasattr(self.consult_type, 'to_alipay_dict'):
                params['consult_type'] = self.consult_type.to_alipay_dict()
            else:
                params['consult_type'] = self.consult_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandTerminateConsultresultSyncModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'consult_type' in d:
            o.consult_type = d['consult_type']
        if 'status' in d:
            o.status = d['status']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


