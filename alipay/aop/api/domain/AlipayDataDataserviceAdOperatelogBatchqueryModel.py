#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdOperatelogBatchqueryModel(object):

    def __init__(self):
        self._end_date = None
        self._operate_source = None
        self._operation_staff_type = None
        self._operation_target = None
        self._operation_type = None
        self._page_num = None
        self._page_size = None
        self._principal_id = None
        self._principal_tag = None
        self._start_date = None
        self._target_id = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def operate_source(self):
        return self._operate_source

    @operate_source.setter
    def operate_source(self, value):
        self._operate_source = value
    @property
    def operation_staff_type(self):
        return self._operation_staff_type

    @operation_staff_type.setter
    def operation_staff_type(self, value):
        self._operation_staff_type = value
    @property
    def operation_target(self):
        return self._operation_target

    @operation_target.setter
    def operation_target(self, value):
        self._operation_target = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.operate_source:
            if hasattr(self.operate_source, 'to_alipay_dict'):
                params['operate_source'] = self.operate_source.to_alipay_dict()
            else:
                params['operate_source'] = self.operate_source
        if self.operation_staff_type:
            if hasattr(self.operation_staff_type, 'to_alipay_dict'):
                params['operation_staff_type'] = self.operation_staff_type.to_alipay_dict()
            else:
                params['operation_staff_type'] = self.operation_staff_type
        if self.operation_target:
            if hasattr(self.operation_target, 'to_alipay_dict'):
                params['operation_target'] = self.operation_target.to_alipay_dict()
            else:
                params['operation_target'] = self.operation_target
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdOperatelogBatchqueryModel()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'operate_source' in d:
            o.operate_source = d['operate_source']
        if 'operation_staff_type' in d:
            o.operation_staff_type = d['operation_staff_type']
        if 'operation_target' in d:
            o.operation_target = d['operation_target']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'target_id' in d:
            o.target_id = d['target_id']
        return o


