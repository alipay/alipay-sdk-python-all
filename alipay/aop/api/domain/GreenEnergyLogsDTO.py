#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GreenEnergyLogsDTO(object):

    def __init__(self):
        self._energy_amount = None
        self._energy_desc = None
        self._energy_tags = None
        self._goods_name = None
        self._log_id = None
        self._record_time = None
        self._result_code = None
        self._result_message = None
        self._status = None

    @property
    def energy_amount(self):
        return self._energy_amount

    @energy_amount.setter
    def energy_amount(self, value):
        self._energy_amount = value
    @property
    def energy_desc(self):
        return self._energy_desc

    @energy_desc.setter
    def energy_desc(self, value):
        self._energy_desc = value
    @property
    def energy_tags(self):
        return self._energy_tags

    @energy_tags.setter
    def energy_tags(self, value):
        if isinstance(value, list):
            self._energy_tags = list()
            for i in value:
                self._energy_tags.append(i)
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def log_id(self):
        return self._log_id

    @log_id.setter
    def log_id(self, value):
        self._log_id = value
    @property
    def record_time(self):
        return self._record_time

    @record_time.setter
    def record_time(self, value):
        self._record_time = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_message(self):
        return self._result_message

    @result_message.setter
    def result_message(self, value):
        self._result_message = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.energy_amount:
            if hasattr(self.energy_amount, 'to_alipay_dict'):
                params['energy_amount'] = self.energy_amount.to_alipay_dict()
            else:
                params['energy_amount'] = self.energy_amount
        if self.energy_desc:
            if hasattr(self.energy_desc, 'to_alipay_dict'):
                params['energy_desc'] = self.energy_desc.to_alipay_dict()
            else:
                params['energy_desc'] = self.energy_desc
        if self.energy_tags:
            if isinstance(self.energy_tags, list):
                for i in range(0, len(self.energy_tags)):
                    element = self.energy_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.energy_tags[i] = element.to_alipay_dict()
            if hasattr(self.energy_tags, 'to_alipay_dict'):
                params['energy_tags'] = self.energy_tags.to_alipay_dict()
            else:
                params['energy_tags'] = self.energy_tags
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.log_id:
            if hasattr(self.log_id, 'to_alipay_dict'):
                params['log_id'] = self.log_id.to_alipay_dict()
            else:
                params['log_id'] = self.log_id
        if self.record_time:
            if hasattr(self.record_time, 'to_alipay_dict'):
                params['record_time'] = self.record_time.to_alipay_dict()
            else:
                params['record_time'] = self.record_time
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
        if self.result_message:
            if hasattr(self.result_message, 'to_alipay_dict'):
                params['result_message'] = self.result_message.to_alipay_dict()
            else:
                params['result_message'] = self.result_message
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
        o = GreenEnergyLogsDTO()
        if 'energy_amount' in d:
            o.energy_amount = d['energy_amount']
        if 'energy_desc' in d:
            o.energy_desc = d['energy_desc']
        if 'energy_tags' in d:
            o.energy_tags = d['energy_tags']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'log_id' in d:
            o.log_id = d['log_id']
        if 'record_time' in d:
            o.record_time = d['record_time']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'result_message' in d:
            o.result_message = d['result_message']
        if 'status' in d:
            o.status = d['status']
        return o


