#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceBusinessorderQueryModel(object):

    def __init__(self):
        self._begin_time = None
        self._end_time = None
        self._isv_appid = None
        self._page_num = None
        self._page_size = None
        self._platform_type = None
        self._status_list = None
        self._user_id = None

    @property
    def begin_time(self):
        return self._begin_time

    @begin_time.setter
    def begin_time(self, value):
        self._begin_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def isv_appid(self):
        return self._isv_appid

    @isv_appid.setter
    def isv_appid(self, value):
        self._isv_appid = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def platform_type(self):
        return self._platform_type

    @platform_type.setter
    def platform_type(self, value):
        self._platform_type = value
    @property
    def status_list(self):
        return self._status_list

    @status_list.setter
    def status_list(self, value):
        if isinstance(value, list):
            self._status_list = list()
            for i in value:
                self._status_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.begin_time:
            if hasattr(self.begin_time, 'to_alipay_dict'):
                params['begin_time'] = self.begin_time.to_alipay_dict()
            else:
                params['begin_time'] = self.begin_time
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.isv_appid:
            if hasattr(self.isv_appid, 'to_alipay_dict'):
                params['isv_appid'] = self.isv_appid.to_alipay_dict()
            else:
                params['isv_appid'] = self.isv_appid
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.platform_type:
            if hasattr(self.platform_type, 'to_alipay_dict'):
                params['platform_type'] = self.platform_type.to_alipay_dict()
            else:
                params['platform_type'] = self.platform_type
        if self.status_list:
            if isinstance(self.status_list, list):
                for i in range(0, len(self.status_list)):
                    element = self.status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.status_list[i] = element.to_alipay_dict()
            if hasattr(self.status_list, 'to_alipay_dict'):
                params['status_list'] = self.status_list.to_alipay_dict()
            else:
                params['status_list'] = self.status_list
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceBusinessorderQueryModel()
        if 'begin_time' in d:
            o.begin_time = d['begin_time']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'isv_appid' in d:
            o.isv_appid = d['isv_appid']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'platform_type' in d:
            o.platform_type = d['platform_type']
        if 'status_list' in d:
            o.status_list = d['status_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


