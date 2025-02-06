#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryRecruitMessageSendModel(object):

    def __init__(self):
        self._notify_type = None
        self._out_apply_id_list = None
        self._out_job_id = None
        self._server_job_url = None
        self._surplus_time = None

    @property
    def notify_type(self):
        return self._notify_type

    @notify_type.setter
    def notify_type(self, value):
        self._notify_type = value
    @property
    def out_apply_id_list(self):
        return self._out_apply_id_list

    @out_apply_id_list.setter
    def out_apply_id_list(self, value):
        if isinstance(value, list):
            self._out_apply_id_list = list()
            for i in value:
                self._out_apply_id_list.append(i)
    @property
    def out_job_id(self):
        return self._out_job_id

    @out_job_id.setter
    def out_job_id(self, value):
        self._out_job_id = value
    @property
    def server_job_url(self):
        return self._server_job_url

    @server_job_url.setter
    def server_job_url(self, value):
        self._server_job_url = value
    @property
    def surplus_time(self):
        return self._surplus_time

    @surplus_time.setter
    def surplus_time(self, value):
        self._surplus_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.notify_type:
            if hasattr(self.notify_type, 'to_alipay_dict'):
                params['notify_type'] = self.notify_type.to_alipay_dict()
            else:
                params['notify_type'] = self.notify_type
        if self.out_apply_id_list:
            if isinstance(self.out_apply_id_list, list):
                for i in range(0, len(self.out_apply_id_list)):
                    element = self.out_apply_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_apply_id_list[i] = element.to_alipay_dict()
            if hasattr(self.out_apply_id_list, 'to_alipay_dict'):
                params['out_apply_id_list'] = self.out_apply_id_list.to_alipay_dict()
            else:
                params['out_apply_id_list'] = self.out_apply_id_list
        if self.out_job_id:
            if hasattr(self.out_job_id, 'to_alipay_dict'):
                params['out_job_id'] = self.out_job_id.to_alipay_dict()
            else:
                params['out_job_id'] = self.out_job_id
        if self.server_job_url:
            if hasattr(self.server_job_url, 'to_alipay_dict'):
                params['server_job_url'] = self.server_job_url.to_alipay_dict()
            else:
                params['server_job_url'] = self.server_job_url
        if self.surplus_time:
            if hasattr(self.surplus_time, 'to_alipay_dict'):
                params['surplus_time'] = self.surplus_time.to_alipay_dict()
            else:
                params['surplus_time'] = self.surplus_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryRecruitMessageSendModel()
        if 'notify_type' in d:
            o.notify_type = d['notify_type']
        if 'out_apply_id_list' in d:
            o.out_apply_id_list = d['out_apply_id_list']
        if 'out_job_id' in d:
            o.out_job_id = d['out_job_id']
        if 'server_job_url' in d:
            o.server_job_url = d['server_job_url']
        if 'surplus_time' in d:
            o.surplus_time = d['surplus_time']
        return o


