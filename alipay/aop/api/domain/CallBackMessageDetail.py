#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CallBackMessageDetail(object):

    def __init__(self):
        self._answer_time = None
        self._batch_id = None
        self._call_begin_time = None
        self._call_id = None
        self._chat_record = None
        self._chats = None
        self._hangup_time = None
        self._import_time = None
        self._individual_tag = None
        self._intent_description = None
        self._intent_tag = None
        self._keywords = None
        self._ring_time = None
        self._sms_size = None
        self._speaking_duration = None
        self._speaking_turns = None
        self._status_code = None
        self._status_description = None
        self._success = None
        self._task_id = None
        self._template_id = None

    @property
    def answer_time(self):
        return self._answer_time

    @answer_time.setter
    def answer_time(self, value):
        self._answer_time = value
    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def call_begin_time(self):
        return self._call_begin_time

    @call_begin_time.setter
    def call_begin_time(self, value):
        self._call_begin_time = value
    @property
    def call_id(self):
        return self._call_id

    @call_id.setter
    def call_id(self, value):
        self._call_id = value
    @property
    def chat_record(self):
        return self._chat_record

    @chat_record.setter
    def chat_record(self, value):
        self._chat_record = value
    @property
    def chats(self):
        return self._chats

    @chats.setter
    def chats(self, value):
        self._chats = value
    @property
    def hangup_time(self):
        return self._hangup_time

    @hangup_time.setter
    def hangup_time(self, value):
        self._hangup_time = value
    @property
    def import_time(self):
        return self._import_time

    @import_time.setter
    def import_time(self, value):
        self._import_time = value
    @property
    def individual_tag(self):
        return self._individual_tag

    @individual_tag.setter
    def individual_tag(self, value):
        self._individual_tag = value
    @property
    def intent_description(self):
        return self._intent_description

    @intent_description.setter
    def intent_description(self, value):
        self._intent_description = value
    @property
    def intent_tag(self):
        return self._intent_tag

    @intent_tag.setter
    def intent_tag(self, value):
        self._intent_tag = value
    @property
    def keywords(self):
        return self._keywords

    @keywords.setter
    def keywords(self, value):
        self._keywords = value
    @property
    def ring_time(self):
        return self._ring_time

    @ring_time.setter
    def ring_time(self, value):
        self._ring_time = value
    @property
    def sms_size(self):
        return self._sms_size

    @sms_size.setter
    def sms_size(self, value):
        self._sms_size = value
    @property
    def speaking_duration(self):
        return self._speaking_duration

    @speaking_duration.setter
    def speaking_duration(self, value):
        self._speaking_duration = value
    @property
    def speaking_turns(self):
        return self._speaking_turns

    @speaking_turns.setter
    def speaking_turns(self, value):
        self._speaking_turns = value
    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value
    @property
    def status_description(self):
        return self._status_description

    @status_description.setter
    def status_description(self, value):
        self._status_description = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.answer_time:
            if hasattr(self.answer_time, 'to_alipay_dict'):
                params['answer_time'] = self.answer_time.to_alipay_dict()
            else:
                params['answer_time'] = self.answer_time
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.call_begin_time:
            if hasattr(self.call_begin_time, 'to_alipay_dict'):
                params['call_begin_time'] = self.call_begin_time.to_alipay_dict()
            else:
                params['call_begin_time'] = self.call_begin_time
        if self.call_id:
            if hasattr(self.call_id, 'to_alipay_dict'):
                params['call_id'] = self.call_id.to_alipay_dict()
            else:
                params['call_id'] = self.call_id
        if self.chat_record:
            if hasattr(self.chat_record, 'to_alipay_dict'):
                params['chat_record'] = self.chat_record.to_alipay_dict()
            else:
                params['chat_record'] = self.chat_record
        if self.chats:
            if hasattr(self.chats, 'to_alipay_dict'):
                params['chats'] = self.chats.to_alipay_dict()
            else:
                params['chats'] = self.chats
        if self.hangup_time:
            if hasattr(self.hangup_time, 'to_alipay_dict'):
                params['hangup_time'] = self.hangup_time.to_alipay_dict()
            else:
                params['hangup_time'] = self.hangup_time
        if self.import_time:
            if hasattr(self.import_time, 'to_alipay_dict'):
                params['import_time'] = self.import_time.to_alipay_dict()
            else:
                params['import_time'] = self.import_time
        if self.individual_tag:
            if hasattr(self.individual_tag, 'to_alipay_dict'):
                params['individual_tag'] = self.individual_tag.to_alipay_dict()
            else:
                params['individual_tag'] = self.individual_tag
        if self.intent_description:
            if hasattr(self.intent_description, 'to_alipay_dict'):
                params['intent_description'] = self.intent_description.to_alipay_dict()
            else:
                params['intent_description'] = self.intent_description
        if self.intent_tag:
            if hasattr(self.intent_tag, 'to_alipay_dict'):
                params['intent_tag'] = self.intent_tag.to_alipay_dict()
            else:
                params['intent_tag'] = self.intent_tag
        if self.keywords:
            if hasattr(self.keywords, 'to_alipay_dict'):
                params['keywords'] = self.keywords.to_alipay_dict()
            else:
                params['keywords'] = self.keywords
        if self.ring_time:
            if hasattr(self.ring_time, 'to_alipay_dict'):
                params['ring_time'] = self.ring_time.to_alipay_dict()
            else:
                params['ring_time'] = self.ring_time
        if self.sms_size:
            if hasattr(self.sms_size, 'to_alipay_dict'):
                params['sms_size'] = self.sms_size.to_alipay_dict()
            else:
                params['sms_size'] = self.sms_size
        if self.speaking_duration:
            if hasattr(self.speaking_duration, 'to_alipay_dict'):
                params['speaking_duration'] = self.speaking_duration.to_alipay_dict()
            else:
                params['speaking_duration'] = self.speaking_duration
        if self.speaking_turns:
            if hasattr(self.speaking_turns, 'to_alipay_dict'):
                params['speaking_turns'] = self.speaking_turns.to_alipay_dict()
            else:
                params['speaking_turns'] = self.speaking_turns
        if self.status_code:
            if hasattr(self.status_code, 'to_alipay_dict'):
                params['status_code'] = self.status_code.to_alipay_dict()
            else:
                params['status_code'] = self.status_code
        if self.status_description:
            if hasattr(self.status_description, 'to_alipay_dict'):
                params['status_description'] = self.status_description.to_alipay_dict()
            else:
                params['status_description'] = self.status_description
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CallBackMessageDetail()
        if 'answer_time' in d:
            o.answer_time = d['answer_time']
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'call_begin_time' in d:
            o.call_begin_time = d['call_begin_time']
        if 'call_id' in d:
            o.call_id = d['call_id']
        if 'chat_record' in d:
            o.chat_record = d['chat_record']
        if 'chats' in d:
            o.chats = d['chats']
        if 'hangup_time' in d:
            o.hangup_time = d['hangup_time']
        if 'import_time' in d:
            o.import_time = d['import_time']
        if 'individual_tag' in d:
            o.individual_tag = d['individual_tag']
        if 'intent_description' in d:
            o.intent_description = d['intent_description']
        if 'intent_tag' in d:
            o.intent_tag = d['intent_tag']
        if 'keywords' in d:
            o.keywords = d['keywords']
        if 'ring_time' in d:
            o.ring_time = d['ring_time']
        if 'sms_size' in d:
            o.sms_size = d['sms_size']
        if 'speaking_duration' in d:
            o.speaking_duration = d['speaking_duration']
        if 'speaking_turns' in d:
            o.speaking_turns = d['speaking_turns']
        if 'status_code' in d:
            o.status_code = d['status_code']
        if 'status_description' in d:
            o.status_description = d['status_description']
        if 'success' in d:
            o.success = d['success']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


