#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentAftersaleMediaInfoVO import RentAftersaleMediaInfoVO
from alipay.aop.api.domain.RentAftersaleFundInfoVO import RentAftersaleFundInfoVO


class RentAftersaleOperationRecordVO(object):

    def __init__(self):
        self._additional_description = None
        self._additional_media_list = None
        self._fund_info = None
        self._next_operation_type_list = None
        self._operation_deadline = None
        self._operation_time = None
        self._operation_type = None
        self._reason_description = None

    @property
    def additional_description(self):
        return self._additional_description

    @additional_description.setter
    def additional_description(self, value):
        self._additional_description = value
    @property
    def additional_media_list(self):
        return self._additional_media_list

    @additional_media_list.setter
    def additional_media_list(self, value):
        if isinstance(value, list):
            self._additional_media_list = list()
            for i in value:
                if isinstance(i, RentAftersaleMediaInfoVO):
                    self._additional_media_list.append(i)
                else:
                    self._additional_media_list.append(RentAftersaleMediaInfoVO.from_alipay_dict(i))
    @property
    def fund_info(self):
        return self._fund_info

    @fund_info.setter
    def fund_info(self, value):
        if isinstance(value, RentAftersaleFundInfoVO):
            self._fund_info = value
        else:
            self._fund_info = RentAftersaleFundInfoVO.from_alipay_dict(value)
    @property
    def next_operation_type_list(self):
        return self._next_operation_type_list

    @next_operation_type_list.setter
    def next_operation_type_list(self, value):
        if isinstance(value, list):
            self._next_operation_type_list = list()
            for i in value:
                self._next_operation_type_list.append(i)
    @property
    def operation_deadline(self):
        return self._operation_deadline

    @operation_deadline.setter
    def operation_deadline(self, value):
        self._operation_deadline = value
    @property
    def operation_time(self):
        return self._operation_time

    @operation_time.setter
    def operation_time(self, value):
        self._operation_time = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def reason_description(self):
        return self._reason_description

    @reason_description.setter
    def reason_description(self, value):
        self._reason_description = value


    def to_alipay_dict(self):
        params = dict()
        if self.additional_description:
            if hasattr(self.additional_description, 'to_alipay_dict'):
                params['additional_description'] = self.additional_description.to_alipay_dict()
            else:
                params['additional_description'] = self.additional_description
        if self.additional_media_list:
            if isinstance(self.additional_media_list, list):
                for i in range(0, len(self.additional_media_list)):
                    element = self.additional_media_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.additional_media_list[i] = element.to_alipay_dict()
            if hasattr(self.additional_media_list, 'to_alipay_dict'):
                params['additional_media_list'] = self.additional_media_list.to_alipay_dict()
            else:
                params['additional_media_list'] = self.additional_media_list
        if self.fund_info:
            if hasattr(self.fund_info, 'to_alipay_dict'):
                params['fund_info'] = self.fund_info.to_alipay_dict()
            else:
                params['fund_info'] = self.fund_info
        if self.next_operation_type_list:
            if isinstance(self.next_operation_type_list, list):
                for i in range(0, len(self.next_operation_type_list)):
                    element = self.next_operation_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.next_operation_type_list[i] = element.to_alipay_dict()
            if hasattr(self.next_operation_type_list, 'to_alipay_dict'):
                params['next_operation_type_list'] = self.next_operation_type_list.to_alipay_dict()
            else:
                params['next_operation_type_list'] = self.next_operation_type_list
        if self.operation_deadline:
            if hasattr(self.operation_deadline, 'to_alipay_dict'):
                params['operation_deadline'] = self.operation_deadline.to_alipay_dict()
            else:
                params['operation_deadline'] = self.operation_deadline
        if self.operation_time:
            if hasattr(self.operation_time, 'to_alipay_dict'):
                params['operation_time'] = self.operation_time.to_alipay_dict()
            else:
                params['operation_time'] = self.operation_time
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.reason_description:
            if hasattr(self.reason_description, 'to_alipay_dict'):
                params['reason_description'] = self.reason_description.to_alipay_dict()
            else:
                params['reason_description'] = self.reason_description
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentAftersaleOperationRecordVO()
        if 'additional_description' in d:
            o.additional_description = d['additional_description']
        if 'additional_media_list' in d:
            o.additional_media_list = d['additional_media_list']
        if 'fund_info' in d:
            o.fund_info = d['fund_info']
        if 'next_operation_type_list' in d:
            o.next_operation_type_list = d['next_operation_type_list']
        if 'operation_deadline' in d:
            o.operation_deadline = d['operation_deadline']
        if 'operation_time' in d:
            o.operation_time = d['operation_time']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'reason_description' in d:
            o.reason_description = d['reason_description']
        return o


