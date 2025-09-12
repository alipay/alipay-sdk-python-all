#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalIndustrydataMedicalrecordSyncModel(object):

    def __init__(self):
        self._delete_flag = None
        self._medical_record_id = None
        self._private_flag = None

    @property
    def delete_flag(self):
        return self._delete_flag

    @delete_flag.setter
    def delete_flag(self, value):
        self._delete_flag = value
    @property
    def medical_record_id(self):
        return self._medical_record_id

    @medical_record_id.setter
    def medical_record_id(self, value):
        self._medical_record_id = value
    @property
    def private_flag(self):
        return self._private_flag

    @private_flag.setter
    def private_flag(self, value):
        self._private_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.delete_flag:
            if hasattr(self.delete_flag, 'to_alipay_dict'):
                params['delete_flag'] = self.delete_flag.to_alipay_dict()
            else:
                params['delete_flag'] = self.delete_flag
        if self.medical_record_id:
            if hasattr(self.medical_record_id, 'to_alipay_dict'):
                params['medical_record_id'] = self.medical_record_id.to_alipay_dict()
            else:
                params['medical_record_id'] = self.medical_record_id
        if self.private_flag:
            if hasattr(self.private_flag, 'to_alipay_dict'):
                params['private_flag'] = self.private_flag.to_alipay_dict()
            else:
                params['private_flag'] = self.private_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataMedicalrecordSyncModel()
        if 'delete_flag' in d:
            o.delete_flag = d['delete_flag']
        if 'medical_record_id' in d:
            o.medical_record_id = d['medical_record_id']
        if 'private_flag' in d:
            o.private_flag = d['private_flag']
        return o


