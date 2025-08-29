#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentAftersaleOperationRecordVO import RentAftersaleOperationRecordVO


class RentAftersaleOrderVO(object):

    def __init__(self):
        self._aftersale_id = None
        self._aftersale_status = None
        self._aftersale_type = None
        self._apply_time = None
        self._finished = None
        self._operation_records = None
        self._out_aftersale_id = None
        self._source_type = None

    @property
    def aftersale_id(self):
        return self._aftersale_id

    @aftersale_id.setter
    def aftersale_id(self, value):
        self._aftersale_id = value
    @property
    def aftersale_status(self):
        return self._aftersale_status

    @aftersale_status.setter
    def aftersale_status(self, value):
        self._aftersale_status = value
    @property
    def aftersale_type(self):
        return self._aftersale_type

    @aftersale_type.setter
    def aftersale_type(self, value):
        self._aftersale_type = value
    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def finished(self):
        return self._finished

    @finished.setter
    def finished(self, value):
        self._finished = value
    @property
    def operation_records(self):
        return self._operation_records

    @operation_records.setter
    def operation_records(self, value):
        if isinstance(value, list):
            self._operation_records = list()
            for i in value:
                if isinstance(i, RentAftersaleOperationRecordVO):
                    self._operation_records.append(i)
                else:
                    self._operation_records.append(RentAftersaleOperationRecordVO.from_alipay_dict(i))
    @property
    def out_aftersale_id(self):
        return self._out_aftersale_id

    @out_aftersale_id.setter
    def out_aftersale_id(self, value):
        self._out_aftersale_id = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.aftersale_id:
            if hasattr(self.aftersale_id, 'to_alipay_dict'):
                params['aftersale_id'] = self.aftersale_id.to_alipay_dict()
            else:
                params['aftersale_id'] = self.aftersale_id
        if self.aftersale_status:
            if hasattr(self.aftersale_status, 'to_alipay_dict'):
                params['aftersale_status'] = self.aftersale_status.to_alipay_dict()
            else:
                params['aftersale_status'] = self.aftersale_status
        if self.aftersale_type:
            if hasattr(self.aftersale_type, 'to_alipay_dict'):
                params['aftersale_type'] = self.aftersale_type.to_alipay_dict()
            else:
                params['aftersale_type'] = self.aftersale_type
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.finished:
            if hasattr(self.finished, 'to_alipay_dict'):
                params['finished'] = self.finished.to_alipay_dict()
            else:
                params['finished'] = self.finished
        if self.operation_records:
            if isinstance(self.operation_records, list):
                for i in range(0, len(self.operation_records)):
                    element = self.operation_records[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operation_records[i] = element.to_alipay_dict()
            if hasattr(self.operation_records, 'to_alipay_dict'):
                params['operation_records'] = self.operation_records.to_alipay_dict()
            else:
                params['operation_records'] = self.operation_records
        if self.out_aftersale_id:
            if hasattr(self.out_aftersale_id, 'to_alipay_dict'):
                params['out_aftersale_id'] = self.out_aftersale_id.to_alipay_dict()
            else:
                params['out_aftersale_id'] = self.out_aftersale_id
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentAftersaleOrderVO()
        if 'aftersale_id' in d:
            o.aftersale_id = d['aftersale_id']
        if 'aftersale_status' in d:
            o.aftersale_status = d['aftersale_status']
        if 'aftersale_type' in d:
            o.aftersale_type = d['aftersale_type']
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'finished' in d:
            o.finished = d['finished']
        if 'operation_records' in d:
            o.operation_records = d['operation_records']
        if 'out_aftersale_id' in d:
            o.out_aftersale_id = d['out_aftersale_id']
        if 'source_type' in d:
            o.source_type = d['source_type']
        return o


