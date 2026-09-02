#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DisResInfo import DisResInfo


class AlipayCommerceRentAgentTicketConfirmModel(object):

    def __init__(self):
        self._action = None
        self._assignment_id = None
        self._result = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def assignment_id(self):
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, value):
        self._assignment_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, DisResInfo):
            self._result = value
        else:
            self._result = DisResInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.assignment_id:
            if hasattr(self.assignment_id, 'to_alipay_dict'):
                params['assignment_id'] = self.assignment_id.to_alipay_dict()
            else:
                params['assignment_id'] = self.assignment_id
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentAgentTicketConfirmModel()
        if 'action' in d:
            o.action = d['action']
        if 'assignment_id' in d:
            o.assignment_id = d['assignment_id']
        if 'result' in d:
            o.result = d['result']
        return o


