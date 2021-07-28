#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MpPrizeSendOrder(object):

    def __init__(self):
        self._camp_id = None
        self._camp_log_id = None
        self._display_name = None
        self._extend_field = None
        self._out_prize_id = None
        self._prize_flag = None
        self._prize_id = None
        self._prize_log_id = None
        self._prize_name = None
        self._repeat_trigger_flag = None
        self._trigger_result = None

    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def camp_log_id(self):
        return self._camp_log_id

    @camp_log_id.setter
    def camp_log_id(self, value):
        self._camp_log_id = value
    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def out_prize_id(self):
        return self._out_prize_id

    @out_prize_id.setter
    def out_prize_id(self, value):
        self._out_prize_id = value
    @property
    def prize_flag(self):
        return self._prize_flag

    @prize_flag.setter
    def prize_flag(self, value):
        self._prize_flag = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def prize_log_id(self):
        return self._prize_log_id

    @prize_log_id.setter
    def prize_log_id(self, value):
        self._prize_log_id = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def repeat_trigger_flag(self):
        return self._repeat_trigger_flag

    @repeat_trigger_flag.setter
    def repeat_trigger_flag(self, value):
        self._repeat_trigger_flag = value
    @property
    def trigger_result(self):
        return self._trigger_result

    @trigger_result.setter
    def trigger_result(self, value):
        self._trigger_result = value


    def to_alipay_dict(self):
        params = dict()
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.camp_log_id:
            if hasattr(self.camp_log_id, 'to_alipay_dict'):
                params['camp_log_id'] = self.camp_log_id.to_alipay_dict()
            else:
                params['camp_log_id'] = self.camp_log_id
        if self.display_name:
            if hasattr(self.display_name, 'to_alipay_dict'):
                params['display_name'] = self.display_name.to_alipay_dict()
            else:
                params['display_name'] = self.display_name
        if self.extend_field:
            if hasattr(self.extend_field, 'to_alipay_dict'):
                params['extend_field'] = self.extend_field.to_alipay_dict()
            else:
                params['extend_field'] = self.extend_field
        if self.out_prize_id:
            if hasattr(self.out_prize_id, 'to_alipay_dict'):
                params['out_prize_id'] = self.out_prize_id.to_alipay_dict()
            else:
                params['out_prize_id'] = self.out_prize_id
        if self.prize_flag:
            if hasattr(self.prize_flag, 'to_alipay_dict'):
                params['prize_flag'] = self.prize_flag.to_alipay_dict()
            else:
                params['prize_flag'] = self.prize_flag
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.prize_log_id:
            if hasattr(self.prize_log_id, 'to_alipay_dict'):
                params['prize_log_id'] = self.prize_log_id.to_alipay_dict()
            else:
                params['prize_log_id'] = self.prize_log_id
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.repeat_trigger_flag:
            if hasattr(self.repeat_trigger_flag, 'to_alipay_dict'):
                params['repeat_trigger_flag'] = self.repeat_trigger_flag.to_alipay_dict()
            else:
                params['repeat_trigger_flag'] = self.repeat_trigger_flag
        if self.trigger_result:
            if hasattr(self.trigger_result, 'to_alipay_dict'):
                params['trigger_result'] = self.trigger_result.to_alipay_dict()
            else:
                params['trigger_result'] = self.trigger_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MpPrizeSendOrder()
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'camp_log_id' in d:
            o.camp_log_id = d['camp_log_id']
        if 'display_name' in d:
            o.display_name = d['display_name']
        if 'extend_field' in d:
            o.extend_field = d['extend_field']
        if 'out_prize_id' in d:
            o.out_prize_id = d['out_prize_id']
        if 'prize_flag' in d:
            o.prize_flag = d['prize_flag']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_log_id' in d:
            o.prize_log_id = d['prize_log_id']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'repeat_trigger_flag' in d:
            o.repeat_trigger_flag = d['repeat_trigger_flag']
        if 'trigger_result' in d:
            o.trigger_result = d['trigger_result']
        return o


