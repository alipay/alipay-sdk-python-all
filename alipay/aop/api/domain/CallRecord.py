#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CallRecord(object):

    def __init__(self):
        self._acid = None
        self._biz_owner = None
        self._call_time = None
        self._call_type = None
        self._callee = None
        self._caller = None
        self._connect_status = None
        self._cue_id = None
        self._customer_name = None
        self._gmt_create = None
        self._gmt_modified = None
        self._hangup_dir = None
        self._hangup_reason = None
        self._ivr_time = None
        self._manual_time = None
        self._process = None
        self._queue_time = None
        self._release_time = None
        self._ring_time = None
        self._start_time = None
        self._talk_time = None

    @property
    def acid(self):
        return self._acid

    @acid.setter
    def acid(self, value):
        self._acid = value
    @property
    def biz_owner(self):
        return self._biz_owner

    @biz_owner.setter
    def biz_owner(self, value):
        self._biz_owner = value
    @property
    def call_time(self):
        return self._call_time

    @call_time.setter
    def call_time(self, value):
        self._call_time = value
    @property
    def call_type(self):
        return self._call_type

    @call_type.setter
    def call_type(self, value):
        self._call_type = value
    @property
    def callee(self):
        return self._callee

    @callee.setter
    def callee(self, value):
        self._callee = value
    @property
    def caller(self):
        return self._caller

    @caller.setter
    def caller(self, value):
        self._caller = value
    @property
    def connect_status(self):
        return self._connect_status

    @connect_status.setter
    def connect_status(self, value):
        self._connect_status = value
    @property
    def cue_id(self):
        return self._cue_id

    @cue_id.setter
    def cue_id(self, value):
        self._cue_id = value
    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def hangup_dir(self):
        return self._hangup_dir

    @hangup_dir.setter
    def hangup_dir(self, value):
        self._hangup_dir = value
    @property
    def hangup_reason(self):
        return self._hangup_reason

    @hangup_reason.setter
    def hangup_reason(self, value):
        self._hangup_reason = value
    @property
    def ivr_time(self):
        return self._ivr_time

    @ivr_time.setter
    def ivr_time(self, value):
        self._ivr_time = value
    @property
    def manual_time(self):
        return self._manual_time

    @manual_time.setter
    def manual_time(self, value):
        self._manual_time = value
    @property
    def process(self):
        return self._process

    @process.setter
    def process(self, value):
        self._process = value
    @property
    def queue_time(self):
        return self._queue_time

    @queue_time.setter
    def queue_time(self, value):
        self._queue_time = value
    @property
    def release_time(self):
        return self._release_time

    @release_time.setter
    def release_time(self, value):
        self._release_time = value
    @property
    def ring_time(self):
        return self._ring_time

    @ring_time.setter
    def ring_time(self, value):
        self._ring_time = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def talk_time(self):
        return self._talk_time

    @talk_time.setter
    def talk_time(self, value):
        self._talk_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.acid:
            if hasattr(self.acid, 'to_alipay_dict'):
                params['acid'] = self.acid.to_alipay_dict()
            else:
                params['acid'] = self.acid
        if self.biz_owner:
            if hasattr(self.biz_owner, 'to_alipay_dict'):
                params['biz_owner'] = self.biz_owner.to_alipay_dict()
            else:
                params['biz_owner'] = self.biz_owner
        if self.call_time:
            if hasattr(self.call_time, 'to_alipay_dict'):
                params['call_time'] = self.call_time.to_alipay_dict()
            else:
                params['call_time'] = self.call_time
        if self.call_type:
            if hasattr(self.call_type, 'to_alipay_dict'):
                params['call_type'] = self.call_type.to_alipay_dict()
            else:
                params['call_type'] = self.call_type
        if self.callee:
            if hasattr(self.callee, 'to_alipay_dict'):
                params['callee'] = self.callee.to_alipay_dict()
            else:
                params['callee'] = self.callee
        if self.caller:
            if hasattr(self.caller, 'to_alipay_dict'):
                params['caller'] = self.caller.to_alipay_dict()
            else:
                params['caller'] = self.caller
        if self.connect_status:
            if hasattr(self.connect_status, 'to_alipay_dict'):
                params['connect_status'] = self.connect_status.to_alipay_dict()
            else:
                params['connect_status'] = self.connect_status
        if self.cue_id:
            if hasattr(self.cue_id, 'to_alipay_dict'):
                params['cue_id'] = self.cue_id.to_alipay_dict()
            else:
                params['cue_id'] = self.cue_id
        if self.customer_name:
            if hasattr(self.customer_name, 'to_alipay_dict'):
                params['customer_name'] = self.customer_name.to_alipay_dict()
            else:
                params['customer_name'] = self.customer_name
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.hangup_dir:
            if hasattr(self.hangup_dir, 'to_alipay_dict'):
                params['hangup_dir'] = self.hangup_dir.to_alipay_dict()
            else:
                params['hangup_dir'] = self.hangup_dir
        if self.hangup_reason:
            if hasattr(self.hangup_reason, 'to_alipay_dict'):
                params['hangup_reason'] = self.hangup_reason.to_alipay_dict()
            else:
                params['hangup_reason'] = self.hangup_reason
        if self.ivr_time:
            if hasattr(self.ivr_time, 'to_alipay_dict'):
                params['ivr_time'] = self.ivr_time.to_alipay_dict()
            else:
                params['ivr_time'] = self.ivr_time
        if self.manual_time:
            if hasattr(self.manual_time, 'to_alipay_dict'):
                params['manual_time'] = self.manual_time.to_alipay_dict()
            else:
                params['manual_time'] = self.manual_time
        if self.process:
            if hasattr(self.process, 'to_alipay_dict'):
                params['process'] = self.process.to_alipay_dict()
            else:
                params['process'] = self.process
        if self.queue_time:
            if hasattr(self.queue_time, 'to_alipay_dict'):
                params['queue_time'] = self.queue_time.to_alipay_dict()
            else:
                params['queue_time'] = self.queue_time
        if self.release_time:
            if hasattr(self.release_time, 'to_alipay_dict'):
                params['release_time'] = self.release_time.to_alipay_dict()
            else:
                params['release_time'] = self.release_time
        if self.ring_time:
            if hasattr(self.ring_time, 'to_alipay_dict'):
                params['ring_time'] = self.ring_time.to_alipay_dict()
            else:
                params['ring_time'] = self.ring_time
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.talk_time:
            if hasattr(self.talk_time, 'to_alipay_dict'):
                params['talk_time'] = self.talk_time.to_alipay_dict()
            else:
                params['talk_time'] = self.talk_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CallRecord()
        if 'acid' in d:
            o.acid = d['acid']
        if 'biz_owner' in d:
            o.biz_owner = d['biz_owner']
        if 'call_time' in d:
            o.call_time = d['call_time']
        if 'call_type' in d:
            o.call_type = d['call_type']
        if 'callee' in d:
            o.callee = d['callee']
        if 'caller' in d:
            o.caller = d['caller']
        if 'connect_status' in d:
            o.connect_status = d['connect_status']
        if 'cue_id' in d:
            o.cue_id = d['cue_id']
        if 'customer_name' in d:
            o.customer_name = d['customer_name']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'hangup_dir' in d:
            o.hangup_dir = d['hangup_dir']
        if 'hangup_reason' in d:
            o.hangup_reason = d['hangup_reason']
        if 'ivr_time' in d:
            o.ivr_time = d['ivr_time']
        if 'manual_time' in d:
            o.manual_time = d['manual_time']
        if 'process' in d:
            o.process = d['process']
        if 'queue_time' in d:
            o.queue_time = d['queue_time']
        if 'release_time' in d:
            o.release_time = d['release_time']
        if 'ring_time' in d:
            o.ring_time = d['ring_time']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'talk_time' in d:
            o.talk_time = d['talk_time']
        return o


