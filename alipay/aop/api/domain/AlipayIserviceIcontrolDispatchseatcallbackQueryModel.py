#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIcontrolDispatchseatcallbackQueryModel(object):

    def __init__(self):
        self._seat_id = None
        self._seat_type = None
        self._service_uniq_code = None
        self._skill_group_id = None
        self._skill_group_type = None
        self._status = None

    @property
    def seat_id(self):
        return self._seat_id

    @seat_id.setter
    def seat_id(self, value):
        self._seat_id = value
    @property
    def seat_type(self):
        return self._seat_type

    @seat_type.setter
    def seat_type(self, value):
        self._seat_type = value
    @property
    def service_uniq_code(self):
        return self._service_uniq_code

    @service_uniq_code.setter
    def service_uniq_code(self, value):
        self._service_uniq_code = value
    @property
    def skill_group_id(self):
        return self._skill_group_id

    @skill_group_id.setter
    def skill_group_id(self, value):
        self._skill_group_id = value
    @property
    def skill_group_type(self):
        return self._skill_group_type

    @skill_group_type.setter
    def skill_group_type(self, value):
        self._skill_group_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.seat_id:
            if hasattr(self.seat_id, 'to_alipay_dict'):
                params['seat_id'] = self.seat_id.to_alipay_dict()
            else:
                params['seat_id'] = self.seat_id
        if self.seat_type:
            if hasattr(self.seat_type, 'to_alipay_dict'):
                params['seat_type'] = self.seat_type.to_alipay_dict()
            else:
                params['seat_type'] = self.seat_type
        if self.service_uniq_code:
            if hasattr(self.service_uniq_code, 'to_alipay_dict'):
                params['service_uniq_code'] = self.service_uniq_code.to_alipay_dict()
            else:
                params['service_uniq_code'] = self.service_uniq_code
        if self.skill_group_id:
            if hasattr(self.skill_group_id, 'to_alipay_dict'):
                params['skill_group_id'] = self.skill_group_id.to_alipay_dict()
            else:
                params['skill_group_id'] = self.skill_group_id
        if self.skill_group_type:
            if hasattr(self.skill_group_type, 'to_alipay_dict'):
                params['skill_group_type'] = self.skill_group_type.to_alipay_dict()
            else:
                params['skill_group_type'] = self.skill_group_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIcontrolDispatchseatcallbackQueryModel()
        if 'seat_id' in d:
            o.seat_id = d['seat_id']
        if 'seat_type' in d:
            o.seat_type = d['seat_type']
        if 'service_uniq_code' in d:
            o.service_uniq_code = d['service_uniq_code']
        if 'skill_group_id' in d:
            o.skill_group_id = d['skill_group_id']
        if 'skill_group_type' in d:
            o.skill_group_type = d['skill_group_type']
        if 'status' in d:
            o.status = d['status']
        return o


