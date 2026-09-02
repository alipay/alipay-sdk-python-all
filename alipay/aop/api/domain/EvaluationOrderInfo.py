#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EvaluationOrderInfo(object):

    def __init__(self):
        self._apply_name = None
        self._apply_time = None
        self._channel = None
        self._ep_cert_no = None
        self._expire_time = None
        self._fail_reason = None
        self._finish_time = None
        self._order_no = None
        self._order_status = None
        self._result_file_url = None

    @property
    def apply_name(self):
        return self._apply_name

    @apply_name.setter
    def apply_name(self, value):
        self._apply_name = value
    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def result_file_url(self):
        return self._result_file_url

    @result_file_url.setter
    def result_file_url(self, value):
        self._result_file_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_name:
            if hasattr(self.apply_name, 'to_alipay_dict'):
                params['apply_name'] = self.apply_name.to_alipay_dict()
            else:
                params['apply_name'] = self.apply_name
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.finish_time:
            if hasattr(self.finish_time, 'to_alipay_dict'):
                params['finish_time'] = self.finish_time.to_alipay_dict()
            else:
                params['finish_time'] = self.finish_time
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.result_file_url:
            if hasattr(self.result_file_url, 'to_alipay_dict'):
                params['result_file_url'] = self.result_file_url.to_alipay_dict()
            else:
                params['result_file_url'] = self.result_file_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EvaluationOrderInfo()
        if 'apply_name' in d:
            o.apply_name = d['apply_name']
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'channel' in d:
            o.channel = d['channel']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'finish_time' in d:
            o.finish_time = d['finish_time']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'result_file_url' in d:
            o.result_file_url = d['result_file_url']
        return o


