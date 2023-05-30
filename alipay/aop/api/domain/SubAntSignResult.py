#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AntSignUrlResult import AntSignUrlResult


class SubAntSignResult(object):

    def __init__(self):
        self._ant_sign_url_result_list = None
        self._our_user_id = None
        self._related_business = None
        self._sign_task_id = None
        self._sub_biz_no = None

    @property
    def ant_sign_url_result_list(self):
        return self._ant_sign_url_result_list

    @ant_sign_url_result_list.setter
    def ant_sign_url_result_list(self, value):
        if isinstance(value, list):
            self._ant_sign_url_result_list = list()
            for i in value:
                if isinstance(i, AntSignUrlResult):
                    self._ant_sign_url_result_list.append(i)
                else:
                    self._ant_sign_url_result_list.append(AntSignUrlResult.from_alipay_dict(i))
    @property
    def our_user_id(self):
        return self._our_user_id

    @our_user_id.setter
    def our_user_id(self, value):
        self._our_user_id = value
    @property
    def related_business(self):
        return self._related_business

    @related_business.setter
    def related_business(self, value):
        self._related_business = value
    @property
    def sign_task_id(self):
        return self._sign_task_id

    @sign_task_id.setter
    def sign_task_id(self, value):
        self._sign_task_id = value
    @property
    def sub_biz_no(self):
        return self._sub_biz_no

    @sub_biz_no.setter
    def sub_biz_no(self, value):
        self._sub_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_sign_url_result_list:
            if isinstance(self.ant_sign_url_result_list, list):
                for i in range(0, len(self.ant_sign_url_result_list)):
                    element = self.ant_sign_url_result_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ant_sign_url_result_list[i] = element.to_alipay_dict()
            if hasattr(self.ant_sign_url_result_list, 'to_alipay_dict'):
                params['ant_sign_url_result_list'] = self.ant_sign_url_result_list.to_alipay_dict()
            else:
                params['ant_sign_url_result_list'] = self.ant_sign_url_result_list
        if self.our_user_id:
            if hasattr(self.our_user_id, 'to_alipay_dict'):
                params['our_user_id'] = self.our_user_id.to_alipay_dict()
            else:
                params['our_user_id'] = self.our_user_id
        if self.related_business:
            if hasattr(self.related_business, 'to_alipay_dict'):
                params['related_business'] = self.related_business.to_alipay_dict()
            else:
                params['related_business'] = self.related_business
        if self.sign_task_id:
            if hasattr(self.sign_task_id, 'to_alipay_dict'):
                params['sign_task_id'] = self.sign_task_id.to_alipay_dict()
            else:
                params['sign_task_id'] = self.sign_task_id
        if self.sub_biz_no:
            if hasattr(self.sub_biz_no, 'to_alipay_dict'):
                params['sub_biz_no'] = self.sub_biz_no.to_alipay_dict()
            else:
                params['sub_biz_no'] = self.sub_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubAntSignResult()
        if 'ant_sign_url_result_list' in d:
            o.ant_sign_url_result_list = d['ant_sign_url_result_list']
        if 'our_user_id' in d:
            o.our_user_id = d['our_user_id']
        if 'related_business' in d:
            o.related_business = d['related_business']
        if 'sign_task_id' in d:
            o.sign_task_id = d['sign_task_id']
        if 'sub_biz_no' in d:
            o.sub_biz_no = d['sub_biz_no']
        return o


