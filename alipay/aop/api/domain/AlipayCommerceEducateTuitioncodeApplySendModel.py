#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MonitorInfo import MonitorInfo
from alipay.aop.api.domain.PayeeInfo import PayeeInfo


class AlipayCommerceEducateTuitioncodeApplySendModel(object):

    def __init__(self):
        self._complain_url = None
        self._fund_type = None
        self._monitor_info = None
        self._out_apply_id = None
        self._payee_info = None
        self._scene_type = None
        self._smid = None
        self._sys_service_provider_id = None

    @property
    def complain_url(self):
        return self._complain_url

    @complain_url.setter
    def complain_url(self, value):
        self._complain_url = value
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def monitor_info(self):
        return self._monitor_info

    @monitor_info.setter
    def monitor_info(self, value):
        if isinstance(value, MonitorInfo):
            self._monitor_info = value
        else:
            self._monitor_info = MonitorInfo.from_alipay_dict(value)
    @property
    def out_apply_id(self):
        return self._out_apply_id

    @out_apply_id.setter
    def out_apply_id(self, value):
        self._out_apply_id = value
    @property
    def payee_info(self):
        return self._payee_info

    @payee_info.setter
    def payee_info(self, value):
        if isinstance(value, PayeeInfo):
            self._payee_info = value
        else:
            self._payee_info = PayeeInfo.from_alipay_dict(value)
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def sys_service_provider_id(self):
        return self._sys_service_provider_id

    @sys_service_provider_id.setter
    def sys_service_provider_id(self, value):
        self._sys_service_provider_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.complain_url:
            if hasattr(self.complain_url, 'to_alipay_dict'):
                params['complain_url'] = self.complain_url.to_alipay_dict()
            else:
                params['complain_url'] = self.complain_url
        if self.fund_type:
            if hasattr(self.fund_type, 'to_alipay_dict'):
                params['fund_type'] = self.fund_type.to_alipay_dict()
            else:
                params['fund_type'] = self.fund_type
        if self.monitor_info:
            if hasattr(self.monitor_info, 'to_alipay_dict'):
                params['monitor_info'] = self.monitor_info.to_alipay_dict()
            else:
                params['monitor_info'] = self.monitor_info
        if self.out_apply_id:
            if hasattr(self.out_apply_id, 'to_alipay_dict'):
                params['out_apply_id'] = self.out_apply_id.to_alipay_dict()
            else:
                params['out_apply_id'] = self.out_apply_id
        if self.payee_info:
            if hasattr(self.payee_info, 'to_alipay_dict'):
                params['payee_info'] = self.payee_info.to_alipay_dict()
            else:
                params['payee_info'] = self.payee_info
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.sys_service_provider_id:
            if hasattr(self.sys_service_provider_id, 'to_alipay_dict'):
                params['sys_service_provider_id'] = self.sys_service_provider_id.to_alipay_dict()
            else:
                params['sys_service_provider_id'] = self.sys_service_provider_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateTuitioncodeApplySendModel()
        if 'complain_url' in d:
            o.complain_url = d['complain_url']
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        if 'monitor_info' in d:
            o.monitor_info = d['monitor_info']
        if 'out_apply_id' in d:
            o.out_apply_id = d['out_apply_id']
        if 'payee_info' in d:
            o.payee_info = d['payee_info']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'smid' in d:
            o.smid = d['smid']
        if 'sys_service_provider_id' in d:
            o.sys_service_provider_id = d['sys_service_provider_id']
        return o


