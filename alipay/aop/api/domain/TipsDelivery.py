#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TipsDelivery(object):

    def __init__(self):
        self._delivery_content = None
        self._delivery_id = None
        self._delivery_name = None
        self._end_time = None
        self._fail_reason = None
        self._match_type = None
        self._match_url = None
        self._start_time = None
        self._status = None

    @property
    def delivery_content(self):
        return self._delivery_content

    @delivery_content.setter
    def delivery_content(self, value):
        self._delivery_content = value
    @property
    def delivery_id(self):
        return self._delivery_id

    @delivery_id.setter
    def delivery_id(self, value):
        self._delivery_id = value
    @property
    def delivery_name(self):
        return self._delivery_name

    @delivery_name.setter
    def delivery_name(self, value):
        self._delivery_name = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def match_type(self):
        return self._match_type

    @match_type.setter
    def match_type(self, value):
        self._match_type = value
    @property
    def match_url(self):
        return self._match_url

    @match_url.setter
    def match_url(self, value):
        self._match_url = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_content:
            if hasattr(self.delivery_content, 'to_alipay_dict'):
                params['delivery_content'] = self.delivery_content.to_alipay_dict()
            else:
                params['delivery_content'] = self.delivery_content
        if self.delivery_id:
            if hasattr(self.delivery_id, 'to_alipay_dict'):
                params['delivery_id'] = self.delivery_id.to_alipay_dict()
            else:
                params['delivery_id'] = self.delivery_id
        if self.delivery_name:
            if hasattr(self.delivery_name, 'to_alipay_dict'):
                params['delivery_name'] = self.delivery_name.to_alipay_dict()
            else:
                params['delivery_name'] = self.delivery_name
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.match_type:
            if hasattr(self.match_type, 'to_alipay_dict'):
                params['match_type'] = self.match_type.to_alipay_dict()
            else:
                params['match_type'] = self.match_type
        if self.match_url:
            if hasattr(self.match_url, 'to_alipay_dict'):
                params['match_url'] = self.match_url.to_alipay_dict()
            else:
                params['match_url'] = self.match_url
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
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
        o = TipsDelivery()
        if 'delivery_content' in d:
            o.delivery_content = d['delivery_content']
        if 'delivery_id' in d:
            o.delivery_id = d['delivery_id']
        if 'delivery_name' in d:
            o.delivery_name = d['delivery_name']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'match_type' in d:
            o.match_type = d['match_type']
        if 'match_url' in d:
            o.match_url = d['match_url']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        return o


