#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderInfoDTO(object):

    def __init__(self):
        self._apply_id = None
        self._create_time = None
        self._operator_id = None
        self._out_biz_no = None
        self._pid = None
        self._request_id = None
        self._result_code = None
        self._result_desc = None
        self._shop_id = None
        self._status = None
        self._sub_status = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_desc(self):
        return self._result_desc

    @result_desc.setter
    def result_desc(self, value):
        self._result_desc = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_status(self):
        return self._sub_status

    @sub_status.setter
    def sub_status(self, value):
        self._sub_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
        if self.result_desc:
            if hasattr(self.result_desc, 'to_alipay_dict'):
                params['result_desc'] = self.result_desc.to_alipay_dict()
            else:
                params['result_desc'] = self.result_desc
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_status:
            if hasattr(self.sub_status, 'to_alipay_dict'):
                params['sub_status'] = self.sub_status.to_alipay_dict()
            else:
                params['sub_status'] = self.sub_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderInfoDTO()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pid' in d:
            o.pid = d['pid']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'result_desc' in d:
            o.result_desc = d['result_desc']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'status' in d:
            o.status = d['status']
        if 'sub_status' in d:
            o.sub_status = d['sub_status']
        return o


