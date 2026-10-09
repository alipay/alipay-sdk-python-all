#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppEbppBangdaoMsgUploadModel(object):

    def __init__(self):
        self._charge_inst = None
        self._chargeoff_inst = None
        self._msg_notify_content = None
        self._notify_type = None
        self._sub_biz_type = None

    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def chargeoff_inst(self):
        return self._chargeoff_inst

    @chargeoff_inst.setter
    def chargeoff_inst(self, value):
        self._chargeoff_inst = value
    @property
    def msg_notify_content(self):
        return self._msg_notify_content

    @msg_notify_content.setter
    def msg_notify_content(self, value):
        self._msg_notify_content = value
    @property
    def notify_type(self):
        return self._notify_type

    @notify_type.setter
    def notify_type(self, value):
        self._notify_type = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.charge_inst:
            if hasattr(self.charge_inst, 'to_alipay_dict'):
                params['charge_inst'] = self.charge_inst.to_alipay_dict()
            else:
                params['charge_inst'] = self.charge_inst
        if self.chargeoff_inst:
            if hasattr(self.chargeoff_inst, 'to_alipay_dict'):
                params['chargeoff_inst'] = self.chargeoff_inst.to_alipay_dict()
            else:
                params['chargeoff_inst'] = self.chargeoff_inst
        if self.msg_notify_content:
            if hasattr(self.msg_notify_content, 'to_alipay_dict'):
                params['msg_notify_content'] = self.msg_notify_content.to_alipay_dict()
            else:
                params['msg_notify_content'] = self.msg_notify_content
        if self.notify_type:
            if hasattr(self.notify_type, 'to_alipay_dict'):
                params['notify_type'] = self.notify_type.to_alipay_dict()
            else:
                params['notify_type'] = self.notify_type
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppEbppBangdaoMsgUploadModel()
        if 'charge_inst' in d:
            o.charge_inst = d['charge_inst']
        if 'chargeoff_inst' in d:
            o.chargeoff_inst = d['chargeoff_inst']
        if 'msg_notify_content' in d:
            o.msg_notify_content = d['msg_notify_content']
        if 'notify_type' in d:
            o.notify_type = d['notify_type']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        return o


