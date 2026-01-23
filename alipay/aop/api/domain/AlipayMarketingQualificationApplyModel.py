#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingQualificationApplyModel(object):

    def __init__(self):
        self._biz_info = None
        self._open_id = None
        self._out_biz_no = None
        self._qual_id = None
        self._qual_instance_id = None
        self._user_id = None

    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        self._biz_info = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def qual_id(self):
        return self._qual_id

    @qual_id.setter
    def qual_id(self, value):
        self._qual_id = value
    @property
    def qual_instance_id(self):
        return self._qual_instance_id

    @qual_instance_id.setter
    def qual_instance_id(self, value):
        self._qual_instance_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.qual_id:
            if hasattr(self.qual_id, 'to_alipay_dict'):
                params['qual_id'] = self.qual_id.to_alipay_dict()
            else:
                params['qual_id'] = self.qual_id
        if self.qual_instance_id:
            if hasattr(self.qual_instance_id, 'to_alipay_dict'):
                params['qual_instance_id'] = self.qual_instance_id.to_alipay_dict()
            else:
                params['qual_instance_id'] = self.qual_instance_id
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
        o = AlipayMarketingQualificationApplyModel()
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'qual_id' in d:
            o.qual_id = d['qual_id']
        if 'qual_instance_id' in d:
            o.qual_instance_id = d['qual_instance_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


