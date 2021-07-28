#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApiContractGoal import ApiContractGoal


class ApiContractItem(object):

    def __init__(self):
        self._actual_due_time = None
        self._complete_time = None
        self._contract_no = None
        self._due_time = None
        self._goals = None
        self._item_no = None
        self._item_phase = None
        self._item_status = None
        self._offer_no = None
        self._phase_serial_num = None
        self._template_no = None

    @property
    def actual_due_time(self):
        return self._actual_due_time

    @actual_due_time.setter
    def actual_due_time(self, value):
        self._actual_due_time = value
    @property
    def complete_time(self):
        return self._complete_time

    @complete_time.setter
    def complete_time(self, value):
        self._complete_time = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def due_time(self):
        return self._due_time

    @due_time.setter
    def due_time(self, value):
        self._due_time = value
    @property
    def goals(self):
        return self._goals

    @goals.setter
    def goals(self, value):
        if isinstance(value, list):
            self._goals = list()
            for i in value:
                if isinstance(i, ApiContractGoal):
                    self._goals.append(i)
                else:
                    self._goals.append(ApiContractGoal.from_alipay_dict(i))
    @property
    def item_no(self):
        return self._item_no

    @item_no.setter
    def item_no(self, value):
        self._item_no = value
    @property
    def item_phase(self):
        return self._item_phase

    @item_phase.setter
    def item_phase(self, value):
        self._item_phase = value
    @property
    def item_status(self):
        return self._item_status

    @item_status.setter
    def item_status(self, value):
        self._item_status = value
    @property
    def offer_no(self):
        return self._offer_no

    @offer_no.setter
    def offer_no(self, value):
        self._offer_no = value
    @property
    def phase_serial_num(self):
        return self._phase_serial_num

    @phase_serial_num.setter
    def phase_serial_num(self, value):
        self._phase_serial_num = value
    @property
    def template_no(self):
        return self._template_no

    @template_no.setter
    def template_no(self, value):
        self._template_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_due_time:
            if hasattr(self.actual_due_time, 'to_alipay_dict'):
                params['actual_due_time'] = self.actual_due_time.to_alipay_dict()
            else:
                params['actual_due_time'] = self.actual_due_time
        if self.complete_time:
            if hasattr(self.complete_time, 'to_alipay_dict'):
                params['complete_time'] = self.complete_time.to_alipay_dict()
            else:
                params['complete_time'] = self.complete_time
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.due_time:
            if hasattr(self.due_time, 'to_alipay_dict'):
                params['due_time'] = self.due_time.to_alipay_dict()
            else:
                params['due_time'] = self.due_time
        if self.goals:
            if isinstance(self.goals, list):
                for i in range(0, len(self.goals)):
                    element = self.goals[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goals[i] = element.to_alipay_dict()
            if hasattr(self.goals, 'to_alipay_dict'):
                params['goals'] = self.goals.to_alipay_dict()
            else:
                params['goals'] = self.goals
        if self.item_no:
            if hasattr(self.item_no, 'to_alipay_dict'):
                params['item_no'] = self.item_no.to_alipay_dict()
            else:
                params['item_no'] = self.item_no
        if self.item_phase:
            if hasattr(self.item_phase, 'to_alipay_dict'):
                params['item_phase'] = self.item_phase.to_alipay_dict()
            else:
                params['item_phase'] = self.item_phase
        if self.item_status:
            if hasattr(self.item_status, 'to_alipay_dict'):
                params['item_status'] = self.item_status.to_alipay_dict()
            else:
                params['item_status'] = self.item_status
        if self.offer_no:
            if hasattr(self.offer_no, 'to_alipay_dict'):
                params['offer_no'] = self.offer_no.to_alipay_dict()
            else:
                params['offer_no'] = self.offer_no
        if self.phase_serial_num:
            if hasattr(self.phase_serial_num, 'to_alipay_dict'):
                params['phase_serial_num'] = self.phase_serial_num.to_alipay_dict()
            else:
                params['phase_serial_num'] = self.phase_serial_num
        if self.template_no:
            if hasattr(self.template_no, 'to_alipay_dict'):
                params['template_no'] = self.template_no.to_alipay_dict()
            else:
                params['template_no'] = self.template_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApiContractItem()
        if 'actual_due_time' in d:
            o.actual_due_time = d['actual_due_time']
        if 'complete_time' in d:
            o.complete_time = d['complete_time']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'due_time' in d:
            o.due_time = d['due_time']
        if 'goals' in d:
            o.goals = d['goals']
        if 'item_no' in d:
            o.item_no = d['item_no']
        if 'item_phase' in d:
            o.item_phase = d['item_phase']
        if 'item_status' in d:
            o.item_status = d['item_status']
        if 'offer_no' in d:
            o.offer_no = d['offer_no']
        if 'phase_serial_num' in d:
            o.phase_serial_num = d['phase_serial_num']
        if 'template_no' in d:
            o.template_no = d['template_no']
        return o


