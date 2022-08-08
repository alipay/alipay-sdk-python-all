#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherMiniAppSendGuideInfo import VoucherMiniAppSendGuideInfo


class VoucherSendGuideInfo(object):

    def __init__(self):
        self._mini_app_send_guide_info = None
        self._send_guide_mode = None

    @property
    def mini_app_send_guide_info(self):
        return self._mini_app_send_guide_info

    @mini_app_send_guide_info.setter
    def mini_app_send_guide_info(self, value):
        if isinstance(value, VoucherMiniAppSendGuideInfo):
            self._mini_app_send_guide_info = value
        else:
            self._mini_app_send_guide_info = VoucherMiniAppSendGuideInfo.from_alipay_dict(value)
    @property
    def send_guide_mode(self):
        return self._send_guide_mode

    @send_guide_mode.setter
    def send_guide_mode(self, value):
        if isinstance(value, list):
            self._send_guide_mode = list()
            for i in value:
                self._send_guide_mode.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.mini_app_send_guide_info:
            if hasattr(self.mini_app_send_guide_info, 'to_alipay_dict'):
                params['mini_app_send_guide_info'] = self.mini_app_send_guide_info.to_alipay_dict()
            else:
                params['mini_app_send_guide_info'] = self.mini_app_send_guide_info
        if self.send_guide_mode:
            if isinstance(self.send_guide_mode, list):
                for i in range(0, len(self.send_guide_mode)):
                    element = self.send_guide_mode[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.send_guide_mode[i] = element.to_alipay_dict()
            if hasattr(self.send_guide_mode, 'to_alipay_dict'):
                params['send_guide_mode'] = self.send_guide_mode.to_alipay_dict()
            else:
                params['send_guide_mode'] = self.send_guide_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherSendGuideInfo()
        if 'mini_app_send_guide_info' in d:
            o.mini_app_send_guide_info = d['mini_app_send_guide_info']
        if 'send_guide_mode' in d:
            o.send_guide_mode = d['send_guide_mode']
        return o


