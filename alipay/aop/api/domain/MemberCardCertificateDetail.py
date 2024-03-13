#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MemberCardCertificateDetail(object):

    def __init__(self):
        self._direct_url = None
        self._effect_time = None
        self._expire_time = None
        self._id = None
        self._out_no = None
        self._status = None
        self._target = None
        self._total_count = None
        self._url = None
        self._usage_count = None
        self._user_mobile = None
        self._value = None
        self._verify_mode = None

    @property
    def direct_url(self):
        return self._direct_url

    @direct_url.setter
    def direct_url(self, value):
        self._direct_url = value
    @property
    def effect_time(self):
        return self._effect_time

    @effect_time.setter
    def effect_time(self, value):
        self._effect_time = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def out_no(self):
        return self._out_no

    @out_no.setter
    def out_no(self, value):
        self._out_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
    @property
    def usage_count(self):
        return self._usage_count

    @usage_count.setter
    def usage_count(self, value):
        self._usage_count = value
    @property
    def user_mobile(self):
        return self._user_mobile

    @user_mobile.setter
    def user_mobile(self, value):
        self._user_mobile = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
    @property
    def verify_mode(self):
        return self._verify_mode

    @verify_mode.setter
    def verify_mode(self, value):
        self._verify_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.direct_url:
            if hasattr(self.direct_url, 'to_alipay_dict'):
                params['direct_url'] = self.direct_url.to_alipay_dict()
            else:
                params['direct_url'] = self.direct_url
        if self.effect_time:
            if hasattr(self.effect_time, 'to_alipay_dict'):
                params['effect_time'] = self.effect_time.to_alipay_dict()
            else:
                params['effect_time'] = self.effect_time
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.out_no:
            if hasattr(self.out_no, 'to_alipay_dict'):
                params['out_no'] = self.out_no.to_alipay_dict()
            else:
                params['out_no'] = self.out_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.target:
            if hasattr(self.target, 'to_alipay_dict'):
                params['target'] = self.target.to_alipay_dict()
            else:
                params['target'] = self.target
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        if self.usage_count:
            if hasattr(self.usage_count, 'to_alipay_dict'):
                params['usage_count'] = self.usage_count.to_alipay_dict()
            else:
                params['usage_count'] = self.usage_count
        if self.user_mobile:
            if hasattr(self.user_mobile, 'to_alipay_dict'):
                params['user_mobile'] = self.user_mobile.to_alipay_dict()
            else:
                params['user_mobile'] = self.user_mobile
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        if self.verify_mode:
            if hasattr(self.verify_mode, 'to_alipay_dict'):
                params['verify_mode'] = self.verify_mode.to_alipay_dict()
            else:
                params['verify_mode'] = self.verify_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberCardCertificateDetail()
        if 'direct_url' in d:
            o.direct_url = d['direct_url']
        if 'effect_time' in d:
            o.effect_time = d['effect_time']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'id' in d:
            o.id = d['id']
        if 'out_no' in d:
            o.out_no = d['out_no']
        if 'status' in d:
            o.status = d['status']
        if 'target' in d:
            o.target = d['target']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'url' in d:
            o.url = d['url']
        if 'usage_count' in d:
            o.usage_count = d['usage_count']
        if 'user_mobile' in d:
            o.user_mobile = d['user_mobile']
        if 'value' in d:
            o.value = d['value']
        if 'verify_mode' in d:
            o.verify_mode = d['verify_mode']
        return o


