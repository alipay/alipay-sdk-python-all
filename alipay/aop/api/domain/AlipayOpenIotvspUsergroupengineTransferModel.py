#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotvspUsergroupengineTransferModel(object):

    def __init__(self):
        self._biz_id = None
        self._elastic_type = None
        self._isv_pid = None
        self._org_out_id = None
        self._vid_list = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def elastic_type(self):
        return self._elastic_type

    @elastic_type.setter
    def elastic_type(self, value):
        self._elastic_type = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def org_out_id(self):
        return self._org_out_id

    @org_out_id.setter
    def org_out_id(self, value):
        self._org_out_id = value
    @property
    def vid_list(self):
        return self._vid_list

    @vid_list.setter
    def vid_list(self, value):
        if isinstance(value, list):
            self._vid_list = list()
            for i in value:
                self._vid_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.elastic_type:
            if hasattr(self.elastic_type, 'to_alipay_dict'):
                params['elastic_type'] = self.elastic_type.to_alipay_dict()
            else:
                params['elastic_type'] = self.elastic_type
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.org_out_id:
            if hasattr(self.org_out_id, 'to_alipay_dict'):
                params['org_out_id'] = self.org_out_id.to_alipay_dict()
            else:
                params['org_out_id'] = self.org_out_id
        if self.vid_list:
            if isinstance(self.vid_list, list):
                for i in range(0, len(self.vid_list)):
                    element = self.vid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.vid_list[i] = element.to_alipay_dict()
            if hasattr(self.vid_list, 'to_alipay_dict'):
                params['vid_list'] = self.vid_list.to_alipay_dict()
            else:
                params['vid_list'] = self.vid_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotvspUsergroupengineTransferModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'elastic_type' in d:
            o.elastic_type = d['elastic_type']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'org_out_id' in d:
            o.org_out_id = d['org_out_id']
        if 'vid_list' in d:
            o.vid_list = d['vid_list']
        return o


