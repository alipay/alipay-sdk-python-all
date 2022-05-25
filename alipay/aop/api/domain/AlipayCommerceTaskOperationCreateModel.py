#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTaskOperationCreateModel(object):

    def __init__(self):
        self._channel = None
        self._cycle = None
        self._cycle_type = None
        self._desc = None
        self._end_time = None
        self._ext_info = None
        self._name = None
        self._out_biz_no = None
        self._scene = None
        self._scene_type = None
        self._shop_scope_type = None
        self._start_time = None
        self._startup_type = None
        self._target = None
        self._target_type = None
        self._task_rule_type = None
        self._type = None
        self._voucher_template_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def cycle(self):
        return self._cycle

    @cycle.setter
    def cycle(self, value):
        self._cycle = value
    @property
    def cycle_type(self):
        return self._cycle_type

    @cycle_type.setter
    def cycle_type(self, value):
        self._cycle_type = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def shop_scope_type(self):
        return self._shop_scope_type

    @shop_scope_type.setter
    def shop_scope_type(self, value):
        self._shop_scope_type = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def startup_type(self):
        return self._startup_type

    @startup_type.setter
    def startup_type(self, value):
        self._startup_type = value
    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value
    @property
    def target_type(self):
        return self._target_type

    @target_type.setter
    def target_type(self, value):
        self._target_type = value
    @property
    def task_rule_type(self):
        return self._task_rule_type

    @task_rule_type.setter
    def task_rule_type(self, value):
        self._task_rule_type = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def voucher_template_id(self):
        return self._voucher_template_id

    @voucher_template_id.setter
    def voucher_template_id(self, value):
        self._voucher_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.cycle:
            if hasattr(self.cycle, 'to_alipay_dict'):
                params['cycle'] = self.cycle.to_alipay_dict()
            else:
                params['cycle'] = self.cycle
        if self.cycle_type:
            if hasattr(self.cycle_type, 'to_alipay_dict'):
                params['cycle_type'] = self.cycle_type.to_alipay_dict()
            else:
                params['cycle_type'] = self.cycle_type
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.shop_scope_type:
            if hasattr(self.shop_scope_type, 'to_alipay_dict'):
                params['shop_scope_type'] = self.shop_scope_type.to_alipay_dict()
            else:
                params['shop_scope_type'] = self.shop_scope_type
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.startup_type:
            if hasattr(self.startup_type, 'to_alipay_dict'):
                params['startup_type'] = self.startup_type.to_alipay_dict()
            else:
                params['startup_type'] = self.startup_type
        if self.target:
            if hasattr(self.target, 'to_alipay_dict'):
                params['target'] = self.target.to_alipay_dict()
            else:
                params['target'] = self.target
        if self.target_type:
            if hasattr(self.target_type, 'to_alipay_dict'):
                params['target_type'] = self.target_type.to_alipay_dict()
            else:
                params['target_type'] = self.target_type
        if self.task_rule_type:
            if hasattr(self.task_rule_type, 'to_alipay_dict'):
                params['task_rule_type'] = self.task_rule_type.to_alipay_dict()
            else:
                params['task_rule_type'] = self.task_rule_type
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.voucher_template_id:
            if hasattr(self.voucher_template_id, 'to_alipay_dict'):
                params['voucher_template_id'] = self.voucher_template_id.to_alipay_dict()
            else:
                params['voucher_template_id'] = self.voucher_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTaskOperationCreateModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'cycle' in d:
            o.cycle = d['cycle']
        if 'cycle_type' in d:
            o.cycle_type = d['cycle_type']
        if 'desc' in d:
            o.desc = d['desc']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'name' in d:
            o.name = d['name']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'scene' in d:
            o.scene = d['scene']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'shop_scope_type' in d:
            o.shop_scope_type = d['shop_scope_type']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'startup_type' in d:
            o.startup_type = d['startup_type']
        if 'target' in d:
            o.target = d['target']
        if 'target_type' in d:
            o.target_type = d['target_type']
        if 'task_rule_type' in d:
            o.task_rule_type = d['task_rule_type']
        if 'type' in d:
            o.type = d['type']
        if 'voucher_template_id' in d:
            o.voucher_template_id = d['voucher_template_id']
        return o


