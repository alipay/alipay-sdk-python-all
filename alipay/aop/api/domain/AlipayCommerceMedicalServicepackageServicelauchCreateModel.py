#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MainUserInfo import MainUserInfo
from alipay.aop.api.domain.MainUserInfo import MainUserInfo


class AlipayCommerceMedicalServicepackageServicelauchCreateModel(object):

    def __init__(self):
        self._main_user_info = None
        self._out_pay_time = None
        self._out_unique_biz_no = None
        self._project_id = None
        self._sub_user_info_list = None
        self._valid_end_time = None
        self._valid_start_time = None

    @property
    def main_user_info(self):
        return self._main_user_info

    @main_user_info.setter
    def main_user_info(self, value):
        if isinstance(value, MainUserInfo):
            self._main_user_info = value
        else:
            self._main_user_info = MainUserInfo.from_alipay_dict(value)
    @property
    def out_pay_time(self):
        return self._out_pay_time

    @out_pay_time.setter
    def out_pay_time(self, value):
        self._out_pay_time = value
    @property
    def out_unique_biz_no(self):
        return self._out_unique_biz_no

    @out_unique_biz_no.setter
    def out_unique_biz_no(self, value):
        self._out_unique_biz_no = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def sub_user_info_list(self):
        return self._sub_user_info_list

    @sub_user_info_list.setter
    def sub_user_info_list(self, value):
        if isinstance(value, list):
            self._sub_user_info_list = list()
            for i in value:
                if isinstance(i, MainUserInfo):
                    self._sub_user_info_list.append(i)
                else:
                    self._sub_user_info_list.append(MainUserInfo.from_alipay_dict(i))
    @property
    def valid_end_time(self):
        return self._valid_end_time

    @valid_end_time.setter
    def valid_end_time(self, value):
        self._valid_end_time = value
    @property
    def valid_start_time(self):
        return self._valid_start_time

    @valid_start_time.setter
    def valid_start_time(self, value):
        self._valid_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.main_user_info:
            if hasattr(self.main_user_info, 'to_alipay_dict'):
                params['main_user_info'] = self.main_user_info.to_alipay_dict()
            else:
                params['main_user_info'] = self.main_user_info
        if self.out_pay_time:
            if hasattr(self.out_pay_time, 'to_alipay_dict'):
                params['out_pay_time'] = self.out_pay_time.to_alipay_dict()
            else:
                params['out_pay_time'] = self.out_pay_time
        if self.out_unique_biz_no:
            if hasattr(self.out_unique_biz_no, 'to_alipay_dict'):
                params['out_unique_biz_no'] = self.out_unique_biz_no.to_alipay_dict()
            else:
                params['out_unique_biz_no'] = self.out_unique_biz_no
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.sub_user_info_list:
            if isinstance(self.sub_user_info_list, list):
                for i in range(0, len(self.sub_user_info_list)):
                    element = self.sub_user_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_user_info_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_user_info_list, 'to_alipay_dict'):
                params['sub_user_info_list'] = self.sub_user_info_list.to_alipay_dict()
            else:
                params['sub_user_info_list'] = self.sub_user_info_list
        if self.valid_end_time:
            if hasattr(self.valid_end_time, 'to_alipay_dict'):
                params['valid_end_time'] = self.valid_end_time.to_alipay_dict()
            else:
                params['valid_end_time'] = self.valid_end_time
        if self.valid_start_time:
            if hasattr(self.valid_start_time, 'to_alipay_dict'):
                params['valid_start_time'] = self.valid_start_time.to_alipay_dict()
            else:
                params['valid_start_time'] = self.valid_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalServicepackageServicelauchCreateModel()
        if 'main_user_info' in d:
            o.main_user_info = d['main_user_info']
        if 'out_pay_time' in d:
            o.out_pay_time = d['out_pay_time']
        if 'out_unique_biz_no' in d:
            o.out_unique_biz_no = d['out_unique_biz_no']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'sub_user_info_list' in d:
            o.sub_user_info_list = d['sub_user_info_list']
        if 'valid_end_time' in d:
            o.valid_end_time = d['valid_end_time']
        if 'valid_start_time' in d:
            o.valid_start_time = d['valid_start_time']
        return o


