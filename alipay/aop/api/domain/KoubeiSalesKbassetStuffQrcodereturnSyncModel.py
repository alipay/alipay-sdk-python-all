#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AccessReturnQrcode import AccessReturnQrcode


class KoubeiSalesKbassetStuffQrcodereturnSyncModel(object):

    def __init__(self):
        self._return_qrcodes = None

    @property
    def return_qrcodes(self):
        return self._return_qrcodes

    @return_qrcodes.setter
    def return_qrcodes(self, value):
        if isinstance(value, list):
            self._return_qrcodes = list()
            for i in value:
                if isinstance(i, AccessReturnQrcode):
                    self._return_qrcodes.append(i)
                else:
                    self._return_qrcodes.append(AccessReturnQrcode.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.return_qrcodes:
            if isinstance(self.return_qrcodes, list):
                for i in range(0, len(self.return_qrcodes)):
                    element = self.return_qrcodes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.return_qrcodes[i] = element.to_alipay_dict()
            if hasattr(self.return_qrcodes, 'to_alipay_dict'):
                params['return_qrcodes'] = self.return_qrcodes.to_alipay_dict()
            else:
                params['return_qrcodes'] = self.return_qrcodes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiSalesKbassetStuffQrcodereturnSyncModel()
        if 'return_qrcodes' in d:
            o.return_qrcodes = d['return_qrcodes']
        return o


