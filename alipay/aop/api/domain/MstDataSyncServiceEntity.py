#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MstDataSyncServiceEntity(object):

    def __init__(self):
        self._biz_uniq_id = None
        self._extend_info = None
        self._operate_type = None
        self._service_title = None
        self._service_url = None

    @property
    def biz_uniq_id(self):
        return self._biz_uniq_id

    @biz_uniq_id.setter
    def biz_uniq_id(self, value):
        self._biz_uniq_id = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def service_title(self):
        return self._service_title

    @service_title.setter
    def service_title(self, value):
        self._service_title = value
    @property
    def service_url(self):
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        self._service_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_uniq_id:
            if hasattr(self.biz_uniq_id, 'to_alipay_dict'):
                params['biz_uniq_id'] = self.biz_uniq_id.to_alipay_dict()
            else:
                params['biz_uniq_id'] = self.biz_uniq_id
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.service_title:
            if hasattr(self.service_title, 'to_alipay_dict'):
                params['service_title'] = self.service_title.to_alipay_dict()
            else:
                params['service_title'] = self.service_title
        if self.service_url:
            if hasattr(self.service_url, 'to_alipay_dict'):
                params['service_url'] = self.service_url.to_alipay_dict()
            else:
                params['service_url'] = self.service_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MstDataSyncServiceEntity()
        if 'biz_uniq_id' in d:
            o.biz_uniq_id = d['biz_uniq_id']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'service_title' in d:
            o.service_title = d['service_title']
        if 'service_url' in d:
            o.service_url = d['service_url']
        return o


