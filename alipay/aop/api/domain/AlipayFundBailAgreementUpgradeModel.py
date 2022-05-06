#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundBailAgreementUpgradeModel(object):

    def __init__(self):
        self._agreement_no = None
        self._trusteeship_mode = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def trusteeship_mode(self):
        return self._trusteeship_mode

    @trusteeship_mode.setter
    def trusteeship_mode(self, value):
        self._trusteeship_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.trusteeship_mode:
            if hasattr(self.trusteeship_mode, 'to_alipay_dict'):
                params['trusteeship_mode'] = self.trusteeship_mode.to_alipay_dict()
            else:
                params['trusteeship_mode'] = self.trusteeship_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundBailAgreementUpgradeModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'trusteeship_mode' in d:
            o.trusteeship_mode = d['trusteeship_mode']
        return o


