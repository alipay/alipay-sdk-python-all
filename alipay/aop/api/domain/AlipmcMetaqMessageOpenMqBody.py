#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipmcMetaqMessageOpenMqBody(object):

    def __init__(self):
        self._activity_id = None
        self._activity_instance_id = None
        self._alipmc_message_id = None
        self._before = None
        self._class_alias = None
        self._event_type = None
        self._exception_info = None
        self._notify_message_type = None
        self._notify_topic = None
        self._operator = None
        self._out_result = None
        self._process_code = None
        self._process_id = None
        self._process_instance_id = None
        self._resumption_id = None
        self._task_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_instance_id(self):
        return self._activity_instance_id

    @activity_instance_id.setter
    def activity_instance_id(self, value):
        self._activity_instance_id = value
    @property
    def alipmc_message_id(self):
        return self._alipmc_message_id

    @alipmc_message_id.setter
    def alipmc_message_id(self, value):
        self._alipmc_message_id = value
    @property
    def before(self):
        return self._before

    @before.setter
    def before(self, value):
        self._before = value
    @property
    def class_alias(self):
        return self._class_alias

    @class_alias.setter
    def class_alias(self, value):
        self._class_alias = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def exception_info(self):
        return self._exception_info

    @exception_info.setter
    def exception_info(self, value):
        self._exception_info = value
    @property
    def notify_message_type(self):
        return self._notify_message_type

    @notify_message_type.setter
    def notify_message_type(self, value):
        self._notify_message_type = value
    @property
    def notify_topic(self):
        return self._notify_topic

    @notify_topic.setter
    def notify_topic(self, value):
        self._notify_topic = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def out_result(self):
        return self._out_result

    @out_result.setter
    def out_result(self, value):
        self._out_result = value
    @property
    def process_code(self):
        return self._process_code

    @process_code.setter
    def process_code(self, value):
        self._process_code = value
    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value
    @property
    def process_instance_id(self):
        return self._process_instance_id

    @process_instance_id.setter
    def process_instance_id(self, value):
        self._process_instance_id = value
    @property
    def resumption_id(self):
        return self._resumption_id

    @resumption_id.setter
    def resumption_id(self, value):
        self._resumption_id = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_instance_id:
            if hasattr(self.activity_instance_id, 'to_alipay_dict'):
                params['activity_instance_id'] = self.activity_instance_id.to_alipay_dict()
            else:
                params['activity_instance_id'] = self.activity_instance_id
        if self.alipmc_message_id:
            if hasattr(self.alipmc_message_id, 'to_alipay_dict'):
                params['alipmc_message_id'] = self.alipmc_message_id.to_alipay_dict()
            else:
                params['alipmc_message_id'] = self.alipmc_message_id
        if self.before:
            if hasattr(self.before, 'to_alipay_dict'):
                params['before'] = self.before.to_alipay_dict()
            else:
                params['before'] = self.before
        if self.class_alias:
            if hasattr(self.class_alias, 'to_alipay_dict'):
                params['class_alias'] = self.class_alias.to_alipay_dict()
            else:
                params['class_alias'] = self.class_alias
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.exception_info:
            if hasattr(self.exception_info, 'to_alipay_dict'):
                params['exception_info'] = self.exception_info.to_alipay_dict()
            else:
                params['exception_info'] = self.exception_info
        if self.notify_message_type:
            if hasattr(self.notify_message_type, 'to_alipay_dict'):
                params['notify_message_type'] = self.notify_message_type.to_alipay_dict()
            else:
                params['notify_message_type'] = self.notify_message_type
        if self.notify_topic:
            if hasattr(self.notify_topic, 'to_alipay_dict'):
                params['notify_topic'] = self.notify_topic.to_alipay_dict()
            else:
                params['notify_topic'] = self.notify_topic
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.out_result:
            if hasattr(self.out_result, 'to_alipay_dict'):
                params['out_result'] = self.out_result.to_alipay_dict()
            else:
                params['out_result'] = self.out_result
        if self.process_code:
            if hasattr(self.process_code, 'to_alipay_dict'):
                params['process_code'] = self.process_code.to_alipay_dict()
            else:
                params['process_code'] = self.process_code
        if self.process_id:
            if hasattr(self.process_id, 'to_alipay_dict'):
                params['process_id'] = self.process_id.to_alipay_dict()
            else:
                params['process_id'] = self.process_id
        if self.process_instance_id:
            if hasattr(self.process_instance_id, 'to_alipay_dict'):
                params['process_instance_id'] = self.process_instance_id.to_alipay_dict()
            else:
                params['process_instance_id'] = self.process_instance_id
        if self.resumption_id:
            if hasattr(self.resumption_id, 'to_alipay_dict'):
                params['resumption_id'] = self.resumption_id.to_alipay_dict()
            else:
                params['resumption_id'] = self.resumption_id
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipmcMetaqMessageOpenMqBody()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_instance_id' in d:
            o.activity_instance_id = d['activity_instance_id']
        if 'alipmc_message_id' in d:
            o.alipmc_message_id = d['alipmc_message_id']
        if 'before' in d:
            o.before = d['before']
        if 'class_alias' in d:
            o.class_alias = d['class_alias']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'exception_info' in d:
            o.exception_info = d['exception_info']
        if 'notify_message_type' in d:
            o.notify_message_type = d['notify_message_type']
        if 'notify_topic' in d:
            o.notify_topic = d['notify_topic']
        if 'operator' in d:
            o.operator = d['operator']
        if 'out_result' in d:
            o.out_result = d['out_result']
        if 'process_code' in d:
            o.process_code = d['process_code']
        if 'process_id' in d:
            o.process_id = d['process_id']
        if 'process_instance_id' in d:
            o.process_instance_id = d['process_instance_id']
        if 'resumption_id' in d:
            o.resumption_id = d['resumption_id']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


