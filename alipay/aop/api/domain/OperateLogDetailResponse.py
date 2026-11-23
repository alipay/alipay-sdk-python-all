#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OperateLogDetailResponse(object):

    def __init__(self):
        self._date = None
        self._id = None
        self._operate_details = None
        self._operate_ip = None
        self._operate_source = None
        self._operate_source_zh = None
        self._operation_staff_name = None
        self._operation_staff_type = None
        self._operation_staff_type_zh = None
        self._operation_target = None
        self._operation_target_zh = None
        self._operation_type = None
        self._operation_type_zh = None
        self._target_id = None
        self._target_name = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def operate_details(self):
        return self._operate_details

    @operate_details.setter
    def operate_details(self, value):
        if isinstance(value, list):
            self._operate_details = list()
            for i in value:
                self._operate_details.append(i)
    @property
    def operate_ip(self):
        return self._operate_ip

    @operate_ip.setter
    def operate_ip(self, value):
        self._operate_ip = value
    @property
    def operate_source(self):
        return self._operate_source

    @operate_source.setter
    def operate_source(self, value):
        self._operate_source = value
    @property
    def operate_source_zh(self):
        return self._operate_source_zh

    @operate_source_zh.setter
    def operate_source_zh(self, value):
        self._operate_source_zh = value
    @property
    def operation_staff_name(self):
        return self._operation_staff_name

    @operation_staff_name.setter
    def operation_staff_name(self, value):
        self._operation_staff_name = value
    @property
    def operation_staff_type(self):
        return self._operation_staff_type

    @operation_staff_type.setter
    def operation_staff_type(self, value):
        self._operation_staff_type = value
    @property
    def operation_staff_type_zh(self):
        return self._operation_staff_type_zh

    @operation_staff_type_zh.setter
    def operation_staff_type_zh(self, value):
        self._operation_staff_type_zh = value
    @property
    def operation_target(self):
        return self._operation_target

    @operation_target.setter
    def operation_target(self, value):
        self._operation_target = value
    @property
    def operation_target_zh(self):
        return self._operation_target_zh

    @operation_target_zh.setter
    def operation_target_zh(self, value):
        self._operation_target_zh = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def operation_type_zh(self):
        return self._operation_type_zh

    @operation_type_zh.setter
    def operation_type_zh(self, value):
        self._operation_type_zh = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value
    @property
    def target_name(self):
        return self._target_name

    @target_name.setter
    def target_name(self, value):
        self._target_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.operate_details:
            if isinstance(self.operate_details, list):
                for i in range(0, len(self.operate_details)):
                    element = self.operate_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operate_details[i] = element.to_alipay_dict()
            if hasattr(self.operate_details, 'to_alipay_dict'):
                params['operate_details'] = self.operate_details.to_alipay_dict()
            else:
                params['operate_details'] = self.operate_details
        if self.operate_ip:
            if hasattr(self.operate_ip, 'to_alipay_dict'):
                params['operate_ip'] = self.operate_ip.to_alipay_dict()
            else:
                params['operate_ip'] = self.operate_ip
        if self.operate_source:
            if hasattr(self.operate_source, 'to_alipay_dict'):
                params['operate_source'] = self.operate_source.to_alipay_dict()
            else:
                params['operate_source'] = self.operate_source
        if self.operate_source_zh:
            if hasattr(self.operate_source_zh, 'to_alipay_dict'):
                params['operate_source_zh'] = self.operate_source_zh.to_alipay_dict()
            else:
                params['operate_source_zh'] = self.operate_source_zh
        if self.operation_staff_name:
            if hasattr(self.operation_staff_name, 'to_alipay_dict'):
                params['operation_staff_name'] = self.operation_staff_name.to_alipay_dict()
            else:
                params['operation_staff_name'] = self.operation_staff_name
        if self.operation_staff_type:
            if hasattr(self.operation_staff_type, 'to_alipay_dict'):
                params['operation_staff_type'] = self.operation_staff_type.to_alipay_dict()
            else:
                params['operation_staff_type'] = self.operation_staff_type
        if self.operation_staff_type_zh:
            if hasattr(self.operation_staff_type_zh, 'to_alipay_dict'):
                params['operation_staff_type_zh'] = self.operation_staff_type_zh.to_alipay_dict()
            else:
                params['operation_staff_type_zh'] = self.operation_staff_type_zh
        if self.operation_target:
            if hasattr(self.operation_target, 'to_alipay_dict'):
                params['operation_target'] = self.operation_target.to_alipay_dict()
            else:
                params['operation_target'] = self.operation_target
        if self.operation_target_zh:
            if hasattr(self.operation_target_zh, 'to_alipay_dict'):
                params['operation_target_zh'] = self.operation_target_zh.to_alipay_dict()
            else:
                params['operation_target_zh'] = self.operation_target_zh
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.operation_type_zh:
            if hasattr(self.operation_type_zh, 'to_alipay_dict'):
                params['operation_type_zh'] = self.operation_type_zh.to_alipay_dict()
            else:
                params['operation_type_zh'] = self.operation_type_zh
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        if self.target_name:
            if hasattr(self.target_name, 'to_alipay_dict'):
                params['target_name'] = self.target_name.to_alipay_dict()
            else:
                params['target_name'] = self.target_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OperateLogDetailResponse()
        if 'date' in d:
            o.date = d['date']
        if 'id' in d:
            o.id = d['id']
        if 'operate_details' in d:
            o.operate_details = d['operate_details']
        if 'operate_ip' in d:
            o.operate_ip = d['operate_ip']
        if 'operate_source' in d:
            o.operate_source = d['operate_source']
        if 'operate_source_zh' in d:
            o.operate_source_zh = d['operate_source_zh']
        if 'operation_staff_name' in d:
            o.operation_staff_name = d['operation_staff_name']
        if 'operation_staff_type' in d:
            o.operation_staff_type = d['operation_staff_type']
        if 'operation_staff_type_zh' in d:
            o.operation_staff_type_zh = d['operation_staff_type_zh']
        if 'operation_target' in d:
            o.operation_target = d['operation_target']
        if 'operation_target_zh' in d:
            o.operation_target_zh = d['operation_target_zh']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'operation_type_zh' in d:
            o.operation_type_zh = d['operation_type_zh']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_name' in d:
            o.target_name = d['target_name']
        return o


