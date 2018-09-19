#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityAuditDTO import ActivityAuditDTO


class ActivityOrderDTO(object):

    def __init__(self):
        self._activity_audit_list = None
        self._audit_status = None
        self._order_id = None
        self._order_status = None
        self._order_type = None

    @property
    def activity_audit_list(self):
        return self._activity_audit_list

    @activity_audit_list.setter
    def activity_audit_list(self, value):
        if isinstance(value, list):
            self._activity_audit_list = list()
            for i in value:
                if isinstance(i, ActivityAuditDTO):
                    self._activity_audit_list.append(i)
                else:
                    self._activity_audit_list.append(ActivityAuditDTO.from_alipay_dict(i))
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_audit_list:
            if isinstance(self.activity_audit_list, list):
                for i in range(0, len(self.activity_audit_list)):
                    element = self.activity_audit_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_audit_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_audit_list, 'to_alipay_dict'):
                params['activity_audit_list'] = self.activity_audit_list.to_alipay_dict()
            else:
                params['activity_audit_list'] = self.activity_audit_list
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityOrderDTO()
        if 'activity_audit_list' in d:
            o.activity_audit_list = d['activity_audit_list']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_type' in d:
            o.order_type = d['order_type']
        return o


