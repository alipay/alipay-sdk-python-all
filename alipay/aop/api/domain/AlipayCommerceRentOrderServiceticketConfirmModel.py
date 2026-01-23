#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRentOrderServiceticketConfirmModel(object):

    def __init__(self):
        self._additional_description = None
        self._operation_type = None
        self._reason_code = None
        self._service_ticket_id = None

    @property
    def additional_description(self):
        return self._additional_description

    @additional_description.setter
    def additional_description(self, value):
        self._additional_description = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value
    @property
    def service_ticket_id(self):
        return self._service_ticket_id

    @service_ticket_id.setter
    def service_ticket_id(self, value):
        self._service_ticket_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.additional_description:
            if hasattr(self.additional_description, 'to_alipay_dict'):
                params['additional_description'] = self.additional_description.to_alipay_dict()
            else:
                params['additional_description'] = self.additional_description
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.reason_code:
            if hasattr(self.reason_code, 'to_alipay_dict'):
                params['reason_code'] = self.reason_code.to_alipay_dict()
            else:
                params['reason_code'] = self.reason_code
        if self.service_ticket_id:
            if hasattr(self.service_ticket_id, 'to_alipay_dict'):
                params['service_ticket_id'] = self.service_ticket_id.to_alipay_dict()
            else:
                params['service_ticket_id'] = self.service_ticket_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentOrderServiceticketConfirmModel()
        if 'additional_description' in d:
            o.additional_description = d['additional_description']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'reason_code' in d:
            o.reason_code = d['reason_code']
        if 'service_ticket_id' in d:
            o.service_ticket_id = d['service_ticket_id']
        return o


