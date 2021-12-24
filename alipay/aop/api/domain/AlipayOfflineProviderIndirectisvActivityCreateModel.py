#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndirectIsvTerminalInfo import IndirectIsvTerminalInfo


class AlipayOfflineProviderIndirectisvActivityCreateModel(object):

    def __init__(self):
        self._ext_info = None
        self._indirect_isv_terminal_info = None
        self._merchant_id = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def indirect_isv_terminal_info(self):
        return self._indirect_isv_terminal_info

    @indirect_isv_terminal_info.setter
    def indirect_isv_terminal_info(self, value):
        if isinstance(value, list):
            self._indirect_isv_terminal_info = list()
            for i in value:
                if isinstance(i, IndirectIsvTerminalInfo):
                    self._indirect_isv_terminal_info.append(i)
                else:
                    self._indirect_isv_terminal_info.append(IndirectIsvTerminalInfo.from_alipay_dict(i))
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.indirect_isv_terminal_info:
            if isinstance(self.indirect_isv_terminal_info, list):
                for i in range(0, len(self.indirect_isv_terminal_info)):
                    element = self.indirect_isv_terminal_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.indirect_isv_terminal_info[i] = element.to_alipay_dict()
            if hasattr(self.indirect_isv_terminal_info, 'to_alipay_dict'):
                params['indirect_isv_terminal_info'] = self.indirect_isv_terminal_info.to_alipay_dict()
            else:
                params['indirect_isv_terminal_info'] = self.indirect_isv_terminal_info
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderIndirectisvActivityCreateModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'indirect_isv_terminal_info' in d:
            o.indirect_isv_terminal_info = d['indirect_isv_terminal_info']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        return o


