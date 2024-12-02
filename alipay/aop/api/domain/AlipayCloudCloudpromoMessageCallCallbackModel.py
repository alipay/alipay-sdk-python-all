#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CallBackActionDetail import CallBackActionDetail


class AlipayCloudCloudpromoMessageCallCallbackModel(object):

    def __init__(self):
        self._action_detail = None
        self._action_result = None
        self._biz_id = None
        self._call_times = None
        self._customer_key = None
        self._out_serial_no = None
        self._param_type = None
        self._result_code = None
        self._result_msg = None
        self._scene_strategy_id = None

    @property
    def action_detail(self):
        return self._action_detail

    @action_detail.setter
    def action_detail(self, value):
        if isinstance(value, CallBackActionDetail):
            self._action_detail = value
        else:
            self._action_detail = CallBackActionDetail.from_alipay_dict(value)
    @property
    def action_result(self):
        return self._action_result

    @action_result.setter
    def action_result(self, value):
        self._action_result = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def call_times(self):
        return self._call_times

    @call_times.setter
    def call_times(self, value):
        self._call_times = value
    @property
    def customer_key(self):
        return self._customer_key

    @customer_key.setter
    def customer_key(self, value):
        self._customer_key = value
    @property
    def out_serial_no(self):
        return self._out_serial_no

    @out_serial_no.setter
    def out_serial_no(self, value):
        self._out_serial_no = value
    @property
    def param_type(self):
        return self._param_type

    @param_type.setter
    def param_type(self, value):
        self._param_type = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value
    @property
    def scene_strategy_id(self):
        return self._scene_strategy_id

    @scene_strategy_id.setter
    def scene_strategy_id(self, value):
        self._scene_strategy_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_detail:
            if hasattr(self.action_detail, 'to_alipay_dict'):
                params['action_detail'] = self.action_detail.to_alipay_dict()
            else:
                params['action_detail'] = self.action_detail
        if self.action_result:
            if hasattr(self.action_result, 'to_alipay_dict'):
                params['action_result'] = self.action_result.to_alipay_dict()
            else:
                params['action_result'] = self.action_result
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.call_times:
            if hasattr(self.call_times, 'to_alipay_dict'):
                params['call_times'] = self.call_times.to_alipay_dict()
            else:
                params['call_times'] = self.call_times
        if self.customer_key:
            if hasattr(self.customer_key, 'to_alipay_dict'):
                params['customer_key'] = self.customer_key.to_alipay_dict()
            else:
                params['customer_key'] = self.customer_key
        if self.out_serial_no:
            if hasattr(self.out_serial_no, 'to_alipay_dict'):
                params['out_serial_no'] = self.out_serial_no.to_alipay_dict()
            else:
                params['out_serial_no'] = self.out_serial_no
        if self.param_type:
            if hasattr(self.param_type, 'to_alipay_dict'):
                params['param_type'] = self.param_type.to_alipay_dict()
            else:
                params['param_type'] = self.param_type
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
        if self.result_msg:
            if hasattr(self.result_msg, 'to_alipay_dict'):
                params['result_msg'] = self.result_msg.to_alipay_dict()
            else:
                params['result_msg'] = self.result_msg
        if self.scene_strategy_id:
            if hasattr(self.scene_strategy_id, 'to_alipay_dict'):
                params['scene_strategy_id'] = self.scene_strategy_id.to_alipay_dict()
            else:
                params['scene_strategy_id'] = self.scene_strategy_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoMessageCallCallbackModel()
        if 'action_detail' in d:
            o.action_detail = d['action_detail']
        if 'action_result' in d:
            o.action_result = d['action_result']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'call_times' in d:
            o.call_times = d['call_times']
        if 'customer_key' in d:
            o.customer_key = d['customer_key']
        if 'out_serial_no' in d:
            o.out_serial_no = d['out_serial_no']
        if 'param_type' in d:
            o.param_type = d['param_type']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'result_msg' in d:
            o.result_msg = d['result_msg']
        if 'scene_strategy_id' in d:
            o.scene_strategy_id = d['scene_strategy_id']
        return o


