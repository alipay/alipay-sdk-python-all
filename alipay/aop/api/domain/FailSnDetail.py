#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FailSnDetail(object):

    def __init__(self):
        self._result_code = None
        self._result_msg = None
        self._route_url = None
        self._status = None
        self._tag_id = None
        self._tag_sn = None

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
    def route_url(self):
        return self._route_url

    @route_url.setter
    def route_url(self, value):
        self._route_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value
    @property
    def tag_sn(self):
        return self._tag_sn

    @tag_sn.setter
    def tag_sn(self, value):
        self._tag_sn = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.route_url:
            if hasattr(self.route_url, 'to_alipay_dict'):
                params['route_url'] = self.route_url.to_alipay_dict()
            else:
                params['route_url'] = self.route_url
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tag_id:
            if hasattr(self.tag_id, 'to_alipay_dict'):
                params['tag_id'] = self.tag_id.to_alipay_dict()
            else:
                params['tag_id'] = self.tag_id
        if self.tag_sn:
            if hasattr(self.tag_sn, 'to_alipay_dict'):
                params['tag_sn'] = self.tag_sn.to_alipay_dict()
            else:
                params['tag_sn'] = self.tag_sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FailSnDetail()
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'result_msg' in d:
            o.result_msg = d['result_msg']
        if 'route_url' in d:
            o.route_url = d['route_url']
        if 'status' in d:
            o.status = d['status']
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        if 'tag_sn' in d:
            o.tag_sn = d['tag_sn']
        return o


