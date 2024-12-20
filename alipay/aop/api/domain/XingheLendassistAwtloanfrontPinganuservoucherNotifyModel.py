#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class XingheLendassistAwtloanfrontPinganuservoucherNotifyModel(object):

    def __init__(self):
        self._coupon_bind_time = None
        self._coupon_expire_time = None
        self._coupon_id = None
        self._coupon_receive_time = None
        self._coupon_status = None
        self._coupon_template_id = None
        self._notify_type = None
        self._order_no = None
        self._request_id = None
        self._submit_time = None

    @property
    def coupon_bind_time(self):
        return self._coupon_bind_time

    @coupon_bind_time.setter
    def coupon_bind_time(self, value):
        self._coupon_bind_time = value
    @property
    def coupon_expire_time(self):
        return self._coupon_expire_time

    @coupon_expire_time.setter
    def coupon_expire_time(self, value):
        self._coupon_expire_time = value
    @property
    def coupon_id(self):
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, value):
        self._coupon_id = value
    @property
    def coupon_receive_time(self):
        return self._coupon_receive_time

    @coupon_receive_time.setter
    def coupon_receive_time(self, value):
        self._coupon_receive_time = value
    @property
    def coupon_status(self):
        return self._coupon_status

    @coupon_status.setter
    def coupon_status(self, value):
        self._coupon_status = value
    @property
    def coupon_template_id(self):
        return self._coupon_template_id

    @coupon_template_id.setter
    def coupon_template_id(self, value):
        self._coupon_template_id = value
    @property
    def notify_type(self):
        return self._notify_type

    @notify_type.setter
    def notify_type(self, value):
        self._notify_type = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def submit_time(self):
        return self._submit_time

    @submit_time.setter
    def submit_time(self, value):
        self._submit_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.coupon_bind_time:
            if hasattr(self.coupon_bind_time, 'to_alipay_dict'):
                params['coupon_bind_time'] = self.coupon_bind_time.to_alipay_dict()
            else:
                params['coupon_bind_time'] = self.coupon_bind_time
        if self.coupon_expire_time:
            if hasattr(self.coupon_expire_time, 'to_alipay_dict'):
                params['coupon_expire_time'] = self.coupon_expire_time.to_alipay_dict()
            else:
                params['coupon_expire_time'] = self.coupon_expire_time
        if self.coupon_id:
            if hasattr(self.coupon_id, 'to_alipay_dict'):
                params['coupon_id'] = self.coupon_id.to_alipay_dict()
            else:
                params['coupon_id'] = self.coupon_id
        if self.coupon_receive_time:
            if hasattr(self.coupon_receive_time, 'to_alipay_dict'):
                params['coupon_receive_time'] = self.coupon_receive_time.to_alipay_dict()
            else:
                params['coupon_receive_time'] = self.coupon_receive_time
        if self.coupon_status:
            if hasattr(self.coupon_status, 'to_alipay_dict'):
                params['coupon_status'] = self.coupon_status.to_alipay_dict()
            else:
                params['coupon_status'] = self.coupon_status
        if self.coupon_template_id:
            if hasattr(self.coupon_template_id, 'to_alipay_dict'):
                params['coupon_template_id'] = self.coupon_template_id.to_alipay_dict()
            else:
                params['coupon_template_id'] = self.coupon_template_id
        if self.notify_type:
            if hasattr(self.notify_type, 'to_alipay_dict'):
                params['notify_type'] = self.notify_type.to_alipay_dict()
            else:
                params['notify_type'] = self.notify_type
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.submit_time:
            if hasattr(self.submit_time, 'to_alipay_dict'):
                params['submit_time'] = self.submit_time.to_alipay_dict()
            else:
                params['submit_time'] = self.submit_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistAwtloanfrontPinganuservoucherNotifyModel()
        if 'coupon_bind_time' in d:
            o.coupon_bind_time = d['coupon_bind_time']
        if 'coupon_expire_time' in d:
            o.coupon_expire_time = d['coupon_expire_time']
        if 'coupon_id' in d:
            o.coupon_id = d['coupon_id']
        if 'coupon_receive_time' in d:
            o.coupon_receive_time = d['coupon_receive_time']
        if 'coupon_status' in d:
            o.coupon_status = d['coupon_status']
        if 'coupon_template_id' in d:
            o.coupon_template_id = d['coupon_template_id']
        if 'notify_type' in d:
            o.notify_type = d['notify_type']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'submit_time' in d:
            o.submit_time = d['submit_time']
        return o


