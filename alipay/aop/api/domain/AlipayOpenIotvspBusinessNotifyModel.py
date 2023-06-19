#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessInfoRequest import BusinessInfoRequest
from alipay.aop.api.domain.NotifyEventParam import NotifyEventParam


class AlipayOpenIotvspBusinessNotifyModel(object):

    def __init__(self):
        self._biz_id = None
        self._business_list = None
        self._isv_pid = None
        self._label_out_no = None
        self._notify_event_param = None
        self._org_out_id = None
        self._scene_code = None
        self._vid = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def business_list(self):
        return self._business_list

    @business_list.setter
    def business_list(self, value):
        if isinstance(value, list):
            self._business_list = list()
            for i in value:
                if isinstance(i, BusinessInfoRequest):
                    self._business_list.append(i)
                else:
                    self._business_list.append(BusinessInfoRequest.from_alipay_dict(i))
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def label_out_no(self):
        return self._label_out_no

    @label_out_no.setter
    def label_out_no(self, value):
        self._label_out_no = value
    @property
    def notify_event_param(self):
        return self._notify_event_param

    @notify_event_param.setter
    def notify_event_param(self, value):
        if isinstance(value, NotifyEventParam):
            self._notify_event_param = value
        else:
            self._notify_event_param = NotifyEventParam.from_alipay_dict(value)
    @property
    def org_out_id(self):
        return self._org_out_id

    @org_out_id.setter
    def org_out_id(self, value):
        self._org_out_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def vid(self):
        return self._vid

    @vid.setter
    def vid(self, value):
        self._vid = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.business_list:
            if isinstance(self.business_list, list):
                for i in range(0, len(self.business_list)):
                    element = self.business_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_list[i] = element.to_alipay_dict()
            if hasattr(self.business_list, 'to_alipay_dict'):
                params['business_list'] = self.business_list.to_alipay_dict()
            else:
                params['business_list'] = self.business_list
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.label_out_no:
            if hasattr(self.label_out_no, 'to_alipay_dict'):
                params['label_out_no'] = self.label_out_no.to_alipay_dict()
            else:
                params['label_out_no'] = self.label_out_no
        if self.notify_event_param:
            if hasattr(self.notify_event_param, 'to_alipay_dict'):
                params['notify_event_param'] = self.notify_event_param.to_alipay_dict()
            else:
                params['notify_event_param'] = self.notify_event_param
        if self.org_out_id:
            if hasattr(self.org_out_id, 'to_alipay_dict'):
                params['org_out_id'] = self.org_out_id.to_alipay_dict()
            else:
                params['org_out_id'] = self.org_out_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.vid:
            if hasattr(self.vid, 'to_alipay_dict'):
                params['vid'] = self.vid.to_alipay_dict()
            else:
                params['vid'] = self.vid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotvspBusinessNotifyModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'business_list' in d:
            o.business_list = d['business_list']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'label_out_no' in d:
            o.label_out_no = d['label_out_no']
        if 'notify_event_param' in d:
            o.notify_event_param = d['notify_event_param']
        if 'org_out_id' in d:
            o.org_out_id = d['org_out_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'vid' in d:
            o.vid = d['vid']
        return o


