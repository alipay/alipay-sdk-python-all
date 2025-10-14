#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayCommerceIotMarketingPlanCreateRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._biz_tids = None
        self._end_time = None
        self._hv_screen_1 = None
        self._plan_name = None
        self._priority = None
        self._space_code = None
        self._start_time = None
        self._file_content_1 = None
        self._version = "1.0"
        self._terminal_type = None
        self._terminal_info = None
        self._prod_code = None
        self._notify_url = None
        self._return_url = None
        self._udf_params = None
        self._need_encrypt = False

    @property
    def biz_model(self):
        return self._biz_model

    @biz_model.setter
    def biz_model(self, value):
        self._biz_model = value

    @property
    def biz_tids(self):
        return self._biz_tids

    @biz_tids.setter
    def biz_tids(self, value):
        if isinstance(value, list):
            self._biz_tids = list()
            for i in value:
                self._biz_tids.append(i)
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def hv_screen_1(self):
        return self._hv_screen_1

    @hv_screen_1.setter
    def hv_screen_1(self, value):
        self._hv_screen_1 = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def space_code(self):
        return self._space_code

    @space_code.setter
    def space_code(self, value):
        self._space_code = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    @property
    def file_content_1(self):
        return self._file_content_1

    @file_content_1.setter
    def file_content_1(self, value):
        if not isinstance(value, FileItem):
            return
        self._file_content_1 = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value

    @property
    def terminal_info(self):
        return self._terminal_info

    @terminal_info.setter
    def terminal_info(self, value):
        self._terminal_info = value

    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value

    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, value):
        self._notify_url = value

    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value

    @property
    def udf_params(self):
        return self._udf_params

    @udf_params.setter
    def udf_params(self, value):
        if not isinstance(value, dict):
            return
        self._udf_params = value

    @property
    def need_encrypt(self):
        return self._need_encrypt

    @need_encrypt.setter
    def need_encrypt(self, value):
        self._need_encrypt = value

    def add_other_text_param(self, key, value):
        if not self.udf_params:
            self.udf_params = dict()
        self.udf_params[key] = value

    def get_params(self):
        params = dict()
        params[P_METHOD] = 'alipay.commerce.iot.marketing.plan.create'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.biz_tids:
            if isinstance(self.biz_tids, list):
                for i in range(0, len(self.biz_tids)):
                    element = self.biz_tids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_tids[i] = element.to_alipay_dict()
                params['biz_tids'] = json.dumps(obj=self.biz_tids, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = json.dumps(obj=self.end_time.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['end_time'] = self.end_time
        if self.hv_screen_1:
            if hasattr(self.hv_screen_1, 'to_alipay_dict'):
                params['hv_screen_1'] = json.dumps(obj=self.hv_screen_1.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['hv_screen_1'] = self.hv_screen_1
        if self.plan_name:
            if hasattr(self.plan_name, 'to_alipay_dict'):
                params['plan_name'] = json.dumps(obj=self.plan_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['plan_name'] = self.plan_name
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = json.dumps(obj=self.priority.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['priority'] = self.priority
        if self.space_code:
            if hasattr(self.space_code, 'to_alipay_dict'):
                params['space_code'] = json.dumps(obj=self.space_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['space_code'] = self.space_code
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = json.dumps(obj=self.start_time.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['start_time'] = self.start_time
        if self.terminal_type:
            params['terminal_type'] = self.terminal_type
        if self.terminal_info:
            params['terminal_info'] = self.terminal_info
        if self.prod_code:
            params['prod_code'] = self.prod_code
        if self.notify_url:
            params['notify_url'] = self.notify_url
        if self.return_url:
            params['return_url'] = self.return_url
        if self.udf_params:
            params.update(self.udf_params)
        return params

    def get_multipart_params(self):
        multipart_params = dict()
        if self.file_content_1:
            multipart_params['file_content_1'] = self.file_content_1
        return multipart_params
